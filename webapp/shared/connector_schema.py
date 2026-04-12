"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2023 binary butterfly GmbH

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

from flask_openapi.decorator import Schema as Component
from flask_openapi.schema import ArrayField, DateTimeField, EnumField, IntegerField, JsonSchema, StringField, UriField

from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType

connector_schema = JsonSchema(
    title='Connector',
    description='A Connector is the socket or cable and plug available for the EV to use. A single EVSE may provide multiple Connectors '
    'but only one of them can be in use at the same time. A Connector always belongs to an EVSE object.',
    properties={
        'id': StringField(
            maxLength=36,
            description='Identifier of the Connector within the EVSE. Two Connectors may have the same id as long as they do not belong to '
            'the same EVSE object.',
        ),
        'standard': EnumField(enum=ConnectorType, description='The standard of the installed connector.'),
        'format': EnumField(enum=ConnectorFormat, description='The format (socket/cable) of the installed connector.'),
        'power_type': EnumField(enum=PowerType, description=''),
        'max_voltage': IntegerField(
            minimum=0,
            description='Maximum voltage of the connector (line to neutral for AC_3_PHASE), in volt [V]. For example: DC Chargers might '
            'vary the voltage during charging when battery almost full.',
        ),
        'max_amperage': IntegerField(minimum=0, description='Maximum amperage of the connector, in ampere [A].'),
        'max_electric_power': IntegerField(
            minimum=0,
            required=False,
            description='Maximum electric power that can be delivered by this connector, in Watts (W). When the maximum electric power is '
            'lower than the calculated value from voltage and amperage, this value should be set. For example: A DC Charge '
            'Point which can delivers up to 920V and up to 400A can be limited to a maximum of 150kW (max_electric_power = '
            '150000). Depending on the car, it may supply max voltage or current, but not both at the same time. For AC Charge '
            'Points, the amount of phases used can also have influence on the maximum power.',
        ),
        'tariff_ids': ArrayField(
            items=StringField(maxLength=36),
            required=False,
            description='Identifiers of the currently valid charging tariffs. Multiple tariffs are possible, but only one of each '
            'Tariff.type can be active at the same time. Tariffs with the same type are only allowed if they are not active at '
            'the same time: start_date_time and end_date_time period not overlapping. When preference-based smart charging is '
            'supported, one tariff for every possible ProfileType should be provided. These tell the user about the options '
            'they have at this Connector, and what the tariff is for every option. For a "free of charge" tariff, this field '
            'should be set and point to a defined "free of charge" tariff.',
        ),
        'terms_and_conditions': UriField(required=False, description="URL to the operator's terms and conditions."),
        'last_updated': DateTimeField(description='Timestamp when this Connector was last updated (or created).'),
    },
)


connector_example = {}


connector_component = Component('Connector', connector_schema, connector_example)


all_connector_components = [
    connector_component,
]
