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
from tests.integration.model_generators.tariff import get_tariff_1, get_tariff_2, get_tariff_association
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.models.enums import TariffAudience
from webapp.models.tariff import TariffElement, TariffPriceComponent


def test_get_ocpi_22_tariffs(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    ta1 = get_tariff_association(uid='TA-1', tariff=tariff)
    ta2 = get_tariff_association(uid='TA-2', tariff=tariff)
    db.session.add_all([ta1, ta2])
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/2.2/tariffs')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2


def test_get_ocpi_22_tariff(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    ta = get_tariff_association(tariff=tariff, audience=TariffAudience.AD_HOC_PAYMENT)
    db.session.add(ta)
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/2.2/tariffs/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'id': '1',
        'original_id': 'TA-1',
        'source': SOURCE_UID_1,
        'currency': 'EUR',
        'type': 'AD_HOC_PAYMENT',
        'elements': [],
        'start_date_time': ANY,
        'last_updated': ANY,
    }


def test_get_ocpi_22_tariff_regular_type(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    ta = get_tariff_association(tariff=tariff, audience=TariffAudience.EMSP_CONTRACT)
    db.session.add(ta)
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/2.2/tariffs/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json['type'] == 'REGULAR'


def test_get_ocpi_22_tariff_with_elements(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    tariff = get_tariff_1()
    tariff.elements = [
        TariffElement(
            price_components=[
                TariffPriceComponent(type='ENERGY', price=0.30),
            ],
        ),
    ]
    db.session.add(tariff)
    db.session.flush()

    ta = get_tariff_association(tariff=tariff)
    db.session.add(ta)
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/2.2/tariffs/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json['elements'] == [
        {
            'price_components': [
                {'type': 'ENERGY', 'price': 0.30},
            ],
        },
    ]


def test_get_ocpi_22_tariffs_filter_by_source(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    tariff1 = get_tariff_1()
    tariff2 = get_tariff_2()
    db.session.add_all([tariff1, tariff2])
    db.session.flush()

    ta1 = get_tariff_association(uid='TA-1', tariff=tariff1)
    ta2 = get_tariff_association(uid='TA-2', source=SOURCE_UID_2, tariff=tariff2)
    db.session.add_all([ta1, ta2])
    db.session.commit()

    response = public_test_client.get(path=f'/api/public/ocpi/2.2/tariffs?source_uid={SOURCE_UID_1}')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert response.json['items'][0]['original_id'] == 'TA-1'


def test_get_ocpi_22_tariff_merges_tariff_data(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    """Two associations pointing to the same tariff produce two OCPI 2.2 tariffs with same pricing but different types."""
    tariff = get_tariff_1()
    tariff.elements = [
        TariffElement(
            price_components=[
                TariffPriceComponent(type='ENERGY', price=0.30),
            ],
        ),
    ]
    db.session.add(tariff)
    db.session.flush()

    ta1 = get_tariff_association(uid='TA-AD-HOC', tariff=tariff, audience=TariffAudience.AD_HOC_PAYMENT)
    ta2 = get_tariff_association(uid='TA-CONTRACT', tariff=tariff, audience=TariffAudience.EMSP_CONTRACT)
    db.session.add_all([ta1, ta2])
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/2.2/tariffs')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2

    items_by_type = {item['type']: item for item in response.json['items']}
    assert 'AD_HOC_PAYMENT' in items_by_type
    assert 'REGULAR' in items_by_type
    # Both share the same tariff elements
    assert items_by_type['AD_HOC_PAYMENT']['elements'] == items_by_type['REGULAR']['elements']
    assert items_by_type['AD_HOC_PAYMENT']['currency'] == 'EUR'
