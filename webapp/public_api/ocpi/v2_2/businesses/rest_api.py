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
from webapp.public_api.business_api.business_handler import BusinessHandler
from webapp.public_api.business_api.business_search_queries import BusinessSearchQuery
from webapp.shared.ocpi_schema import all_business_components


class OcpiBusinessBlueprint(BaseBlueprint):
    documented = True
    business_handler: BusinessHandler

    def __init__(self):
        self.business_handler = BusinessHandler(
            **self.get_base_handler_dependencies(),
            business_repository=dependencies.get_business_repository(),
        )

        super().__init__('ocpi_businesses', __name__, url_prefix='/businesses')

        self.add_url_rule(
            '',
            view_func=OcpiBusinessListMethodView.as_view(
                'ocpi_businesses',
                **self.get_base_method_view_dependencies(),
                business_handler=self.business_handler,
            ),
        )
        self.add_url_rule(
            '/<int:business_id>',
            view_func=OcpiBusinessItemMethodView.as_view(
                'ocpi_business',
                **self.get_base_method_view_dependencies(),
                business_handler=self.business_handler,
            ),
        )


class OcpiBusinessBaseMethodView(BaseMethodView):
    business_handler: BusinessHandler

    def __init__(self, *args, business_handler: BusinessHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_handler = business_handler


class OcpiBusinessListMethodView(OcpiBusinessBaseMethodView):
    search_query_validator = DataclassValidator(BusinessSearchQuery)

    @document(
        description='Get list of Businesses',
        query=[
            Parameter(
                'sorted_by',
                schema=AnyOfField(allowed_values=['name', 'created', 'modified'], required=False, default='name'),
            ),
            Parameter('name', schema=StringField(required=False), description='Filter by name (contains)'),
            Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
        ],
        response=[
            Response(ResponseData(SchemaListReference('BusinessDetails'), ExampleListReference('BusinessDetails')))
        ],
        components=all_business_components,
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        businesses = self.business_handler.search_businesses(search_query)
        return self.jsonify_paginated_response(businesses, search_query)


class OcpiBusinessItemMethodView(OcpiBusinessBaseMethodView):
    @document(
        description='Get single Business',
        path=[Parameter('business_id', schema=IntegerField(minimum=1))],
        response=[Response(ResponseData(SchemaReference('BusinessDetails'), ExampleReference('BusinessDetails')))],
        components=all_business_components,
    )
    @cross_origin()
    def get(self, business_id: int):
        business = self.business_handler.get_business_by_id(business_id)
        return jsonify(business)
