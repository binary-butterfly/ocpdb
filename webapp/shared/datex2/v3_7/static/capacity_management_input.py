"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .capacity_management_measure_input import CapacityManagementMeasureInput


@validataclass
class CapacityManagementInput(ValidataclassMixin):
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    capacityManagementMeasure: list[CapacityManagementMeasureInput] = ListValidator(
        DataclassValidator(CapacityManagementMeasureInput)
    )
