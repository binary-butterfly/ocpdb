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

from webapp.models import Location
from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.public_api.location_api.location_search_queries import LocationSearchQuery
from validataclass_search_queries.pagination import PaginatedResult
from webapp.repositories import LocationRepository


class LocationHandler(PublicApiBaseHandler):
    location_repository: LocationRepository

    def __init__(self, *args, location_repository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository

    def get_locations(self, query: LocationSearchQuery) -> PaginatedResult[Location]:
        locations = self.location_repository.fetch_locations(query)
        return locations
