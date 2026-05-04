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

import logging
from datetime import datetime, timezone

from webapp.common.logging.models import LogMessageType
from webapp.common.rest.exceptions import NotFoundException, UnauthorizedException
from webapp.models import Source, SourceStatus
from webapp.server_rest_api.base_handler import ServerApiBaseHandler
from webapp.services.import_services import ImportServices
from webapp.services.import_services.datex2.v3_5.base_datex2_v3_5_import_service import (
    BaseDatex2V35ImportService,
    RealtimeResult,
)
from webapp.services.import_services.exceptions import ImportException

logger = logging.getLogger(__name__)


class Datex2Handler(ServerApiBaseHandler):
    import_services: ImportServices

    def __init__(self, *, import_services: ImportServices, **kwargs):
        super().__init__(**kwargs)
        self.import_services = import_services

    def get_last_modified(self, source_uid: str, key: str | None) -> datetime | None:
        source, _ = self._get_source_and_service(source_uid, key)

        return source.realtime_data_updated_at

    def handle_realtime_push(self, source_uid: str, key: str | None, data: dict) -> None:
        source, service = self._get_source_and_service(source_uid, key)
        last_modified = datetime.now(tz=timezone.utc)
        result = RealtimeResult()

        try:
            message_container = service.add_realtime_data(data, result)
        except ImportException as e:
            logger.error(
                e.message,
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            service.update_source(source, realtime_status=SourceStatus.FAILED)
            return

        service.save_evse_updates(list(result.evse_updates_by_evse.values()))

        if message_container.messageContainer.payload:
            payload = message_container.messageContainer.payload[0]
            if payload.aegiEnergyInfrastructureStatusPublication.publicationTime:
                last_modified = payload.aegiEnergyInfrastructureStatusPublication.publicationTime

        service.update_source(
            source=source,
            realtime_status=SourceStatus.ACTIVE,
            realtime_error_count=result.realtime_error_count,
            realtime_data_updated_at=last_modified,
        )
        logger.info(
            f'Imported DATEX2 realtime data for {source_uid} via REST API with {result.realtime_success_count} '
            f'valid EVSEs and {result.realtime_error_count} failed EVSEs.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def _get_source_and_service(self, source_uid: str, key: str | None) -> tuple[Source, BaseDatex2V35ImportService]:
        if source_uid not in self.import_services.importer_by_uid:
            raise NotFoundException(message=f'Source {source_uid} not found')

        service = self.import_services.importer_by_uid[source_uid]
        if not isinstance(service, BaseDatex2V35ImportService):
            raise NotFoundException(message=f'Source {source_uid} is not a DATEX2 v3.5 source')

        source = service.get_source()
        if not key or key != service.config.get('api_key'):
            raise UnauthorizedException(message='Invalid API key')

        return source, service
