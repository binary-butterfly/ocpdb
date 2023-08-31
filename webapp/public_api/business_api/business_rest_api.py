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
from typing import Optional

from flask import jsonify, request
from flask_cors import cross_origin
from validataclass.validators import DataclassValidator

from webapp.dependencies import dependencies
from webapp.common.base_blueprint import BaseBlueprint
from .business_search_queries import BusinessSearchQuery
from webapp.common.rest import BaseMethodView
from .business_handler import BusinessHandler


class BusinessBlueprint(BaseBlueprint):
    business_handler: BusinessHandler

    def __init__(self):
        self.business_handler = BusinessHandler(
            **self.get_base_handler_dependencies(),
            business_repository=dependencies.get_business_repository(),
        )

        super().__init__('businesses', __name__, url_prefix='/api/public/v1/businesses')

        self.add_url_rule(
            '/<int:business_id>',
            view_func=BusinessIdMethodView.as_view(
                'id',
                **self.get_base_method_view_dependencies(),
                business_handler=self.business_handler,
            ),

        )

        self.add_url_rule(
            '/<string:business_name>',
            view_func=BusinessNameMethodView.as_view(
                'name',
                **self.get_base_method_view_dependencies(),
                business_handler=self.business_handler,
            ),

        )
        self.add_url_rule(
            '',
            view_func=ViewAllMethodView.as_view(
                'all',
                **self.get_base_method_view_dependencies(),
                business_handler=self.business_handler,
            ),

        )


class BusinessIdMethodView(BaseMethodView):
    business_handler: BusinessHandler

    def __init__(self, *args, business_handler: BusinessHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_handler = business_handler

    @cross_origin()
    def get(self, business_id: int):
        business = self.business_handler.get_business_by_id(business_id)
        return jsonify(business.to_dict())


class BusinessNameMethodView(BaseMethodView):
    business_handler: BusinessHandler

    def __init__(self, *args, business_handler: BusinessHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_handler = business_handler

    @cross_origin()
    def get(self, business_name: str):
        business = self.business_handler.get_business_by_name(business_name)
        return jsonify(business.to_dict())


class ViewAllMethodView(BaseMethodView):
    business_handler: BusinessHandler

    def __init__(self, *args, business_handler: BusinessHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_handler = business_handler

    @cross_origin()
    def get(self):
        arguments = request.args.to_dict()
        if len(arguments) == 0:
            business = self.business_handler.list_all_businesses()

        else:
            name_validator = DataclassValidator(BusinessSearchQuery)
            query = arguments
            search_query = name_validator.validate(query)
            business = self.business_handler.search_businesses(search_query)

        return jsonify(business)
