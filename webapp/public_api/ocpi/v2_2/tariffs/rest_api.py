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
from flask_openapi.schema import AnyOfField, DateTimeField, IntegerField, StringField
from validataclass.validators import DataclassValidator

from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.public_api.base_blueprint import BaseBlueprint
from webapp.public_api.ocpi.v3_0.tariff_associations.tariff_association_search_queries import (
    TariffAssociationSearchQuery,
)
from webapp.shared.tariff_schema import all_tariff_components

from .tariff_handler import TariffHandler


class OcpiTariffBlueprint(BaseBlueprint):
    documented = True
    tariff_handler: TariffHandler

    def __init__(self):
        self.tariff_handler = TariffHandler(
            **self.get_base_handler_dependencies(),
            tariff_association_repository=dependencies.get_tariff_association_repository(),
        )

        super().__init__('ocpi_tariffs', __name__, url_prefix='/tariffs')

        self.add_url_rule(
            '',
            view_func=OcpiTariffListMethodView.as_view(
                'ocpi_tariffs',
                **self.get_base_method_view_dependencies(),
                tariff_handler=self.tariff_handler,
            ),
        )
        self.add_url_rule(
            '/<int:tariff_id>',
            view_func=OcpiTariffItemMethodView.as_view(
                'ocpi_tariff',
                **self.get_base_method_view_dependencies(),
                tariff_handler=self.tariff_handler,
            ),
        )


class OcpiTariffBaseMethodView(BaseMethodView):
    tariff_handler: TariffHandler

    def __init__(self, *args, tariff_handler: TariffHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.tariff_handler = tariff_handler


class OcpiTariffListMethodView(OcpiTariffBaseMethodView):
    search_query_validator = DataclassValidator(TariffAssociationSearchQuery)

    @document(
        description='Get list of Tariffs (OCPI 2.2 format, merging tariff data with tariff association metadata)',
        query=[
            Parameter(
                'sorted_by',
                schema=AnyOfField(
                    allowed_values=['id', 'created', 'modified', 'last_updated'],
                    required=False,
                    default='id',
                ),
            ),
            Parameter('source_uid', schema=StringField(required=False), example='datex2_enbw'),
            Parameter(
                'source_uids',
                schema=StringField(required=False),
                example='datex2_enbw,something_else',
                description='Comma separated list of sources',
            ),
            Parameter(
                'exclude_source_uid',
                schema=StringField(required=False),
                example='datex2_enbw',
                description='Source to exclude',
            ),
            Parameter(
                'exclude_source_uids',
                schema=StringField(required=False),
                example='datex2_enbw,something_else',
                description='Comma separated list of sources which should be excluded',
            ),
            Parameter(
                'tariff_id',
                schema=IntegerField(required=False, minimum=1),
                example=1,
                description='Filter by underlying Tariff ID',
            ),
            Parameter(
                'last_updated_since',
                schema=DateTimeField(),
                example='2023-01-01T00:00:00Z',
                description='Filter Tariffs updated since this timestamp',
            ),
            Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
        ],
        response=[Response(ResponseData(SchemaListReference('Tariff'), ExampleListReference('Tariff')))],
        components=all_tariff_components,
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        tariffs = self.tariff_handler.get_tariffs(search_query)
        return self.jsonify_paginated_response(tariffs, search_query)


class OcpiTariffItemMethodView(OcpiTariffBaseMethodView):
    @document(
        description='Get single Tariff (OCPI 2.2 format)',
        path=[Parameter('tariff_id', schema=IntegerField(minimum=1))],
        response=[Response(ResponseData(SchemaReference('Tariff'), ExampleReference('Tariff')))],
        components=all_tariff_components,
    )
    @cross_origin()
    def get(self, tariff_id: int):
        tariff = self.tariff_handler.get_tariff(tariff_id)
        return jsonify(tariff)
