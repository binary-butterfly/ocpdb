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

from typing import Union, List
from wtfjson import DictInput
from wtfjson.fields import StringField, DecimalField, DateTimeField, IntegerField, ListField, ObjectField, BooleanField
from wtfjson.validators import Length
from ...extensions import logger
from ..generic.SaveLocation import LocationUpdate, upsert_location
from ..generic.SaveConnector import upsert_connector
from ..generic.SaveChargepoint import upsert_chargepoint
from .SaveChargepoint import get_chargepoint_update
from .SaveConnector import get_connector_update
from ...enums import ExceptionalPeriodType
from ..generic.SaveOpeningTimes import ExceptionalPeriodUpdate, RegularHoursUpdate


def save_locations(ocpi_locations: List[dict]):
    for ocpi_location in ocpi_locations:
        save_location(ocpi_location)


def save_location(ocpi_location: dict):
    location_update = get_location_update(ocpi_location)
    if not location_update:
        return
    location = upsert_location(location_update)
    if not location:
        return
    for ocpi_chargepoint in ocpi_location['evses']:
        chargepoint_update = get_chargepoint_update(ocpi_chargepoint)
        if not chargepoint_update:
            continue
        chargepoint = upsert_chargepoint(chargepoint_update, location)
        if not chargepoint:
            continue
        for ocpi_connector in ocpi_chargepoint['connectors']:
            connector_update = get_connector_update(ocpi_connector)
            if not connector_update:
                continue
            upsert_connector(connector_update, chargepoint)


def get_location_update(data_location: dict) -> Union[LocationUpdate, None]:
    location = {
        'exceptional_openings': [],
        'exceptional_closings': [],
        'regular_hours': []
    }
    location.update(data_location)
    if location.get('opening_times'):
        location.update(location['opening_times'])
        del location['opening_times']
    else:
        location['opening_times'] = []
    if location.get('coordinates'):
        location.update(location['coordinates'])
        del location['coordinates']
    validator = LocationValidator(location)
    if not validator.validate():
        logger.error('ocpi.location', 'invalid location found: %s %s' % (validator.errors, data_location))
        return
    location_update = LocationUpdate()
    validator.populate_obj(location_update)
    return location_update


class RegularHoursValidator(DictInput):
    weekday = IntegerField(input_filters=[lambda item: int(item)])
    period_begin = IntegerField(input_filters=[lambda item: int(item[0:2]) * 3600 + int(item[4:6]) * 60])
    period_end = IntegerField(input_filters=[lambda item: int(item[0:2]) * 3600 + int(item[4:6]) * 60])


class ExceptionalPeriodValidator(DictInput):
    period_begin = DateTimeField(localized=True)
    period_end = DateTimeField(localized=True)


class LocationValidator(DictInput):
    uid = StringField(validators=[Length(max=32)])
    name = StringField(required=False, validators=[Length(max=100)])
    address = StringField(validators=[Length(max=45)])
    postal_code = StringField(validators=[Length(max=10)])
    city = StringField(validators=[Length(max=45)])
    country = StringField(validators=[Length(min=2, max=2)])
    lat = DecimalField()
    lon = DecimalField()
    last_updated = DateTimeField(required=False, localized=True)
    twentyfourseven = BooleanField(required=False)
    regular_hours = ListField(ObjectField(
        RegularHoursValidator,
        output_filters=[lambda item: RegularHoursUpdate(**item)]
    ))
    exceptional_openings = ListField(ObjectField(
        ExceptionalPeriodValidator,
        output_filters=[lambda item: ExceptionalPeriodUpdate(type=ExceptionalPeriodType.opening, **item)]
    ))
    exceptional_closings = ListField(ObjectField(
        ExceptionalPeriodValidator,
        output_filters=[lambda item: ExceptionalPeriodUpdate(type=ExceptionalPeriodType.closing, **item)]
    ))

