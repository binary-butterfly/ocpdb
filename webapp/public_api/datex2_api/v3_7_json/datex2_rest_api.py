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
    ExampleReference,
    Response,
    ResponseData,
    SchemaReference,
    document,
)

from webapp.common.dataclass import filter_unset_value
from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.public_api.base_blueprint import BaseBlueprint
from webapp.shared.datex2.v3_7_json_static.schema import all_datex2_v37_static_components

from .datex2_handler import Datex2V37JSONHandler


class Datex2V37JSONBlueprint(BaseBlueprint):
    documented = True
    datex2_handler: Datex2V37JSONHandler

    def __init__(self):
        self.datex2_handler = Datex2V37JSONHandler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
        )

        super().__init__('datex2_v3_7', __name__, url_prefix='/v3.7')

        self.add_url_rule(
            '/json/static',
            view_func=Datex2V37JSONStaticMethodView.as_view(
                'datex_v3_7_json_static',
                **self.get_base_method_view_dependencies(),
                datex2_handler=self.datex2_handler,
            ),
        )


class Datex2V37JSONStaticMethodView(BaseMethodView):
    datex2_handler: Datex2V37JSONHandler

    def __init__(self, *args, datex2_handler: Datex2V37JSONHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.datex2_handler = datex2_handler

    @document(
        description='Get static DATEX II v3.7 energy infrastructure data',
        response=[
            Response(
                ResponseData(
                    SchemaReference('Datex2V37StaticPayload'),
                    ExampleReference('Datex2V37StaticPayload'),
                ),
            ),
        ],
        components=all_datex2_v37_static_components,
    )
    @cross_origin()
    def get(self):
        result = self.datex2_handler.get_datex2_payload()

        return jsonify(filter_unset_value(result.to_dict()))
