"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2024 binary butterfly GmbH

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

from validataclass.validators import StringValidator


class ReplacingStringValidator(StringValidator):
    mapping: dict[str, str]

    def __init__(self, *args, mapping: dict[str, str], **kwargs):
        super().__init__(*args, **kwargs)
        self.mapping = mapping

    def validate(self, input_data: Any, **kwargs) -> str:
        self._ensure_type(input_data, str)

        for search, replace in self.mapping.items():
            input_data = input_data.replace(search, replace)

        return super().validate(input_data, **kwargs)
