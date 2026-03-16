"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from __future__ import annotations

from dataclasses import fields as dc_fields
from decimal import Decimal
from enum import Enum

from validataclass.helpers import UnsetValue


def datex_to_dict(obj) -> dict:
    result = {}
    for f in dc_fields(obj):
        value = getattr(obj, f.name)
        if value is None or value is UnsetValue:
            continue
        result[f.name] = _serialize_value(value)
    return result


def _serialize_value(value):
    if value is None or value is UnsetValue:
        return None
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Decimal):
        return float(value)
    if hasattr(value, '__dataclass_fields__'):
        return datex_to_dict(value)
    if isinstance(value, list):
        return [_serialize_value(item) for item in value]
    if isinstance(value, dict):
        return value
    return value
