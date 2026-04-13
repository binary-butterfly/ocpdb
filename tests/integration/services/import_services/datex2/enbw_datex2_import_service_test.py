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
from webapp.models import Business, ChargingStation, Connector, Evse, Location, Tariff
from webapp.models.enums import VehicleCategoryEnum
from webapp.models.evse import EvseStatus
from webapp.services.import_services.datex2 import EnBWDatex2ImportService


def _load_test_data(filename: str) -> str:
    json_path = Path(Path(__file__).parent, 'data', filename)
    with json_path.open() as json_file:
        return json_file.read()


@pytest.fixture
def enbw_datex2_import_service(requests_mock: Mocker) -> EnBWDatex2ImportService:
    json_data = _load_test_data('datex2_enbw_static_reduced.json')

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
    assert db.session.query(ChargingStation).count() == 27
    assert db.session.query(Evse).count() == 57
    assert db.session.query(Connector).count() == 57
    assert db.session.query(Business).count() == 1
    assert db.session.query(Tariff).count() == 57

    # Check that site-level parking spaces are mapped to locations
    location = db.session.query(Location).filter(Location.uid == '800030182').first()
    assert location is not None
    assert len(location.parking_spaces) == 1
    parking_space = location.parking_spaces[0]
    assert parking_space.vehicle_types == [VehicleCategoryEnum.M1]
    assert parking_space.parking_space_count == 4
    assert parking_space.has_roof is False
    assert parking_space.is_illuminated is False
    assert parking_space.is_accessible is False

    # Each EVSE and its connector should be linked to a tariff association
    evse = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
    assert len(evse.tariff_associations) == 1
    assert len(evse.connectors) == 1
    # assert len(evse.connectors[0].tariff_associations) == 1
    # EVSE and its connector share the same tariff association
    # assert evse.tariff_associations[0].id == evse.connectors[0].tariff_associations[0].id


def test_enbw_datex2_realtime_import(db: SQLAlchemy, requests_mock: Mocker) -> None:
    """
    Test for EnBWDatex2ImportService.fetch_realtime_data().

    First imports static data to populate the database,
    then tests realtime update functionality.
    """
    static_data = _load_test_data('datex2_enbw_static_reduced.json')
    realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')

    requests_mock.get(
        'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID=12345',
        status_code=200,
        text=static_data,
        headers={'Content-Type': 'application/json'},
    )
    requests_mock.get(
        'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID=67890',
        status_code=200,
        text=realtime_data,
        headers={'Content-Type': 'application/json'},
    )

    enbw_service: EnBWDatex2ImportService = dependencies.get_import_services().importer_by_uid['datex2_enbw']

    # First populate database with static data
    enbw_service.fetch_static_data()

    # Verify all EVSEs start with UNKNOWN status after static import
    assert db.session.query(Evse).filter(Evse.status == EvseStatus.UNKNOWN).count() == 57

    # Run realtime update
    enbw_service.fetch_realtime_data()

    db.session.expire_all()

    # Verify EVSE statuses updated from realtime data
    # available -> AVAILABLE (status changed from UNKNOWN)
    evse_available = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*2').first()
    assert evse_available is not None
    assert evse_available.status == EvseStatus.AVAILABLE

    # charging -> CHARGING
    evse_charging = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
    assert evse_charging is not None
    assert evse_charging.status == EvseStatus.CHARGING

    # faulted -> OUTOFORDER
    evse_faulted = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914081*1').first()
    assert evse_faulted is not None
    assert evse_faulted.status == EvseStatus.OUTOFORDER

    # occupied -> CHARGING
    evse_occupied = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E909938*3').first()
    assert evse_occupied is not None
    assert evse_occupied.status == EvseStatus.CHARGING

    # EVSEs not in realtime data should remain UNKNOWN
    evse_unchanged = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E916701*2').first()
    assert evse_unchanged is not None
    assert evse_unchanged.status == EvseStatus.UNKNOWN
