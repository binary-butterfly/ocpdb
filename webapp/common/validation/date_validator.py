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

from datetime import date, datetime
from typing import Any

from validataclass.exceptions import ValidationError
from validataclass.validators import StringValidator


class ParsedDateValidator(StringValidator):
    date_format: str

    def __init__(self, *args, date_format: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.date_format = date_format

    def validate(self, input_data: Any, **kwargs) -> date:
        input_data = super().validate(input_data, **kwargs)

        try:
            return datetime.strptime(input_data, self.date_format).date()
        except ValueError as e:
            raise ValidationError(
                code='invalid_date', reason=f'{input_data} does not have required date format {self.date_format}.'
            ) from e
