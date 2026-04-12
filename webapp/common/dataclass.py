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

from dataclasses import fields, is_dataclass
from typing import Any

from validataclass.helpers import UnsetValue


def recursive_to_dict(data: Any, init: bool = False) -> Any:
    if hasattr(data, 'to_dict') and not init:
        return data.to_dict()
    if is_dataclass(data):
        return {field.name: recursive_to_dict(getattr(data, field.name)) for field in fields(data)}
    if isinstance(data, list):
        return [recursive_to_dict(item) for item in data]
    return data


def filter_unset_value(data: Any) -> Any:
    if isinstance(data, dict):
        return {key: filter_unset_value(value) for key, value in data.items() if value is not UnsetValue}
    if isinstance(data, list):
        return [filter_unset_value(item) for item in data if item is not UnsetValue]
    return data


def filter_none_recursive(data: Any) -> Any:
    if isinstance(data, dict):
        return {key: filter_none_recursive(value) for key, value in data.items() if value is not None}
    if isinstance(data, list):
        return [filter_none_recursive(item) for item in data]
    return data


class DataclassMixin:
    def to_dict(self) -> Any:
        return filter_unset_value(recursive_to_dict(self, True))
