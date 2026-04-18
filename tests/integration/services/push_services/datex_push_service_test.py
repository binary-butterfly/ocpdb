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

import json
from datetime import datetime, timezone
from unittest.mock import MagicMock

from requests_mock import Mocker

from tests.integration.model_generators.business import get_business_1
from tests.integration.model_generators.evse import get_full_evse_1, get_full_evse_2
from tests.integration.model_generators.location import get_full_location_1, get_full_location_2, get_location_1
from webapp.common.config import ConfigHelper
from webapp.common.contexts import ContextHelper
from webapp.common.redis import RedisKeyNotFoundException
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models.evse import EvseStatus
from webapp.services.push_services.datex_push_service import ChargeLocationService

MOBILITHEK_BASE_URL = 'https://mobilithek.info:8443/mobilithek/api/v1.0/publication'
STATIC_PUBLICATION_ID = '980054862909370368'
REALTIME_PUBLICATION_ID = '980084361378099200'


def _build_service(
    config_helper: ConfigHelper, context_helper: ContextHelper, version: str = '3.5'
) -> ChargeLocationService:
    redis_helper = MagicMock()
    redis_helper.get = MagicMock(side_effect=RedisKeyNotFoundException(message='not found'))
    redis_helper.set = MagicMock()

    config_helper.app.config['MOBILITHEK_VERSION'] = version
    config_helper.app.config['MOBILITHEK_NAME'] = 'binary butterfly GmbH'
    config_helper.app.config['MOBILITHEK_STATIC_PUBLICATION_ID'] = STATIC_PUBLICATION_ID
    config_helper.app.config['MOBILITHEK_REALTIME_PUBLICATION_ID'] = REALTIME_PUBLICATION_ID
    config_helper.app.config['MOBILITHEK_CERTIFICATE_FILENAME'] = 'test.crt.pem'
    config_helper.app.config['MOBILITHEK_KEY_FILENAME'] = 'test.key.pem'
    config_helper.app.config['KEY_DIR'] = '/app/keys'  # noqa: S108

    service = ChargeLocationService(
        config_helper=config_helper,
        context_helper=context_helper,
        location_repository=dependencies.get_location_repository(),
        redis_helper=redis_helper,
    )
    return service


class DatexPushServiceStaticTest:
    @staticmethod
    def test_push_static_v35_empty(db: SQLAlchemy, requests_mock: Mocker) -> None:
        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
            version='3.5',
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{STATIC_PUBLICATION_ID}', status_code=200)

        service.push_datex_static()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        assert 'payload' in body
        payload = body['payload']
        assert payload['versionG'] == '3.5'
        assert payload['profileNameG'] == 'Afir Energy Infrastructure'
        assert 'aegiEnergyInfrastructureTablePublication' in payload

        exchange_info = body['exchangeInformation']
        assert exchange_info['exchangeContext']['exchangeSpecificationVersion'] == '3.5'
        assert exchange_info['exchangeContext']['codedExchangeProtocol']['value'] == 'snapshotPush'
        assert exchange_info['dynamicInformation']['exchangeStatus']['value'] == 'online'

    @staticmethod
    def test_push_static_v35_with_location(db: SQLAlchemy, requests_mock: Mocker) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
            version='3.5',
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{STATIC_PUBLICATION_ID}', status_code=200)

        service.push_datex_static()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        publication = body['payload']['aegiEnergyInfrastructureTablePublication']
        sites = publication['energyInfrastructureTable'][0]['energyInfrastructureSite']
        assert len(sites) == 1
        assert sites[0]['idG'] == 'LOCATION-1'

    @staticmethod
    def test_push_static_v37_empty(db: SQLAlchemy, requests_mock: Mocker) -> None:
        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
            version='3.7',
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{STATIC_PUBLICATION_ID}', status_code=200)

        service.push_datex_static()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        payload = body['payload']
        assert payload['versionG'] == '3.7'
        assert payload['profileNameG'] == 'Afir Energy Infrastructure'

        exchange_info = body['exchangeInformation']
        assert exchange_info['exchangeContext']['exchangeSpecificationVersion'] == '3.7'

    @staticmethod
    def test_push_static_v37_with_location(db: SQLAlchemy, requests_mock: Mocker) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
            version='3.7',
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{STATIC_PUBLICATION_ID}', status_code=200)

        service.push_datex_static()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        publication = body['payload']['aegiEnergyInfrastructureTablePublication']
        sites = publication['energyInfrastructureTable'][0]['energyInfrastructureSite']
        assert len(sites) == 1
        assert sites[0]['idG'] == 'LOCATION-1'

    @staticmethod
    def test_push_static_v35_skips_location_with_only_static_evses(db: SQLAlchemy, requests_mock: Mocker) -> None:
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

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
            version='3.5',
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{STATIC_PUBLICATION_ID}', status_code=200)

        service.push_datex_static()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        sites = body['payload']['aegiEnergyInfrastructureTablePublication']['energyInfrastructureTable'][0][
            'energyInfrastructureSite'
        ]
        assert sites == []

    @staticmethod
    def test_push_static_v35_multiple_locations(db: SQLAlchemy, requests_mock: Mocker) -> None:
        db.session.add_all([get_full_location_1(), get_full_location_2()])
        db.session.commit()

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
            version='3.5',
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{STATIC_PUBLICATION_ID}', status_code=200)

        service.push_datex_static()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        publication = body['payload']['aegiEnergyInfrastructureTablePublication']
        sites = publication['energyInfrastructureTable'][0]['energyInfrastructureSite']
        assert len(sites) == 2
        site_ids = {site['idG'] for site in sites}
        assert site_ids == {'LOCATION-1', 'LOCATION-2'}


class DatexPushServiceRealtimeTest:
    @staticmethod
    def test_push_realtime_snapshot(db: SQLAlchemy, requests_mock: Mocker) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{REALTIME_PUBLICATION_ID}', status_code=200)

        service.push_datex_realtime()

        assert mock.called_once
        body = json.loads(mock.last_request.body)

        assert body['exchangeInformation']['exchangeContext']['codedExchangeProtocol']['value'] == 'snapshotPush'

        payload = body['payload']
        assert payload['versionG'] == '3.5'
        status_pub = payload['aegiEnergyInfrastructureStatusPublication']
        site_statuses = status_pub['energyInfrastructureSiteStatus']
        assert len(site_statuses) == 1
        assert site_statuses[0]['reference']['idG'] == 'LOCATION-1'

        service.redis_helper.set.assert_called_once()

    @staticmethod
    def test_push_realtime_with_updated_since(db: SQLAlchemy, requests_mock: Mocker) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{REALTIME_PUBLICATION_ID}', status_code=200)

        updated_since = datetime(2020, 1, 1, tzinfo=timezone.utc)
        service.push_datex_realtime(updated_since=updated_since)

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        assert body['exchangeInformation']['exchangeContext']['codedExchangeProtocol']['value'] == 'deltaPush'

    @staticmethod
    def test_push_realtime_incremental_update_no_previous(db: SQLAlchemy, requests_mock: Mocker) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{REALTIME_PUBLICATION_ID}', status_code=200)

        service.push_datex_realtime(incremental_update=True)

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        # No previous push stored in Redis, so updated_since is None -> snapshotPush
        assert body['exchangeInformation']['exchangeContext']['codedExchangeProtocol']['value'] == 'snapshotPush'
        service.redis_helper.get.assert_called_once_with('last_datex_realtime_push')

    @staticmethod
    def test_push_realtime_incremental_update_with_previous(db: SQLAlchemy, requests_mock: Mocker) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
        )
        last_push = datetime(2025, 6, 1, 12, 0, 0, tzinfo=timezone.utc)
        service.redis_helper.get = MagicMock(return_value=last_push.isoformat())

        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{REALTIME_PUBLICATION_ID}', status_code=200)

        service.push_datex_realtime(incremental_update=True)

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        # Previous push found in Redis -> deltaPush
        assert body['exchangeInformation']['exchangeContext']['codedExchangeProtocol']['value'] == 'deltaPush'

    @staticmethod
    def test_push_realtime_evse_status_mapping(db: SQLAlchemy, requests_mock: Mocker) -> None:
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

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{REALTIME_PUBLICATION_ID}', status_code=200)

        service.push_datex_realtime()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        refill_statuses = body['payload']['aegiEnergyInfrastructureStatusPublication'][
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
    def test_push_realtime_v35_filters_static_evse(db: SQLAlchemy, requests_mock: Mocker) -> None:
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

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
            version='3.5',
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{REALTIME_PUBLICATION_ID}', status_code=200)

        service.push_datex_realtime()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        refill_statuses = body['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ][0]['energyInfrastructureStationStatus'][0]['refillPointStatus']

        assert len(refill_statuses) == 1
        assert refill_statuses[0]['aegiRefillPointStatus']['reference']['idG'] == 'EVSE-1'

    @staticmethod
    def test_push_realtime_v37_filters_static_evse(db: SQLAlchemy, requests_mock: Mocker) -> None:
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

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
            version='3.7',
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{REALTIME_PUBLICATION_ID}', status_code=200)

        service.push_datex_realtime()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        refill_statuses = body['payload']['aegiEnergyInfrastructureStatusPublication'][
            'energyInfrastructureSiteStatus'
        ][0]['energyInfrastructureStationStatus'][0]['refillPointStatus']

        assert len(refill_statuses) == 1
        assert refill_statuses[0]['aegiRefillPointStatus']['reference']['idG'] == 'EVSE-1'

    @staticmethod
    def test_push_realtime_skips_location_with_only_static_evses(db: SQLAlchemy, requests_mock: Mocker) -> None:
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

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
        )
        mock = requests_mock.post(f'{MOBILITHEK_BASE_URL}/{REALTIME_PUBLICATION_ID}', status_code=200)

        service.push_datex_realtime()

        assert mock.called_once
        body = json.loads(mock.last_request.body)
        site_statuses = body['payload']['aegiEnergyInfrastructureStatusPublication']['energyInfrastructureSiteStatus']
        assert site_statuses == []

    @staticmethod
    def test_push_realtime_stores_timestamp_in_redis(db: SQLAlchemy, requests_mock: Mocker) -> None:
        db.session.add(get_full_location_1())
        db.session.commit()

        service = _build_service(
            dependencies.get_config_helper(),
            dependencies.get_context_helper(),
        )
        requests_mock.post(f'{MOBILITHEK_BASE_URL}/{REALTIME_PUBLICATION_ID}', status_code=200)

        service.push_datex_realtime()

        service.redis_helper.set.assert_called_once()
        call_args = service.redis_helper.set.call_args
        assert call_args[0][0] == 'last_datex_realtime_push'
        stored_timestamp = datetime.fromisoformat(call_args[0][1])
        assert stored_timestamp.tzinfo is not None
