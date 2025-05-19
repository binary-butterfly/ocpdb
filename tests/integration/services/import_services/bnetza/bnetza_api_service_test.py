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

from pathlib import Path

import pytest
from requests_mock import Mocker

from webapp.common.flask_app import App
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import Location
from webapp.services.import_services.bnetza.bnetza_api_service import BnetzaApiImportService


@pytest.fixture
def mocked_bnetza_api_request(requests_mock: Mocker) -> None:
    bnetza_file_path = Path(Path(__file__).parent, 'bnetza.json')
    with bnetza_file_path.open('rb') as bnetza_file:
        requests_mock.get(
            'https://ladesaeulenregister.bnetza.de/els/service/public/v1/chargepoints',
            content=bnetza_file.read(),
        )


def test_bnetza_api_service(db: SQLAlchemy, mocked_bnetza_api_request: None):
    bnetza_import_service: BnetzaApiImportService = dependencies.get_import_services().importer_by_uid['bnetza_api']

    bnetza_import_service.fetch_static_data()

    assert db.session.query(Location).count() == 918


def test_filtered_bnetza_api_service(flask_app: App, db: SQLAlchemy, mocked_bnetza_api_request: None):
    flask_app.config['SOURCES']['bnetza_api']['ignore_operators'] = ['Stadtwerke Düsseldorf AG']
    bnetza_import_service: BnetzaApiImportService = dependencies.get_import_services().importer_by_uid['bnetza_api']

    bnetza_import_service.fetch_static_data()

    assert db.session.query(Location).count() == 445
