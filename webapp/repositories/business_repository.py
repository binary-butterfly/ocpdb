"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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

from sqlalchemy.orm import joinedload
from validataclass_search_queries.pagination import PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.models import Business

from .base_repository import BaseRepository


class BusinessRepository(BaseRepository[Business]):
    model_cls = Business

    def fetch_by_id(self, business_id: int) -> Business:
        # _map_business_to_ocpi() reads business.logo, so eager-load it to avoid a lazy round-trip.
        return self.fetch_resource_by_id(business_id, load_options=[joinedload(Business.logo)])

    def fetch_businesses(self, search_query: BaseSearchQuery | None = None) -> PaginatedResult[Business]:
        # _map_business_to_ocpi() reads business.logo per row; without this eager load every business in the page
        # triggers an N+1 logo lookup.
        query = self.session.query(Business).options(joinedload(Business.logo))
        return self._search_and_paginate(query, search_query)

    def fetch_business_by_name(self, name: str) -> Business:
        result = self.session.query(Business).filter(Business.name == name).first()

        return self._or_raise(result, f'business with name {name} not found')
