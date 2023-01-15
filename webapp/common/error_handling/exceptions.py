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

from typing import Any, Optional


class AppException(Exception):
    """
    Base exception class for all errors thrown by the application. (See also: RestApiException)
    Each AppException has a "code", which is a string identifier like "auth_failed", an HTTP status code (e.g. 403)
    which should not be confused with the string "code", and a human-readable "message" that may contain more
    details to the error.
    Optionally the "data" attribute can be set, which can contain any type of data (e.g. dicts) with additional
    information on the error.
    Finally, the optional "debug" attribute can be set to any type of data. Contrary to the other attributes the
    "debug" attribute will ONLY be included in API responses when the application is in DEBUG mode, thus it may
    be filled with potentially sensitive and long data (like stack traces or object dumps).
    """
    code: str = 'unspecified_error'
    message: str = ''
    http_status: int = 500
    data: Any = None
    debug_data: Any = None

    def __init__(
        self,
        message: str,
        *,
        http_status: Optional[int] = None,
        code: Optional[str] = None,
        data: Any = None,
        debug: Any = None,
    ):
        self.message = message
        if http_status is not None:
            self.http_status = http_status
        if code is not None:
            self.code = code
        if data is not None:
            self.data = data
        if debug is not None:
            self.debug_data = debug

    def __str__(self):
        if self.message:
            return '{}: {} ({})'.format(self.code, self.message, self.http_status)
        else:
            return '{} ({})'.format(self.code, self.http_status)

    def response_data(self, debug_mode: bool = False):
        response_data = {
            'code': self.code,
            'message': self.message,
        }
        if self.data:
            response_data['data'] = self.data

        # Append debug data only when the application is in debug mode
        if debug_mode and self.debug_data:
            response_data['_debug'] = self.debug_data

        return response_data
