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
from webapp.public_api.charging_station_api.charging_station_handler import ChargingStationHandler
from webapp.public_api.charging_station_api.charging_station_search_queries import ChargingStationSearchQuery
from webapp.shared.ocpi_schema import all_charging_station_components


class Ocpi30ChargingStationBlueprint(BaseBlueprint):
    documented = True
    charging_station_handler: ChargingStationHandler

    def __init__(self):
        self.charging_station_handler = ChargingStationHandler(
            **self.get_base_handler_dependencies(),
            charging_station_repository=dependencies.get_charging_station_repository(),
        )

        super().__init__('ocpi_30_charging_stations', __name__, url_prefix='/charge-stations')

        self.add_url_rule(
            '',
            view_func=Ocpi30ChargingStationListMethodView.as_view(
                'ocpi_30_charging_stations',
                **self.get_base_method_view_dependencies(),
                charging_station_handler=self.charging_station_handler,
            ),
        )
        self.add_url_rule(
            '/<int:charging_station_id>',
            view_func=Ocpi30ChargingStationItemMethodView.as_view(
                'ocpi_30_charging_station',
                **self.get_base_method_view_dependencies(),
                charging_station_handler=self.charging_station_handler,
            ),
        )


class Ocpi30ChargingStationBaseMethodView(BaseMethodView):
    charging_station_handler: ChargingStationHandler

    def __init__(self, *args, charging_station_handler: ChargingStationHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.charging_station_handler = charging_station_handler


class Ocpi30ChargingStationListMethodView(Ocpi30ChargingStationBaseMethodView):
    search_query_validator = DataclassValidator(ChargingStationSearchQuery)

    @document(
        description='Get list of ChargingStations',
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
                'location_id',
                schema=IntegerField(required=False, minimum=1),
                example=1,
                description='Filter by location ID',
            ),
            Parameter(
                'last_updated_since',
                schema=DateTimeField(),
                example='2023-01-01T00:00:00Z',
                description='Filter ChargingStations updated since this timestamp',
            ),
            Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
            Parameter(
                'strict',
                schema=BooleanField(),
                description='If set to true, all additional fields will be omitted for full OCPI compatibility.',
            ),
        ],
        response=[
            Response(ResponseData(SchemaListReference('ChargingStation'), ExampleListReference('ChargingStation')))
        ],
        components=all_charging_station_components,
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        charging_stations = self.charging_station_handler.get_charging_stations(
            search_query,
            strict=self.request_helper.get_query_args().get('strict') == 'true',
        )
        return self.jsonify_paginated_response(charging_stations, search_query)


class Ocpi30ChargingStationItemMethodView(Ocpi30ChargingStationBaseMethodView):
    @document(
        description='Get single ChargingStation',
        path=[Parameter('charging_station_id', schema=IntegerField(minimum=1))],
        response=[Response(ResponseData(SchemaReference('ChargingStation'), ExampleReference('ChargingStation')))],
        query=[
            Parameter(
                'strict',
                schema=BooleanField(),
                description='If set to true, all additional fields will be omitted for full OCPI compatibility.',
            ),
        ],
        components=all_charging_station_components,
    )
    @cross_origin()
    def get(self, charging_station_id: int):
        charging_station = self.charging_station_handler.get_charging_station(
            charging_station_id,
            strict=self.request_helper.get_query_args().get('strict') == 'true',
        )

        return jsonify(charging_station)
