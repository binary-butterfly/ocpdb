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
from pathlib import Path
from unittest.mock import patch

import pytest

from tests.integration.helpers import OpenApiFlaskClient, basic_auth_header
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies


@pytest.fixture
def stub_celery_delay():
    """Stub out CeleryHelper.delay so the bnetza import task is not actually enqueued."""
    with patch.object(dependencies.get_celery_helper(), 'delay') as mock_delay:
        yield mock_delay


@pytest.fixture
def isolated_bnetza_dir(tmp_path: Path):
    """Redirect BNETZA_IMPORT_DIR to a per-test temp directory to avoid polluting `data/`."""
    config = dependencies.get_config_helper().get_config()
    original = config.get('BNETZA_IMPORT_DIR')
    config['BNETZA_IMPORT_DIR'] = str(tmp_path)
    try:
        yield tmp_path
    finally:
        config['BNETZA_IMPORT_DIR'] = original


class BnetzaImportApiTest:
    @staticmethod
    def test_post_uploads_excel_and_queues_import(
        db: SQLAlchemy,
        admin_test_client: OpenApiFlaskClient,
        stub_celery_delay,
        isolated_bnetza_dir: Path,
    ) -> None:
        excel_bytes = b'PK\x03\x04stub-excel-payload'

        response = admin_test_client.post(
            path='/api/server/v1/bnetza/',
            data=excel_bytes,
            content_type='application/octet-stream',
        )

        assert response.status_code == HTTPStatus.OK

        # File was written to the configured import dir
        written = list(isolated_bnetza_dir.iterdir())
        assert len(written) == 1
        assert written[0].suffix == '.xlsx'
        assert written[0].read_bytes() == excel_bytes

        # Celery task was queued with the path
        stub_celery_delay.assert_called_once()
        args, _ = stub_celery_delay.call_args
        assert args[1] == str(written[0])

    @staticmethod
    def test_post_without_body_returns_400(
        db: SQLAlchemy,
        admin_test_client: OpenApiFlaskClient,
        stub_celery_delay,
        isolated_bnetza_dir: Path,
    ) -> None:
        response = admin_test_client.post(
            path='/api/server/v1/bnetza/',
            data=b'',
            content_type='application/octet-stream',
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST
        stub_celery_delay.assert_not_called()

    @staticmethod
    def test_post_requires_basic_auth(
        db: SQLAlchemy,
        admin_unauthenticated_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_unauthenticated_test_client.post(
            path='/api/server/v1/bnetza/',
            data=b'anything',
            content_type='application/octet-stream',
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED

    @staticmethod
    def test_post_rejects_invalid_credentials(
        db: SQLAlchemy,
        admin_unauthenticated_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_unauthenticated_test_client.post(
            path='/api/server/v1/bnetza/',
            data=b'anything',
            content_type='application/octet-stream',
            headers={'Authorization': basic_auth_header('dev', 'wrong-password')},
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED

    @staticmethod
    def test_post_rejects_missing_role(
        db: SQLAlchemy,
        admin_unauthenticated_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_unauthenticated_test_client.post(
            path='/api/server/v1/bnetza/',
            data=b'anything',
            content_type='application/octet-stream',
            headers={'Authorization': basic_auth_header('unprivileged', 'test')},
        )

        # Missing role is reported as 401 (ServerApiMissingRoleException inherits from ServerApiUnauthorizedException).
        assert response.status_code == HTTPStatus.UNAUTHORIZED
