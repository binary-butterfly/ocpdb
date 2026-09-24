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

from http import HTTPStatus

import mercantile
import pytest
from mapbox_vector_tile import decode

from tests.integration.helpers import OpenApiFlaskClient
from tests.integration.model_generators.evse import get_full_evse_1, get_full_evse_2
from tests.integration.model_generators.location import get_location_1
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.models.evse import EvseStatus

# Tile at zoom 12 which contains the default test location
TILE = mercantile.tile(13.40489, 52.52003, 12)


@pytest.mark.parametrize(
    ('query', 'expected_counts'),
    [
        ('', {'c': 2, 'ca': 1, 'cs': 1}),
        ('?static=true', {'c': 1, 'ca': 0, 'cs': 1}),
        ('?static=false', {'c': 1, 'ca': 1, 'cs': 0}),
    ],
)
def test_get_tile(
    db: SQLAlchemy,
    test_client: OpenApiFlaskClient,
    query: str,
    expected_counts: dict[str, int],
) -> None:
    db.session.add(
        get_location_1(
            evses=[
                get_full_evse_1(status=EvseStatus.AVAILABLE),
                get_full_evse_2(status=EvseStatus.STATIC),
            ],
        ),
    )
    db.session.commit()

    response = test_client.get(path=f'/tiles/{TILE.z}/{TILE.x}/{TILE.y}.mvt{query}')

    assert response.status_code == HTTPStatus.OK
    features = decode(response.data)['chargepoints']['features']
    assert len(features) == 1
    properties = features[0]['properties']
    assert {key: properties[key] for key in expected_counts} == expected_counts
