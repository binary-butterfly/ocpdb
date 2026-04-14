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
from validataclass.validators import DataclassValidator

from webapp.common.dataclass import filter_none_recursive, filter_unset_value, recursive_to_dict
from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.public_api.base_blueprint import BaseBlueprint
from webapp.public_api.datex2_api.location_schema import location_search_query_parameters
from webapp.shared.datex2.v3_5_json_realtime.schema import all_datex2_v35_realtime_components
from webapp.shared.datex2.v3_5_json_static.schema import all_datex2_v35_static_components
from webapp.shared.location_search_queries import LocationApiSearchQuery

from .datex2_handler import Datex2V35JSONHandler


class Datex2V35JSONBlueprint(BaseBlueprint):
    documented = True
    datex2_handler: Datex2V35JSONHandler

    def __init__(self):
        self.datex2_handler = Datex2V35JSONHandler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
            tariff_repository=dependencies.get_tariff_repository(),
        )

        super().__init__('datex2_v3_5', __name__, url_prefix='/v3.5')

        self.add_url_rule(
            '/json/static',
            view_func=Datex2V35JSONStaticMethodView.as_view(
                'datex_v3_5_json_static',
                **self.get_base_method_view_dependencies(),
                datex2_handler=self.datex2_handler,
            ),
        )

        self.add_url_rule(
            '/json/realtime',
            view_func=Datex2V35JSONRealtimeMethodView.as_view(
                'datex_v3_5_json_realtime',
                **self.get_base_method_view_dependencies(),
                datex2_handler=self.datex2_handler,
            ),
        )

        self.add_url_rule(
            '/json/mobilithek/realtime',
            view_func=Datex2V35JSONMobilithekRealtimeMethodView.as_view(
                'datex_v3_5_json_mobilithek_realtime',
                **self.get_base_method_view_dependencies(),
                datex2_handler=self.datex2_handler,
            ),
        )


class Datex2V35JSONStaticMethodView(BaseMethodView):
    datex2_handler: Datex2V35JSONHandler
    search_query_validator = DataclassValidator(LocationApiSearchQuery)

    def __init__(self, *args, datex2_handler: Datex2V35JSONHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.datex2_handler = datex2_handler

    @document(
        description='Get static DATEX II v3.5 energy infrastructure data. Warning: this endpoint is experimental!',
        query=location_search_query_parameters,
        response=[
            Response(
                ResponseData(
                    SchemaReference('Datex2V35StaticPayload'),
                    ExampleReference('Datex2V35StaticPayload'),
                ),
            ),
        ],
        components=all_datex2_v35_static_components,
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        result = self.datex2_handler.get_datex2_payload(search_query)

        return jsonify(filter_unset_value(result.to_dict()))


class Datex2V35JSONRealtimeMethodView(BaseMethodView):
    datex2_handler: Datex2V35JSONHandler
    search_query_validator = DataclassValidator(LocationApiSearchQuery)

    def __init__(self, *args, datex2_handler: Datex2V35JSONHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.datex2_handler = datex2_handler

    @document(
        description='Get realtime DATEX II v3.5 energy infrastructure status data. Warning: this endpoint is experimental!',
        query=location_search_query_parameters,
        response=[
            Response(
                ResponseData(
                    SchemaReference('Datex2V35RealtimePayload'),
                    ExampleReference('Datex2V35RealtimePayload'),
                ),
            ),
        ],
        components=all_datex2_v35_realtime_components,
    )
    @cross_origin()
    def get(self):
        search_query: LocationApiSearchQuery = self.validate_query_args(self.search_query_validator)
        result = self.datex2_handler.get_datex2_realtime_payload(search_query)

        return jsonify(filter_unset_value(result.to_dict()))


class Datex2V35JSONMobilithekRealtimeMethodView(BaseMethodView):
    datex2_handler: Datex2V35JSONHandler
    search_query_validator = DataclassValidator(LocationApiSearchQuery)

    def __init__(self, *args, datex2_handler: Datex2V35JSONHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.datex2_handler = datex2_handler

    @cross_origin()
    def get(self):
        search_query: LocationApiSearchQuery = self.validate_query_args(self.search_query_validator)

        result = self.datex2_handler.get_datex2_mobilithek_realtime(
            search_query=search_query,
        )

        return jsonify(filter_none_recursive(filter_unset_value(recursive_to_dict(result))))
