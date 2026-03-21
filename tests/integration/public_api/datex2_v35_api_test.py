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

from datetime import datetime, timezone
from http import HTTPStatus
from unittest.mock import ANY

from tests.integration.helpers import OpenApiFlaskClient
from tests.integration.model_generators.business import BUSINESS_1_NAME, get_business_1
from tests.integration.model_generators.evse import get_full_evse_1, get_full_evse_2
from tests.integration.model_generators.location import get_full_location_1, get_full_location_2, get_location_1
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.models.evse import EvseStatus


class Datex2V35StaticApiTest:
    @staticmethod
    def test_get_static_empty(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.5/json/static')

        assert response.status_code == HTTPStatus.OK
        data = response.json

        assert 'payload' in data
        payload = data['payload']
        assert payload['versionG'] == '3.5'
        assert payload['profileNameG'] == 'Afir Energy Infrastructure'
        assert payload['profileVersionG'] == '01-00-00'

        publication = payload['aegiEnergyInfrastructureTablePublication']
        assert publication['lang'] == 'de'
        assert publication['publicationCreator'] == {'country': 'DE', 'nationalIdentifier': 'OCPDB'}
        assert publication['energyInfrastructureTable'] == [
            {'idG': '1', 'versionG': '1', 'energyInfrastructureSite': []}
        ]

    @staticmethod
    def test_get_static_with_location(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/static')

        assert response.status_code == HTTPStatus.OK
        data = response.json

        publication = data['payload']['aegiEnergyInfrastructureTablePublication']
        sites = publication['energyInfrastructureTable'][0]['energyInfrastructureSite']
        assert len(sites) == 1

        site = sites[0]
        assert site['idG'] == 'LOCATION-1'
        assert site['versionG'] == ANY
        assert site['additionalInformation'] == [{'values': [{'lang': 'de', 'value': 'Test Location'}]}]
        assert site['operatingHours'] == {'afacOpenAllHours': {}}

    @staticmethod
    def test_get_static_location_reference(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/static')

        site = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ][0]

        location_ref = site['locationReference']
        assert location_ref['locAreaLocation']['coordinatesForDisplay']['latitude'] == 52.52003
        assert location_ref['locAreaLocation']['coordinatesForDisplay']['longitude'] == 13.40489

        facility_location = location_ref['locPointLocation']['locLocationExtensionG']['FacilityLocation']
        address = facility_location['address']
        assert address['postcode'] == '12345'
        assert address['city'] == {'values': [{'lang': 'de', 'value': 'Test City'}]}
        assert address['countryCode'] == 'DE'

        address_lines = address['addressLine']
        assert len(address_lines) == 2
        assert address_lines[0]['order'] == 1
        assert address_lines[0]['type'] == {'value': 'street'}
        assert address_lines[0]['text'] == {'values': [{'lang': 'de', 'value': 'Test Street'}]}
        assert address_lines[1]['order'] == 2
        assert address_lines[1]['type'] == {'value': 'houseNumber'}
        assert address_lines[1]['text'] == {'values': [{'lang': 'de', 'value': '123'}]}

    @staticmethod
    def test_get_static_operator(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/static')

        site = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ][0]

        operator = site['operator']
        assert operator == {
            'afacAnOrganisation': {
                'name': {'values': [{'lang': 'de', 'value': BUSINESS_1_NAME}]},
            },
        }

    @staticmethod
    def test_get_static_station_and_evse(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/static')

        site = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ][0]

        stations = site['energyInfrastructureStation']
        assert len(stations) == 1

        station = stations[0]
        assert station['idG'] == 'CS-1'
        assert station['numberOfRefillPoints'] == 2

        refill_points = station['refillPoint']
        assert len(refill_points) == 2

        charging_point = refill_points[0]['aegiElectricChargingPoint']
        assert charging_point['idG'] == 'EVSE-1'
        assert charging_point['deliveryUnit'] == {'value': 'kWh'}
        assert charging_point['currentType'] == {'value': 'ac'}
        assert charging_point['numberOfConnectors'] == 1

    @staticmethod
    def test_get_static_connector_details(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/static')

        charging_point = response.json['payload']['aegiEnergyInfrastructureTablePublication'][
            'energyInfrastructureTable'
        ][0]['energyInfrastructureSite'][0]['energyInfrastructureStation'][0]['refillPoint'][0][
            'aegiElectricChargingPoint'
        ]

        assert charging_point['availableVoltage'] == [400.0]
        assert charging_point['availableChargingPower'] == [22.0]

        connectors = charging_point['connector']
        assert len(connectors) == 1

        connector = connectors[0]
        assert connector['connectorType'] == {'value': 'iec62196T2'}
        assert connector['connectorFormat'] == {'value': 'socket'}
        assert connector['maxPowerAtSocket'] == 22.0
        assert connector['voltage'] == 400.0
        assert connector['maximumCurrent'] == 32.0

    @staticmethod
    def test_get_static_dc_connector(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_2())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/static')

        charging_point = response.json['payload']['aegiEnergyInfrastructureTablePublication'][
            'energyInfrastructureTable'
        ][0]['energyInfrastructureSite'][0]['energyInfrastructureStation'][0]['refillPoint'][0][
            'aegiElectricChargingPoint'
        ]

        assert charging_point['currentType'] == {'value': 'dc'}

        connector = charging_point['connector'][0]
        assert connector['connectorType'] == {'value': 'iec62196T2COMBO'}
        assert connector['connectorFormat'] == {'value': 'cableMode3'}
        assert connector['maxPowerAtSocket'] == 150.0
        assert connector['voltage'] == 400.0
        assert connector['maximumCurrent'] == 350.0

    @staticmethod
    def test_get_static_location_without_name(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_location_1(name=None, evses=[get_full_evse_1()], operator=get_business_1()))
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/static')

        assert response.status_code == HTTPStatus.OK
        site = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ][0]
        assert 'additionalInformation' not in site

    @staticmethod
    def test_get_static_multiple_locations(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add_all([get_full_location_1(), get_full_location_2()])
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/static')

        assert response.status_code == HTTPStatus.OK
        sites = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ]
        assert len(sites) == 2

        site_ids = {site['idG'] for site in sites}
        assert site_ids == {'LOCATION-1', 'LOCATION-2'}


class Datex2RealtimeApiTest:
    @staticmethod
    def test_get_realtime_empty(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        assert response.status_code == HTTPStatus.OK
        data = response.json

        assert 'payload' in data

    @staticmethod
    def test_get_realtime_payload_structure(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        assert response.status_code == HTTPStatus.OK
        payload = response.json['payload']

        assert payload['versionG'] == '3.5'
        assert payload['profileNameG'] == 'AFIR Energy Infrastructure'
        assert payload['profileVersionG'] == '01-00-00'

        status_pub = payload['aegiEnergyInfrastructureStatusPublication']
        assert status_pub['lang'] == 'de'
        assert status_pub['publicationCreator'] == {'country': 'DE', 'nationalIdentifier': 'OCPDB'}

    @staticmethod
    def test_get_realtime_with_location(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        assert response.status_code == HTTPStatus.OK
        status_pub = response.json['payload']['aegiEnergyInfrastructureStatusPublication']

        site_statuses = status_pub['energyInfrastructureSiteStatus']
        assert len(site_statuses) == 1

        site_status = site_statuses[0]
        assert site_status['reference']['targetClass'] == 'FacilityObject'
        assert site_status['reference']['idG'] == 'LOCATION-1'
        assert site_status['lastUpdated'] == ANY

    @staticmethod
    def test_get_realtime_station_status(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        site_status = response.json['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ][0]

        station_statuses = site_status['energyInfrastructureStationStatus']
        assert len(station_statuses) == 1

        station_status = station_statuses[0]
        assert station_status['reference']['targetClass'] == 'FacilityObject'
        assert station_status['reference']['idG'] == 'CS-1'

    @staticmethod
    def test_get_realtime_evse_status(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        station_status = response.json['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ][0]['energyInfrastructureStationStatus'][0]

        refill_statuses = station_status['refillPointStatus']
        assert len(refill_statuses) == 2

        refill_status = refill_statuses[0]['aegiRefillPointStatus']
        assert refill_status['reference']['targetClass'] == 'FacilityObject'
        assert refill_status['reference']['idG'] == 'EVSE-1'
        assert refill_status['status'] == {'value': 'available'}
        assert 'lastUpdated' in refill_status

    @staticmethod
    def test_get_realtime_evse_status_mapping(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(
            get_location_1(
                evses=[
                    get_full_evse_1(status=EvseStatus.CHARGING),
                    get_full_evse_2(status=EvseStatus.OUTOFORDER),
                ],
                operator=get_business_1(),
            ),
        )
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        refill_statuses = response.json['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ][0]['energyInfrastructureStationStatus'][0]['refillPointStatus']

        statuses = {
            rs['aegiRefillPointStatus']['reference']['idG']: rs['aegiRefillPointStatus']['status']['value']
            for rs in refill_statuses
        }
        assert statuses == {
            'EVSE-1': 'charging',
            'EVSE-2': 'outOfOrder',
        }

    @staticmethod
    def test_get_realtime_skips_static_evse(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(
            get_location_1(
                evses=[
                    get_full_evse_1(status=EvseStatus.AVAILABLE),
                    get_full_evse_2(status=EvseStatus.STATIC),
                ],
                operator=get_business_1(),
            ),
        )
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        refill_statuses = response.json['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ][0]['energyInfrastructureStationStatus'][0]['refillPointStatus']

        assert len(refill_statuses) == 1
        assert refill_statuses[0]['aegiRefillPointStatus']['reference']['idG'] == 'EVSE-1'

    @staticmethod
    def test_get_realtime_skips_station_with_all_unmappable_evses(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(
            get_location_1(
                evses=[
                    get_full_evse_1(status=EvseStatus.STATIC),
                    get_full_evse_2(status=EvseStatus.STATIC),
                ],
                operator=get_business_1(),
            ),
        )
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        site_statuses = response.json['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ]

        assert len(site_statuses) == 0

    @staticmethod
    def test_get_realtime_multiple_locations(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add_all([get_full_location_1(), get_full_location_2()])
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        assert response.status_code == HTTPStatus.OK
        site_statuses = response.json['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ]
        assert len(site_statuses) == 2

        site_ids = {ss['reference']['idG'] for ss in site_statuses}
        assert site_ids == {'LOCATION-1', 'LOCATION-2'}

    @staticmethod
    def test_get_realtime_evse_status_last_updated_fallback(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        now = datetime.now(tz=timezone.utc)
        status_updated = datetime(2026, 1, 15, 12, 0, 0, tzinfo=timezone.utc)

        db.session.add(
            get_location_1(
                evses=[
                    get_full_evse_1(last_updated=now, status_last_updated=status_updated),
                    get_full_evse_2(last_updated=now, status_last_updated=None),
                ],
                operator=get_business_1(),
            ),
        )
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/realtime')

        refill_statuses = response.json['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ][0]['energyInfrastructureStationStatus'][0]['refillPointStatus']

        evse_1_status = next(
            rs['aegiRefillPointStatus']
            for rs in refill_statuses
            if rs['aegiRefillPointStatus']['reference']['idG'] == 'EVSE-1'
        )
        assert evse_1_status['lastUpdated'] == status_updated.isoformat()

        evse_2_status = next(
            rs['aegiRefillPointStatus']
            for rs in refill_statuses
            if rs['aegiRefillPointStatus']['reference']['idG'] == 'EVSE-2'
        )
        assert evse_2_status['lastUpdated'] == now.isoformat()
