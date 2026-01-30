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


def test_get_locations_strict(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_full_location_1(), get_full_location_2(), get_full_location_3()])
    db.session.commit()

    response = public_test_client.get(
        path='/api/public/v1/locations?strict=true',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == LOCATIONS_RESPONSE


def test_get_locations_by_source_strict(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_full_location_1(), get_full_location_2(), get_full_location_3()])
    db.session.commit()

    response = public_test_client.get(
        path=f'/api/public/v1/locations?strict=true&source_uid={SOURCE_UID_1}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'items': [
            LOCATIONS_1_RESPONSE,
            LOCATIONS_2_RESPONSE,
        ],
        'total_count': 2,
    }


def test_get_location_strict(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(get_full_location_1())
    db.session.commit()

    response = public_test_client.get(
        path='/api/public/v1/locations/1?strict=true',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == LOCATIONS_1_RESPONSE


def test_get_locations_by_bounding_box(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    # Location 1: Berlin (lat=52.52003, lon=13.40489) - inside bounding box
    # Location 2: Munich area (lat=48.13, lon=11.58) - outside bounding box
    # Location 3: Hamburg area (lat=53.55, lon=9.99) - outside bounding box
    db.session.add_all([
        get_full_location_1(),  # Berlin - default coordinates
        get_full_location_2(lat=Decimal('48.13'), lon=Decimal('11.58')),  # Munich
        get_full_location_3(lat=Decimal('53.55'), lon=Decimal('9.99')),  # Hamburg
    ])
    db.session.commit()

    # Bounding box around Berlin only
    response = public_test_client.get(
        path='/api/public/v1/locations?strict=true&lat_min=52.0&lat_max=53.0&lon_min=13.0&lon_max=14.0',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1
    assert response.json['items'][0]['id'] == '1'


def test_get_locations_by_bounding_box_multiple_results(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    # Location 1: Berlin (lat=52.52003, lon=13.40489)
    # Location 2: Also in Berlin area (lat=52.51, lon=13.38)
    # Location 3: Munich area (lat=48.13, lon=11.58) - outside bounding box
    db.session.add_all([
        get_full_location_1(),  # Berlin - default coordinates
        get_full_location_2(lat=Decimal('52.51'), lon=Decimal('13.38')),  # Also Berlin
        get_full_location_3(lat=Decimal('48.13'), lon=Decimal('11.58')),  # Munich
    ])
    db.session.commit()

    # Bounding box around Berlin
    response = public_test_client.get(
        path='/api/public/v1/locations?strict=true&lat_min=52.0&lat_max=53.0&lon_min=13.0&lon_max=14.0',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2
    ids = [item['id'] for item in response.json['items']]
    assert '1' in ids
    assert '2' in ids


def test_get_locations_by_bounding_box_no_results(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    # All locations are in Berlin, bounding box is in Munich area
    db.session.add_all([get_full_location_1(), get_full_location_2(), get_full_location_3()])
    db.session.commit()

    # Bounding box around Munich (no locations there)
    response = public_test_client.get(
        path='/api/public/v1/locations?strict=true&lat_min=48.0&lat_max=49.0&lon_min=11.0&lon_max=12.0',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 0
    assert len(response.json['items']) == 0


def test_get_locations_by_bounding_box_partial_params_ignored(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    # When only some bounding box params are provided, the filter should not be applied
    db.session.add_all([get_full_location_1(), get_full_location_2(), get_full_location_3()])
    db.session.commit()

    # Only lat_min and lat_max provided - should return all locations
    response = public_test_client.get(
        path='/api/public/v1/locations?strict=true&lat_min=52.0&lat_max=53.0',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 3


def test_get_locations_by_bounding_box_combined_with_source_filter(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    # Test that bounding box works with other filters
    db.session.add_all([
        get_full_location_1(),  # Berlin, source 1
        get_full_location_2(),  # Berlin, source 1
        get_full_location_3(),  # Berlin, source 2
    ])
    db.session.commit()

    # Bounding box around Berlin + source filter
    response = public_test_client.get(
        path=f'/api/public/v1/locations?strict=true&lat_min=52.0&lat_max=53.0&lon_min=13.0&lon_max=14.0'
        f'&source_uid={SOURCE_UID_1}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    ids = [item['id'] for item in response.json['items']]
    assert '1' in ids
    assert '2' in ids


def test_get_locations_by_last_updated_since(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    old_timestamp = now - timedelta(days=7)
    recent_timestamp = now - timedelta(hours=1)

    # Location 1: updated recently (location and EVSEs)
    # Location 2: updated a week ago (location and EVSEs)
    # Location 3: updated a week ago (location and EVSEs)
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

    # Filter for locations updated in the last day
    filter_timestamp = (now - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/locations?strict=true&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1
    assert response.json['items'][0]['id'] == '1'


def test_get_locations_by_last_updated_since_no_results(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    old_timestamp = now - timedelta(days=7)

    # All locations and EVSEs were updated a week ago
    db.session.add_all([
        get_location_1(
            last_updated=old_timestamp,
            evses=[
                get_full_evse_1(last_updated=old_timestamp),
                get_full_evse_2(last_updated=old_timestamp),
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

    # Filter for locations updated in the last hour - should return none
    filter_timestamp = (now - timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/locations?strict=true&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 0
    assert len(response.json['items']) == 0


def test_get_locations_by_last_updated_since_all_results(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    recent_timestamp = now - timedelta(hours=1)

    # All locations and EVSEs were updated recently
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
            last_updated=recent_timestamp,
            evses=[
                get_full_evse_3(last_updated=recent_timestamp),
                get_full_evse_4(last_updated=recent_timestamp),
            ],
            operator=get_business_1(),
        ),
        get_location_3(
            last_updated=recent_timestamp,
            source=SOURCE_UID_2,
            evses=[
                get_full_evse_5(last_updated=recent_timestamp),
                get_full_evse_6(last_updated=recent_timestamp),
            ],
            operator=get_business_2(),
        ),
    ])
    db.session.commit()

    # Filter for locations updated in the last week - should return all
    filter_timestamp = (now - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/locations?strict=true&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 3
    assert len(response.json['items']) == 3


def test_get_locations_by_last_updated_since_evse_updated(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    old_timestamp = now - timedelta(days=7)
    recent_timestamp = now - timedelta(hours=1)

    # Location 1: location is old but has a recently updated EVSE
    # Location 2: both location and EVSEs are old
    db.session.add_all([
        get_location_1(
            last_updated=old_timestamp,
            evses=[
                get_full_evse_1(last_updated=recent_timestamp),
                get_full_evse_2(last_updated=old_timestamp),
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
    ])
    db.session.commit()

    # Filter for locations updated in the last day - should return location 1 due to EVSE update
    filter_timestamp = (now - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/locations?strict=true&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1
    assert response.json['items'][0]['id'] == '1'


def test_get_locations_by_last_updated_since_combined_with_source_filter(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    old_timestamp = now - timedelta(days=7)
    recent_timestamp = now - timedelta(hours=1)

    # Location 1: source 1, recently updated
    # Location 2: source 1, old
    # Location 3: source 2, recently updated
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
            last_updated=recent_timestamp,
            source=SOURCE_UID_2,
            evses=[
                get_full_evse_5(last_updated=recent_timestamp),
                get_full_evse_6(last_updated=recent_timestamp),
            ],
            operator=get_business_2(),
        ),
    ])
    db.session.commit()

    # Filter for source 1 and updated in the last day
    filter_timestamp = (now - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/locations?strict=true&source_uid={SOURCE_UID_1}&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1
    assert response.json['items'][0]['id'] == '1'


def test_get_locations_by_last_updated_since_boundary(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    now = datetime.now(tz=timezone.utc)
    exact_timestamp = now - timedelta(hours=1)

    # Location updated at exactly the filter timestamp (should be included due to >= comparison)
    db.session.add_all([
        get_location_1(
            last_updated=exact_timestamp,
            evses=[
                get_full_evse_1(last_updated=exact_timestamp),
                get_full_evse_2(last_updated=exact_timestamp),
            ],
            operator=get_business_1(),
        ),
    ])
    db.session.commit()

    # Filter with exact same timestamp - should include the location
    filter_timestamp = exact_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
    response = public_test_client.get(
        path=f'/api/public/v1/locations?strict=true&last_updated_since={filter_timestamp}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1
