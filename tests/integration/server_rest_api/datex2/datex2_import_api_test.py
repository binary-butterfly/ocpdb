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

import json
from base64 import b64encode
from http import HTTPStatus
from pathlib import Path

from tests.integration.helpers import OpenApiFlaskClient
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.models import Business, ChargingStation, Connector, Evse, Location, Tariff
from webapp.models.evse import EvseStatus

# Basic Auth header for the test user (dev:test)
AUTH_HEADER = {'Authorization': f'Basic {b64encode(b"dev:test").decode()}'}

SOURCE_UID = 'datex2_enbw'


def _load_test_data(filename: str) -> dict:
    json_path = Path(__file__).parent.parent.parent / 'services' / 'import_services' / 'datex2' / 'data' / filename
    with json_path.open() as json_file:
        return json.load(json_file)


class Datex2StaticImportApiV35Test:
    @staticmethod
    def test_push_static_v35(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        data = _load_test_data('datex2_enbw_static_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/static',
            json=data,
            headers=AUTH_HEADER,
        )

        assert response.status_code == HTTPStatus.NO_CONTENT

        assert db.session.query(Location).count() == 10
        assert db.session.query(ChargingStation).count() == 27
        assert db.session.query(Evse).count() == 57
        assert db.session.query(Connector).count() == 57
        assert db.session.query(Business).count() == 1
        assert db.session.query(Tariff).count() == 57

    @staticmethod
    def test_push_static_v35_location_details(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        data = _load_test_data('datex2_enbw_static_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/static',
            json=data,
            headers=AUTH_HEADER,
        )

        assert response.status_code == HTTPStatus.NO_CONTENT

        location = db.session.query(Location).filter(Location.uid == '800030182').first()
        assert location is not None
        assert len(location.parking_spaces) == 1
        parking_space = location.parking_spaces[0]
        assert parking_space.parking_space_count == 4
        assert parking_space.has_roof is False
        assert parking_space.is_illuminated is False

    @staticmethod
    def test_push_static_v35_unauthorized(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        data = _load_test_data('datex2_enbw_static_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/static',
            json=data,
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED

    @staticmethod
    def test_push_static_v35_unknown_source(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        data = _load_test_data('datex2_enbw_static_reduced.json')

        response = test_client.post(
            path='/api/server/v1/datex/v3.5/unknown_source/static',
            json=data,
            headers=AUTH_HEADER,
        )

        assert response.status_code == HTTPStatus.NOT_FOUND


class Datex2RealtimeImportApiV35Test:
    @staticmethod
    def test_push_realtime_v35(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        # First populate with static data
        static_data = _load_test_data('datex2_enbw_static_reduced.json')
        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/static',
            json=static_data,
            headers=AUTH_HEADER,
        )
        assert response.status_code == HTTPStatus.NO_CONTENT

        # All EVSEs should start as UNKNOWN
        assert db.session.query(Evse).filter(Evse.status == EvseStatus.UNKNOWN).count() == 57

        # Push realtime data
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime',
            json=realtime_data,
            headers=AUTH_HEADER,
        )
        assert response.status_code == HTTPStatus.NO_CONTENT

        db.session.expire_all()

        # Verify status updates
        evse_available = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*2').first()
        assert evse_available.status == EvseStatus.AVAILABLE

        evse_charging = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
        assert evse_charging.status == EvseStatus.CHARGING

        evse_faulted = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914081*1').first()
        assert evse_faulted.status == EvseStatus.OUTOFORDER

        evse_occupied = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E909938*3').first()
        assert evse_occupied.status == EvseStatus.CHARGING

        # EVSEs not in realtime data should remain UNKNOWN
        evse_unchanged = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E916701*2').first()
        assert evse_unchanged.status == EvseStatus.UNKNOWN

    @staticmethod
    def test_push_realtime_v35_unauthorized(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime',
            json=realtime_data,
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED


class Datex2StaticImportApiV37Test:
    @staticmethod
    def test_push_static_v37(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        data = _load_test_data('datex2_enbw_static_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.7/{SOURCE_UID}/static',
            json=data,
            headers=AUTH_HEADER,
        )

        assert response.status_code == HTTPStatus.NO_CONTENT

        assert db.session.query(Location).count() == 10
        assert db.session.query(Evse).count() == 57

    @staticmethod
    def test_push_realtime_v37(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        # First populate with static data
        static_data = _load_test_data('datex2_enbw_static_reduced.json')
        response = test_client.post(
            path=f'/api/server/v1/datex/v3.7/{SOURCE_UID}/static',
            json=static_data,
            headers=AUTH_HEADER,
        )
        assert response.status_code == HTTPStatus.NO_CONTENT

        # Push realtime data
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        response = test_client.post(
            path=f'/api/server/v1/datex/v3.7/{SOURCE_UID}/realtime',
            json=realtime_data,
            headers=AUTH_HEADER,
        )
        assert response.status_code == HTTPStatus.NO_CONTENT

        db.session.expire_all()

        evse_available = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*2').first()
        assert evse_available.status == EvseStatus.AVAILABLE
