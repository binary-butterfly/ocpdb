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
from validataclass.helpers import OptionalUnsetNone, UnsetValue
from webapp.models import Location
from webapp.extensions import logger, db
from .SaveOpeningTimes import ExceptionalPeriod, ExceptionalPeriodUpdate, RegularHoursUpdate, get_opening_time_update, \
    save_opening_times, RegularHours
from .SaveChargepoint import ChargepointUpdate


@dataclass
class LocationUpdate:
    source: str  # TODO: this should not be part of an update
    uid: str  # TODO: this should not be part of an update
    name: OptionalUnsetNone[str] = UnsetValue
    address: OptionalUnsetNone[str] = UnsetValue
    postal_code: OptionalUnsetNone[str] = UnsetValue
    city: OptionalUnsetNone[str] = UnsetValue
    country: OptionalUnsetNone[str] = UnsetValue
    lat: OptionalUnsetNone[Decimal] = UnsetValue
    lon: OptionalUnsetNone[Decimal] = UnsetValue
    last_updated: OptionalUnsetNone[datetime] = UnsetValue
    exceptional_openings: OptionalUnsetNone[List[ExceptionalPeriodUpdate]] = UnsetValue
    exceptional_closings: OptionalUnsetNone[List[ExceptionalPeriodUpdate]] = UnsetValue
    regular_hours: OptionalUnsetNone[List[RegularHoursUpdate]] = UnsetValue
    twentyfourseven: OptionalUnsetNone[bool] = UnsetValue
    chargepoints: OptionalUnsetNone[List[ChargepointUpdate]] = UnsetValue


def upsert_location(
        location_update: LocationUpdate,
        old_location: Optional[Location] = None,
        old_regular_hours: Optional[List[RegularHours]] = None,
        old_exceptionals: Optional[List[ExceptionalPeriod]] = None,
        commit: bool = True) -> Location:
    location = old_location if old_location else Location.query\
        .filter_by(uid=location_update.uid)\
        .filter_by(source=location_update.source)\
        .first()
    opening_time_update = get_opening_time_update(location, location_update, old_regular_hours, old_exceptionals)
    update_required = opening_time_update.update_required
    if location:
        for field, value in asdict(location_update).items():
            if getattr(location, field) != value:
                if field in ['exceptional_openings', 'exceptional_closings', 'regular_hours', 'chargepoints']:
                    continue
                if value is UnsetValue:
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
    for field, value in asdict(location_update).items():
        if field in ['exceptional_openings', 'exceptional_closings', 'regular_hours', 'chargepoints']:
            continue
        if value is UnsetValue:
            continue
        setattr(location, field, value)
    if commit:
        db.session.add(location)
        db.session.commit()
        save_opening_times(location, opening_time_update)
        logger.info('ochp.chargepoint.update', 'updated location %s' % location.id)
    return location
