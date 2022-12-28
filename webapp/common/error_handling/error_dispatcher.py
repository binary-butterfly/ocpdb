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

from typing import Optional

from flask import Request, request as flask_request

from .base_error_handler import BaseErrorHandler


class ErrorDispatcher:
    """
    Class that can be registered as the global error handler. Dispatches errors/exceptions to other error handlers
    (classes that implement BaseErrorHandler).
    """
    rest_api_error_handler: BaseErrorHandler

    def __init__(self, rest_api_error_handler: BaseErrorHandler):
        # Initialize error handlers
        self.rest_api_error_handler = rest_api_error_handler

    def dispatch_error(self, error: Exception, request: Optional[Request] = None):
        """
        Passes the exception to Error Handler.
        Returns the result of the error handler, which should be a tuple of an HTTP response and a response code.
        If the exception could not be handled (e.g. because no handler is registered), the exception is re-raised.
        """
        if request is None:  # pragma: no cover
            request = flask_request

        response = self.rest_api_error_handler.handle_error(error)

        if response:
            return response
        else:
            raise error

    def wrap(self, func):
        """
        Decorator to wrap a function inside a try-except block that dispatches exceptions raised by the function.
        """

        def decorator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return self.dispatch_error(e)

        return decorator
