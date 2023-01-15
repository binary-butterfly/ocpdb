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


from typing import Any

from validataclass.validators import Validator

__all__ = [
    'UnvalidatedDictValidator',
]


class UnvalidatedDictValidator(Validator):
    """
    Validator for dict values ignoring its content, the content should be validated afterwards.

    Examples:

    ```
    UnvalidatedDictValidator()
    ```

    Valid input: `dict`
    Output: `dict`
    """

    def validate(self, input_data: Any, **kwargs) -> dict:
        """
        Validate type of input data. Returns unmodified dict.
        """
        self._ensure_type(input_data, dict)

        return input_data
