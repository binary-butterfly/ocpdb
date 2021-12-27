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

from typing import List
from validataclass.exceptions import ValidationError
from flask import Flask, request, Response
from webapp.common.blueprint import Blueprint
from webapp.extensions import logger
from .response import ServerApiResponse
from webapp.common.exceptions import AppException

from .giroe.giroe_rest_api import GiroeBlueprint


catch_all_blueprint = Blueprint('server_api_catch_all', 'server_api_catch_all')


@catch_all_blueprint.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path: str):
    return ServerApiResponse.error(code='not_found', http_status=404)


class ServerApi(Blueprint):
    documentation_base = True
    blueprints: List[Blueprint] = []

    def __init__(self, app: Flask):
        super().__init__('server', __name__, url_prefix='/server/v1')
        self.blueprints = [
            GiroeBlueprint(app)
        ]
        for blueprint in self.blueprints:
            self.register_blueprint(blueprint)

        # finally: catch all other paths and return 404 in server format
        self.register_blueprint(catch_all_blueprint)

        @self.after_request
        def after_request(response: Response):
            if not request.path.startswith('/server'):
                return response
            logger.info('server-api', "%s: HTTP %s%s\n>> %s" % (
                request.full_path,
                response.status,
                "\n<< %s" % request.data.decode() if request.method in ['POST', 'PUT', 'PATCH'] and request.data else '',
                response.data.decode() if response.data else ''
            ))
            return response

        @self.errorhandler(401)
        def handle_server_api_401(code: int):
            if not request.path.startswith('/server'):
                return
            return ServerApiResponse.error(401)

        @self.errorhandler(ValidationError)
        def handle_server_api_validation_error(exception: ValidationError):
            if not request.path.startswith('/server'):
                return
            return ServerApiResponse.error(http_status=400, code='validation failed', data=exception.to_dict())

        @self.errorhandler(AppException)
        def handle_server_api_exception(exception: AppException):
            if not request.path.startswith('/server'):
                return
            return ServerApiResponse.error(exception=exception)

        @self.errorhandler(Exception)
        def handle_server_api_method_not_allowed(exception: Exception):
            if not request.path.startswith('/server'):
                return
            return ServerApiResponse.error(code='internal_server_error', http_status=500, exception=exception)

