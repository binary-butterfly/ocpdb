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
from webapp.shared.v3_0.tariff_association_schema import all_tariff_association_components

from .tariff_association_handler import TariffAssociationHandler
from .tariff_association_search_queries import TariffAssociationSearchQuery


class Ocpi30TariffAssociationBlueprint(BaseBlueprint):
    documented = True
    tariff_association_handler: TariffAssociationHandler

    def __init__(self):
        self.tariff_association_handler = TariffAssociationHandler(
            **self.get_base_handler_dependencies(),
            tariff_association_repository=dependencies.get_tariff_association_repository(),
        )

        super().__init__('ocpi_30_tariff_associations', __name__, url_prefix='/tariff-associations')

        self.add_url_rule(
            '',
            view_func=Ocpi30TariffAssociationListMethodView.as_view(
                'ocpi_30_tariff_associations',
                **self.get_base_method_view_dependencies(),
                tariff_association_handler=self.tariff_association_handler,
            ),
        )
        self.add_url_rule(
            '/<int:tariff_association_id>',
            view_func=Ocpi30TariffAssociationItemMethodView.as_view(
                'ocpi_30_tariff_association',
                **self.get_base_method_view_dependencies(),
                tariff_association_handler=self.tariff_association_handler,
            ),
        )


class Ocpi30TariffAssociationBaseMethodView(BaseMethodView):
    tariff_association_handler: TariffAssociationHandler

    def __init__(self, *args, tariff_association_handler: TariffAssociationHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.tariff_association_handler = tariff_association_handler


class Ocpi30TariffAssociationListMethodView(Ocpi30TariffAssociationBaseMethodView):
    search_query_validator = DataclassValidator(TariffAssociationSearchQuery)

    @document(
        description='Get list of TariffAssociations',
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
                description='Filter by Tariff ID',
            ),
            Parameter(
                'last_updated_since',
                schema=DateTimeField(),
                example='2023-01-01T00:00:00Z',
                description='Filter TariffAssociations updated since this timestamp',
            ),
            Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
        ],
        response=[
            Response(ResponseData(SchemaListReference('TariffAssociation'), ExampleListReference('TariffAssociation'))),
        ],
        components=all_tariff_association_components,
    )
    @cross_origin()
    def get(self):
        search_query = self.validate_query_args(self.search_query_validator)
        tariff_associations = self.tariff_association_handler.get_tariff_associations(search_query)
        return self.jsonify_paginated_response(tariff_associations, search_query)


class Ocpi30TariffAssociationItemMethodView(Ocpi30TariffAssociationBaseMethodView):
    @document(
        description='Get single TariffAssociation',
        path=[Parameter('tariff_association_id', schema=IntegerField(minimum=1))],
        response=[
            Response(ResponseData(SchemaReference('TariffAssociation'), ExampleReference('TariffAssociation'))),
        ],
        components=all_tariff_association_components,
    )
    @cross_origin()
    def get(self, tariff_association_id: int):
        tariff_association = self.tariff_association_handler.get_tariff_association(tariff_association_id)
        return jsonify(tariff_association)
