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

from http import HTTPStatus

from tests.integration.helpers import OpenApiFlaskClient
from tests.integration.model_generators.location import get_full_location_1, get_full_location_2, get_full_location_3
from tests.integration.model_generators.source import SOURCE_UID_1
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
