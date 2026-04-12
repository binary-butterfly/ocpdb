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
from http import HTTPStatus
from unittest.mock import ANY

from tests.integration.helpers import OpenApiFlaskClient
from tests.integration.model_generators.business import BUSINESS_1_NAME, get_business_1
from tests.integration.model_generators.evse import get_full_evse_1
from tests.integration.model_generators.location import get_full_location_1, get_full_location_2, get_location_1
from tests.integration.model_generators.source import SOURCE_UID_1
from webapp.common.sqlalchemy import SQLAlchemy


class Datex2V37StaticApiTest:
    @staticmethod
    def test_get_static_empty(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.7/json/static')

        assert response.status_code == HTTPStatus.OK
        data = response.json

        assert 'payload' in data
        payload = data['payload']
        assert payload['versionG'] == '3.7'
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

        response = test_client.get(path='/api/public/datex/v3.7/json/static')

        assert response.status_code == HTTPStatus.OK
        data = response.json

        publication = data['payload']['aegiEnergyInfrastructureTablePublication']
        sites = publication['energyInfrastructureTable'][0]['energyInfrastructureSite']
        assert len(sites) == 1

        site = sites[0]
        assert site['idG'] == 'LOCATION-1'
        assert site['versionG'] == ANY
        assert site['name'] == {'values': [{'lang': 'de', 'value': 'Test Location'}]}
        assert site['operatingHours'] == {'afacOpenAllHours': {}}

    @staticmethod
    def test_get_static_location_reference(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.7/json/static')

        site = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ][0]

        location_ref = site['locationReference']
        point_location = location_ref['locPointLocation']
        coordinates = point_location['pointByCoordinates']['pointCoordinates']
        assert coordinates['latitude'] == 52.52003
        assert coordinates['longitude'] == 13.40489

        facility_location = point_location['locLocationExtensionG']['AfirFacilityLocation']
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

        response = test_client.get(path='/api/public/datex/v3.7/json/static')

        site = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ][0]

        operator = site['operator']
        org = operator['afacReferenceableOrganisation']
        assert org['name'] == {'values': [{'lang': 'de', 'value': BUSINESS_1_NAME}]}
        assert org['versionG'] == '1'
        assert org['organisationUnit'] == [{}]

    @staticmethod
    def test_get_static_station_and_evse(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.7/json/static')

        site = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ][0]

        stations = site['energyInfrastructureStation']
        assert len(stations) == 1

        station = stations[0]
        assert station['idG'] == 'CS-1'

        refill_points = station['refillPoint']
        assert len(refill_points) == 2

        charging_point = refill_points[0]['aegiElectricChargingPoint']
        assert charging_point['idG'] == 'EVSE-1'

    @staticmethod
    def test_get_static_connector_details(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.7/json/static')

        charging_point = response.json['payload']['aegiEnergyInfrastructureTablePublication'][
            'energyInfrastructureTable'
        ][0]['energyInfrastructureSite'][0]['energyInfrastructureStation'][0]['refillPoint'][0][
            'aegiElectricChargingPoint'
        ]

        assert charging_point['availableVoltage'] == [400.0]
        assert charging_point['availableChargingPower'] == [22000.0]

        connectors = charging_point['connector']
        assert len(connectors) == 1

        connector = connectors[0]
        assert connector['connectorType'] == {'value': 'iec62196T2'}
        assert connector['connectorFormat'] == {'value': 'socket'}
        assert connector['maxPowerAtSocket'] == 22000.0
        assert connector['voltage'] == 400.0
        assert connector['maximumCurrent'] == 32.0

    @staticmethod
    def test_get_static_dc_connector(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_2())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.7/json/static')

        charging_point = response.json['payload']['aegiEnergyInfrastructureTablePublication'][
            'energyInfrastructureTable'
        ][0]['energyInfrastructureSite'][0]['energyInfrastructureStation'][0]['refillPoint'][0][
            'aegiElectricChargingPoint'
        ]

        connector = charging_point['connector'][0]
        assert connector['connectorType'] == {'value': 'iec62196T2COMBO'}
        assert connector['connectorFormat'] == {'value': 'cableMode3'}
        assert connector['maxPowerAtSocket'] == 150000.0
        assert connector['voltage'] == 400.0
        assert connector['maximumCurrent'] == 350.0

    @staticmethod
    def test_get_static_location_without_name(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_location_1(name=None, evses=[get_full_evse_1()], operator=get_business_1()))
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.7/json/static')

        assert response.status_code == HTTPStatus.OK
        site = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ][0]
        assert 'name' not in site

    @staticmethod
    def test_get_static_multiple_locations(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add_all([get_full_location_1(), get_full_location_2()])
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.7/json/static')

        assert response.status_code == HTTPStatus.OK
        sites = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ]
        assert len(sites) == 2

        site_ids = {site['idG'] for site in sites}
        assert site_ids == {'LOCATION-1', 'LOCATION-2'}

    @staticmethod
    def test_get_static_filter_by_source_uid(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add_all([get_full_location_1(), get_full_location_2(source='OTHER-SOURCE')])
        db.session.commit()

        response = test_client.get(path=f'/api/public/datex/v3.7/json/static?source_uid={SOURCE_UID_1}')

        assert response.status_code == HTTPStatus.OK
        sites = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ]
        assert len(sites) == 1
        assert sites[0]['idG'] == 'LOCATION-1'

    @staticmethod
    def test_get_static_filter_by_bounding_box(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add_all([
            get_full_location_1(),
            get_full_location_2(lat=Decimal('48.13'), lon=Decimal('11.58')),
        ])
        db.session.commit()

        response = test_client.get(
            path='/api/public/datex/v3.7/json/static?lat_min=52.0&lat_max=53.0&lon_min=13.0&lon_max=14.0',
        )

        assert response.status_code == HTTPStatus.OK
        sites = response.json['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ]
        assert len(sites) == 1
        assert sites[0]['idG'] == 'LOCATION-1'
