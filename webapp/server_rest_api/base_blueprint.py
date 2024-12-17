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

from flask import current_app, request

from webapp.common.base_blueprint import BaseBlueprint
from webapp.dependencies import dependencies


class ServerApiBaseBlueprint(BaseBlueprint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.before_request
        def before_request():
            if getattr(current_app.view_functions[request.endpoint], 'skip_basic_auth', False):
                return
            # Authenticate user via Basic Auth (raises ServerApiUnauthorizedException if unauthenticated)
            server_auth_helper = dependencies.get_server_auth_helper()
            server_auth_helper.authenticate_request(request)
