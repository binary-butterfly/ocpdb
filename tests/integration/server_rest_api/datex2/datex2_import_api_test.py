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

import gzip
import json
from http import HTTPStatus
from pathlib import Path

from requests_mock import Mocker

from tests.integration.helpers import OpenApiFlaskClient
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import Evse
from webapp.models.evse import EvseStatus

SOURCE_UID = 'datex2_enbw'
API_KEY = 'test-datex2-api-key'
STATIC_SUBSCRIPTION_URL = 'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID=12345'


def _load_test_data_text(filename: str) -> str:
    json_path = Path(__file__).parent.parent.parent / 'services' / 'import_services' / 'datex2' / 'data' / filename
    with json_path.open() as json_file:
        return json_file.read()


def _load_test_data(filename: str) -> dict:
    return json.loads(_load_test_data_text(filename))


def _import_static_data(requests_mock: Mocker) -> None:
    requests_mock.get(
        STATIC_SUBSCRIPTION_URL,
        status_code=200,
        text=_load_test_data_text('datex2_enbw_static_reduced.json'),
        headers={'Content-Type': 'application/json'},
    )
    dependencies.get_import_services().importer_by_uid[SOURCE_UID].fetch_static_data()


class Datex2RealtimeImportApiV35Test:
    @staticmethod
    def test_push_realtime_v35(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
    ) -> None:
        # First populate with static data via the pull service
        _import_static_data(requests_mock)

        # All EVSEs should start as UNKNOWN
        assert db.session.query(Evse).filter(Evse.status == EvseStatus.UNKNOWN).count() == 57

        # Push realtime data
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            json=realtime_data,
        )
        assert response.status_code == HTTPStatus.OK

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
    def test_push_realtime_v35_gzip_encoded(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
    ) -> None:
        """
        Realtime payloads gzip-compressed with Content-Encoding: gzip must be transparently decoded by the
        server_rest_api before_request hook and processed like any other push.
        """
        _import_static_data(requests_mock)

        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        compressed_body = gzip.compress(json.dumps(realtime_data).encode('utf-8'))

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            data=compressed_body,
            content_type='application/json',
            headers={'Content-Encoding': 'gzip'},
        )
        assert response.status_code == HTTPStatus.OK

        db.session.expire_all()
        evse_available = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*2').first()
        assert evse_available.status == EvseStatus.AVAILABLE
        evse_charging = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
        assert evse_charging.status == EvseStatus.CHARGING

    @staticmethod
    def test_push_realtime_v35_invalid_api_key(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key=wrong-key',
            json=realtime_data,
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED

    @staticmethod
    def test_push_realtime_v35_unauthorized(db: SQLAlchemy, test_client: OpenApiFlaskClient) -> None:
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime',
            json=realtime_data,
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED
