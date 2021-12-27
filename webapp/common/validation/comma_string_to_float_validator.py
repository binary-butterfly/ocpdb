# encoding: utf-8

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

from validataclass.validators import FloatValidator as BaseFloatValidator
from validataclass.exceptions import InvalidTypeError


class CommaStringToFloatValidator(BaseFloatValidator):
    def validate(self, input_data: Any) -> float:
        self._ensure_type(input_data, [float, str, int])

        if type(input_data) is int:
            input_data = float(input_data)

        if type(input_data) is str:
            try:
                input_data = float(input_data.replace(',', '.'))
            except ValueError:
                raise InvalidTypeError(expected_types=[float])

        return super().validate(input_data)
