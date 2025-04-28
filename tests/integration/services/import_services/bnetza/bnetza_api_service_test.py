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

from requests_mock import Mocker

from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.services.import_services.bnetza.bnetza_api_service import BnetzaApiImportService


def test_bnetza_api_service(db: SQLAlchemy, requests_mock: Mocker):
    bnetza_import_service: BnetzaApiImportService = dependencies.get_import_services().bnetza_api_import_service

    bnetza_file_path = Path(Path(__file__).parent, 'bnetza.json')
    with bnetza_file_path.open('rb') as bnetza_file:
        requests_mock.get(
            'https://ladesaeulenregister.bnetza.de/els/service/public/v1/chargepoints',
            content=bnetza_file.read(),
        )

    bnetza_import_service.fetch_static_data()
