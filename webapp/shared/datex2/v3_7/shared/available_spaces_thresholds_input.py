"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, FloatValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AvailableSpacesThresholdsInput(ValidataclassMixin):
    lowerThreshold: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    upperThreshold: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    lowerThresholdInPercent: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    upperThresholdInPercent: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    boundaryValuesExcluded: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    prkThresholdsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkAvailableSpacesThresholdsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
