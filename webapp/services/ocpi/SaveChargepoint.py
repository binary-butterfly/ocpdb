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

from typing import Union
from wtfjson import DictInput
from wtfjson.fields import StringField, DateTimeField, ListField, FloatField, IntegerField, BooleanField
from wtfjson.validators import Length, Regexp, AnyOf
from ...extensions import logger
from ...enums import ChargepointStatus, ParkingRestriction, Capability
from ..generic.SaveChargepoint import ChargepointUpdate


def get_chargepoint_update(data_chargepoint: dict) -> Union[ChargepointUpdate, None]:
    chargepoint = {
        'parking_restrictions': []
    }
    chargepoint.update(data_chargepoint)
    validator = ChargepointValidator(chargepoint)
    if not validator.validate():
        logger.error('ocpi.chargepoint', 'invalid chargepoint found: %s - %s' % (data_chargepoint, validator.errors))
        return
    chargepoint_update = ChargepointUpdate()
    validator.populate_obj(chargepoint_update)
    return chargepoint_update


class RegularHoursValidator(DictInput):
    weekday = IntegerField(input_filters=[lambda item: int(item)])
    period_begin = IntegerField(input_filters=[lambda item: int(item[0:2]) * 3600 + int(item[4:6]) * 60])
    period_end = IntegerField(input_filters=[lambda item: int(item[0:2]) * 3600 + int(item[4:6]) * 60])


class ExceptionalPeriodValidator(DictInput):
    period_begin = DateTimeField(localized=True)
    period_end = DateTimeField(localized=True)


class ChargepointValidator(DictInput):
    evse_id = StringField(validators=[Length(max=36)])
    phone = StringField(required=False, validators=[Length(max=20), Regexp(r'[\d -]+')])
    last_updated = DateTimeField(required=False)
    capabilities = ListField(StringField(
        validators=[AnyOf([item.name for item in Capability])],
        output_filters=[lambda item: getattr(Capability, item)]
    ), required=False, output_filters=[lambda item: sorted(list(set(item)), key=lambda item: item.value)])
    parking_restrictions = ListField(StringField(
        validators=[AnyOf([item.name for item in ParkingRestriction])],
        output_filters=[lambda item: getattr(ParkingRestriction, item)]
    ), required=False, output_filters=[lambda item: sorted(list(set(item)), key=lambda item: item.value)])
    parking_uid = StringField(required=False, validators=[Length(max=64)])
    parking_floor_level = StringField(required=False, validators=[Length(max=4)])
    parking_spot_number = StringField(required=False, validators=[Length(max=5)])
    max_reservation = FloatField(required=False)
    status = StringField(
        required=False,
        validators=[AnyOf([item.name for item in ChargepointStatus])],
        output_filters=[lambda item: getattr(ChargepointStatus, item)]
    )
