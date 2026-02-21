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


def test_get_ocpi_22_evses_strict(
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
        path='/api/ocpi/2.2/evses?strict=true',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 4
    assert len(response.json['items']) == 4


def test_get_ocpi_22_evse_strict(
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
        path='/api/ocpi/2.2/evses/1?strict=true',
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


def test_get_ocpi_22_evses_by_status(
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
        path='/api/ocpi/2.2/evses?strict=true&status=AVAILABLE',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2
    for item in response.json['items']:
        assert item['status'] == 'AVAILABLE'


def test_get_ocpi_22_evses_by_source_uid(
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
        path=f'/api/ocpi/2.2/evses?strict=true&source_uid={SOURCE_UID_1}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2


def test_get_ocpi_22_evse_non_strict(
    db: SQLAlchemy,
    test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(
        get_location_1(
            evses=[get_full_evse_1()],
            operator=get_business_1(),
        )
    )
    db.session.commit()

    response = test_client.get(
        path='/api/ocpi/2.2/evses/1',
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json
    assert 'uid' in data
    assert 'status' in data
    assert 'connectors' in data
    assert 'original_uid' in data
