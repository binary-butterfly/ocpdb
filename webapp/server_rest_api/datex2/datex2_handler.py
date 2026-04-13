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

from webapp.common.logging.models import LogMessageType
from webapp.common.rest.exceptions import NotFoundException
from webapp.server_rest_api.base_handler import ServerApiBaseHandler
from webapp.services.import_services import ImportServices
from webapp.services.import_services.datex2.base_datex2_v3_5_import_service import BaseDatex2V35ImportService

logger = logging.getLogger(__name__)


class Datex2Handler(ServerApiBaseHandler):
    import_services: ImportServices

    def __init__(self, *, import_services: ImportServices, **kwargs):
        super().__init__(**kwargs)
        self.import_services = import_services

    def _get_import_service(self, source_uid: str) -> BaseDatex2V35ImportService:
        if source_uid not in self.import_services.importer_by_uid:
            raise NotFoundException(message=f'Source {source_uid} not found')

        service = self.import_services.importer_by_uid[source_uid]
        if not isinstance(service, BaseDatex2V35ImportService):
            raise NotFoundException(message=f'Source {source_uid} is not a DATEX2 v3.5 source')

        return service

    def handle_static_push(self, source_uid: str, data: dict) -> None:
        service = self._get_import_service(source_uid)
        service.import_static_data(data)

        logger.info(
            f'Imported DATEX2 static data for {source_uid} via REST API.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def handle_realtime_push(self, source_uid: str, data: dict) -> None:
        service = self._get_import_service(source_uid)
        service.import_realtime_data(data)

        logger.info(
            f'Imported DATEX2 realtime data for {source_uid} via REST API.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )
