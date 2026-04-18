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

from webapp.common.response import empty_json_response
from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.server_rest_api.base_blueprint import ServerApiBaseBlueprint

from .datex2_handler import Datex2Handler


class Datex2ImportBlueprint(ServerApiBaseBlueprint):
    datex2_handler: Datex2Handler

    def __init__(self):
        self.datex2_handler = Datex2Handler(
            **self.get_base_handler_dependencies(),
            import_services=dependencies.get_import_services(),
        )
        super().__init__('datex2', __name__, url_prefix='/datex')

        for version_url, version_name in (('v3.5', 'v3_5'), ('v3.7', 'v3_7')):
            static_view = Datex2StaticMethodView.as_view(
                f'datex2_{version_name}_static',
                **self.get_base_method_view_dependencies(),
                datex2_handler=self.datex2_handler,
            )
            static_view.skip_basic_auth = True
            self.add_url_rule(
                f'/{version_url}/<source_uid>/static',
                view_func=static_view,
                methods=['POST'],
            )
            realtime_view = Datex2RealtimeMethodView.as_view(
                f'datex2_{version_name}_realtime',
                **self.get_base_method_view_dependencies(),
                datex2_handler=self.datex2_handler,
            )
            realtime_view.skip_basic_auth = True
            self.add_url_rule(
                f'/{version_url}/<source_uid>/realtime',
                view_func=realtime_view,
                methods=['POST'],
            )


class Datex2BaseMethodView(BaseMethodView):
    datex2_handler: Datex2Handler

    def __init__(self, *args, datex2_handler: Datex2Handler, **kwargs):
        super().__init__(*args, **kwargs)
        self.datex2_handler = datex2_handler


class Datex2StaticMethodView(Datex2BaseMethodView):
    def post(self, source_uid: str):
        self.datex2_handler.authenticate(source_uid)
        data = self.request_helper.get_parsed_json()
        self.datex2_handler.handle_static_push(source_uid, data)
        return empty_json_response(), 204


class Datex2RealtimeMethodView(Datex2BaseMethodView):
    def post(self, source_uid: str):
        self.datex2_handler.authenticate(source_uid)
        data = self.request_helper.get_parsed_json()
        self.datex2_handler.handle_realtime_push(source_uid, data)
        return empty_json_response(), 204
