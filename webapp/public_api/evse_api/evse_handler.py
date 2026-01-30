"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from webapp.models import Evse
from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.public_api.evse_api.evse_search_queries import EvseSearchQuery
from webapp.repositories import EvseRepository


class EvseHandler(PublicApiBaseHandler):
    evse_repository: EvseRepository

    def __init__(self, *args, evse_repository: EvseRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.evse_repository = evse_repository

    def get_evses(self, query: EvseSearchQuery, strict: bool = False) -> PaginatedResult[dict]:
        evses = self.evse_repository.fetch_evses(query)
        return evses.map(lambda evse: self._map_evse_to_ocpi(evse, strict=strict))

    def get_evse(self, evse_id: int, strict: bool = False) -> dict:
        evse = self.evse_repository.fetch_evse_by_id(evse_id, include_children=True)
        return self._map_evse_to_ocpi(evse, strict=strict)

    def _map_evse_to_ocpi(self, evse: Evse, strict: bool = False) -> dict:
        evse_dict = evse.to_dict(strict=strict)

        evse_dict['connectors'] = []
        for connector in evse.connectors:
            evse_dict['connectors'].append(self.filter_none(connector.to_dict(strict=strict)))

        for image in evse.images:
            if 'images' not in evse_dict:
                evse_dict['images'] = []
            evse_dict['images'].append(self.filter_none(image.to_dict(strict=strict)))

        return self.filter_none_and_empty_list(evse_dict)
