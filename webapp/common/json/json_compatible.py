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

import json
from typing import Any

from .default_json_encoder import DefaultJSONEncoder


def to_json_compatible(data: Any) -> Any:
    """
    Converts data to plain JSON types, rendering datetimes, enums and decimals exactly like the app's JSON provider. Use
    it for small parts of a response that is serialized with orjson, which renders datetimes differently.
    """
    return json.loads(json.dumps(data, cls=DefaultJSONEncoder))
