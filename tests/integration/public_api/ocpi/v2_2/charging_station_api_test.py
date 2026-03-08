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
from tests.integration.model_generators.location import get_full_location_1, get_full_location_2, get_full_location_3
from tests.integration.model_generators.source import SOURCE_UID_1
from webapp.common.sqlalchemy import SQLAlchemy


def test_get_ocpi_22_charging_stations_strict(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_full_location_1(), get_full_location_2()])
    db.session.commit()

    response = public_test_client.get(
        path='/api/ocpi/2.2/charge-stations?strict=true',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2
    for item in response.json['items']:
        assert 'uid' in item
        assert 'evses' in item
        assert 'last_updated' in item
        assert 'original_uid' not in item


def test_get_ocpi_22_charging_station_strict(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(get_full_location_1())
    db.session.commit()

    response = public_test_client.get(
        path='/api/ocpi/2.2/charge-stations/1?strict=true',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'uid': '1',
        'last_updated': ANY,
        'evses': [
            {
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
            },
            {
                'uid': '2',
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
                        'id': '2',
                    },
                ],
            },
        ],
    }


def test_get_ocpi_22_charging_stations_by_source_uid(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_full_location_1(), get_full_location_2(), get_full_location_3()])
    db.session.commit()

    response = public_test_client.get(
        path=f'/api/ocpi/2.2/charge-stations?strict=true&source_uid={SOURCE_UID_1}',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2


def test_get_ocpi_22_charging_stations_by_location_id(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    db.session.add_all([get_full_location_1(), get_full_location_2()])
    db.session.commit()

    response = public_test_client.get(
        path='/api/ocpi/2.2/charge-stations?strict=true&location_id=1',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert len(response.json['items']) == 1


def test_get_ocpi_22_charging_station_non_strict(
    db: SQLAlchemy,
    test_client: OpenApiFlaskClient,
) -> None:
    db.session.add(get_full_location_1())
    db.session.commit()

    response = test_client.get(
        path='/api/ocpi/2.2/charge-stations/1',
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json
    assert 'uid' in data
    assert 'evses' in data
    assert 'original_uid' in data
