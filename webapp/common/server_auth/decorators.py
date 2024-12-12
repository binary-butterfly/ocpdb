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

import functools

from webapp.dependencies import dependencies

from .server_auth_helper import ServerAuthHelper
from .server_auth_users import ServerAuthRole


def require_roles(*roles: ServerAuthRole, require_all: bool = False):
    """
    Decorator for server API view functions that ensures that the authenticated user has the required roles.
    If require_all is True, the user must have ALL of the specified roles, otherwise (default) the user must have
    AT LEAST ONE of the specified roles.

    Raises ServerApiMissingRoleException if the role requirements are not met (or ServerApiUnauthorizedException
    if the request is not authenticated at all).
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check that authenticated user has required roles
            server_auth_helper: ServerAuthHelper = dependencies.get_server_auth_helper()
            server_auth_helper.require_roles(*roles, require_all=require_all)

            # Call wrapped function
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Singular version of require_roles
def require_role(role: ServerAuthRole):
    """
    Decorator for server API view functions that ensures that the authenticated user has the required role.

    Raises ServerApiMissingRoleException if the role requirements are not met (or ServerApiUnauthorizedException
    if the request is not authenticated at all).
    """
    return require_roles(role)


def skip_basic_auth(fn):
    fn.skip_basic_auth = True
    return fn
