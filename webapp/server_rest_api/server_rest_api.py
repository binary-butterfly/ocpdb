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

from flask import Response, request

from webapp.common.base_blueprint import BaseBlueprint

from .base_blueprint import ServerApiBaseBlueprint
from .bnetza.bnetza_import_rest_api import BnetzaImportBlueprint
from .giroe.giroe_rest_api import GiroeBlueprint


class ServerRestApi(BaseBlueprint):
    documentation_base = True
    documentation_auth = False
    blueprints: list[type[ServerApiBaseBlueprint]] = []

    def __init__(self):
        super().__init__('server', __name__, url_prefix='/api/server/v1')
        self.blueprints = [
            GiroeBlueprint,
            BnetzaImportBlueprint,
        ]
        for blueprint in self.blueprints:
            self.register_blueprint(blueprint())

        @self.after_request
        def after_request(response: Response):
            if not request.path.startswith('/api/server/v1'):
                return response

            log_fragments = [f'{request.method.upper()} {request.full_path}: HTTP {response.status}']
            if request.data:
                if request.mimetype == 'application/json':
                    log_fragments.append(f'>> {request.data.decode()}')
                else:
                    log_fragments.append(f'>> binary data with {len(request.data)} byte')
            if response.data and response.data.decode().strip():
                log_fragments.append(f'<< {response.data.decode().strip()}')

            return response
