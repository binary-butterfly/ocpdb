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

from tests.integration.helpers import OpenApiFlaskClient
from tests.integration.model_generators.business import BUSINESS_1_NAME, get_business_1, get_business_2
from webapp.common.sqlalchemy import SQLAlchemy


def test_get_ocpi_22_businesses(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_business_1(), get_business_2()])
    db.session.commit()

    response = public_test_client.get(
        path='/api/ocpi/2.2/businesses',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2


def test_get_ocpi_22_business(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(get_business_1())
    db.session.commit()

    response = public_test_client.get(
        path='/api/ocpi/2.2/businesses/1',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == {'name': BUSINESS_1_NAME}


def test_get_ocpi_22_businesses_by_name(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_business_1(), get_business_2()])
    db.session.commit()

    response = public_test_client.get(
        path='/api/ocpi/2.2/businesses?name=Electro',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert response.json['items'][0]['name'] == BUSINESS_1_NAME


def test_get_ocpi_22_business_with_website(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(get_business_1(website='https://example.com'))
    db.session.commit()

    response = public_test_client.get(
        path='/api/ocpi/2.2/businesses/1',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'name': BUSINESS_1_NAME,
        'website': 'https://example.com',
    }
