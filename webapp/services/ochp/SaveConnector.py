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

from lxml import etree
from wtfjson import DictInput
from typing import Union, List
from wtfjson.fields import StringField, IntegerField, FloatField
from wtfjson.validators import AnyOf, NumberRange
from ...extensions import logger
from .Helper import get_nsmap, get_field
from ...enums import ConnectorType, ConnectorFormat, PowerType
from ..generic.SaveConnector import ConnectorUpdate


connector_format_mapping = {
    'Socket': ConnectorFormat.SOCKET,
    'Cable': ConnectorFormat.CABLE
}

connector_type_mapping = {
    'Chademo': ConnectorType.CHADEMO,
    'IEC_62196_T1': ConnectorType.IEC_62196_T1,
    'IEC_62196_T1_COMBO': ConnectorType.IEC_62196_T1_COMBO,
    'IEC_62196_T2': ConnectorType.IEC_62196_T2,
    'IEC_62196_T2_COMBO': ConnectorType.IEC_62196_T2_COMBO,
    'IEC_62196_T3A': ConnectorType.IEC_62196_T3A,
    'IEC_62196_T3C': ConnectorType.IEC_62196_T3C,
    'DOMESTIC_A': ConnectorType.DOMESTIC_A,
    'DOMESTIC_B': ConnectorType.DOMESTIC_B,
    'DOMESTIC_C': ConnectorType.DOMESTIC_C,
    'DOMESTIC_D': ConnectorType.DOMESTIC_D,
    'DOMESTIC_E': ConnectorType.DOMESTIC_E,
    'DOMESTIC_F': ConnectorType.DOMESTIC_F,
    'DOMESTIC_G': ConnectorType.DOMESTIC_G,
    'DOMESTIC_H': ConnectorType.DOMESTIC_H,
    'DOMESTIC_I': ConnectorType.DOMESTIC_I,
    'DOMESTIC_J': ConnectorType.DOMESTIC_J,
    'DOMESTIC_K': ConnectorType.DOMESTIC_K,
    'DOMESTIC_L': ConnectorType.DOMESTIC_L,
    'TESLA_R': ConnectorType.TESLA_R,
    'TESLA_S': ConnectorType.TESLA_S,
    'IEC_60309_2_single_16': ConnectorType.IEC_60309_2_single_16,
    'IEC_60309_2_three_16': ConnectorType.IEC_60309_2_three_16,
    'IEC_60309_2_three_32': ConnectorType.IEC_60309_2_three_32,
    'IEC_60309_2_three_64': ConnectorType.IEC_60309_2_three_64
}


power_type_mapping = {
    'AC': PowerType.AC_3_PHASE,
    'DC': PowerType.DC
}


def get_connector_updates(data_chargepoint: etree) -> List[ConnectorUpdate]:
    nsmap = get_nsmap()
    kwargs = {
        'power_type': get_field(data_chargepoint, 'chargePointType', nsmap)
    }
    ratings_data = get_field(data_chargepoint, 'ratings', nsmap, text=False)
    if ratings_data is not None:
        kwargs['max_electric_power'] = float(get_field(ratings_data, 'maximumPower', nsmap))
        if get_field(ratings_data, 'nominalVoltage', nsmap):
            kwargs['max_voltage'] = get_field(ratings_data, 'nominalVoltage', nsmap)
    counter = 1
    connector_updates = []
    for data_connector in get_field(data_chargepoint, 'connectors', nsmap, list=True, text=False):
        connector_update = get_connector_update(data_connector, uid=str(counter), **kwargs)
        counter += 1
        if connector_update:
            connector_updates.append(connector_update)
    return connector_updates


def get_connector_update(data_connector: etree, **kwargs) -> Union[ConnectorUpdate, None]:
    connector = kwargs.copy()
    nsmap = get_nsmap()
    connector['standard'] = get_field(data_connector, 'connectorStandard/ns:ConnectorStandard', nsmap)
    connector['format'] = get_field(data_connector, 'connectorFormat/ns:ConnectorFormat', nsmap)

    validator = ConnectorValidator(connector)
    if not validator.validate():
        logger.error('ochp.chargepoint', 'invalid connector found: %s' % connector)
        return
    chargepoint_update = ConnectorUpdate()
    validator.populate_obj(chargepoint_update)
    return chargepoint_update


class ConnectorValidator(DictInput):
    uid = StringField()
    standard = StringField(
        validators=[AnyOf(list(connector_type_mapping.keys()))],
        output_filters=[lambda item: connector_type_mapping.get(item)]
    )
    format = StringField(
        validators=[AnyOf(list(connector_format_mapping.keys()))],
        output_filters=[lambda item: connector_format_mapping.get(item)]
    )
    max_electric_power = FloatField(
        required=False,
        validators=[NumberRange(min=0)],
        output_filters=[lambda item: int(item * 1000)]
    )
    max_voltage = IntegerField(required=False, validators=[NumberRange(min=0)])

