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

from typing import List, Type

from flask import request, Response

from webapp.common.base_blueprint import BaseBlueprint
from webapp.extensions import logger
from .base_blueprint import ServerApiBaseBlueprint
from .giroe.giroe_rest_api import GiroeBlueprint


class ServerRestApi(BaseBlueprint):
    documentation_base = True
    blueprints: List[Type[ServerApiBaseBlueprint]] = []

    def __init__(self):
        super().__init__('server', __name__, url_prefix='/api/server/v1')
        self.blueprints = [
            GiroeBlueprint,
        ]
        for blueprint in self.blueprints:
            self.register_blueprint(blueprint())

        @self.after_request
        def after_request(response: Response):
            if not request.path.startswith('/api/server'):
                return response
            logger.info(
                'server-api',
                "\n".join([
                    f"{request.full_path}: HTTP {response.status}\n",
                    *([f'<< {request.data.decode()}'] if request.method in ["POST", "PUT", "PATCH"] and request.data else []),
                    *([f'>> {response.data.decode()}'] if response.data else []),
                ]),
            )
            return response
