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
from base64 import b64encode
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


def basic_auth_header(username: str, password: str) -> str:
    """
    Build a HTTP Basic Authorization header value from a username and password.
    """
    token = b64encode(f'{username}:{password}'.encode()).decode()
    return f'Basic {token}'


class OpenApiFlaskClient(FlaskClient):
    openapi_realm: str | None = None
    default_auth_header: str | None = None

    def __init__(
        self,
        *args: Any,
        openapi_realm: str | None = None,
        default_auth_header: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.openapi_realm = openapi_realm
        self.default_auth_header = default_auth_header

    def open(self, *args: Any, **kwargs: Any) -> TestResponse:
        if self.default_auth_header is not None:
            headers = kwargs.get('headers') or {}
            if isinstance(headers, dict):
                headers = dict(headers)
                if 'Authorization' not in headers:
                    headers['Authorization'] = self.default_auth_header
            kwargs['headers'] = headers

        response = super().open(*args, **kwargs)

        if self.openapi_realm is None or os.environ.get('OPENAPI_SKIP_VALIDATION'):
            return response

        if self.openapi_realm not in OPENAPI_BY_REALM:
            openapi_dict = generate_openapi(self.openapi_realm)
            openapi_dict = self.no_additional_properties(openapi_dict)
            self.drop_empty_response_content(openapi_dict)

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

    @staticmethod
    def drop_empty_response_content(openapi_dict: dict) -> None:
        """
        flask_openapi emits ``content: {<mimetype>: {}}`` for responses declared via
        ``EmptyResponse`` (and ``content: {}`` for responses with no declared body at all).
        openapi_core then rejects empty-bodied HTTP 200/204 replies with ``MissingData``.
        Strip those placeholder blocks so the validator treats the response as having no
        body.
        """
        for path_item in openapi_dict.get('paths', {}).values():
            for operation in path_item.values():
                if not isinstance(operation, dict):
                    continue
                for response in operation.get('responses', {}).values():
                    if not isinstance(response, dict):
                        continue
                    content = response.get('content')
                    if content is None:
                        continue
                    if not content or all(entry == {} for entry in content.values()):
                        response.pop('content')


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
