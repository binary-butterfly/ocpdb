"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2023 binary butterfly GmbH

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
from typing import List
from validataclass_search_queries.pagination import PaginatedResult

from webapp.models import Business
from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.public_api.business_api.business_Search_Querries import BusinessSearchQuery
from webapp.repositories import BusinessRepository


class BusinessHandler(PublicApiBaseHandler):
    business_repository: BusinessRepository

    def __init__(self, *args, business_repository: BusinessRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_repository = business_repository

    def get_business_by_id(self, business_id: int):
        business = self.business_repository.fetch_by_id(business_id)
        return business

    def get_business_by_name(self, query: BusinessSearchQuery) -> PaginatedResult[Business]:
        return self.business_repository.fetch_business_by_name(query)

    def get_businesses(self) -> List[Business]:
        businesses = self.business_repository.fetch_businesses()
        return businesses
