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
    SchemaListReference,
    SchemaReference,
    document,
)
from flask_openapi.schema import AnyOfField, BooleanField, IntegerField, NumericField, StringField
from validataclass.validators import DataclassValidator

from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.public_api.base_blueprint import BaseBlueprint
from webapp.shared.ocpi_schema import all_location_components

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
            Parameter(
                'sorted_by',
                schema=AnyOfField(allowed_values=['name', 'created', 'modified'], required=False, default='name'),
            ),
            Parameter('name', schema=StringField(required=False)),
            Parameter('source_uid', schema=StringField(required=False), example='bnetza_api'),
            Parameter(
                'source_uids',
                schema=StringField(required=False),
                example='bnetza_api,something_else',
                description='Comma separated list of sources',
            ),
            Parameter(
                'exclude_source_uid',
                schema=StringField(required=False),
                example='bnetza_api',
                description='Sources to exclude',
            ),
            Parameter(
                'exclude_source_uids',
                schema=StringField(required=False),
                example='bnetza_api,something_else',
                description='Comma separated list of sources which should be excluded',
            ),
            Parameter('address', schema=StringField(required=False), example='Erlenweg', description='Contain query'),
            Parameter('postal_code', schema=StringField(required=False), example='59423'),
            Parameter('city', schema=StringField(required=False), example='Bad Gateway', description='Contain query'),
            Parameter('country', schema=StringField(required=False), example='59423'),
            Parameter('operator_name', schema=StringField(required=False), example='Electro Inc'),
            Parameter(
                'lat',
                schema=NumericField(required=False),
                example='51.58',
                description='Radius, lat and lon always have to be set together.',
            ),
            Parameter(
                'lon',
                schema=NumericField(required=False),
                example='7.67',
                description='Radius, lat and lon always have to be set together.',
            ),
            Parameter(
                'radius',
                schema=IntegerField(required=False),
                example='1000',
                description='In meter. Radius, lat and lon always have to be set together.',
            ),
            Parameter('lat_min', schema=NumericField(), example=55.0, description='Bounding box'),
            Parameter('lat_max', schema=NumericField(), example=55.5, description='Bounding box'),
            Parameter('lon_min', schema=NumericField(), example=5.0, description='Bounding box'),
            Parameter('lon_max', schema=NumericField(), example=5.5, description='Bounding box'),
            Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
            Parameter(
                'strict',
                schema=BooleanField(),
                description='If set to true, all additional fields will be omitted for full OCPI compatibility.',
            ),
        ],
        response=[Response(ResponseData(SchemaListReference('Location'), ExampleListReference('Location')))],
        components=all_location_components,
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        locations = self.location_handler.get_locations(
            search_query,
            strict=self.request_helper.get_query_args().get('strict') == 'true',
        )
        return self.jsonify_paginated_response(locations, search_query)


class LocationItemMethodView(LocationBaseMethodView):
    @document(
        description='Get single Location',
        path=[Parameter('location_id', schema=IntegerField(minimum=1))],
        response=[Response(ResponseData(SchemaReference('Location'), ExampleReference('Location')))],
        query=[
            Parameter(
                'strict',
                schema=BooleanField(),
                description='If set to true, all additional fields will be omitted for full OCPI compatibility.',
            ),
        ],
        components=all_location_components,
    )
    @cross_origin()
    def get(self, location_id: int):
        location = self.location_handler.get_location(
            location_id,
            strict=self.request_helper.get_query_args().get('strict') == 'true',
        )

        return jsonify(location)
