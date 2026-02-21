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

from datetime import datetime, timezone

from validataclass.dataclasses import Default
from validataclass.validators import (
    AnyOfValidator,
    DateTimeValidator,
    EnumValidator,
    IntegerValidator,
    StringValidator,
)
from validataclass_search_queries.filters import (
    SearchParamCustom,
    SearchParamEquals,
    SearchParamGreaterThan,
    SearchParamMultiSelect,
)
from validataclass_search_queries.pagination import OffsetPaginationMixin, PaginationLimitValidator
from validataclass_search_queries.search_queries import BaseSearchQuery, search_query_dataclass
from validataclass_search_queries.sorting import SortingMixin
from validataclass_search_queries.validators import MultiSelectValidator

from webapp.models.evse import EvseStatus


@search_query_dataclass
class EvseSearchQuery(SortingMixin, OffsetPaginationMixin, BaseSearchQuery):
    # Set allowed sorting keys and default sorting key
    sorted_by: str = AnyOfValidator(['id', 'created', 'modified', 'last_updated']), Default('id')

    # Search filters
    status: EvseStatus | None = SearchParamEquals(), EnumValidator(EvseStatus)
    statuses: list[EvseStatus] | None = (
        SearchParamMultiSelect('status'),
        MultiSelectValidator(EnumValidator(EvseStatus)),
    )

    source_uid: str | None = SearchParamCustom(), StringValidator()
    source_uids: list[str] | None = (
        SearchParamCustom(),
        MultiSelectValidator(StringValidator(min_length=1)),
    )
    exclude_source_uid: str | None = SearchParamCustom(), StringValidator()
    exclude_source_uids: list[str] | None = (
        SearchParamCustom(),
        MultiSelectValidator(StringValidator(min_length=1)),
    )

    location_id: int | None = SearchParamCustom(), IntegerValidator(allow_strings=True)

    last_updated_since: datetime | None = (
        SearchParamGreaterThan('last_updated'),
        DateTimeValidator(local_timezone=timezone.utc, target_timezone=timezone.utc),
    )

    # Pagination
    limit: int = PaginationLimitValidator(optional=False, max_value=1000), Default(100)
