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

from flask import Request

from webapp.common.contexts import ContextHelper
from .exceptions import ServerApiUnauthorizedException, ServerApiMissingRoleException
from .server_auth_users import ServerAuthDatabase, ServerAuthRole, ServerAuthUser


class ServerAuthHelper:
    """
    Helper class for server API authentication via Basic Auth.
    """
    server_auth_users: ServerAuthDatabase
    context_helper: ContextHelper

    def __init__(self, *, server_auth_users: ServerAuthDatabase, context_helper: ContextHelper):
        self.server_auth_users = server_auth_users
        self.context_helper = context_helper

    def authenticate_request(self, request: Request) -> None:
        """
        Authenticates a request via Basic Auth. Raises ServerApiUnauthorizedException if authentication fails.
        """
        # First check if the Authorization header was set
        if not request.authorization or not request.authorization.username or not request.authorization.password:
            raise ServerApiUnauthorizedException(message='Missing basic auth credentials')

        # Authenticate user with server auth database
        user = self.server_auth_users.authenticate_user(
            request.authorization.username,
            request.authorization.password,
        )

        # Set user in request context
        request_ctx = self.context_helper.get_request_context()
        setattr(request_ctx, 'server_auth_user', user)

    def is_authenticated(self) -> bool:
        """
        Returns True if the current request is authenticated by a server API user.
        """
        # Check user in request context
        request_ctx = self.context_helper.get_request_context()
        return request_ctx is not None and getattr(request_ctx, 'server_auth_user', None) is not None

    def get_current_user(self) -> ServerAuthUser:
        """
        If the current request is authenticated, return the corresponding ServerAuthUser.
        Raises ServerApiUnauthorizedException otherwise.
        """
        # Check request context
        request_ctx = self.context_helper.get_request_context()
        if request_ctx is None:
            raise ServerApiUnauthorizedException(message='No request context')

        # Get user from request context
        user = getattr(request_ctx, 'server_auth_user', None)
        if user is None:
            raise ServerApiUnauthorizedException(message='Unauthenticated request')
        return user

    def require_roles(self, *roles: ServerAuthRole, require_all: bool = False) -> None:
        """
        Verifies that the current request is authenticated and that the current user has the required roles.
        If require_all is True, the user must have ALL of the specified roles, otherwise (default) the user must have
        AT LEAST ONE of the specified roles.

        Raises ServerApiMissingRoleException if the role requirements are not met (or ServerApiUnauthorizedException
        if the request is not authenticated at all).
        """
        # Get current user's roles
        user_roles = self.get_current_user().roles

        if require_all:
            # User must have all of the specified roles
            result = all(role in user_roles for role in roles)
        else:
            # User must have at least one of the specified roles
            result = any(role in user_roles for role in roles)

        if not result:
            raise ServerApiMissingRoleException(message='Insufficient user roles')
