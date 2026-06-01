"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from butterfly_pubsub.giroe import ChargeConnectorStatus
from flask_openapi.decorator import Schema as Component
from flask_openapi.schema import (
    ArrayField,
    BooleanField,
    DateTimeField,
    EnumField,
    IntegerField,
    JsonSchema,
    NumericField,
    ObjectField,
    StringField,
)

from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import EvseStatus

giroe_connector_input_schema = ObjectField(
    description='Single charge connector reported by giro-e.',
    properties={
        'id': IntegerField(minimum=1, description='giro-e internal connector ID'),
        'created': DateTimeField(),
        'modified': DateTimeField(),
        'uid': StringField(description='Stable connector UID assigned by giro-e'),
        'ocpp_connector_id': IntegerField(),
        'status': EnumField(enum=ChargeConnectorStatus, description='Current connector status'),
        'power': IntegerField(description='Maximum power in watts'),
        'power_type': EnumField(enum=PowerType),
        'standard': EnumField(enum=ConnectorType),
        'format': EnumField(enum=ConnectorFormat),
        'meter_public_key': StringField(required=False, nullable=True),
        'meter_serial_number': StringField(required=False, nullable=True),
    },
)

giroe_station_input_schema = ObjectField(
    description='A charging station belonging to a giro-e location.',
    properties={
        'id': IntegerField(minimum=1),
        'created': DateTimeField(),
        'modified': DateTimeField(),
        'uid': StringField(maxLength=36, description='Stable station UID assigned by giro-e'),
        'technical_backend': StringField(),
        'hardware_id': IntegerField(),
        'connectors': ArrayField(items=giroe_connector_input_schema),
    },
)

giroe_location_input_schema = JsonSchema(
    title='GiroeLocationInput',
    description='Location payload received from the giro-e backend.',
    properties={
        'id': IntegerField(minimum=1, description='giro-e internal location ID'),
        'created': DateTimeField(),
        'modified': DateTimeField(),
        'lat': NumericField(description='Latitude (WGS84)'),
        'lon': NumericField(description='Longitude (WGS84)'),
        'address': StringField(),
        'postalcode': StringField(),
        'locality': StringField(),
        'country': StringField(description='ISO 3166-1 alpha-2 country code'),
        'public': BooleanField(description='When false, OCPDB drops the location instead of upserting it.'),
        'public_description': StringField(),
        'stations': ArrayField(items=giroe_station_input_schema),
    },
)

giroe_location_input_example = {
    'id': 1234,
    'created': '2026-01-01T00:00:00Z',
    'modified': '2026-01-15T10:30:00Z',
    'lat': 52.520,
    'lon': 13.405,
    'address': 'Alexanderplatz 1',
    'postalcode': '10178',
    'locality': 'Berlin',
    'country': 'DE',
    'public': True,
    'public_description': 'Berlin Alexanderplatz parking deck',
    'stations': [
        {
            'id': 100,
            'created': '2026-01-01T00:00:00Z',
            'modified': '2026-01-15T10:30:00Z',
            'uid': '11111111-1111-1111-1111-111111111111',
            'technical_backend': 'tcc',
            'hardware_id': 42,
            'connectors': [
                {
                    'id': 1000,
                    'created': '2026-01-01T00:00:00Z',
                    'modified': '2026-01-15T10:30:00Z',
                    'uid': 'giroe-evse-1000',
                    'ocpp_connector_id': 1,
                    'status': 'available',
                    'power': 22000,
                    'power_type': 'AC_3_PHASE',
                    'standard': 'IEC_62196_T2',
                    'format': 'SOCKET',
                },
            ],
        },
    ],
}

giroe_location_input_component = Component(
    'GiroeLocationInput',
    giroe_location_input_schema,
    giroe_location_input_example,
)

giroe_connector_patch_schema = JsonSchema(
    title='GiroeConnectorPatch',
    description='Status update for a single giro-e connector (EVSE).',
    properties={
        'modified': DateTimeField(description='Timestamp when this status change was observed.'),
        'status': EnumField(enum=EvseStatus, required=False, description='New EVSE status.'),
    },
)

giroe_connector_patch_example = {
    'modified': '2026-01-15T10:30:00Z',
    'status': 'CHARGING',
}

giroe_connector_patch_component = Component(
    'GiroeConnectorPatch',
    giroe_connector_patch_schema,
    giroe_connector_patch_example,
)
