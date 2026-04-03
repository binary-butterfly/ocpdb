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
from unittest.mock import ANY

from tests.integration.helpers import OpenApiFlaskClient
from tests.integration.model_generators.source import SOURCE_UID_1, SOURCE_UID_2
from tests.integration.model_generators.tariff import TARIFF_UID_1, get_tariff_1, get_tariff_2
from webapp.common.sqlalchemy import SQLAlchemy


def test_get_ocpi_30_tariffs(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_tariff_1(), get_tariff_2()])
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/tariffs')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2


def test_get_ocpi_30_tariff(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(get_tariff_1())
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/tariffs/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'id': '1',
        'original_id': TARIFF_UID_1,
        'source': SOURCE_UID_1,
        'currency': 'EUR',
        'elements': [],
        'last_updated': ANY,
    }


def test_get_ocpi_30_tariff_with_elements(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    tariff = get_tariff_1()
    tariff.elements = [
        {
            'price_components': [
                {'type': 'ENERGY', 'price': 0.30},
            ],
        },
    ]
    db.session.add(tariff)
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/tariffs/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json['elements'] == [
        {
            'price_components': [
                {'type': 'ENERGY', 'price': 0.30},
            ],
        },
    ]


def test_get_ocpi_30_tariffs_filter_by_source(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_tariff_1(), get_tariff_2(source=SOURCE_UID_2)])
    db.session.commit()

    response = public_test_client.get(path=f'/api/public/ocpi/3.0/tariffs?source_uid={SOURCE_UID_1}')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert response.json['items'][0]['original_id'] == TARIFF_UID_1


def test_get_ocpi_30_tariff_not_found(
    db: SQLAlchemy,
    test_client: OpenApiFlaskClient,
) -> None:
    response = test_client.get(path='/api/public/ocpi/3.0/tariffs/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
