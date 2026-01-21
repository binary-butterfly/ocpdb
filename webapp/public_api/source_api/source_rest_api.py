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
from flask_openapi.schema import AnyOfField, IntegerField, StringField
from validataclass.validators import DataclassValidator

from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.public_api.base_blueprint import BaseBlueprint

from .source_handler import SourceHandler
from .source_schema import source_component
from .source_search_queries import SourceSearchQuery


class SourceBlueprint(BaseBlueprint):
    documented = True
    source_handler: SourceHandler

    def __init__(self):
        self.source_handler = SourceHandler(
            **self.get_base_handler_dependencies(),
            source_repository=dependencies.get_source_repository(),
        )

        super().__init__('sources', __name__, url_prefix='/api/public/v1/sources')

        self.add_url_rule(
            '/<int:source_id>',
            view_func=SourceIdMethodView.as_view(
                'id',
                **self.get_base_method_view_dependencies(),
                source_handler=self.source_handler,
            ),
        )

        self.add_url_rule(
            '',
            view_func=SourceListMethodView.as_view(
                'all',
                **self.get_base_method_view_dependencies(),
                source_handler=self.source_handler,
            ),
        )


class SourceIdMethodView(BaseMethodView):
    source_handler: SourceHandler

    def __init__(self, *args, source_handler: SourceHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.source_handler = source_handler

    @document(
        description='Get a single Source',
        path=[Parameter('source_id', schema=IntegerField(minimum=1))],
        response=[Response(ResponseData(SchemaReference('Source'), ExampleReference('Source')))],
        components=[source_component],
    )
    @cross_origin()
    def get(self, source_id: int):
        source = self.source_handler.get_source_by_id(source_id)
        return jsonify(source)


class SourceListMethodView(BaseMethodView):
    source_handler: SourceHandler
    search_query_validator = DataclassValidator(SourceSearchQuery)

    def __init__(self, *args, source_handler: SourceHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.source_handler = source_handler

    @document(
        description='Get a list of Sources',
        query=[
            Parameter(
                'sorted_by',
                schema=AnyOfField(allowed_values=['uid', 'name', 'created', 'modified'], required=False, default='uid'),
            ),
            Parameter('name', schema=StringField(required=False)),
            Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
        ],
        response=[Response(ResponseData(SchemaListReference('Source'), ExampleListReference('Source')))],
        components=[source_component],
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        sources = self.source_handler.search_sources(search_query)

        return self.jsonify_paginated_response(sources, search_query)
