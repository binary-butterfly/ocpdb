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

from uuid import UUID

from requests_mock import Mocker

from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.services.import_services.ocpi.eaaze_pbw import EaazePbwImportService

SOURCE_URL = 'https://ocpi.eaaze.cloud/cpo/2.2.1/locations'

EMPTY_OCPI_RESPONSE = {
    'status_code': 1000,
    'timestamp': '2026-01-01T00:00:00Z',
    'data': [],
}


def test_eaaze_pbw_sends_x_request_id(db: SQLAlchemy, requests_mock: Mocker) -> None:
    """Every request to eaaze_pbw must carry an X-Request-ID header containing a random uuid4."""
    eaaze_pbw_service: EaazePbwImportService = dependencies.get_import_services().importer_by_uid['eaaze_pbw']

    requests_mock.get(SOURCE_URL, status_code=200, json=EMPTY_OCPI_RESPONSE)

    eaaze_pbw_service.download_and_save()

    request_id = requests_mock.last_request.headers.get('X-Request-ID')
    assert request_id is not None
    # Must be a valid uuid4 (raises ValueError otherwise).
    assert UUID(request_id).version == 4
    # The token auth header must still be present.
    assert requests_mock.last_request.headers['Authorization'].startswith('Token ')


def test_eaaze_pbw_x_request_id_is_unique_per_request(db: SQLAlchemy, requests_mock: Mocker) -> None:
    """The X-Request-ID must be regenerated for each request, not reused."""
    eaaze_pbw_service: EaazePbwImportService = dependencies.get_import_services().importer_by_uid['eaaze_pbw']

    requests_mock.get(SOURCE_URL, status_code=200, json=EMPTY_OCPI_RESPONSE)

    eaaze_pbw_service.download_and_save()
    eaaze_pbw_service.download_and_save()

    request_ids = [request.headers.get('X-Request-ID') for request in requests_mock.request_history]
    assert len(request_ids) == 2
    assert all(request_id is not None for request_id in request_ids)
    assert request_ids[0] != request_ids[1]
