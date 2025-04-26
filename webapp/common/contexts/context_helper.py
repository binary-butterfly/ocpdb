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

import secrets

from flask.ctx import AppContext, RequestContext, has_request_context
from flask.globals import app_ctx, request_ctx

from .models import TelemetryContext


class ContextHelper:
    """
    Helper class for working with Flask application and request contexts.
    """

    @staticmethod
    def get_app_context() -> AppContext | None:
        """
        Returns the current application context, or None if no application context exists.
        """
        return app_ctx

    @staticmethod
    def get_request_context() -> RequestContext | None:
        """
        Returns the current request context, or None if no request context exists.
        """
        return request_ctx

    @staticmethod
    def has_request_context() -> bool:
        """
        Returns True if a request context exists on the request context stack, False otherwise.
        """
        return has_request_context()

    def set_default_tracing_ids(self) -> None:
        app_context = self.get_app_context()

        setattr(app_context, 'trace_id', secrets.token_hex(16))
        setattr(app_context, 'span_id', secrets.token_hex(8))

    def set_telemetry_context(self, telemetry_context: TelemetryContext, value: str | int):
        app_context = self.get_app_context()
        if not hasattr(app_context, 'butterfly_butterfly_telemetry_context'):
            app_context.butterfly_butterfly_telemetry_context = {}
        app_context.butterfly_butterfly_telemetry_context[telemetry_context] = value
