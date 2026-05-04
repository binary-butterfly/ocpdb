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

from decimal import Decimal
from pathlib import Path

import pytest
from requests_mock import Mocker

from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import Business, ChargingStation, Connector, Evse, Location, Tariff
from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import EvseStatus
from webapp.models.source import SourceStatus
from webapp.services.import_services.datex2 import GiroEDatex2ImportService

STATIC_SUBSCRIPTION_URL = 'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID=13579'

SOURCE_UID = 'datex2_giroe'
EXPECTED_LOCATION_COUNT = 8
EXPECTED_STATION_COUNT = 43
EXPECTED_EVSE_COUNT = 72


def _load_test_data(filename: str) -> str:
    json_path = Path(Path(__file__).parent, 'data', filename)
    with json_path.open() as json_file:
        return json_file.read()


@pytest.fixture
def giroe_datex2_import_service(requests_mock: Mocker) -> GiroEDatex2ImportService:
    requests_mock.get(
        STATIC_SUBSCRIPTION_URL,
        status_code=200,
        text=_load_test_data('datex2_giroe_static_reduced.json'),
        headers={'Content-Type': 'application/json'},
    )

    return dependencies.get_import_services().importer_by_uid[SOURCE_UID]


def test_giroe_datex2_static_import(
    db: SQLAlchemy,
    giroe_datex2_import_service: GiroEDatex2ImportService,
) -> None:
    giroe_datex2_import_service.fetch_static_data()

    assert db.session.query(Location).count() == EXPECTED_LOCATION_COUNT
    assert db.session.query(ChargingStation).count() == EXPECTED_STATION_COUNT
    assert db.session.query(Evse).count() == EXPECTED_EVSE_COUNT
    assert db.session.query(Connector).count() == EXPECTED_EVSE_COUNT
    # All sites share the same operator GLS Mobility GmbH
    assert db.session.query(Business).count() == 1
    business = db.session.query(Business).first()
    assert business.name == 'GLS Mobility GmbH'

    # Each EVSE keeps the tariff association of its last energy rate, so #tariffs == #EVSEs
    assert db.session.query(Tariff).count() == EXPECTED_EVSE_COUNT

    source = giroe_datex2_import_service.get_source()
    assert source.static_status == SourceStatus.ACTIVE


def test_giroe_datex2_static_import_maps_location_fields(
    db: SQLAlchemy,
    giroe_datex2_import_service: GiroEDatex2ImportService,
) -> None:
    giroe_datex2_import_service.fetch_static_data()

    # Site 2629 in Bochum: address line composed from street + houseNumber, country mapped to alpha-3.
    location = db.session.query(Location).filter(Location.uid == '2629').first()
    assert location is not None
    assert location.lat == Decimal('51.4708953')
    assert location.lon == Decimal('7.2195074')
    assert location.address == 'Christstr. 9-11'
    assert location.city == 'Bochum'
    assert location.postal_code == '44789 '
    assert location.country == 'DEU'
    assert location.time_zone == '+01:00'
    assert location.twentyfourseven is True
    assert location.operator is not None
    assert location.operator.name == 'GLS Mobility GmbH'

    # Five stations under site 2629 (10338, 10687, 10994, 12628, 17032), eight EVSEs in total.
    station_uids = sorted(cs.uid for cs in location.charging_pool)
    assert station_uids == ['10338', '10687', '10994', '12628', '17032']
    assert sum(len(cs.evses) for cs in location.charging_pool) == 8


def test_giroe_datex2_static_import_maps_evse_and_connector(
    db: SQLAlchemy,
    giroe_datex2_import_service: GiroEDatex2ImportService,
) -> None:
    giroe_datex2_import_service.fetch_static_data()

    # 22 kW Type 2 socket on AC, 3-phase derived from mode2AC3p / iec62196T2.
    evse = db.session.query(Evse).filter(Evse.uid == '10338').first()
    assert evse is not None
    assert evse.evse_id == '10338'
    # No realtime data fetched yet - EVSE status defaults to UNKNOWN.
    assert evse.status == EvseStatus.UNKNOWN
    assert len(evse.connectors) == 1

    connector = evse.connectors[0]
    assert connector.standard == ConnectorType.IEC_62196_T2
    assert connector.format == ConnectorFormat.SOCKET
    assert connector.power_type == PowerType.AC_3_PHASE
    assert connector.max_electric_power == 22000

    # Site 17032 / EVSE 20842 uses connectorFormat "cableMode2" in the source data,
    # but the mapper picks SOCKET for AC connectors regardless of the source format.
    cable_evse = db.session.query(Evse).filter(Evse.uid == '20842').first()
    assert cable_evse is not None
    assert len(cable_evse.connectors) == 1
    assert cable_evse.connectors[0].format == ConnectorFormat.SOCKET
    assert cable_evse.connectors[0].max_electric_power == 11000

    # Each EVSE collapses to a single TariffAssociation (last energy rate wins).
    assert len(evse.tariff_associations) == 1
    assert len(evse.connectors) == 1


def test_giroe_datex2_static_import_handles_empty_energy_price_list(
    db: SQLAlchemy,
    giroe_datex2_import_service: GiroEDatex2ImportService,
) -> None:
    """
    Some Bochum (4378) EVSEs have a single energyRate with an empty energyPrice list. The importer must still
    create a Tariff for them (even if it carries no price elements) rather than dropping the EVSE.
    """
    giroe_datex2_import_service.fetch_static_data()

    evse = db.session.query(Evse).filter(Evse.uid == '18812').first()
    assert evse is not None
    assert len(evse.tariff_associations) == 1
    tariff = evse.tariff_associations[0].tariff
    assert tariff is not None
    assert tariff.elements == []
