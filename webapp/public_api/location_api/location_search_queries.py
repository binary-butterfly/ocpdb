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

from validataclass.dataclasses import Default
from validataclass.exceptions import ValidationError
from validataclass.validators import (
    AnyOfValidator,
    DecimalValidator,
    IntegerValidator,
    NumericValidator,
    StringValidator,
)
from validataclass_search_queries.filters import (
    SearchParamContains,
    SearchParamCustom,
    SearchParamEquals,
    SearchParamMultiSelect,
)
from validataclass_search_queries.pagination import OffsetPaginationMixin, PaginationLimitValidator
from validataclass_search_queries.search_queries import BaseSearchQuery, search_query_dataclass
from validataclass_search_queries.sorting import SortingMixin
from validataclass_search_queries.validators import MultiSelectValidator

from webapp.common.validation import SearchParamNotInList, SearchParamUnequal


@search_query_dataclass
class LocationSearchQuery(SortingMixin, OffsetPaginationMixin, BaseSearchQuery):
    # Set allowed sorting keys and default sorting key
    sorted_by: str = AnyOfValidator(['id', 'name', 'created', 'modified']), Default('id')

    # Search filters
    name: str | None = SearchParamContains(), StringValidator()
    source_uid: str | None = SearchParamEquals('source'), StringValidator()
    source_uids: list[str] | None = (
        SearchParamMultiSelect('source'),
        MultiSelectValidator(StringValidator(min_length=1)),
    )
    exclude_source_uid: str | None = SearchParamUnequal('source'), StringValidator()
    exclude_source_uids: list[str] | None = (
        SearchParamNotInList('source'),
        MultiSelectValidator(StringValidator(min_length=1)),
    )
    postal_code: str | None = SearchParamEquals(), StringValidator()
    address: str | None = SearchParamContains(), StringValidator()
    city: str | None = SearchParamContains(), StringValidator()
    country: str | None = SearchParamEquals(), StringValidator(min_length=3, max_length=3)

    operator_name: str | None = SearchParamContains(), StringValidator()

    lat: Decimal | None = SearchParamCustom(), DecimalValidator()
    lon: Decimal | None = SearchParamCustom(), DecimalValidator()
    radius: int | None = SearchParamCustom(), IntegerValidator(allow_strings=True)

    lat_min: Decimal | None = SearchParamCustom(), NumericValidator()
    lat_max: Decimal | None = SearchParamCustom(), NumericValidator()
    lon_min: Decimal | None = SearchParamCustom(), NumericValidator()
    lon_max: Decimal | None = SearchParamCustom(), NumericValidator()

    # Pagination
    limit: int = PaginationLimitValidator(optional=False, max_value=1000), Default(100)

    def __post_init__(self):
        if (self.lat is not None or self.lon is not None or self.radius is not None) and not (
            self.lat and self.lon and self.radius
        ):
            raise ValidationError(reason='lat, lon and radius have all to be set if one is set')
