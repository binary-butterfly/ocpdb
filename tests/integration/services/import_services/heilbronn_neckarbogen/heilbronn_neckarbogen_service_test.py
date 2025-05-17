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

from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import Evse, Location
from webapp.services.import_services.goldbeck_ipcm import HeilbronnNeckarbogenImportService


@pytest.fixture
def heilbronn_neckarbogen_import_service(requests_mock: Mocker) -> HeilbronnNeckarbogenImportService:
    json_path = Path(Path(__file__).parent, 'heilbronn_neckarbogen.json')
    with json_path.open() as json_file:
        json_data = json_file.read()

    requests_mock.get(
        'https://control.goldbeck-parking.de/ipaw/services/charging/v1x0/charging-stations',
        status_code=200,
        text=json_data,
        headers={'Content-Type': 'application/json;charset=UTF-8'},
    )

    return dependencies.get_import_services().importer_by_uid['heilbronn_neckarbogen']


def test_heilbronn_neckarbogen_import(
    db: SQLAlchemy,
    heilbronn_neckarbogen_import_service: HeilbronnNeckarbogenImportService,
) -> None:
    heilbronn_neckarbogen_import_service.fetch_static_data()

    assert db.session.query(Location).count() == 3
    assert db.session.query(Evse).count() == 211

    heilbronn_neckarbogen_import_service.fetch_realtime_data()
