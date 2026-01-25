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

import re
import unicodedata
from typing import Any

from validataclass.validators import StringValidator

categories = {'Zs', 'Zl', 'Zp', 'Cc', 'Cf', 'Cs', 'Co', 'Cn'}
# We could use sys.maxunicode here, but it's horribly slow as unicode is so waste, so we go for 0xFFFF max
all_chars = (chr(i) for i in range(65535))
filtered_chars = ''.join(c for c in all_chars if unicodedata.category(c) in categories and c != ' ')
FILTERED_CHAR_RE = re.compile('[%s]' % re.escape(filtered_chars))


class PrintableStringValidator(StringValidator):
    stripped: bool

    def __init__(self, *args, stripped: bool = True, **kwargs):
        super().__init__(*args, **kwargs)
        self.stripped = stripped

    def validate(self, input_data: Any, **kwargs) -> Any:
        self._ensure_type(input_data, str)

        # Filter out unprintable characters
        input_data = FILTERED_CHAR_RE.sub('', input_data)

        if self.stripped:
            input_data = input_data.strip()

        return super().validate(input_data=input_data)
