"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from collections.abc import Callable, Iterable


class OcpiPathRewriteMiddleware:
    """WSGI middleware that rewrites /api/ocpi/ paths to /api/public/ocpi/ so the existing
    OCPI endpoints are transparently available under both prefixes."""

    def __init__(self, app: Callable):
        self.app = app

    def __call__(self, environ: dict, start_response: Callable) -> Iterable:
        path = environ.get('PATH_INFO', '')
        if path == '/api/ocpi' or path.startswith('/api/ocpi/'):
            environ['PATH_INFO'] = '/api/public' + path[4:]
        return self.app(environ, start_response)
