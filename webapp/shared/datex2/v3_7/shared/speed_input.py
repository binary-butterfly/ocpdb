"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .extension_type_g_input import ExtensionTypeGInput
from .unit_of_speed_enum_g_input import UnitOfSpeedEnumGInput


@validataclass
class SpeedInput(ValidataclassMixin):
    numericValue: float = FloatValidator(allow_integers=True)
    unitOfMeasure: UnitOfSpeedEnumGInput = DataclassValidator(UnitOfSpeedEnumGInput)
    comxSpeedExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
