# encoding: utf-8

"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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

from flask import Flask
from webapp.openapi.openapi_decorator import document, Parameter,  ErrorResponse, EmptyResponse, Schema, Request
from ..base_method_view import ServerApiBaseMethodView
from .giroe_handler import GiroeHandler
from ..response import ServerApiResponse
from ..base_blueprint import ServerApiBaseBlueprint
from webapp.common.request_helper import ensure_role
from webapp.dependencies import dependencies


class GiroeBlueprint(ServerApiBaseBlueprint):
    documented = True
    giroe_handler: GiroeHandler

    def __init__(self, app: Flask):
        self.giroe_handler = GiroeHandler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
            evse_repository=dependencies.get_evse_repository(),
            connector_repository=dependencies.get_connector_repository(),
        )
        super().__init__('giroe', __name__, url_prefix='/giroe')

    def load_routes(self):
        self.add_url_rule(
            '/locations/<int:location_id>',
            view_func=GiroeLocationMethodView.as_view(
                'location',
                **self.get_base_method_view_dependencies(),
                giroe_handler=self.giroe_handler
            ),
            methods=['PUT', 'DELETE']
        )
        self.add_url_rule(
            '/connectors/<int:connector_id>',
            view_func=GiroeConnectorMethodView.as_view(
                'connector',
                **self.get_base_method_view_dependencies(),
                giroe_handler=self.giroe_handler
            ),
            methods=['PATCH']
        )


class GiroeBaseMethodView(ServerApiBaseMethodView):
    giroe_handler: GiroeHandler

    def __init__(self, *args, giroe_handler: GiroeHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.giroe_handler = giroe_handler


class GiroeLocationMethodView(GiroeBaseMethodView):

    @document(
        description='Puts a location.',
        path=[Parameter('location_id', schema=int, example=1)],
        request=Request('location-put-request', 'location-put-request-example'),
        response=[EmptyResponse(), ErrorResponse()],
        components=[Schema('Location', 'location-schema', 'location-example')]
    )
    @ensure_role('giroe')
    def put(self, location_id: int):
        return ServerApiResponse.success(
            self.giroe_handler.handle_put_location(
                location_id,
                self.request_helper.get_parsed_json()
            )
        )

    @document(
        description='Deletes a location.',
        path=[Parameter('location_id', schema=int, example=1)],
        response=[EmptyResponse(), ErrorResponse()],
    )
    @ensure_role('giroe')
    def delete(self, location_id: int):
        return ServerApiResponse.success(
            self.giroe_handler.handle_delete_location(
                location_id
            )
        )


class GiroeConnectorMethodView(GiroeBaseMethodView):

    @document(
        description='Patches an connector.',
        path=[Parameter('connector_id', schema=int, example=1)],
        request=Request('connector-patch-request', 'connector-patch-request-example'),
        response=[EmptyResponse(), ErrorResponse()],
        components=[Schema('Connector', 'connector-schema', 'connector-example')]
    )
    @ensure_role('giroe')
    def patch(self, connector_id: int):
        return ServerApiResponse.success(
            self.giroe_handler.handle_patch_connector(
                connector_id,
                self.request_helper.get_parsed_json()
            )
        )



