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

from typing import Any, Dict, Optional

from flask import Request
from flask import request as flask_request

from webapp.common.unset_parameter import UnsetParameter

from .exceptions import WrongContentTypeException


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
        # Don't raise a "Failed to decode JSON object" BadRequest exception if the request body is empty
        parsed_json = self.request.get_json() if self.request.content_length else None

        if parsed_json is None and default is UnsetParameter:
            raise WrongContentTypeException('Request must have Content-Type application/json and a valid JSON body.')

        return parsed_json if parsed_json is not None else default

    def get_query_args(self, skip_empty: bool = False) -> Dict[str, str]:
        """
        Returns a dictionary containing all query arguments of the request as strings. If `skip_empty` is True, empty
        parameters (i.e. empty strings) will be removed from the dictionary.

        For example, the query string `?foo=abc&bar=&baz=42` results in `{'foo': 'abc', 'bar': '', 'baz': '42'}` by
        default, or in `{'foo': 'abc', 'baz': '42'}` if `skip_empty` is True.
        """
        args = dict(self.request.args)
        if skip_empty:
            args = {key: value for key, value in args.items() if value is not None and value != ''}
        return args

    def get_path(self) -> str:
        return self.request.path

    def get_client_ip(self):
        return self.request.headers.get('X-Forwarded-For', None)

    def get_request_body(self) -> bytes:
        return self.request.get_data()
