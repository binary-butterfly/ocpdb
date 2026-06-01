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

from typing import Generator

import pytest

from tests.integration.helpers import OpenApiFlaskClient, TestApp, basic_auth_header

ADMIN_USER = 'dev'
ADMIN_PASSWORD = 'test'
UNPRIVILEGED_USER = 'unprivileged'
UNPRIVILEGED_PASSWORD = 'test'


@pytest.fixture
def admin_test_client(flask_app: TestApp) -> Generator[OpenApiFlaskClient, None, None]:
    """
    Test client for the server (admin) REST API. Validates responses against the
    `server` OpenAPI realm and pre-populates the Authorization header with valid
    basic-auth credentials for the privileged dev user.
    """
    with flask_app.test_client(
        openapi_realm='server',
        default_auth_header=basic_auth_header(ADMIN_USER, ADMIN_PASSWORD),
    ) as client:
        yield client  # type: ignore


@pytest.fixture
def admin_unauthenticated_test_client(flask_app: TestApp) -> Generator[OpenApiFlaskClient, None, None]:
    """
    Test client for the server (admin) REST API without any Authorization header.
    """
    with flask_app.test_client(openapi_realm='server') as client:
        yield client  # type: ignore
