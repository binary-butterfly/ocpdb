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

from webapp.models import Source
from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.public_api.source_api.source_search_queries import SourceSearchQuery
from webapp.repositories import SourceRepository


class SourceHandler(PublicApiBaseHandler):
    source_repository: SourceRepository

    def __init__(self, *args, source_repository: SourceRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.source_repository = source_repository

    def get_source_by_id(self, source_id: int) -> Source:
        return self.source_repository.fetch_source_by_id(source_id)

    def search_sources(self, search_query: SourceSearchQuery | None = None) -> PaginatedResult[Source]:
        return self.source_repository.fetch_sources(search_query=search_query)
