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

from validataclass_search_queries.pagination import PaginatedResult

from webapp.models import Connector
from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.public_api.connector_api.connector_search_queries import ConnectorSearchQuery
from webapp.repositories import ConnectorRepository


class ConnectorHandler(PublicApiBaseHandler):
    connector_repository: ConnectorRepository

    def __init__(self, *args, connector_repository: ConnectorRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.connector_repository = connector_repository

    def get_connectors(self, query: ConnectorSearchQuery, strict: bool = False) -> PaginatedResult[dict]:
        connectors = self.connector_repository.fetch_connectors(query)
        return connectors.map(lambda connector: self._map_connector_to_ocpi(connector, strict=strict))

    def get_connector(self, connector_id: int, strict: bool = False) -> dict:
        connector = self.connector_repository.fetch_connector_by_id(connector_id)
        return self._map_connector_to_ocpi(connector, strict=strict)

    def _map_connector_to_ocpi(self, connector: Connector, strict: bool = False) -> dict:
        return self.filter_none(connector.to_dict(strict=strict))
