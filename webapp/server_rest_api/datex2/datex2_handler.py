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

from datetime import datetime

from webapp.common.rest.exceptions import NotFoundException, UnauthorizedException
from webapp.models import Source
from webapp.server_rest_api.base_handler import ServerApiBaseHandler
from webapp.services.import_services import ImportServices
from webapp.services.import_services.datex2.v3_5.base_datex2_v3_5_import_service import BaseDatex2V35ImportService


class Datex2Handler(ServerApiBaseHandler):
    """
    REST-layer concerns for the DATEX II v3.5 server endpoints: resolving sources, validating
    per-source API keys, and reporting realtime freshness. All actual import logic lives on
    :class:`BaseDatex2V35ImportService` and runs from the celery task path.
    """

    import_services: ImportServices

    def __init__(self, *, import_services: ImportServices, **kwargs):
        super().__init__(**kwargs)
        self.import_services = import_services

    def validate_realtime_request(self, source_uid: str, key: str | None) -> None:
        """
        Synchronous pre-flight validation for an incoming realtime push: makes sure the source
        exists, is a DATEX II v3.5 source, and the supplied ``key`` query parameter matches the
        source's configured ``api_key``. Raises ``NotFoundException`` / ``UnauthorizedException``.
        """
        self._authenticate(source_uid, key)

    def get_last_modified(self, source_uid: str, key: str | None) -> datetime | None:
        source, _ = self._authenticate(source_uid, key)
        return source.realtime_data_updated_at

    def _get_source_and_service(self, source_uid: str) -> tuple[Source, BaseDatex2V35ImportService]:
        if source_uid not in self.import_services.importer_by_uid:
            raise NotFoundException(message=f'Source {source_uid} not found')

        service = self.import_services.importer_by_uid[source_uid]
        if not isinstance(service, BaseDatex2V35ImportService):
            raise NotFoundException(message=f'Source {source_uid} is not a DATEX2 v3.5 source')

        return service.get_source(), service

    def _authenticate(self, source_uid: str, key: str | None) -> tuple[Source, BaseDatex2V35ImportService]:
        source, service = self._get_source_and_service(source_uid)
        if not key or key != service.config.get('api_key'):
            raise UnauthorizedException(message='Invalid API key')
        return source, service
