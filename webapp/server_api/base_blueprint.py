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

import hmac
from hashlib import sha256
from flask import current_app, request
from webapp.common.blueprint import Blueprint
from webapp.common.exceptions import AppAccessDeniedException


class ServerApiBaseBlueprint(Blueprint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.before_request
        def before_request():
            if not request.authorization \
                    or not request.authorization.username \
                    or not request.authorization.password \
                    or request.authorization.username not in current_app.config['SERVER_AUTH_USERS']:
                raise AppAccessDeniedException
            if not hmac.compare_digest(
                    sha256(request.authorization.password.encode()).hexdigest(),
                    current_app.config['SERVER_AUTH_USERS'][request.authorization.username]['hash']
            ):
                raise AppAccessDeniedException

        self.load_routes()

    def load_routes(self, *args, **kwargs):
        raise Exception('implementation required')

