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

import uuid
from datetime import datetime, timezone
from decimal import Decimal
from http import HTTPStatus

from tests.integration.helpers import OpenApiFlaskClient, basic_auth_header
from tests.integration.model_generators.evse import EVSE_UID_1, get_evse
from tests.integration.model_generators.location import get_location
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import ChargingStation, Evse, Location
from webapp.models.evse import EvseStatus

GIROE_SOURCE_UID = 'giroe'


def _giroe_location_uid(location_id: int) -> str:
    """
    Reproduce the hashed location UID used by the giroe importer (see GiroeMapper.hash_object_id).
    """
    return (
        dependencies
        .get_import_services()
        .importer_by_uid[GIROE_SOURCE_UID]
        .giroe_mapper.hash_object_id(
            'location',
            location_id,
        )
    )


def _giroe_connector_uid(connector_id: int) -> str:
    return (
        dependencies
        .get_import_services()
        .importer_by_uid[GIROE_SOURCE_UID]
        .giroe_mapper.hash_object_id(
            'connector',
            connector_id,
        )
    )


def _valid_location_payload(location_id: int, *, public: bool = True) -> dict:
    """Build a minimal-but-complete giroe Location payload accepted by LocationInput."""
    now = datetime.now(timezone.utc).isoformat()
    return {
        'id': location_id,
        'created': now,
        'modified': now,
        'lat': '52.520000',
        'lon': '13.405000',
        'address': 'Alexanderplatz 1',
        'postalcode': '10178',
        'locality': 'Berlin',
        'country': 'DE',
        'public': public,
        'public_description': 'Test pool',
        'stations': [
            {
                'id': 100 + location_id,
                'created': now,
                'modified': now,
                'uid': str(uuid.uuid4()),
                'technical_backend': 'tcc',
                'hardware_id': 42,
                'connectors': [
                    {
                        'id': 1000 + location_id,
                        'created': now,
                        'modified': now,
                        'uid': f'giroe-evse-{location_id}',
                        'ocpp_connector_id': 1,
                        'status': 'available',
                        'power': 22000,
                        'power_type': 'AC_3_PHASE',
                        'standard': 'IEC_62196_T2',
                        'format': 'SOCKET',
                    },
                ],
            },
        ],
    }


class GiroePutLocationApiTest:
    @staticmethod
    def test_put_location_creates_location(db: SQLAlchemy, admin_test_client: OpenApiFlaskClient) -> None:
        location_id = 1234
        payload = _valid_location_payload(location_id)

        response = admin_test_client.put(
            path=f'/api/server/v1/giroe/locations/{location_id}',
            json=payload,
        )

        assert response.status_code == HTTPStatus.NO_CONTENT
        assert response.data == b''

        location = (
            db.session
            .query(Location)
            .filter(Location.uid == _giroe_location_uid(location_id), Location.source == GIROE_SOURCE_UID)
            .first()
        )
        assert location is not None
        assert location.address == 'Alexanderplatz 1'
        assert location.country == 'DEU'

    @staticmethod
    def test_put_location_with_public_false_deletes(db: SQLAlchemy, admin_test_client: OpenApiFlaskClient) -> None:
        location_id = 5678
        # First create via PUT
        admin_test_client.put(
            path=f'/api/server/v1/giroe/locations/{location_id}',
            json=_valid_location_payload(location_id),
        )
        db.session.expire_all()
        assert db.session.query(Location).filter(Location.uid == _giroe_location_uid(location_id)).count() == 1

        # Then PUT with public: False to delete
        response = admin_test_client.put(
            path=f'/api/server/v1/giroe/locations/{location_id}',
            json=_valid_location_payload(location_id, public=False),
        )

        assert response.status_code == HTTPStatus.NO_CONTENT
        db.session.expire_all()
        assert db.session.query(Location).filter(Location.uid == _giroe_location_uid(location_id)).count() == 0

    @staticmethod
    def test_put_location_rejects_invalid_payload(db: SQLAlchemy, admin_test_client: OpenApiFlaskClient) -> None:
        response = admin_test_client.put(
            path='/api/server/v1/giroe/locations/42',
            json={'id': 42},  # missing required fields
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST

    @staticmethod
    def test_put_location_requires_basic_auth(
        db: SQLAlchemy,
        admin_unauthenticated_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_unauthenticated_test_client.put(
            path='/api/server/v1/giroe/locations/42',
            json=_valid_location_payload(42),
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED

    @staticmethod
    def test_put_location_rejects_invalid_credentials(
        db: SQLAlchemy,
        admin_unauthenticated_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_unauthenticated_test_client.put(
            path='/api/server/v1/giroe/locations/42',
            json=_valid_location_payload(42),
            headers={'Authorization': basic_auth_header('dev', 'wrong-password')},
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED

    @staticmethod
    def test_put_location_rejects_missing_role(
        db: SQLAlchemy,
        admin_unauthenticated_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_unauthenticated_test_client.put(
            path='/api/server/v1/giroe/locations/42',
            json=_valid_location_payload(42),
            headers={'Authorization': basic_auth_header('unprivileged', 'test')},
        )

        # Missing role is reported as 401 (ServerApiMissingRoleException inherits from ServerApiUnauthorizedException).
        assert response.status_code == HTTPStatus.UNAUTHORIZED


class GiroeDeleteLocationApiTest:
    @staticmethod
    def test_delete_location_removes_existing(db: SQLAlchemy, admin_test_client: OpenApiFlaskClient) -> None:
        location_id = 9999
        db.session.add(
            get_location(
                uid=_giroe_location_uid(location_id),
                source=GIROE_SOURCE_UID,
            ),
        )
        db.session.commit()

        response = admin_test_client.delete(
            path=f'/api/server/v1/giroe/locations/{location_id}',
        )

        assert response.status_code == HTTPStatus.NO_CONTENT
        db.session.expire_all()
        assert db.session.query(Location).filter(Location.uid == _giroe_location_uid(location_id)).count() == 0

    @staticmethod
    def test_delete_location_unknown_returns_404(db: SQLAlchemy, admin_test_client: OpenApiFlaskClient) -> None:
        response = admin_test_client.delete(
            path='/api/server/v1/giroe/locations/999999',
        )

        assert response.status_code == HTTPStatus.NOT_FOUND

    @staticmethod
    def test_delete_location_requires_basic_auth(
        db: SQLAlchemy,
        admin_unauthenticated_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_unauthenticated_test_client.delete(
            path='/api/server/v1/giroe/locations/42',
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED


class GiroePatchConnectorApiTest:
    @staticmethod
    def _seed_evse(db: SQLAlchemy, evse_uid: str) -> None:
        location = get_location(
            uid=str(uuid.uuid4()),
            source=GIROE_SOURCE_UID,
            lat=Decimal('52.52'),
            lon=Decimal('13.40'),
            charging_pool=[
                ChargingStation(
                    uid=str(uuid.uuid4()),
                    last_updated=datetime.now(tz=timezone.utc),
                    evses=[get_evse(uid=evse_uid, evse_id=evse_uid)],
                ),
            ],
        )
        db.session.add(location)
        db.session.commit()

    @staticmethod
    def test_patch_connector_updates_status(db: SQLAlchemy, admin_test_client: OpenApiFlaskClient) -> None:
        evse_uid = 'giroe-evse-patch'
        GiroePatchConnectorApiTest._seed_evse(db, evse_uid)

        response = admin_test_client.patch(
            path=f'/api/server/v1/giroe/connectors/{evse_uid}',
            json={
                'modified': '2026-01-15T10:30:00+00:00',
                'status': 'CHARGING',
            },
        )

        assert response.status_code == HTTPStatus.NO_CONTENT
        db.session.expire_all()
        evse = db.session.query(Evse).filter(Evse.uid == evse_uid).first()
        assert evse.status == EvseStatus.CHARGING

    @staticmethod
    def test_patch_connector_unknown_returns_404(
        db: SQLAlchemy,
        admin_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_test_client.patch(
            path='/api/server/v1/giroe/connectors/does-not-exist',
            json={
                'modified': '2026-01-15T10:30:00+00:00',
                'status': 'CHARGING',
            },
        )

        assert response.status_code == HTTPStatus.NOT_FOUND

    @staticmethod
    def test_patch_connector_requires_basic_auth(
        db: SQLAlchemy,
        admin_unauthenticated_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_unauthenticated_test_client.patch(
            path=f'/api/server/v1/giroe/connectors/{EVSE_UID_1}',
            json={'modified': '2026-01-15T10:30:00+00:00'},
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED

    @staticmethod
    def test_patch_connector_rejects_missing_role(
        db: SQLAlchemy,
        admin_unauthenticated_test_client: OpenApiFlaskClient,
    ) -> None:
        response = admin_unauthenticated_test_client.patch(
            path=f'/api/server/v1/giroe/connectors/{EVSE_UID_1}',
            json={'modified': '2026-01-15T10:30:00+00:00'},
            headers={'Authorization': basic_auth_header('unprivileged', 'test')},
        )

        # Missing role is reported as 401 (ServerApiMissingRoleException inherits from ServerApiUnauthorizedException).
        assert response.status_code == HTTPStatus.UNAUTHORIZED
