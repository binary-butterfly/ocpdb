"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2024 binary butterfly GmbH

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

from decimal import Decimal
from unittest.mock import ANY

from requests_mock import Mocker

from tests.integration.services.import_services.ocpi.sw_stuttgart.sw_stuttgart_data import sw_stuttgart_response_json
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import Connector, Evse, Location
from webapp.services.import_services.ocpi.chargecloud.sw_stuttgart import SWStuttgartImportService


def test_sw_stuttgart_import(db: SQLAlchemy, requests_mock: Mocker) -> None:
    """
    Test for the SWStuttgartImportService.

    Checks the total number of imported datasets
    (should be 234 locations, 523 evses and 526 connectors more than before),
    and a sample of the imported data's content.
    """

    sw_stuttgart_service: SWStuttgartImportService = dependencies.get_import_services().importer_by_uid[
        'chargecloud_stuttgart'
    ]

    locations_in_db_before = db.session.query(Location).count()
    evses_in_db_before = db.session.query(Evse).count()
    connectors_in_db_before = db.session.query(Connector).count()

    # define mocked response
    requests_mock.get(
        'https://new-poi.chargecloud.de/SW-Stuttgart',
        status_code=200,
        json=sw_stuttgart_response_json,
    )

    # run the import (this should make a request to the mocked sw stuttgart, parse the response, and save the data).
    sw_stuttgart_service.download_and_save()

    # check numbers of imported objects
    assert db.session.query(Location).count() - locations_in_db_before == 234
    assert db.session.query(Evse).count() - evses_in_db_before == 523
    assert db.session.query(Connector).count() - connectors_in_db_before == 526

    # check a sample of the imported data
    sample_location = db.session.query(Location).filter(Location.uid == '2185120').first()
    assert sample_location is not None
    assert sample_location.to_dict() == {
        'id': ANY,
        'original_id': '2185120',
        'source': 'chargecloud_stuttgart',
        'name': 'B+B Tiefgarage / Kronprinzstr. 6 / 4. UG',
        'address': 'Kronprinzstr. 6 / 4. UG',
        'postal_code': '70173',
        'city': 'Stuttgart',
        'state': None,
        'country': 'DEU',
        'coordinates': {
            'lat': Decimal('48.7774100'),
            'lon': Decimal('9.1762120'),
            'latitude': Decimal('48.7774100'),
            'longitude': Decimal('9.1762120'),
        },
        'directions': [
            {
                'language': 'DE',
                'text': 'Die Ladestationen befinden sich in der Tiefgarage im 4. UG. '
                'Bitte beachten Sie: 7 Ladestationen sind durchgehend verfügbar. '
                'Bei 3 Ladestationen sind die Öffnungszeiten eingeschränkt, '
                'genauere Infos finden Sie an der Beschilderung vor Ort.',
            },
        ],
        'opening_times': {'twentyfourseven': True},
        'parking_type': None,
        'time_zone': 'Europe/Berlin',
        'last_updated': None,
        'terms_and_conditions': None,
    }
    assert len(sample_location.evses) == 10
    assert sample_location.operator.to_dict() == {
        'name': 'Stadtwerke Stuttgart GmbH',
        'website': None,
    }
