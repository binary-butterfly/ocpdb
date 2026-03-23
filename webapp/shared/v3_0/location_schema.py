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

from flask_openapi.decorator import Schema as Component
from flask_openapi.schema import ArrayField, DateField, DateTimeField, EnumField, JsonSchema, Reference, StringField

from webapp.models.charging_station import Capability
from webapp.shared.connector_schema import connector_component
from webapp.shared.evse_schema import evse_component
from webapp.shared.location_schema import (
    additional_geo_location_component,
    business_details_component,
    display_text_component,
    energy_mix_component,
    energy_source_component,
    environmental_impact_component,
    exceptional_period_component,
    geo_location_component,
    hours_component,
    image_component,
    location_schema,
    max_power_component,
    publish_token_type_component,
    regular_hours_component,
    status_schedule_component,
)

charging_station_schema = JsonSchema(
    title='ChargingStation',
    description='The ChargingStation object groups EVSEs that belong to the same physical charging station. '
    'It always belongs to a Location object.',
    properties={
        'id': StringField(
            maxLength=36,
            description='Unique identifier of the ChargingStation within the Location.',
        ),
        'original_uid': StringField(
            maxLength=36,
            description='Original unique identifier of the ChargingStation within the Location.',
            required=False,
        ),
        'capabilities': ArrayField(
            items=EnumField(enum=Capability),
            required=False,
            description='List of functionalities that the ChargingStation is capable of.',
        ),
        'floor_level': StringField(
            maxLength=16,
            required=False,
            description='Level on which the ChargingStation is located (in garage buildings) in the locally displayed '
            'numbering scheme.',
        ),
        'coordinates': Reference(obj='GeoLocation', required=False, description='Coordinates of the ChargingStation.'),
        'physical_reference': StringField(
            maxLength=16,
            required=False,
            description='A number/string printed on the outside of the ChargingStation for visual identification.',
        ),
        'directions': ArrayField(
            items=Reference(obj='DisplayText'),
            required=False,
            description='Multi-language human-readable directions when more detailed information on how to reach the '
            'ChargingStation from the Location is required.',
        ),
        'images': ArrayField(
            items=Reference(obj='Image'),
            required=False,
            description='Links to images related to the ChargingStation such as photos or logos.',
        ),
        'evses': ArrayField(
            items=Reference(obj='EVSE'),
            minItems=1,
            description='List of EVSEs that belong to this ChargingStation.',
        ),
        'max_power': Reference(
            obj='MaxPower',
            required=False,
            description='Maximum power available at this ChargingStation.',
        ),
        'go_live_date': DateField(
            required=False,
            description='Date when the ChargingStation went or will go live.',
        ),
        'last_updated': DateTimeField(
            description='Timestamp when this ChargingStation or one of its EVSEs was last updated (or created).',
        ),
    },
)

charging_station_example = {}

charging_station_component = Component('ChargingStation', charging_station_schema, charging_station_example)


ocpi_30_location_schema = JsonSchema(
    title='Ocpi30Location',
    description='OCPI 3.0 Location object. Contains ChargingStations instead of a flat list of EVSEs. '
    'The Location describes the location and its properties where a group of ChargingStations that belong together '
    'are installed.',
    properties={
        **{k: v for k, v in location_schema.properties.items() if k != 'evses'},
        'charging_pool': ArrayField(
            items=Reference(obj='ChargingStation'),
            required=False,
            description='List of ChargingStations that belong to this Location.',
        ),
    },
)

ocpi_30_location_example = {}

ocpi_30_location_component = Component('Ocpi30Location', ocpi_30_location_schema, ocpi_30_location_example)


all_charging_station_components = [
    charging_station_component,
    connector_component,
    display_text_component,
    evse_component,
    geo_location_component,
    image_component,
    max_power_component,
]


all_ocpi_30_location_components = [
    additional_geo_location_component,
    business_details_component,
    charging_station_component,
    connector_component,
    display_text_component,
    energy_mix_component,
    energy_source_component,
    environmental_impact_component,
    evse_component,
    exceptional_period_component,
    geo_location_component,
    hours_component,
    image_component,
    max_power_component,
    ocpi_30_location_component,
    publish_token_type_component,
    regular_hours_component,
    status_schedule_component,
]
