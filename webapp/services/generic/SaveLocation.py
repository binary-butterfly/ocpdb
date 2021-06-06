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

from decimal import Decimal
from datetime import datetime
from typing import Optional, List
from dataclasses import dataclass, asdict
from ...models import Location
from ...extensions import logger, db
from .SaveOpeningTimes import ExceptionalPeriod, ExceptionalPeriodUpdate, RegularHoursUpdate, get_opening_time_update, \
    save_opening_times, RegularHours


@dataclass
class LocationUpdate:
    uid: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    lat: Optional[Decimal] = None
    lon: Optional[Decimal] = None
    last_updated: Optional[datetime] = None
    exceptional_openings: Optional[List[ExceptionalPeriodUpdate]] = None
    exceptional_closings: Optional[List[ExceptionalPeriodUpdate]] = None
    regular_hours: Optional[List[RegularHoursUpdate]] = None
    twentyfourseven: Optional[bool] = None


def upsert_location(
        location_update: LocationUpdate,
        old_location: Optional[Location] = None,
        old_regular_hours: Optional[List[RegularHours]] = None,
        old_exceptionals: Optional[List[ExceptionalPeriod]] = None,
        commit: bool = True) -> Location:
    location = old_location if old_location else Location.query.filter_by(uid=location_update.uid).first()
    opening_time_update = get_opening_time_update(location, location_update, old_regular_hours, old_exceptionals)
    update_required = opening_time_update.update_required
    if location:
        for field in asdict(location_update):
            if getattr(location, field) != getattr(location_update, field):
                if field in ['exceptional_openings', 'exceptional_closings', 'regular_hours']:
                    continue
                update_required = True
                break
        if not update_required:
            return location
    else:
        update_required = True
        location = Location()
    if not update_required:
        return location
    for field in asdict(location_update):
        if field in ['exceptional_openings', 'exceptional_closings', 'regular_hours']:
            continue
        setattr(location, field, getattr(location_update, field))
    if commit:
        db.session.add(location)
        db.session.commit()
        save_opening_times(location, opening_time_update)
        logger.info('ochp.chargepoint.update', 'updated location %s' % location.id)
    return location
