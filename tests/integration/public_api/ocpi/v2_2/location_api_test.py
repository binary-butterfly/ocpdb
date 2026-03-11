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

from datetime import datetime, timedelta, timezone
from decimal import Decimal
from http import HTTPStatus

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
from tests.integration.model_generators.location import (
    get_full_location_1,
    get_full_location_2,
    get_full_location_3,
    get_location_1,
    get_location_2,
    get_location_3,
)
from tests.integration.model_generators.source import SOURCE_UID_1, SOURCE_UID_2
from tests.integration.public_api.location_api_responses import (
    LOCATIONS_1_RESPONSE,
    LOCATIONS_2_RESPONSE,
    LOCATIONS_RESPONSE,
)
from webapp.common.sqlalchemy import SQLAlchemy


def test_get_ocpi_22_locations_strict(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_full_location_1(), get_full_location_2(), get_full_location_3()])
    db.session.commit()

    response = public_test_client.get(
        path='/api/ocpi/2.2/locations?strict=true',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == LOCATIONS_RESPONSE


def test_get_ocpi_22_location(
    db: SQLAlchemy,
    test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(get_full_location_1())
    db.session.commit()

    response = test_client.get(
        path='/api/ocpi/2.2/locations/1',
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json
    assert data['id'] == '1'
    assert data['name'] == 'Test Location'
    assert data['address'] == 'Test Street 123'
    assert data['city'] == 'Test City'
    assert data['country'] == 'DEU'
    assert 'coordinates' in data
    assert 'operator' in data
    assert 'evses' in data
    assert len(data['evses']) == 2


def test_get_ocpi_22_locations_by_source_strict(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_full_location_1(), get_full_location_2(), get_full_location_3()])
    db.session.commit()

    response = public_test_client.get(
        path=f'/api/ocpi/2.2/locations?strict=true&source_uid={SOURCE_UID_1}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'items': [
            LOCATIONS_1_RESPONSE,
            LOCATIONS_2_RESPONSE,
        ],
        'total_count': 2,
    }


def test_get_ocpi_22_locations_by_bounding_box(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([
        get_full_location_1(),
        get_full_location_2(lat=Decimal('48.13'), lon=Decimal('11.58')),
        get_full_location_3(lat=Decimal('53.55'), lon=Decimal('9.99')),
    ])
    db.session.commit()

    response = public_test_client.get(
        path='/api/ocpi/2.2/locations?strict=true&lat_min=52.0&lat_max=53.0&lon_min=13.0&lon_max=14.0',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1
    assert response.json['items'][0]['id'] == '1'


def test_get_ocpi_22_locations_by_last_updated_since(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    old_timestamp = now - timedelta(days=7)
    recent_timestamp = now - timedelta(hours=1)

    db.session.add_all([
        get_location_1(
            last_updated=recent_timestamp,
            evses=[
                get_full_evse_1(last_updated=recent_timestamp),
                get_full_evse_2(last_updated=recent_timestamp),
            ],
            operator=get_business_1(),
        ),
        get_location_2(
            last_updated=old_timestamp,
            evses=[
                get_full_evse_3(last_updated=old_timestamp),
                get_full_evse_4(last_updated=old_timestamp),
            ],
            operator=get_business_1(),
        ),
        get_location_3(
            last_updated=old_timestamp,
            source=SOURCE_UID_2,
            evses=[
                get_full_evse_5(last_updated=old_timestamp),
                get_full_evse_6(last_updated=old_timestamp),
            ],
            operator=get_business_2(),
        ),
    ])
    db.session.commit()

    filter_timestamp = (now - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/ocpi/2.2/locations?strict=true&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1
    assert response.json['items'][0]['id'] == '1'


def test_get_ocpi_22_location_non_strict(
    db: SQLAlchemy,
    test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(get_full_location_1())
    db.session.commit()

    response = test_client.get(
        path='/api/ocpi/2.2/locations/1',
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json
    assert 'source' in data
    assert 'original_id' in data
    assert 'evses' in data
    assert len(data['evses']) == 2
