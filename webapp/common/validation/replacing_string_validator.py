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
    """
    Validator for arbitrary strings, that takes a mapping of substrings to be replaced by others.
    Replacing is applied after making sure the input is actually a string, but before validating the string's content.
    If 'normalize_spaces=True' is given as a parameter, any number of consecutive spaces in the input
    (after replacing) will be reduced a single space.
    """
    mapping: dict[str, str]
    normalize_spaces: bool

    def __init__(self, *args, mapping: dict[str, str], normalize_spaces: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.mapping = mapping
        self.normalize_spaces = normalize_spaces

    def validate(self, input_data: Any, **kwargs) -> str:
        self._ensure_type(input_data, str)

        for search, replace in self.mapping.items():
            input_data = input_data.replace(search, replace)

        if self.normalize_spaces:
            input_words: list[str] = input_data.split()  # removes any number of spaces between words
            input_data = ' '.join(input_words) # adds just one space between words

        return super().validate(input_data, **kwargs)
