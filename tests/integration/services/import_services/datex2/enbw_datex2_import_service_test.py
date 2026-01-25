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
from webapp.models import Business, Connector, Evse, Location
from webapp.services.import_services.datex2 import EnBWDatex2ImportService


@pytest.fixture
def enbw_datex2_import_service(requests_mock: Mocker) -> EnBWDatex2ImportService:
    json_path = Path(Path(__file__).parent, 'data', 'datex2_enbw_reduced.json')
    with json_path.open() as json_file:
        json_data = json_file.read()

    requests_mock.get(
        'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID=12345',
        status_code=200,
        text=json_data,
        headers={'Content-Type': 'application/json'},
    )

    return dependencies.get_import_services().importer_by_uid['datex2_enbw']


def test_enbw_datex2_static_import(
    db: SQLAlchemy,
    enbw_datex2_import_service: EnBWDatex2ImportService,
) -> None:
    enbw_datex2_import_service.fetch_static_data()

    assert db.session.query(Location).count() == 10
    assert db.session.query(Evse).count() == 22
    assert db.session.query(Connector).count() == 22
    assert db.session.query(Business).count() == 1
