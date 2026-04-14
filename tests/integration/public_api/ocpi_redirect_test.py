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

from http import HTTPStatus

from tests.integration.helpers import OpenApiFlaskClient
from webapp.common.sqlalchemy import SQLAlchemy


class OcpiPathRewriteTest:
    @staticmethod
    def test_rewrite_v22_locations(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        canonical = test_client.get(path='/api/public/ocpi/2.2/locations')
        rewritten = test_client.get(path='/api/ocpi/2.2/locations')

        assert rewritten.status_code == canonical.status_code
        assert rewritten.json == canonical.json

    @staticmethod
    def test_rewrite_v30_locations(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        canonical = test_client.get(path='/api/public/ocpi/3.0/locations')
        rewritten = test_client.get(path='/api/ocpi/3.0/locations')

        assert rewritten.status_code == canonical.status_code
        assert rewritten.json == canonical.json

    @staticmethod
    def test_rewrite_preserves_query_parameters(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        canonical = test_client.get(path='/api/public/ocpi/2.2/locations?limit=10')
        rewritten = test_client.get(path='/api/ocpi/2.2/locations?limit=10')

        assert rewritten.status_code == canonical.status_code
        assert rewritten.json == canonical.json

    @staticmethod
    def test_rewrite_returns_ok(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/ocpi/2.2/locations')

        assert response.status_code == HTTPStatus.OK
