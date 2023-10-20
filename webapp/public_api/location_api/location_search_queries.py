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

from typing import Optional

from validataclass.dataclasses import Default
from validataclass.validators import AnyOfValidator, StringValidator, IntegerValidator
from validataclass_search_queries.filters import SearchParamContains, SearchParamEquals
from validataclass_search_queries.pagination import OffsetPaginationMixin, PaginationLimitValidator
from validataclass_search_queries.search_queries import search_query_dataclass, BaseSearchQuery
from validataclass_search_queries.sorting import SortingMixin


@search_query_dataclass
class LocationSearchQuery(SortingMixin, OffsetPaginationMixin, BaseSearchQuery):
    # Set allowed sorting keys and default sorting key
    sorted_by: str = AnyOfValidator(['name', 'created', 'modified']), Default('name')

    # Search filters
    name: Optional[str] = SearchParamContains(), StringValidator()
    source: Optional[str] = SearchParamContains(), StringValidator()
    postal_code: Optional[int] = SearchParamEquals(), StringValidator()

    # Pagination
    limit: Optional[int] = PaginationLimitValidator(optional=True), Default(None)
