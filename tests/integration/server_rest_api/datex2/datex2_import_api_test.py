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

import gzip
import json
from http import HTTPStatus
from pathlib import Path
from unittest.mock import patch

import pytest
from requests_mock import Mocker

from tests.integration.helpers import OpenApiFlaskClient
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import Evse
from webapp.models.evse import EvseStatus

SOURCE_UID = 'datex2_enbw'
API_KEY = 'test-datex2-api-key'
STATIC_SUBSCRIPTION_URL = 'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID=12345'


def _load_test_data_text(filename: str) -> str:
    json_path = Path(__file__).parent.parent.parent / 'services' / 'import_services' / 'datex2' / 'data' / filename
    with json_path.open() as json_file:
        return json_file.read()


def _load_test_data(filename: str) -> dict:
    return json.loads(_load_test_data_text(filename))


def _import_static_data(requests_mock: Mocker) -> None:
    requests_mock.get(
        STATIC_SUBSCRIPTION_URL,
        status_code=200,
        text=_load_test_data_text('datex2_enbw_static_reduced.json'),
        headers={'Content-Type': 'application/json'},
    )
    dependencies.get_import_services().importer_by_uid[SOURCE_UID].fetch_static_data()


@pytest.fixture
def isolated_datex2_dir(tmp_path: Path):
    """Redirect DATEX2_IMPORT_DIR to a per-test temp directory."""
    config = dependencies.get_config_helper().get_config()
    original = config.get('DATEX2_IMPORT_DIR')
    config['DATEX2_IMPORT_DIR'] = str(tmp_path)
    try:
        yield tmp_path
    finally:
        config['DATEX2_IMPORT_DIR'] = original


@pytest.fixture
def eager_celery_helper():
    """
    Run any celery task queued via ``CeleryHelper.delay`` synchronously, so the realtime import
    is executed inline within the request thread of the test and we can assert on its outcome.
    """

    def run_task_synchronously(task, *args, **kwargs):
        return task(*args, **kwargs)

    with patch.object(dependencies.get_celery_helper(), 'delay', side_effect=run_task_synchronously) as mock_delay:
        yield mock_delay


@pytest.fixture
def stubbed_celery_delay():
    """Replace ``CeleryHelper.delay`` with a no-op mock for tests that don't need the task to run."""
    with patch.object(dependencies.get_celery_helper(), 'delay') as mock_delay:
        yield mock_delay


class Datex2RealtimeImportApiV35Test:
    @staticmethod
    def test_push_realtime_v35_persists_payload_and_queues_task(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
        isolated_datex2_dir: Path,
        stubbed_celery_delay,
    ) -> None:
        """
        The endpoint must accept the payload, write it to ``DATEX2_IMPORT_DIR`` and queue the
        celery task — without actually doing the import on the request thread.
        """
        _import_static_data(requests_mock)
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            json=realtime_data,
        )
        assert response.status_code == HTTPStatus.OK

        # Exactly one file was written under the configured import dir.
        written = list(isolated_datex2_dir.iterdir())
        assert len(written) == 1
        assert written[0].name.startswith(f'{SOURCE_UID}_')
        assert written[0].suffix == '.json'

        # The persisted body matches the payload we sent.
        with written[0].open('rb') as f:
            assert json.load(f) == realtime_data

        # Celery task was queued with (source_uid, file_path).
        stubbed_celery_delay.assert_called_once()
        args, _ = stubbed_celery_delay.call_args
        assert args[1] == SOURCE_UID
        assert args[2] == str(written[0])

        # Because the celery task did not run, EVSE statuses should be untouched.
        db.session.expire_all()
        evse_charging = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
        assert evse_charging.status == EvseStatus.UNKNOWN

    @staticmethod
    def test_push_realtime_v35_async_applies_status_updates(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
        isolated_datex2_dir: Path,
        eager_celery_helper,
    ) -> None:
        """
        With the celery task executed inline, EVSE statuses must be updated exactly the same way
        the synchronous endpoint used to update them.
        """
        _import_static_data(requests_mock)

        # All EVSEs should start as UNKNOWN
        assert db.session.query(Evse).filter(Evse.status == EvseStatus.UNKNOWN).count() == 57

        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            json=realtime_data,
        )
        assert response.status_code == HTTPStatus.OK

        db.session.expire_all()

        evse_available = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*2').first()
        assert evse_available.status == EvseStatus.AVAILABLE

        evse_charging = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
        assert evse_charging.status == EvseStatus.CHARGING

        evse_faulted = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914081*1').first()
        assert evse_faulted.status == EvseStatus.OUTOFORDER

        evse_occupied = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E909938*3').first()
        assert evse_occupied.status == EvseStatus.CHARGING

        # EVSEs not in realtime data should remain UNKNOWN
        evse_unchanged = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E916701*2').first()
        assert evse_unchanged.status == EvseStatus.UNKNOWN

        # The celery task deletes its source file once it has been processed.
        assert list(isolated_datex2_dir.iterdir()) == []

    @staticmethod
    def test_static_reimport_after_realtime_push_keeps_status(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
        isolated_datex2_dir: Path,
        eager_celery_helper,
    ) -> None:
        """
        Regression test: a static import that happens *after* realtime updates must not reset
        the EVSE status back to UNKNOWN.

        Sequence:
          1. Import static data (all EVSEs start as UNKNOWN).
          2. Push realtime data via the push endpoint (statuses become AVAILABLE/CHARGING/...).
          3. Import static data *again*.
          4. The realtime statuses must still be there - not reset to UNKNOWN.
        """
        # 1. Static import - all EVSEs start as UNKNOWN.
        _import_static_data(requests_mock)
        assert db.session.query(Evse).filter(Evse.status == EvseStatus.UNKNOWN).count() == 57

        # 2. Push realtime data; the eager celery fixture applies it inline.
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            json=realtime_data,
        )
        assert response.status_code == HTTPStatus.OK

        db.session.expire_all()
        assert db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*2').first().status == EvseStatus.AVAILABLE
        assert db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first().status == EvseStatus.CHARGING

        # 3. Static import again - this is what used to wipe the realtime status.
        _import_static_data(requests_mock)

        # 4. The realtime statuses must survive the static re-import.
        db.session.expire_all()
        evse_available = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*2').first()
        assert evse_available.status == EvseStatus.AVAILABLE, 'static re-import reset an AVAILABLE EVSE to UNKNOWN'

        evse_charging = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
        assert evse_charging.status == EvseStatus.CHARGING, 'static re-import reset a CHARGING EVSE to UNKNOWN'

        # EVSEs that never received a realtime update legitimately stay UNKNOWN.
        evse_unchanged = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E916701*2').first()
        assert evse_unchanged.status == EvseStatus.UNKNOWN

    @staticmethod
    def test_push_realtime_v35_gzip_encoded(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
        isolated_datex2_dir: Path,
        eager_celery_helper,
    ) -> None:
        """
        Realtime payloads gzip-compressed with Content-Encoding: gzip must be transparently decoded
        by the server_rest_api before_request hook, persisted, and processed identically.
        """
        _import_static_data(requests_mock)

        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        compressed_body = gzip.compress(json.dumps(realtime_data).encode('utf-8'))

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            data=compressed_body,
            content_type='application/json',
            headers={'Content-Encoding': 'gzip'},
        )
        assert response.status_code == HTTPStatus.OK

        db.session.expire_all()
        evse_available = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*2').first()
        assert evse_available.status == EvseStatus.AVAILABLE
        evse_charging = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
        assert evse_charging.status == EvseStatus.CHARGING

    @staticmethod
    def test_push_realtime_v35_delta_push_applies_directly(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
        isolated_datex2_dir: Path,
        stubbed_celery_delay,
    ) -> None:
        """
        deltaPush payloads are small incremental updates and must be applied synchronously on the
        request thread, without persisting a file or queueing a celery task.
        """
        _import_static_data(requests_mock)

        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        realtime_data['messageContainer']['exchangeInformation']['exchangeContext']['codedExchangeProtocol'] = {
            'value': 'deltaPush',
        }

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            json=realtime_data,
        )
        assert response.status_code == HTTPStatus.OK

        # Stored directly: nothing persisted to disk and no celery task queued.
        assert list(isolated_datex2_dir.iterdir()) == []
        stubbed_celery_delay.assert_not_called()

        # EVSE statuses are updated synchronously within the request.
        db.session.expire_all()
        evse_available = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*2').first()
        assert evse_available.status == EvseStatus.AVAILABLE
        evse_charging = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
        assert evse_charging.status == EvseStatus.CHARGING

    @staticmethod
    def test_push_realtime_v35_large_delta_push_is_async(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
        isolated_datex2_dir: Path,
        stubbed_celery_delay,
    ) -> None:
        """
        A deltaPush payload carrying more than DATEX2_ASYNC_STATION_STATUS_THRESHOLD station statuses
        must be handed off to celery (persisted + queued) instead of applied inline, even though it
        is a deltaPush.
        """
        _import_static_data(requests_mock)

        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        realtime_data['messageContainer']['exchangeInformation']['exchangeContext']['codedExchangeProtocol'] = {
            'value': 'deltaPush',
        }

        # The reduced payload has 5 station statuses - lower the threshold so it counts as "large".
        config = dependencies.get_config_helper().get_config()
        original = config.get('DATEX2_ASYNC_STATION_STATUS_THRESHOLD')
        config['DATEX2_ASYNC_STATION_STATUS_THRESHOLD'] = 2
        try:
            response = test_client.post(
                path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
                json=realtime_data,
            )
        finally:
            config['DATEX2_ASYNC_STATION_STATUS_THRESHOLD'] = original

        assert response.status_code == HTTPStatus.OK

        # Handed off to celery: payload persisted to disk and task queued.
        written = list(isolated_datex2_dir.iterdir())
        assert len(written) == 1
        stubbed_celery_delay.assert_called_once()

        # Because the celery task did not run, EVSE statuses stay untouched.
        db.session.expire_all()
        evse_charging = db.session.query(Evse).filter(Evse.uid == 'DE*EBW*E914082*1').first()
        assert evse_charging.status == EvseStatus.UNKNOWN

    @staticmethod
    def test_push_realtime_v35_oversized_payload_skips_validation_and_queues(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
        isolated_datex2_dir: Path,
        stubbed_celery_delay,
    ) -> None:
        """
        Payloads larger than DATEX2_SYNC_MAX_CONTENT_LENGTH must be handed off to celery without
        being parsed or validated on the request thread - so even a structurally invalid payload is
        persisted + queued (HTTP 200) instead of being rejected with HTTP 400.
        """
        _import_static_data(requests_mock)

        # A payload that would normally be rejected as invalid, but is pushed over the size limit.
        invalid_payload = {'not': 'a valid messageContainer'}

        config = dependencies.get_config_helper().get_config()
        sentinel = object()
        original = config.get('DATEX2_SYNC_MAX_CONTENT_LENGTH', sentinel)
        config['DATEX2_SYNC_MAX_CONTENT_LENGTH'] = 5
        try:
            response = test_client.post(
                path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
                json=invalid_payload,
            )
        finally:
            if original is sentinel:
                config.pop('DATEX2_SYNC_MAX_CONTENT_LENGTH', None)
            else:
                config['DATEX2_SYNC_MAX_CONTENT_LENGTH'] = original

        assert response.status_code == HTTPStatus.OK

        # Handed off to celery unvalidated: payload persisted to disk and task queued.
        written = list(isolated_datex2_dir.iterdir())
        assert len(written) == 1
        with written[0].open('rb') as f:
            assert json.load(f) == invalid_payload
        stubbed_celery_delay.assert_called_once()

    @staticmethod
    def test_push_realtime_v35_invalid_payload_returns_400(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
        isolated_datex2_dir: Path,
        stubbed_celery_delay,
    ) -> None:
        """
        A structurally invalid payload must be rejected synchronously with HTTP 400 - before any
        file is persisted or task queued - regardless of the (async) exchange protocol.
        """
        _import_static_data(requests_mock)

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            json={},
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert list(isolated_datex2_dir.iterdir()) == []
        stubbed_celery_delay.assert_not_called()

    @staticmethod
    def test_push_realtime_v35_empty_body_returns_400(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        isolated_datex2_dir: Path,
        stubbed_celery_delay,
    ) -> None:
        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            data=b'',
            content_type='application/json',
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert list(isolated_datex2_dir.iterdir()) == []
        stubbed_celery_delay.assert_not_called()

    @staticmethod
    def test_push_realtime_v35_invalid_api_key_does_not_persist(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        isolated_datex2_dir: Path,
        stubbed_celery_delay,
    ) -> None:
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key=wrong-key',
            json=realtime_data,
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        # Unauthorized requests must not leak the payload to disk or queue the task.
        assert list(isolated_datex2_dir.iterdir()) == []
        stubbed_celery_delay.assert_not_called()

    @staticmethod
    def test_push_realtime_v35_missing_key_is_unauthorized(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        isolated_datex2_dir: Path,
        stubbed_celery_delay,
    ) -> None:
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')

        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime',
            json=realtime_data,
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert list(isolated_datex2_dir.iterdir()) == []
        stubbed_celery_delay.assert_not_called()

    @staticmethod
    def test_push_realtime_v35_unknown_source(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        isolated_datex2_dir: Path,
        stubbed_celery_delay,
    ) -> None:
        response = test_client.post(
            path=f'/api/server/v1/datex/v3.5/does_not_exist/realtime?key={API_KEY}',
            json={},
        )

        # Unknown source surfaces as 404 from _get_source_and_service.
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert list(isolated_datex2_dir.iterdir()) == []
        stubbed_celery_delay.assert_not_called()


class Datex2RealtimeImportApiV35HeadTest:
    @staticmethod
    def test_head_realtime_v35_returns_200(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
        isolated_datex2_dir: Path,
        eager_celery_helper,
    ) -> None:
        """
        HEAD must return HTTP 200 (per Mobilithek convention) with a Last-Modified header
        once realtime data has been pushed.
        """
        _import_static_data(requests_mock)
        realtime_data = _load_test_data('datex2_enbw_realtime_reduced.json')
        # First push so the source has a realtime_data_updated_at value (eager celery so the
        # update actually lands in the DB before we issue HEAD).
        test_client.post(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
            json=realtime_data,
        )

        response = test_client.head(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
        )

        assert response.status_code == HTTPStatus.OK
        assert 'Last-Modified' in response.headers

    @staticmethod
    def test_head_realtime_v35_without_push_omits_last_modified(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
        requests_mock: Mocker,
    ) -> None:
        _import_static_data(requests_mock)

        response = test_client.head(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key={API_KEY}',
        )

        assert response.status_code == HTTPStatus.OK
        assert 'Last-Modified' not in response.headers

    @staticmethod
    def test_head_realtime_v35_invalid_key_is_unauthorized(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.head(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime?key=wrong',
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED

    @staticmethod
    def test_head_realtime_v35_missing_key_is_unauthorized(
        db: SQLAlchemy,
        test_client: OpenApiFlaskClient,
    ) -> None:
        response = test_client.head(
            path=f'/api/server/v1/datex/v3.5/{SOURCE_UID}/realtime',
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED
