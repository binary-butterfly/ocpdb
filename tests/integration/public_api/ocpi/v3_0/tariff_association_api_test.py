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
from tests.integration.model_generators.evse import get_full_evse_1
from tests.integration.model_generators.location import get_location_1
from tests.integration.model_generators.source import SOURCE_UID_1
from tests.integration.model_generators.tariff import get_tariff_1, get_tariff_2, get_tariff_association
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.models.enums import TariffAudience


def test_get_ocpi_30_tariff_associations(
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

    response = public_test_client.get(path='/api/public/ocpi/3.0/tariff-associations')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2


def test_get_ocpi_30_tariff_association(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    ta = get_tariff_association(tariff=tariff, audience=TariffAudience.AD_HOC_PAYMENT)
    db.session.add(ta)
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/tariff-associations/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'id': '1',
        'original_id': 'TA-1',
        'source': SOURCE_UID_1,
        'tariff_id': '1',
        'audience': 'AD_HOC_PAYMENT',
        'evses': [],
        'connectors': [],
        'start_date_time': ANY,
        'last_updated': ANY,
    }


def test_get_ocpi_30_tariff_association_with_evse(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    location = get_location_1(evses=[get_full_evse_1()])
    db.session.add(location)
    db.session.flush()

    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    evse = location.charging_pool[0].evses[0]
    ta = get_tariff_association(tariff=tariff, evses=[evse])
    db.session.add(ta)
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/tariff-associations/1')
    assert response.status_code == HTTPStatus.OK
    assert len(response.json['evses']) == 1
    assert response.json['evses'][0] == {'evse_uid': str(evse.id)}
    assert response.json['connectors'] == []


def test_get_ocpi_30_tariff_associations_filter_by_tariff_id(
    db: SQLAlchemy,
    test_client: OpenApiFlaskClient,
) -> None:
    tariff1 = get_tariff_1()
    tariff2 = get_tariff_2()
    db.session.add_all([tariff1, tariff2])
    db.session.flush()

    ta1 = get_tariff_association(uid='TA-1', tariff=tariff1)
    ta2 = get_tariff_association(uid='TA-2', tariff=tariff2)
    db.session.add_all([ta1, ta2])
    db.session.commit()

    response = test_client.get(path=f'/api/public/ocpi/3.0/tariff-associations?tariff_id={tariff1.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert response.json['items'][0]['tariff_id'] == str(tariff1.id)


def test_get_ocpi_30_tariff_association_not_found(
    db: SQLAlchemy,
    test_client: OpenApiFlaskClient,
) -> None:
    response = test_client.get(path='/api/public/ocpi/3.0/tariff-associations/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
