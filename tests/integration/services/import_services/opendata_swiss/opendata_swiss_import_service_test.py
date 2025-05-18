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
from webapp.models.evse import EvseStatus
from webapp.services.import_services.opendata_swiss import OpendataSwissImportService


@pytest.fixture
def opendata_swiss_import_service(requests_mock: Mocker) -> OpendataSwissImportService:
    json_path = Path(Path(__file__).parent, 'opendata_swiss_static.json')
    with json_path.open() as json_file:
        json_data = json_file.read()

    requests_mock.get(
        'https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/oicp'
        '/ch.bfe.ladestellen-elektromobilitaet.json',
        status_code=200,
        text=json_data,
        headers={'Content-Type': 'application/json'},
    )

    return dependencies.get_import_services().importer_by_uid['opendata_swiss']


def test_opendata_swiss_static_import(
    db: SQLAlchemy,
    opendata_swiss_import_service: OpendataSwissImportService,
) -> None:
    opendata_swiss_import_service.fetch_static_data()

    assert db.session.query(Location).count() == 202
    assert db.session.query(Evse).count() == 551
    assert db.session.query(Connector).count() == 551
    assert db.session.query(Business).count() == 2


def test_opendata_swiss_realtime_import(
    db: SQLAlchemy,
    opendata_swiss_import_service: OpendataSwissImportService,
    requests_mock: Mocker,
) -> None:
    json_path = Path(Path(__file__).parent, 'opendata_swiss_realtime.json')
    with json_path.open() as json_file:
        json_data = json_file.read()

    requests_mock.get(
        'https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/status/oicp'
        '/ch.bfe.ladestellen-elektromobilitaet.json',
        status_code=200,
        text=json_data,
        headers={'Content-Type': 'application/json'},
    )

    opendata_swiss_import_service.fetch_static_data()
    opendata_swiss_import_service.fetch_realtime_data()

    assert db.session.query(Evse).filter(Evse.status == EvseStatus.AVAILABLE).count() == 413
