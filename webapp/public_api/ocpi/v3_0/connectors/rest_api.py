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
from webapp.public_api.base_blueprint import BaseBlueprint
from webapp.public_api.connector_api.connector_handler import ConnectorHandler
from webapp.public_api.connector_api.connector_search_queries import ConnectorSearchQuery
from webapp.shared.ocpi_schema import all_connector_components


class Ocpi30ConnectorBlueprint(BaseBlueprint):
    documented = True
    connector_handler: ConnectorHandler

    def __init__(self):
        self.connector_handler = ConnectorHandler(
            **self.get_base_handler_dependencies(),
            connector_repository=dependencies.get_connector_repository(),
        )

        super().__init__('ocpi_30_connectors', __name__, url_prefix='/connectors')

        self.add_url_rule(
            '',
            view_func=Ocpi30ConnectorListMethodView.as_view(
                'ocpi_30_connectors',
                **self.get_base_method_view_dependencies(),
                connector_handler=self.connector_handler,
            ),
        )
        self.add_url_rule(
            '/<int:connector_id>',
            view_func=Ocpi30ConnectorItemMethodView.as_view(
                'ocpi_30_connector',
                **self.get_base_method_view_dependencies(),
                connector_handler=self.connector_handler,
            ),
        )


class Ocpi30ConnectorBaseMethodView(BaseMethodView):
    connector_handler: ConnectorHandler

    def __init__(self, *args, connector_handler: ConnectorHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.connector_handler = connector_handler


class Ocpi30ConnectorListMethodView(Ocpi30ConnectorBaseMethodView):
    search_query_validator = DataclassValidator(ConnectorSearchQuery)

    @document(
        description='Get list of Connectors',
        query=[
            Parameter(
                'sorted_by',
                schema=AnyOfField(
                    allowed_values=['id', 'created', 'modified', 'last_updated'],
                    required=False,
                    default='id',
                ),
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
                'evse_id',
                schema=IntegerField(required=False, minimum=1),
                example=1,
                description='Filter by EVSE ID',
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
                description='Filter Connectors updated since this timestamp',
            ),
            Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
            Parameter(
                'strict',
                schema=BooleanField(),
                description='If set to true, all additional fields will be omitted for full OCPI compatibility.',
            ),
        ],
        response=[Response(ResponseData(SchemaListReference('Connector'), ExampleListReference('Connector')))],
        components=all_connector_components,
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        connectors = self.connector_handler.get_connectors(
            search_query,
            strict=self.request_helper.get_query_args().get('strict') == 'true',
        )
        return self.jsonify_paginated_response(connectors, search_query)


class Ocpi30ConnectorItemMethodView(Ocpi30ConnectorBaseMethodView):
    @document(
        description='Get single Connector',
        path=[Parameter('connector_id', schema=IntegerField(minimum=1))],
        response=[Response(ResponseData(SchemaReference('Connector'), ExampleReference('Connector')))],
        query=[
            Parameter(
                'strict',
                schema=BooleanField(),
                description='If set to true, all additional fields will be omitted for full OCPI compatibility.',
            ),
        ],
        components=all_connector_components,
    )
    @cross_origin()
    def get(self, connector_id: int):
        connector = self.connector_handler.get_connector(
            connector_id,
            strict=self.request_helper.get_query_args().get('strict') == 'true',
        )

        return jsonify(connector)
