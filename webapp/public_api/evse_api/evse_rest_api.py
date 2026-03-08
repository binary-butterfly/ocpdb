"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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
from flask_openapi.schema import AnyOfField, BooleanField, DateTimeField, IntegerField, StringField
from validataclass.validators import DataclassValidator

from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.models.evse import EvseStatus
from webapp.public_api.base_blueprint import BaseBlueprint
from webapp.shared.ocpi_schema import all_evse_components

from .evse_handler import EvseHandler
from .evse_search_queries import EvseSearchQuery


class EvseBlueprint(BaseBlueprint):
    documented = True
    evse_handler: EvseHandler

    def __init__(self):
        self.evse_handler = EvseHandler(
            **self.get_base_handler_dependencies(),
            evse_repository=dependencies.get_evse_repository(),
        )

        super().__init__('evse', __name__, url_prefix='/api/public/v1/evses')

        self.add_url_rule(
            '',
            view_func=EvseListMethodView.as_view(
                'evses',
                **self.get_base_method_view_dependencies(),
                evse_handler=self.evse_handler,
            ),
        )
        self.add_url_rule(
            '/<int:evse_id>',
            view_func=EvseItemMethodView.as_view(
                'evse',
                **self.get_base_method_view_dependencies(),
                evse_handler=self.evse_handler,
            ),
        )


class EvseBaseMethodView(BaseMethodView):
    evse_handler: EvseHandler

    def __init__(self, *args, evse_handler: EvseHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.evse_handler = evse_handler


class EvseListMethodView(EvseBaseMethodView):
    search_query_validator = DataclassValidator(EvseSearchQuery)

    @document(
        description='Get list of EVSEs',
        query=[
            Parameter(
                'sorted_by',
                schema=AnyOfField(
                    allowed_values=['id', 'created', 'modified', 'last_updated'],
                    required=False,
                    default='id',
                ),
            ),
            Parameter(
                'status',
                schema=AnyOfField(allowed_values=[s.value for s in EvseStatus], required=False),
                example='AVAILABLE',
                description='Filter by EVSE status',
            ),
            Parameter(
                'statuses',
                schema=StringField(required=False),
                example='AVAILABLE,CHARGING',
                description='Comma separated list of statuses to filter by',
            ),
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
                description='Source to exclude',
            ),
            Parameter(
                'exclude_source_uids',
                schema=StringField(required=False),
                example='bnetza_api,something_else',
                description='Comma separated list of sources which should be excluded',
            ),
            Parameter(
                'location_id',
                schema=IntegerField(required=False, minimum=1),
                example=1,
                description='Filter by location ID',
            ),
            Parameter(
                'last_updated_since',
                schema=DateTimeField(),
                example='2023-01-01T00:00:00Z',
                description='Filter EVSEs updated since this timestamp',
            ),
            Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
            Parameter(
                'strict',
                schema=BooleanField(),
                description='If set to true, all additional fields will be omitted for full OCPI compatibility.',
            ),
        ],
        response=[Response(ResponseData(SchemaListReference('EVSE'), ExampleListReference('EVSE')))],
        components=all_evse_components,
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        evses = self.evse_handler.get_evses(
            search_query,
            strict=self.request_helper.get_query_args().get('strict') == 'true',
        )
        return self.jsonify_paginated_response(evses, search_query)


class EvseItemMethodView(EvseBaseMethodView):
    @document(
        description='Get single EVSE',
        path=[Parameter('evse_id', schema=IntegerField(minimum=1))],
        response=[Response(ResponseData(SchemaReference('EVSE'), ExampleReference('EVSE')))],
        query=[
            Parameter(
                'strict',
                schema=BooleanField(),
                description='If set to true, all additional fields will be omitted for full OCPI compatibility.',
            ),
        ],
        components=all_evse_components,
    )
    @cross_origin()
    def get(self, evse_id: int):
        evse = self.evse_handler.get_evse(
            evse_id,
            strict=self.request_helper.get_query_args().get('strict') == 'true',
        )

        return jsonify(evse)
