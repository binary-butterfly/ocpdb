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

import json
from decimal import Decimal
from pathlib import Path
from unittest.mock import ANY

from requests_mock import Mocker

from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import Connector, Evse, Location, Source
from webapp.models.evse import EvseStatus
from webapp.models.source import SourceStatus
from webapp.services.import_services.ocpi.chargecloud_afir.ludwigsburg.ludwigsburg_service import (
    LudwigsburgImportService,
)


def _load_test_data(filename: str) -> dict:
    data_dir = Path(__file__).parent / 'data'
    with open(data_dir / filename) as f:
        return json.load(f)


def test_ludwigsburg_fetch_static_data(db: SQLAlchemy, requests_mock: Mocker) -> None:
    """
    Test for LudwigsburgImportService.fetch_static_data().

    Checks the total number of imported datasets
    (should be 129 locations, 367 evses and 367 connectors more than before),
    and a sample of the imported data's content.
    """
    ludwigsburg_service: LudwigsburgImportService = dependencies.get_import_services().importer_by_uid[
        'chargecloud_ludwigsburg'
    ]

    locations_in_db_before = db.session.query(Location).count()
    evses_in_db_before = db.session.query(Evse).count()
    connectors_in_db_before = db.session.query(Connector).count()

    request_1_data = _load_test_data('request_1.json')
    request_2_data = _load_test_data('request_2.json')

    # Mock first request (no cursor param, returns data with next cursor)
    requests_mock.get(
        'https://afir.data.chargecloud.app/v1/2e60790a-4a07-446c-b4fc-30ce433a2735/locations',
        [
            {'status_code': 200, 'json': request_1_data},
            {'status_code': 200, 'json': request_2_data},
        ],
    )

    # Run the import
    ludwigsburg_service.fetch_static_data()

    # Check numbers of imported objects
    assert db.session.query(Location).count() - locations_in_db_before == 129
    assert db.session.query(Evse).count() - evses_in_db_before == 367
    assert db.session.query(Connector).count() - connectors_in_db_before == 367

    # Check a sample of the imported data
    sample_location = db.session.query(Location).filter(Location.uid == '1588625').first()
    assert sample_location is not None
    assert sample_location.to_dict() == {
        'id': ANY,
        'original_id': '1588625',
        'source': 'chargecloud_ludwigsburg',
        'name': 'LB Brenzstraße 2',
        'address': 'Brenzstraße 2',
        'postal_code': '71636',
        'city': 'Ludwigsburg',
        'state': None,
        'country': 'DEU',
        'coordinates': {
            'lat': Decimal('48.89233'),
            'lon': Decimal('9.18329'),
            'latitude': Decimal('48.89233'),
            'longitude': Decimal('9.18329'),
        },
        'directions': None,
        'regular_hours': None,
        'exceptional_openings': None,
        'exceptional_closings': None,
        'opening_times': {'twentyfourseven': True},
        'parking_type': None,
        'time_zone': 'Europe/Berlin',
        'last_updated': ANY,
        'publish': True,
        'terms_and_conditions': None,
    }
    assert len(sample_location.evses) == 2
    assert sample_location.operator.to_dict() == {
        'name': 'sw-ludwigsburg',
        'website': None,
    }


def test_ludwigsburg_fetch_realtime_data(db: SQLAlchemy, requests_mock: Mocker) -> None:
    """
    Test for LudwigsburgImportService.fetch_realtime_data().

    First imports static data to populate the database,
    then tests realtime update functionality.
    """
    ludwigsburg_service: LudwigsburgImportService = dependencies.get_import_services().importer_by_uid[
        'chargecloud_ludwigsburg'
    ]

    request_1_data = _load_test_data('request_1.json')
    request_2_data = _load_test_data('request_2.json')

    # Mock responses for both static and realtime imports
    requests_mock.get(
        'https://afir.data.chargecloud.app/v1/2e60790a-4a07-446c-b4fc-30ce433a2735/locations',
        [
            # First two responses for static import
            {'status_code': 200, 'json': request_1_data},
            {'status_code': 200, 'json': request_2_data},
            # Next two responses for realtime import
            {'status_code': 200, 'json': request_1_data},
            {'status_code': 200, 'json': request_2_data},
        ],
    )

    # First populate database with static data
    ludwigsburg_service.fetch_static_data()

    # Verify initial EVSE status from test data (CHARGING)
    # Note: EVSE uid is mapped from evse_id field, e.g., "DE*SLB*E001L10000*001"
    sample_evse = db.session.query(Evse).filter(Evse.uid == 'DE*SLB*E001L10000*001').first()
    assert sample_evse is not None
    assert sample_evse.status == EvseStatus.CHARGING

    # Run realtime update
    ludwigsburg_service.fetch_realtime_data()

    # Refresh the session to get updated data
    db.session.expire_all()

    # Verify EVSE status is still CHARGING (from test data)
    sample_evse = db.session.query(Evse).filter(Evse.uid == 'DE*SLB*E001L10000*001').first()
    assert sample_evse is not None
    assert sample_evse.status == EvseStatus.CHARGING

    # Verify second EVSE status (AVAILABLE from test data)
    sample_evse_2 = db.session.query(Evse).filter(Evse.uid == 'DE*SLB*E001L10000*002').first()
    assert sample_evse_2 is not None
    assert sample_evse_2.status == EvseStatus.AVAILABLE


def test_ludwigsburg_fetch_static_data_invalid_response(db: SQLAlchemy, requests_mock: Mocker) -> None:
    """
    Test for LudwigsburgImportService.fetch_static_data() with invalid JSON response.

    Verifies that when the API returns invalid data (missing required 'items' field),
    the source status is set to FAILED.
    """
    ludwigsburg_service: LudwigsburgImportService = dependencies.get_import_services().importer_by_uid[
        'chargecloud_ludwigsburg'
    ]

    # Invalid response data - missing required 'items' field
    invalid_response_data = {
        'next': None,
        'invalid_field': 'this response is missing the required items field',
    }

    requests_mock.get(
        'https://afir.data.chargecloud.app/v1/2e60790a-4a07-446c-b4fc-30ce433a2735/locations',
        status_code=200,
        json=invalid_response_data,
    )

    # Run the import - it should handle the error gracefully and set status to FAILED
    ludwigsburg_service.fetch_static_data()

    # Verify source status is set to FAILED
    source = db.session.query(Source).filter(Source.uid == 'chargecloud_ludwigsburg').first()
    assert source is not None
    assert source.static_status == SourceStatus.FAILED
