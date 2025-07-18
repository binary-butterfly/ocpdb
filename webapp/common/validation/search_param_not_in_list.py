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


class SearchParamNotInList(SearchParam):
    """
    Search parameter that can be set to a list of one or more values to search for, i.e. the filtered column must not be
    equal to one of the values given by the user.

    This is implemented using a `column NOT IN (values...)` SQL expression.

    Note: To make use of this search parameter, you must use a validator that outputs a list of values. If the parameter
    is set to a single value, the filter will be equivalent to an "equals" filter. See the `MultiSelectValidator`.
    """

    @staticmethod
    def sqlalchemy_filter(column: ColumnElement, value: Any) -> ColumnElement:
        value_list = value if isinstance(value, list) else [value]
        return column.not_in(value_list)
