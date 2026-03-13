"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import validataclass
from validataclass.validators import DataclassValidator, ListValidator

from .eu_vehicle_category_enum_g_input import EuVehicleCategoryEnumGInput


@validataclass
class VehicleCharacteristicsExtendedInput:
    euVehicleCategory: list[EuVehicleCategoryEnumGInput] = ListValidator(
        DataclassValidator(EuVehicleCategoryEnumGInput)
    )
