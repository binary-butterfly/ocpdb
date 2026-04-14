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

import pytest

from tests.integration.helpers import OpenApiFlaskClient
from tests.integration.model_generators.business import get_business_1
from tests.integration.model_generators.evse import get_full_evse_1, get_full_evse_2, get_full_evse_3, get_full_evse_4
from tests.integration.model_generators.location import get_full_location_1, get_full_location_2, get_location_1
from webapp.common.flask_app import App
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.models.evse import EvseStatus


@pytest.fixture(autouse=True)
def _set_mobilithek_config(flask_app: App) -> None:
    flask_app.config['MOBILITHEK_NAME'] = 'Test Organisation'


class Datex2V37MobilithekRealtimeApiTest:
    @staticmethod
    def test_get_realtime_empty(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.7/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        data = response.json

        assert 'message_container' in data
        message_container = data['message_container']

        assert 'payload' in message_container
        assert 'exchangeInformation' in message_container

        exchange_info = message_container['exchangeInformation']
        assert exchange_info['exchangeContext']['codedExchangeProtocol']['value'] == 'snapshotPush'
        assert exchange_info['exchangeContext']['exchangeSpecificationVersion'] == '3.7'
        assert exchange_info['exchangeContext']['supplierOrCisRequester']['name'] == 'Test Organisation'
        assert exchange_info['dynamicInformation']['exchangeStatus']['value'] == 'online'

    @staticmethod
    def test_get_realtime_snapshot_protocol(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.7/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        exchange_info = response.json['message_container']['exchangeInformation']
        assert exchange_info['exchangeContext']['codedExchangeProtocol']['value'] == 'snapshotPush'

    @staticmethod
    def test_get_realtime_delta_protocol_with_last_modified_since(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(
            path='/api/public/datex/v3.7/json/mobilithek/realtime?last_modified_since=2020-01-01T00:00:00Z',
        )

        assert response.status_code == HTTPStatus.OK
        exchange_info = response.json['message_container']['exchangeInformation']
        assert exchange_info['exchangeContext']['codedExchangeProtocol']['value'] == 'deltaPush'

    @staticmethod
    def test_get_realtime_with_location(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.7/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        payload = response.json['message_container']['payload']
        status_pub = payload['aegiEnergyInfrastructureStatusPublication']

        site_statuses = status_pub['energyInfrastructureSiteStatus']
        assert len(site_statuses) == 1
        assert site_statuses[0]['reference']['idG'] == 'LOCATION-1'

    @staticmethod
    def test_get_realtime_multiple_locations(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add_all([get_full_location_1(), get_full_location_2()])
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.7/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        site_statuses = response.json['message_container']['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ]
        assert len(site_statuses) == 2

        site_ids = {ss['reference']['idG'] for ss in site_statuses}
        assert site_ids == {'LOCATION-1', 'LOCATION-2'}

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

        response = test_client.get(path='/api/public/datex/v3.7/json/mobilithek/realtime')

        refill_statuses = response.json['message_container']['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ][0]['energyInfrastructureStationStatus'][0]['refillPointStatus']

        assert len(refill_statuses) == 1
        assert refill_statuses[0]['aegiRefillPointStatus']['reference']['idG'] == 'EVSE-1'

    @staticmethod
    def test_get_realtime_last_modified_since_filters_locations(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        old_update = datetime(2020, 1, 1, tzinfo=timezone.utc)
        recent_update = datetime(2025, 6, 1, tzinfo=timezone.utc)

        db.session.add_all([
            get_location_1(
                evses=[
                    get_full_evse_1(status_last_updated=old_update),
                    get_full_evse_2(status_last_updated=old_update),
                ],
                operator=get_business_1(),
            ),
            get_location_1(
                uid='LOCATION-2',
                evses=[
                    get_full_evse_3(status_last_updated=recent_update),
                    get_full_evse_4(status_last_updated=recent_update),
                ],
                operator=get_business_1(),
            ),
        ])
        db.session.commit()

        response = test_client.get(
            path='/api/public/datex/v3.7/json/mobilithek/realtime?last_modified_since=2025-01-01T00:00:00Z',
        )

        assert response.status_code == HTTPStatus.OK
        site_statuses = response.json['message_container']['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ]
        assert len(site_statuses) == 1
        assert site_statuses[0]['reference']['idG'] == 'LOCATION-2'

    @staticmethod
    def test_get_realtime_message_generation_timestamp(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.7/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        dynamic_info = response.json['message_container']['exchangeInformation']['dynamicInformation']
        assert 'messageGenerationTimestamp' in dynamic_info


class Datex2V35MobilithekRealtimeApiTest:
    @staticmethod
    def test_get_realtime_empty(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.5/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        data = response.json

        assert 'message_container' in data
        message_container = data['message_container']

        assert 'payload' in message_container
        assert 'exchangeInformation' in message_container

        exchange_info = message_container['exchangeInformation']
        assert exchange_info['exchangeContext']['codedExchangeProtocol']['value'] == 'snapshotPush'
        assert exchange_info['exchangeContext']['exchangeSpecificationVersion'] == '3.5'
        assert exchange_info['exchangeContext']['supplierOrCisRequester']['name'] == 'Test Organisation'
        assert exchange_info['dynamicInformation']['exchangeStatus']['value'] == 'online'

    @staticmethod
    def test_get_realtime_snapshot_protocol(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.5/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        exchange_info = response.json['message_container']['exchangeInformation']
        assert exchange_info['exchangeContext']['codedExchangeProtocol']['value'] == 'snapshotPush'

    @staticmethod
    def test_get_realtime_delta_protocol_with_last_modified_since(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(
            path='/api/public/datex/v3.5/json/mobilithek/realtime?last_modified_since=2020-01-01T00:00:00Z',
        )

        assert response.status_code == HTTPStatus.OK
        exchange_info = response.json['message_container']['exchangeInformation']
        assert exchange_info['exchangeContext']['codedExchangeProtocol']['value'] == 'deltaPush'

    @staticmethod
    def test_get_realtime_with_location(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        payload = response.json['message_container']['payload']
        status_pub = payload['aegiEnergyInfrastructureStatusPublication']

        site_statuses = status_pub['energyInfrastructureSiteStatus']
        assert len(site_statuses) == 1
        assert site_statuses[0]['reference']['idG'] == 'LOCATION-1'

    @staticmethod
    def test_get_realtime_multiple_locations(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        db.session.add_all([get_full_location_1(), get_full_location_2()])
        db.session.commit()

        response = test_client.get(path='/api/public/datex/v3.5/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        site_statuses = response.json['message_container']['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ]
        assert len(site_statuses) == 2

        site_ids = {ss['reference']['idG'] for ss in site_statuses}
        assert site_ids == {'LOCATION-1', 'LOCATION-2'}

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

        response = test_client.get(path='/api/public/datex/v3.5/json/mobilithek/realtime')

        refill_statuses = response.json['message_container']['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ][0]['energyInfrastructureStationStatus'][0]['refillPointStatus']

        assert len(refill_statuses) == 1
        assert refill_statuses[0]['aegiRefillPointStatus']['reference']['idG'] == 'EVSE-1'

    @staticmethod
    def test_get_realtime_last_modified_since_filters_locations(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        old_update = datetime(2020, 1, 1, tzinfo=timezone.utc)
        recent_update = datetime(2025, 6, 1, tzinfo=timezone.utc)

        db.session.add_all([
            get_location_1(
                evses=[
                    get_full_evse_1(status_last_updated=old_update),
                    get_full_evse_2(status_last_updated=old_update),
                ],
                operator=get_business_1(),
            ),
            get_location_1(
                uid='LOCATION-2',
                evses=[
                    get_full_evse_3(status_last_updated=recent_update),
                    get_full_evse_4(status_last_updated=recent_update),
                ],
                operator=get_business_1(),
            ),
        ])
        db.session.commit()

        response = test_client.get(
            path='/api/public/datex/v3.5/json/mobilithek/realtime?last_modified_since=2025-01-01T00:00:00Z',
        )

        assert response.status_code == HTTPStatus.OK
        site_statuses = response.json['message_container']['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ]
        assert len(site_statuses) == 1
        assert site_statuses[0]['reference']['idG'] == 'LOCATION-2'

    @staticmethod
    def test_get_realtime_message_generation_timestamp(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.get(path='/api/public/datex/v3.5/json/mobilithek/realtime')

        assert response.status_code == HTTPStatus.OK
        dynamic_info = response.json['message_container']['exchangeInformation']['dynamicInformation']
        assert 'messageGenerationTimestamp' in dynamic_info
