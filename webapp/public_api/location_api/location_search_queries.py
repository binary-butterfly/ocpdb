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

from decimal import Decimal
from typing import Optional

from validataclass.dataclasses import Default
from validataclass.exceptions import ValidationError
from validataclass.validators import AnyOfValidator, DecimalValidator, IntegerValidator, StringValidator
from validataclass_search_queries.filters import SearchParamContains, SearchParamCustom, SearchParamEquals
from validataclass_search_queries.pagination import OffsetPaginationMixin, PaginationLimitValidator
from validataclass_search_queries.search_queries import BaseSearchQuery, search_query_dataclass
from validataclass_search_queries.sorting import SortingMixin


@search_query_dataclass
class LocationSearchQuery(SortingMixin, OffsetPaginationMixin, BaseSearchQuery):
    # Set allowed sorting keys and default sorting key
    sorted_by: str = AnyOfValidator(['name', 'created', 'modified']), Default('name')

    # Search filters
    name: Optional[str] = SearchParamContains(), StringValidator()
    source: Optional[str] = SearchParamContains(), StringValidator()
    postal_code: Optional[str] = SearchParamEquals(), StringValidator()

    lat: Optional[Decimal] = SearchParamCustom(), DecimalValidator()
    lon: Optional[Decimal] = SearchParamCustom(), DecimalValidator()
    radius: Optional[int] = SearchParamCustom(), IntegerValidator(allow_strings=True)

    # Pagination
    limit: int = PaginationLimitValidator(optional=False, max_value=1000), Default(100)

    def __post_init__(self):
        if (self.lat is not None or self.lon is not None or self.radius is not None) and not (self.lat and self.lon and self.radius):
            raise ValidationError(reason='lat, lon and radius have all to be set if one is set')
