"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .vehicle_characteristics_extended_input import VehicleCharacteristicsExtendedInput


@validataclass
class VehicleCharacteristicsExtensionTypeGInput:
    VehicleCharacteristicsExtended: VehicleCharacteristicsExtendedInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsExtendedInput),
        Default(UnsetValue),
    )
