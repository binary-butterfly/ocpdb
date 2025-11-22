"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

import os
from typing import Any

from flask.testing import FlaskClient
from flask_openapi.generator import generate_openapi
from openapi_core import OpenAPI
from openapi_core.contrib.werkzeug import WerkzeugOpenAPIRequest, WerkzeugOpenAPIResponse
from sqlalchemy import text
from werkzeug.test import TestResponse

from webapp.common.flask_app import App
from webapp.common.sqlalchemy import SQLAlchemy

OPENAPI_BY_REALM = {}


class OpenApiFlaskClient(FlaskClient):
    openapi_realm: str | None = None

    def __init__(self, *args: Any, openapi_realm: str | None = None, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.openapi_realm = openapi_realm

    def open(self, *args: Any, **kwargs: Any) -> TestResponse:
        response = super().open(*args, **kwargs)

        if self.openapi_realm is None or os.environ.get('OPENAPI_SKIP_VALIDATION'):
            return response

        if self.openapi_realm not in OPENAPI_BY_REALM:
            openapi_dict = generate_openapi(self.openapi_realm)
            openapi_dict = self.no_additional_properties(openapi_dict)

            OPENAPI_BY_REALM[self.openapi_realm] = OpenAPI.from_dict(openapi_dict)

        OPENAPI_BY_REALM[self.openapi_realm].validate_response(
            WerkzeugOpenAPIRequest(response.request),
            WerkzeugOpenAPIResponse(response),
        )

        return response

    def no_additional_properties(self, data: Any):
        if isinstance(data, dict):
            # Patch in additionalProperties in case of an object field if it's not already set
            if data.get('type') == 'object' and 'additionalProperties' not in data:
                data['additionalProperties'] = False

            return {key: self.no_additional_properties(value) for key, value in data.items()}

        if isinstance(data, list):
            return [self.no_additional_properties(item) for item in data]

        return data


class TestApp(App):
    test_client_class = OpenApiFlaskClient


def empty_all_tables(db: SQLAlchemy) -> None:
    """
    empty all tables in the database
    (this is much faster than completely deleting the database and creating a new one)
    """
    db.session.close()
    with db.engine.connect() as connection:
        connection.execute(text(f'TRUNCATE {", ".join(db.metadata.tables.keys())} RESTART IDENTITY;'))
        connection.commit()
