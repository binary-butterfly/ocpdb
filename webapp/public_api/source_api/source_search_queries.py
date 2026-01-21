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

from validataclass.dataclasses import Default
from validataclass.validators import AnyOfValidator, StringValidator
from validataclass_search_queries.filters import SearchParamContains
from validataclass_search_queries.pagination import OffsetPaginationMixin, PaginationLimitValidator
from validataclass_search_queries.search_queries import BaseSearchQuery, search_query_dataclass
from validataclass_search_queries.sorting import SortingMixin


@search_query_dataclass
class SourceSearchQuery(SortingMixin, OffsetPaginationMixin, BaseSearchQuery):
    # Set allowed sorting keys and default sorting key
    sorted_by: str = AnyOfValidator(['uid', 'name', 'created', 'modified']), Default('uid')

    # Search filters
    name: str | None = SearchParamContains(), StringValidator()

    # Pagination
    limit: int | None = PaginationLimitValidator(optional=False, max_value=1000), Default(100)
