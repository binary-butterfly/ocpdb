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

from functools import wraps
from typing import Optional, Union, Any
from flask import current_app, request as flask_request, Request

from validataclass.validators.dataclass_validator import DataclassValidator
from validataclass.exceptions import ValidationError
from .unset_parameter import UnsetParameter, UnsetParameterType
from .exceptions import AppWrongContentTypeException, AppWrongJsonTypeException, \
    AppInputValidationException, AppException, AppAccessDeniedException


class RequestHelper:
    """
    Helper class that wraps the Flask request object.
    """
    request: Request

    def __init__(self, request: Optional[Request] = None):
        self.request = request if request else flask_request

    def get_parsed_json(self, *, default: Any = UnsetParameter) -> Any:
        """
        Returns the parsed JSON body of the current request.

        Raises a `WrongContentTypeException` if no JSON body is present, unless the `default` parameter is set, in which case the value
        of it is returned instead.
        """
        parsed_json = self.request.get_json()

        if parsed_json is None and default is UnsetParameter:
            raise AppWrongJsonTypeException(message='Request must have Content-Type application/json and a valid JSON body.')

        return parsed_json if parsed_json is not None else default

    def get_args(self) -> dict:
        return dict(self.request.args)


def ensure_role(*roles, all_rules=False):
    def wrapped(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            user_roles = current_app.config['SERVER_AUTH_USERS'][flask_request.authorization.username].get('roles', [])
            combined_user_roles = [r for r in roles if r in user_roles]
            if all_rules and len(combined_user_roles) != len(roles):
                raise AppAccessDeniedException
            if not all_rules and not len(combined_user_roles):
                raise AppAccessDeniedException
            return func(*args, **kwargs)

        wrapped_function.basic_auth = True
        return wrapped_function
    return wrapped

