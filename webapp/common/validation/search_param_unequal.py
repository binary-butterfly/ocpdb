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

from typing import Any

from sqlalchemy.sql import ColumnElement
from validataclass_search_queries.filters import SearchParam


class SearchParamUnequal(SearchParam):
    """
    Search parameter to filter for unequal (`column != value`).

    Note: For strings, this might or might not be case sensitive, depending on your database collations.
    """

    @staticmethod
    def sqlalchemy_filter(column: ColumnElement, value: Any) -> ColumnElement:
        return column != value
