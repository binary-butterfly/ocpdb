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

from datetime import datetime, timedelta, timezone
from http import HTTPStatus
from unittest.mock import ANY

from tests.integration.helpers import OpenApiFlaskClient
from tests.integration.model_generators.business import get_business_1, get_business_2
from tests.integration.model_generators.evse import (
    get_full_evse_1,
    get_full_evse_2,
    get_full_evse_3,
    get_full_evse_4,
    get_full_evse_5,
    get_full_evse_6,
)
from tests.integration.model_generators.location import get_location_1, get_location_2, get_location_3
from tests.integration.model_generators.source import SOURCE_UID_1, SOURCE_UID_2
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.models.evse import EvseStatus


def test_get_evses_strict(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([
        get_location_1(
            evses=[get_full_evse_1(), get_full_evse_2()],
            operator=get_business_1(),
        ),
        get_location_2(
            evses=[get_full_evse_3(), get_full_evse_4()],
            operator=get_business_1(),
        ),
    ])
    db.session.commit()

    response = public_test_client.get(
        path='/api/public/v1/evses?strict=true',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 4
    assert len(response.json['items']) == 4


def test_get_evse_strict(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(
        get_location_1(
            evses=[get_full_evse_1()],
            operator=get_business_1(),
        )
    )
    db.session.commit()

    response = public_test_client.get(
        path='/api/public/v1/evses/1?strict=true',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'uid': '1',
        'evse_id': 'EVSE-1',
        'status': 'AVAILABLE',
        'presence': 'PRESENT',
        'last_updated': ANY,
        'connectors': [
            {
                'standard': 'IEC_62196_T2',
                'format': 'SOCKET',
                'power_type': 'AC_3_PHASE',
                'max_voltage': 400,
                'max_amperage': 32,
                'max_electric_power': 22000,
                'last_updated': ANY,
                'id': '1',
            },
        ],
    }


def test_get_evses_by_status(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([
        get_location_1(
            evses=[
                get_full_evse_1(status=EvseStatus.AVAILABLE),
                get_full_evse_2(status=EvseStatus.CHARGING),
            ],
            operator=get_business_1(),
        ),
        get_location_2(
            evses=[
                get_full_evse_3(status=EvseStatus.AVAILABLE),
                get_full_evse_4(status=EvseStatus.OUTOFORDER),
            ],
            operator=get_business_1(),
        ),
    ])
    db.session.commit()

    response = public_test_client.get(
        path='/api/public/v1/evses?strict=true&status=AVAILABLE',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2
    for item in response.json['items']:
        assert item['status'] == 'AVAILABLE'


def test_get_evses_by_multiple_statuses(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([
        get_location_1(
            evses=[
                get_full_evse_1(status=EvseStatus.AVAILABLE),
                get_full_evse_2(status=EvseStatus.CHARGING),
            ],
            operator=get_business_1(),
        ),
        get_location_2(
            evses=[
                get_full_evse_3(status=EvseStatus.INOPERATIVE),
                get_full_evse_4(status=EvseStatus.OUTOFORDER),
            ],
            operator=get_business_1(),
        ),
    ])
    db.session.commit()

    response = public_test_client.get(
        path='/api/public/v1/evses?strict=true&statuses=AVAILABLE,CHARGING',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2
    statuses = [item['status'] for item in response.json['items']]
    assert 'AVAILABLE' in statuses
    assert 'CHARGING' in statuses


def test_get_evses_by_last_updated_since(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    old_timestamp = now - timedelta(days=7)
    recent_timestamp = now - timedelta(hours=1)

    db.session.add_all([
        get_location_1(
            evses=[
                get_full_evse_1(last_updated=recent_timestamp),
                get_full_evse_2(last_updated=old_timestamp),
            ],
            operator=get_business_1(),
        ),
        get_location_2(
            evses=[
                get_full_evse_3(last_updated=old_timestamp),
                get_full_evse_4(last_updated=old_timestamp),
            ],
            operator=get_business_1(),
        ),
    ])
    db.session.commit()

    filter_timestamp = (now - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/evses?strict=true&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1
    assert response.json['items'][0]['uid'] == '1'


def test_get_evses_by_last_updated_since_no_results(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    old_timestamp = now - timedelta(days=7)

    db.session.add_all([
        get_location_1(
            evses=[
                get_full_evse_1(last_updated=old_timestamp),
                get_full_evse_2(last_updated=old_timestamp),
            ],
            operator=get_business_1(),
        ),
    ])
    db.session.commit()

    filter_timestamp = (now - timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/evses?strict=true&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 0
    assert len(response.json['items']) == 0


def test_get_evses_by_last_updated_since_all_results(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    recent_timestamp = now - timedelta(hours=1)

    db.session.add_all([
        get_location_1(
            evses=[
                get_full_evse_1(last_updated=recent_timestamp),
                get_full_evse_2(last_updated=recent_timestamp),
            ],
            operator=get_business_1(),
        ),
        get_location_2(
            evses=[
                get_full_evse_3(last_updated=recent_timestamp),
                get_full_evse_4(last_updated=recent_timestamp),
            ],
            operator=get_business_1(),
        ),
    ])
    db.session.commit()

    filter_timestamp = (now - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/evses?strict=true&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 4
    assert len(response.json['items']) == 4


def test_get_evses_by_status_and_last_updated_since(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    old_timestamp = now - timedelta(days=7)
    recent_timestamp = now - timedelta(hours=1)

    db.session.add_all([
        get_location_1(
            evses=[
                get_full_evse_1(status=EvseStatus.AVAILABLE, last_updated=recent_timestamp),
                get_full_evse_2(status=EvseStatus.CHARGING, last_updated=recent_timestamp),
            ],
            operator=get_business_1(),
        ),
        get_location_2(
            evses=[
                get_full_evse_3(status=EvseStatus.AVAILABLE, last_updated=old_timestamp),
                get_full_evse_4(status=EvseStatus.OUTOFORDER, last_updated=recent_timestamp),
            ],
            operator=get_business_1(),
        ),
    ])
    db.session.commit()

    filter_timestamp = (now - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/evses?strict=true&status=AVAILABLE&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1
    assert response.json['items'][0]['uid'] == '1'
    assert response.json['items'][0]['status'] == 'AVAILABLE'


def test_get_evses_by_source_uid(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([
        get_location_1(
            evses=[get_full_evse_1(), get_full_evse_2()],
            operator=get_business_1(),
        ),
        get_location_3(
            source=SOURCE_UID_2,
            evses=[get_full_evse_5(), get_full_evse_6()],
            operator=get_business_2(),
        ),
    ])
    db.session.commit()

    response = public_test_client.get(
        path=f'/api/public/v1/evses?strict=true&source_uid={SOURCE_UID_1}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2


def test_get_evses_by_location_id(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([
        get_location_1(
            evses=[get_full_evse_1(), get_full_evse_2()],
            operator=get_business_1(),
        ),
        get_location_2(
            evses=[get_full_evse_3(), get_full_evse_4()],
            operator=get_business_1(),
        ),
    ])
    db.session.commit()

    response = public_test_client.get(
        path='/api/public/v1/evses?strict=true&location_id=1',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2


def test_get_evses_pagination(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([
        get_location_1(
            evses=[get_full_evse_1(), get_full_evse_2()],
            operator=get_business_1(),
        ),
        get_location_2(
            evses=[get_full_evse_3(), get_full_evse_4()],
            operator=get_business_1(),
        ),
        get_location_3(
            source=SOURCE_UID_2,
            evses=[get_full_evse_5(), get_full_evse_6()],
            operator=get_business_2(),
        ),
    ])
    db.session.commit()

    response = public_test_client.get(
        path='/api/public/v1/evses?strict=true&limit=2',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 6
    assert len(response.json['items']) == 2

    response = public_test_client.get(
        path='/api/public/v1/evses?strict=true&limit=2&offset=2',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 6
    assert len(response.json['items']) == 2
