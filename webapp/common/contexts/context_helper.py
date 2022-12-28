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

from flask import _app_ctx_stack, _request_ctx_stack  # noqa
from flask.ctx import AppContext, RequestContext


class ContextHelper:
    """
    Helper class for working with Flask application and request contexts.
    """

    @staticmethod
    def get_app_context() -> Optional[AppContext]:
        """
        Returns the current application context, or None if no application context exists.
        """
        return _app_ctx_stack.top

    @staticmethod
    def get_request_context() -> Optional[RequestContext]:
        """
        Returns the current request context, or None if no request context exists.
        """
        return _request_ctx_stack.top

    @staticmethod
    def has_request_context() -> bool:
        """
        Returns True if a request context exists on the request context stack, False otherwise.
        """
        return _request_ctx_stack.top is not None
