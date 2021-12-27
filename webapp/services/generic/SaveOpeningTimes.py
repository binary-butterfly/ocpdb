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
from validataclass.helpers import OptionalUnsetNone, UnsetValue
from webapp.models import Location, ExceptionalPeriod, RegularHours
from webapp.enums import ExceptionalPeriodType
from webapp.extensions import db
if TYPE_CHECKING:
    from .SaveLocation import LocationUpdate


@dataclass
class RegularHoursUpdate:
    weekday: OptionalUnsetNone[int] = UnsetValue
    period_begin: OptionalUnsetNone[int] = UnsetValue
    period_end: OptionalUnsetNone[int] = UnsetValue


@dataclass
class ExceptionalPeriodUpdate:
    type: ExceptionalPeriodType
    period_begin: OptionalUnsetNone[datetime] = UnsetValue
    period_end: OptionalUnsetNone[datetime] = UnsetValue


@dataclass
class OpeningTimeUpdate:
    regular_hours: OptionalUnsetNone[List[RegularHours]] = UnsetValue
    exceptionals: OptionalUnsetNone[List[ExceptionalPeriod]] = UnsetValue
    new_regular_hours: OptionalUnsetNone[List[RegularHours]] = UnsetValue
    new_exceptionals: OptionalUnsetNone[List[ExceptionalPeriod]] = UnsetValue
    deleted_regular_hours: OptionalUnsetNone[List[int]] = UnsetValue
    deleted_exceptionals: OptionalUnsetNone[List[int]] = UnsetValue
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
    opening_time_update = OpeningTimeUpdate(
        exceptionals=exceptionals,
        regular_hours=regular_hours,
        new_regular_hours=[],
        new_exceptionals=[],
        deleted_regular_hours=[],
        deleted_exceptionals=[]
    )
    if location_update.regular_hours is not UnsetValue:
        set_regular_hours_update(opening_time_update, location_update.regular_hours)
    if location_update.exceptional_openings is not UnsetValue and location_update.exceptional_closings is not UnsetValue:
        set_exceptional_updates(opening_time_update, location_update.exceptional_openings + location_update.exceptional_closings)
    opening_time_update.update_required = len(opening_time_update.new_regular_hours) > 0\
        or len(opening_time_update.new_exceptionals) > 0 or len(opening_time_update.deleted_regular_hours) > 0\
        or len(opening_time_update.deleted_exceptionals) > 0
    return opening_time_update


def set_regular_hours_update(opening_time_update: OpeningTimeUpdate, regular_hour_updates: List[RegularHoursUpdate]):
    old_ids = [regular_hour.id for regular_hour in opening_time_update.regular_hours]
    for regular_hour_update in regular_hour_updates:
        old_id = next((regular_hour.id for regular_hour in opening_time_update.regular_hours if compare(regular_hour, regular_hour_update)), None)
        if old_id is not None and old_id in old_ids:
            old_ids.remove(old_id)
        else:
            new_regular_hours = RegularHours()
            for field, value in asdict(regular_hour_update).items():
                if value is UnsetValue:
                    continue
                setattr(new_regular_hours, field, value)
            opening_time_update.new_regular_hours.append(new_regular_hours)
    opening_time_update.deleted_regular_hours = old_ids


def set_exceptional_updates(opening_time_update: OpeningTimeUpdate, exceptional_updates: List[ExceptionalPeriodUpdate]):
    old_ids = [exceptional.id for exceptional in opening_time_update.exceptionals]
    for exceptional_update in exceptional_updates:
        old_id = next((exceptional.id for exceptional in opening_time_update.exceptionals if compare(exceptional, exceptional_update)), None)
        if old_id is not None and old_id in old_ids:
            old_ids.remove(old_id)
        else:
            new_exceptional = ExceptionalPeriod()
            for field, value in asdict(exceptional_update).items():
                if value is UnsetValue:
                    continue
                setattr(new_exceptional, field, value)
            opening_time_update.new_exceptionals.append(new_exceptional)
    opening_time_update.deleted_exceptionals = old_ids


def compare(obj: Union[RegularHours, ExceptionalPeriod], update: Union[RegularHoursUpdate, ExceptionalPeriodUpdate]) -> bool:
    for field, value in asdict(update).items():
        if value is not UnsetValue and getattr(obj, field) != value:
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
