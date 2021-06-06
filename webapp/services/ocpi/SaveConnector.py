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

from wtfjson import DictInput
from typing import Union
from wtfjson.fields import StringField, IntegerField, FloatField
from wtfjson.validators import AnyOf, NumberRange
from ...extensions import logger
from ...enums import ConnectorType, ConnectorFormat
from ..generic.SaveConnector import ConnectorUpdate


def get_connector_update(data_connector: dict) -> Union[ConnectorUpdate, None]:
    connector = {}
    connector.update(data_connector)
    validator = ConnectorValidator(connector)
    if not validator.validate():
        logger.error('ocpi.connector', 'invalid connector found: %s - %s' % (validator.errors, data_connector))
        return
    chargepoint_update = ConnectorUpdate()
    validator.populate_obj(chargepoint_update)
    return chargepoint_update


class ConnectorValidator(DictInput):
    uid = StringField()
    standard = StringField(
        validators=[AnyOf([item.name for item in ConnectorType])],
        output_filters=[lambda item: getattr(ConnectorType, item)]
    )
    format = StringField(
        validators=[AnyOf([item.name for item in ConnectorFormat])],
        output_filters=[lambda item: getattr(ConnectorFormat, item)]
    )
    max_electric_power = IntegerField(required=False, validators=[NumberRange(min=0)])
    max_voltage = IntegerField(required=False, validators=[NumberRange(min=0)])

