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
from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
from typing import Dict, List

from flask import Config

from .exceptions import ServerApiUnauthorizedException


class ServerAuthRole(Enum):
    """
    Roles a server API user can have.
    """
    GIROE = 'giroe'


@dataclass
class ServerAuthUser:
    """
    Dataclass representing a server API user. Has a username, password hash and a list of roles.
    """
    username: str
    password_hash: str
    roles: List[ServerAuthRole]

    def __post_init__(self):
        # Type checks
        assert type(self.username) is str
        assert type(self.password_hash) is str
        assert type(self.roles) is list and all(isinstance(role, ServerAuthRole) for role in self.roles)

    @classmethod
    def create_from_dict(cls, username: str, data: dict) -> 'ServerAuthUser':
        """
        Creates a ServerAuthUser object from a raw dictionary (with keys "hash" and "roles").
        """
        # Convert roles from strings to enum members
        valid_roles = [role.value for role in ServerAuthRole]
        roles = [ServerAuthRole(role) for role in data.get('roles') if role in valid_roles]

        # Construct object
        return cls(username=username, password_hash=data.get('hash'), roles=roles)

    def __eq__(self, other):
        return self.username == other.username


class ServerAuthDatabase:
    """
    Manages server API users. Wrapper around the SERVER_AUTH_USERS dictionary from the application config.
    """
    _users: Dict[str, ServerAuthUser]

    def __init__(self, *, server_auth_users: Dict[str, ServerAuthUser]):
        assert all(isinstance(user, ServerAuthUser) for user in server_auth_users.values())
        self._users = server_auth_users

    @classmethod
    def create_from_config(cls, config: Config) -> 'ServerAuthDatabase':
        """
        Parses the "SERVER_AUTH_USERS" dictionary from the application config and creates a ServerAuthDatabase from it.
        """
        users_from_config = config.get('SERVER_AUTH_USERS', None)
        users_parsed = {
            username: ServerAuthUser.create_from_dict(username, userdata)
            for username, userdata in users_from_config.items()
        }
        return cls(server_auth_users=users_parsed)

    def get_user_by_name(self, username: str) -> ServerAuthUser:
        """
        Returns the ServerAuthUser with the specified username.
        Raises ServerApiUnauthorizedException if no user withthat name was found.
        """
        if username not in self._users:
            raise ServerApiUnauthorizedException(message='Invalid credentials')
        return self._users.get(username)

    def authenticate_user(self, username: str, password: str) -> ServerAuthUser:
        """
        Verifies that a user with the given username and password exists, and returns the authenticated user.
        Raises ServerApiUnauthorizedException if no user could be authenticated.
        """
        user = self._users.get(username, None)
        password_digest = sha256(password.encode()).hexdigest()

        if user is None or not hmac.compare_digest(password_digest, user.password_hash):
            raise ServerApiUnauthorizedException(message='Invalid credentials')
        return user
