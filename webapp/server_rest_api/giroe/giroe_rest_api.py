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

from validataclass.validators import DataclassValidator

from webapp.common.response import empty_json_response
from webapp.common.rest import BaseMethodView
from webapp.common.server_auth import ServerAuthRole, require_role
from webapp.dependencies import dependencies
from webapp.server_rest_api.base_blueprint import ServerApiBaseBlueprint
from webapp.services.import_services.giroe.giroe_validator import LocationInput

from .giroe_handler import GiroeHandler
from .giroe_validator import ConnectorPatchInput


class GiroeBlueprint(ServerApiBaseBlueprint):
    documented = True
    giroe_handler: GiroeHandler

    def __init__(self):
        self.giroe_handler = GiroeHandler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
            evse_repository=dependencies.get_evse_repository(),
            import_services=dependencies.get_import_services(),
        )
        super().__init__('giroe', __name__, url_prefix='/giroe')

        self.add_url_rule(
            '/locations/<int:location_id>',
            view_func=GiroeLocationMethodView.as_view(
                'location',
                **self.get_base_method_view_dependencies(),
                giroe_handler=self.giroe_handler,
            ),
            methods=['PUT', 'DELETE'],
        )
        self.add_url_rule(
            '/connectors/<connector_uid>',
            view_func=GiroeConnectorMethodView.as_view(
                'connector',
                **self.get_base_method_view_dependencies(),
                giroe_handler=self.giroe_handler,
            ),
            methods=['PATCH'],
        )


class GiroeBaseMethodView(BaseMethodView):
    giroe_handler: GiroeHandler

    def __init__(self, *args, giroe_handler: GiroeHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.giroe_handler = giroe_handler


class GiroeLocationMethodView(GiroeBaseMethodView):
    location_validator = DataclassValidator(LocationInput)

    @require_role(ServerAuthRole.GIROE)
    def put(self, location_id: int):
        input_data = self.validate_request(self.location_validator)

        self.giroe_handler.handle_put_location(location_id, input_data)

        return empty_json_response(), 204

    @require_role(ServerAuthRole.GIROE)
    def delete(self, location_id: int):
        self.giroe_handler.handle_delete_location(location_id)

        return empty_json_response(), 204


class GiroeConnectorMethodView(GiroeBaseMethodView):
    connector_patch_validator = DataclassValidator(ConnectorPatchInput)

    @require_role(ServerAuthRole.GIROE)
    def patch(self, connector_uid: str):
        connector_input = self.validate_request(self.connector_patch_validator)

        self.giroe_handler.handle_patch_connector(connector_uid, connector_input)

        return empty_json_response(), 204
