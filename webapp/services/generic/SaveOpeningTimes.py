# encoding: utf-8

"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Optional, Union, TYPE_CHECKING
from ...models import Location, ExceptionalPeriod, RegularHours
from ...enums import ExceptionalPeriodType
from ...extensions import db
if TYPE_CHECKING:
    from .SaveLocation import LocationUpdate


@dataclass
class RegularHoursUpdate:
    weekday: Optional[int] = None
    period_begin: Optional[int] = None
    period_end: Optional[int] = None


@dataclass
class ExceptionalPeriodUpdate:
    type: ExceptionalPeriodType
    period_begin: Optional[datetime] = None
    period_end: Optional[datetime] = None


@dataclass
class OpeningTimeUpdate:
    regular_hours: List[RegularHours]
    exceptionals: List[ExceptionalPeriod]
    new_regular_hours: Optional[List[RegularHours]] = None
    new_exceptionals: Optional[List[ExceptionalPeriod]] = None
    deleted_regular_hours: Optional[List[int]] = None
    deleted_exceptionals: Optional[List[int]] = None
    update_required: bool = False


def get_opening_time_update(
        location: Union[Location, None],
        location_update: 'LocationUpdate',
        regular_hours: Optional[List[RegularHoursUpdate]] = None,
        exceptionals: Optional[List[ExceptionalPeriod]] = None) -> OpeningTimeUpdate:
    if regular_hours is None:
        regular_hours = RegularHours.query.filter_by(location_id=location.id).all() if location else []
    if exceptionals is None:
        exceptionals = ExceptionalPeriod.query.filter_by(location_id=location.id).all() if location else []
    opening_time_update = OpeningTimeUpdate(exceptionals=exceptionals, regular_hours=regular_hours)
    set_regular_hours_update(opening_time_update, location_update.regular_hours)
    set_exceptional_updates(opening_time_update, location_update.exceptional_openings + location_update.exceptional_closings)
    opening_time_update.update_required = len(opening_time_update.new_regular_hours) > 0\
        or len(opening_time_update.new_exceptionals) > 0 or len(opening_time_update.deleted_regular_hours) > 0\
        or len(opening_time_update.deleted_exceptionals) > 0
    return opening_time_update


def set_regular_hours_update(opening_time_update: OpeningTimeUpdate, regular_hour_updates: List[RegularHoursUpdate]):
    old_ids = [regular_hour.id for regular_hour in opening_time_update.regular_hours]
    opening_time_update.new_regular_hours = []
    for regular_hour_update in regular_hour_updates:
        old_id = next((regular_hour.id for regular_hour in opening_time_update.regular_hours if compare(regular_hour, regular_hour_update)), None)
        if old_id is not None and old_id in old_ids:
            old_ids.remove(old_id)
        else:
            new_regular_hours = RegularHours()
            for field in asdict(regular_hour_update):
                setattr(new_regular_hours, field, getattr(regular_hour_update, field))
            opening_time_update.new_regular_hours.append(new_regular_hours)
    opening_time_update.deleted_regular_hours = old_ids


def set_exceptional_updates(opening_time_update: OpeningTimeUpdate, exceptional_updates: List[ExceptionalPeriodUpdate]):
    old_ids = [exceptional.id for exceptional in opening_time_update.exceptionals]
    opening_time_update.new_exceptionals = []
    for exceptional_update in exceptional_updates:
        old_id = next((exceptional.id for exceptional in opening_time_update.exceptionals if compare(exceptional, exceptional_update)), None)
        if old_id is not None and old_id in old_ids:
            old_ids.remove(old_id)
        else:
            new_exceptional = ExceptionalPeriod()
            for field in asdict(exceptional_update):
                setattr(new_exceptional, field, getattr(exceptional_update, field))
            opening_time_update.new_exceptionals.append(new_exceptional)
    opening_time_update.deleted_exceptionals = old_ids


def compare(obj: Union[RegularHours, ExceptionalPeriod], update: Union[RegularHoursUpdate, ExceptionalPeriodUpdate]) -> bool:
    for field in asdict(update):
        if getattr(obj, field) != getattr(update, field):
            return False
    return True


def save_opening_times(location: Location, opening_time_update: OpeningTimeUpdate):
    for regular_hours in opening_time_update.new_regular_hours:
        regular_hours.location_id = location.id
        db.session.add(regular_hours)
    for exceptional in opening_time_update.new_exceptionals:
        exceptional.location_id = location.id
        db.session.add(exceptional)
    db.session.commit()

    if len(opening_time_update.deleted_regular_hours) :
        RegularHours.query\
            .filter(RegularHours.id.in_(opening_time_update.deleted_regular_hours))\
            .delete(synchronize_session=False)
    db.session.commit()
    if len(opening_time_update.deleted_exceptionals) :
        ExceptionalPeriod.query\
            .filter(ExceptionalPeriod.id.in_(opening_time_update.deleted_exceptionals))\
            .delete(synchronize_session=False)
    db.session.commit()
