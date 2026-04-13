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
from flask_openapi.schema import JsonSchema, StringField

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

extended_location_schema = JsonSchema(
    title='ExtendedLocation',
    description=f'{location_schema.description}<br>*Extended with non-standard fields.*',
    properties={
        **location_schema.properties,
        'source': StringField(maxLength=255, required=False, description='Source of the location data.'),
        'original_id': StringField(
            minLength=1,
            maxLength=36,
            description='Uniquely identifies the location within the CPOs platform (and suboperator platforms). This field can never be '
            'changed, modified or renamed. In original OCPI, this field is called id.',
        ),
    },
)

location_example = {}


location_component = Component('Location', location_schema, location_example)


all_location_components = [
    additional_geo_location_component,
    business_details_component,
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
    location_component,
    max_power_component,
    publish_token_type_component,
    regular_hours_component,
    status_schedule_component,
]
