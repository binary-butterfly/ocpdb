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
from pathlib import Path
from unittest.mock import ANY

from requests_mock import Mocker

from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import Connector, Evse, Location
from webapp.models.connector import ConnectorFormat, ConnectorType
from webapp.models.evse import EvseStatus
from webapp.services.import_services.bnetza import BnetzaImportService


def test_bnetza_import(db: SQLAlchemy, requests_mock: Mocker) -> None:
    """
    Test for the BnetzaImportService.

    Checks the total number of imported datasets
    (should be 94 locations, 189 evses and 226 connectors more than before),
    and a sample of the imported data's content.

    If you update the bnetza.xlsx, please don't put the full file in there, but cut at a reasonable amount of lines.
    When writing this test, we limited the file to line 119 included.
    """

    bnetza_import_service: BnetzaImportService = dependencies.get_import_services().bnetza_import_service

    bnetza_file_path = Path(Path(__file__).parent, 'bnetza.xlsx')
    with bnetza_file_path.open('rb') as bnetza_file:
        requests_mock.get('mock://bnetza', content=bnetza_file.read())

    bnetza_import_service.load_and_save_from_web()

    assert db.session.query(Location).count() == 94
    assert db.session.query(Evse).count() == 189
    assert db.session.query(Connector).count() == 226

    location = db.session.query(Location).first()

    assert location.to_dict() == {
        'id': '1',
        'original_id': '81d943a159d326f16932',
        'source': 'bnetza',
        'name': None,
        'address': 'Ennabeurer Weg',
        'postal_code': '72535',
        'city': 'Heroldstatt',
        'state': None,
        'country': 'DEU',
        'coordinates': {
            'lat': Decimal('48.4423980'),
            'lon': Decimal('9.6590750'),
            'latitude': Decimal('48.4423980'),
            'longitude': Decimal('9.6590750'),
        },
        'directions': None,
        'parking_type': None,
        'time_zone': None,
        'last_updated': ANY,
        'terms_and_conditions': None,
    }

    evses = db.session.query(Evse).filter(Evse.location_id == 1).all()

    assert len(evses)
    assert evses[0].to_dict() == {
        'uid': '1',
        'original_uid': 'BNETZA*81d943a159d326f16932*0*1',
        'evse_id': 'BNETZA*81d943a159d326f16932*0*1',
        'status': EvseStatus.STATIC,
        'floor_level': None,
        'physical_reference': None,
        'directions': None,
        'phone': None,
        'parking_uid': None,
        'parking_floor_level': None,
        'parking_spot_number': None,
        'last_updated': ANY,
        'max_reservation': None,
        'capabilities': [],
        'parking_restrictions': [],
        'terms_and_conditions': None,
    }

    connectors = db.session.query(Connector).filter(Connector.evse_id == 1).all()

    assert len(connectors) == 1

    assert connectors[0].to_dict() == {
        'id': '1',
        'original_id': '81d943a159d326f16932-0-1-0',
        'standard': ConnectorType.IEC_62196_T2,
        'format': ConnectorFormat.SOCKET,
        'power_type': None,
        'max_voltage': None,
        'max_amperage': None,
        'max_electric_power': 22000,
        'last_updated': None,
        'terms_and_conditions': None,
    }
