"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .multi_lingual_string_value_input import MultiLingualStringValueInput


@validataclass
class MultilingualStringInput:
    values: list[MultiLingualStringValueInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultiLingualStringValueInput)),
        Default(UnsetValue),
    )
