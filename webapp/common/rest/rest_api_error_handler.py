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

import traceback

from flask import jsonify
from validataclass.exceptions import ValidationError
from werkzeug.exceptions import HTTPException

from webapp.common.error_handling import BaseErrorHandler
from webapp.common.error_handling.exceptions import AppException
from webapp.common.rest.exceptions import InputValidationException, RestApiNotImplementedException


class RestApiErrorHandler(BaseErrorHandler):
    """
    Error handler for all REST API endpoints.
    """

    _http_error_code_mapping = {
        400: 'bad_request',
        401: 'unauthorized',
        403: 'forbidden',
        404: 'not_found',
        405: 'method_not_allowed',
        408: 'request_timeout',
        418: 'im_a_teapot',
        500: 'internal_server_error',
        501: 'not_implemented',
        502: 'bad_gateway',
        503: 'service_unavailable',
        504: 'gateway_timeout',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Register handler methods for Exception types
        self.register(AppException, self._handle_app_exception)
        self.register(HTTPException, self._handle_http_exception)
        self.register(ValidationError, self._handle_validation_error)

        # Register handler method for builtin NotImplementedError exception
        self.register(NotImplementedError, self._handle_not_implemented_error)

        # Catch-all for other Exception types
        self.register(Exception, self._handle_generic_exception)

    def _handle_app_exception(self, error: AppException):
        """
        Handles all AppExceptions, including RestApiExceptions.
        """
        # Write to log if server error
        if error.http_status >= 500:
            self._log_critical(error)

        return jsonify({'error': error.response_data(debug_mode=self.debug)}), error.http_status

    def _handle_http_exception(self, error: HTTPException):
        """
        Handles generic HTTPExceptions.
        """
        # Write to log if server error
        if error.code >= 500:
            self._log_critical(error)

        # Generate HTTP response
        response = jsonify({
            'error': {
                'code': self._http_code_to_str(error),
                'message': error.description,
            }
        })

        # Add all headers that error.get_response() would have
        for key, value in error.get_headers():
            # Skip Content-Type (which is already set by jsonify to application/json)
            if key.lower() != 'content-type':
                response.headers.add(key, value)

        return response, error.code

    def _http_code_to_str(self, error: HTTPException) -> str:
        code_str = self._http_error_code_mapping.get(error.code)
        if code_str:
            return code_str

        return 'http_' + type(error).__name__.lower()

    def _handle_validation_error(self, error: ValidationError):
        """
        Handles uncaught ValidationError exceptions from validataclass by wrapping them in an InputValidationException.
        """
        return self._handle_app_exception(
            InputValidationException('Input validation errors while handling the request.', data=error.to_dict())
        )

    def _handle_not_implemented_error(self, error: NotImplementedError):
        """
        Handles uncaught NotImplementedError exceptions by converting them to a RestApiNotImplementedException.
        """
        return self._handle_app_exception(
            RestApiNotImplementedException(str(error) or 'Method not implemented.')
        )

    def _handle_generic_exception(self, error: Exception):
        """
        Handles all exceptions that were not handled by any other handler, i.e. "internal server errors".

        Note: Errors that are to be expected at runtime should ALWAYS be caught and handled either by recovering from the error in
        some way or by raising an AppExceptions (or subclass thereof).
        """
        self._log_critical(error)

        error_data = {
            'code': 'internal_server_error',
            'message': 'There was an unhandled exception on the server side.',
        }

        if self.debug:
            # In debug mode, append exception and stacktrace
            error_data['_debug'] = {
                'exception': repr(error),
                'traceback': traceback.format_exc().splitlines(),
            }

        return jsonify({'error': error_data}), 500
