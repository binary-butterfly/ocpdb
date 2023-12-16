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

from flask import jsonify
from flask_cors import cross_origin
from flask_openapi.decorator import (
    ExampleListReference,
    ExampleReference,
    Parameter,
    Response,
    ResponseData,
    Schema,
    SchemaListReference,
    SchemaReference,
    document,
)
from flask_openapi.schema import AnyOfField, IntegerField, StringField
from validataclass.validators import DataclassValidator

from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.public_api.base_blueprint import BaseBlueprint
from webapp.shared.ocpi_schema import (
    additional_geo_location_example,
    additional_geo_location_schema,
    business_details_example,
    business_details_schema,
    connector_example,
    connector_schema,
    display_text_example,
    display_text_schema,
    energy_mix_example,
    energy_mix_schema,
    energy_source_example,
    energy_source_schema,
    environmental_impact_example,
    environmental_impact_schema,
    evse_example,
    evse_schema,
    exceptional_period_example,
    exceptional_period_schema,
    geo_location_example,
    geo_location_schema,
    hours_example,
    hours_schema,
    image_example,
    image_schema,
    location_example,
    location_schema,
    publish_token_type_example,
    publish_token_type_schema,
    regular_hours_example,
    regular_hours_schema,
)

from .location_handler import LocationHandler
from .location_search_queries import LocationSearchQuery


class LocationBlueprint(BaseBlueprint):
    documented = True
    location_handler: LocationHandler

    def __init__(self):
        self.location_handler = LocationHandler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
        )

        super().__init__('location', __name__, url_prefix='/api/public/v1/locations')

        self.add_url_rule(
            '',
            view_func=LocationListMethodView.as_view(
                'locations',
                **self.get_base_method_view_dependencies(),
                location_handler=self.location_handler,
            ),
        )
        self.add_url_rule(
            '/<int:location_id>',
            view_func=LocationItemMethodView.as_view(
                'location',
                **self.get_base_method_view_dependencies(),
                location_handler=self.location_handler,
            ),
        )


class LocationBaseMethodView(BaseMethodView):
    location_handler: LocationHandler

    def __init__(self, *args, location_handler: LocationHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_handler = location_handler


class LocationListMethodView(LocationBaseMethodView):
    search_query_validator = DataclassValidator(LocationSearchQuery)

    @document(
        description='Get list of Locations',
        query=[
            Parameter('sorted_by', schema=AnyOfField(allowed_values=['name', 'created', 'modified'], required=False, default='name')),
            Parameter('name', schema=StringField(required=False)),
            Parameter('source', schema=StringField(required=False)),
            Parameter('postal_code', schema=StringField(required=False)),
            Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
        ],
        response=[Response(ResponseData(SchemaListReference('Location'), ExampleListReference('Location')))],
        components=[
            Schema('AdditionalGeoLocation', additional_geo_location_schema, additional_geo_location_example),
            Schema('BusinessDetails', business_details_schema, business_details_example),
            Schema('Connector', connector_schema, connector_example),
            Schema('DisplayText', display_text_schema, display_text_example),
            Schema('EnergyMix', energy_mix_schema, energy_mix_example),
            Schema('EnergySource', energy_source_schema, energy_source_example),
            Schema('EnvironmentalImpact', environmental_impact_schema, environmental_impact_example),
            Schema('EVSE', evse_schema, evse_example),
            Schema('ExceptionalPeriod', exceptional_period_schema, exceptional_period_example),
            Schema('GeoLocation', geo_location_schema, geo_location_example),
            Schema('Hours', hours_schema, hours_example),
            Schema('Image', image_schema, image_example),
            Schema('Location', location_schema, location_example),
            Schema('PublishTokenType', publish_token_type_schema, publish_token_type_example),
            Schema('RegularHours', regular_hours_schema, regular_hours_example),
        ],
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        locations = self.location_handler.get_locations(search_query)
        return self.jsonify_paginated_response(locations, search_query)


class LocationItemMethodView(LocationBaseMethodView):
    @document(
        description='Get single Location',
        path=[Parameter('location_id', schema=IntegerField(minimum=1))],
        response=[Response(ResponseData(SchemaReference('Location'), ExampleReference('Location')))],
        components=[
            Schema('AdditionalGeoLocation', additional_geo_location_schema, additional_geo_location_example),
            Schema('BusinessDetails', business_details_schema, business_details_example),
            Schema('Connector', connector_schema, connector_example),
            Schema('DisplayText', display_text_schema, display_text_example),
            Schema('EnergyMix', energy_mix_schema, energy_mix_example),
            Schema('EnergySource', energy_source_schema, energy_source_example),
            Schema('EnvironmentalImpact', environmental_impact_schema, environmental_impact_example),
            Schema('EVSE', evse_schema, evse_example),
            Schema('ExceptionalPeriod', exceptional_period_schema, exceptional_period_example),
            Schema('GeoLocation', geo_location_schema, geo_location_example),
            Schema('Hours', hours_schema, hours_example),
            Schema('Image', image_schema, image_example),
            Schema('Location', location_schema, location_example),
            Schema('PublishTokenType', publish_token_type_schema, publish_token_type_example),
            Schema('RegularHours', regular_hours_schema, regular_hours_example),
        ],
    )
    @cross_origin()
    def get(self, location_id: int):
        return jsonify(self.location_handler.get_location(location_id))
