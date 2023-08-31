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

from typing import List, Optional

from validataclass_search_queries.pagination import PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.models import Business
from .base_repository import BaseRepository, ObjectNotFoundException


class BusinessRepository(BaseRepository[Business]):
    model_cls = Business

    def fetch_by_id(self, business_id: int) -> Business:
        result = self.session.query(Business).filter(Business.id == business_id).one_or_none()

        if result is None:
            raise ObjectNotFoundException(f'business with id {business_id} not found')

        return result

    def search_and_paginate_businesses(self, search_query: Optional[BaseSearchQuery] = None) -> PaginatedResult[Business]:
        query = self.session.query(Business)
        result = (self._search_and_paginate(query, search_query))

        if len(result) == 0:
            raise ObjectNotFoundException(f'business with name containing  {search_query.name} not found')

        return result

    def fetch_business_by_name(self, business_name: str) -> List[Business]:
        result = self.session.query(Business).filter(Business.name == business_name).one_or_none()

        if result is None:
            raise ObjectNotFoundException(f'business with name {business_name} not found')

        return result

    def fetch_businesses(self) -> List[Business]:
        return self.session.query(Business).all()

