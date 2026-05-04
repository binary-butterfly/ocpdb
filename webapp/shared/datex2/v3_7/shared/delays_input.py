"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .delay_band_enum_g_input import DelayBandEnumGInput
from .delays_type_enum_g_input import DelaysTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class DelaysInput(ValidataclassMixin):
    delayBand: DelayBandEnumGInput | UnsetValueType = DataclassValidator(DelayBandEnumGInput), Default(UnsetValue)
    delaysType: DelaysTypeEnumGInput | UnsetValueType = DataclassValidator(DelaysTypeEnumGInput), Default(UnsetValue)
    delayTimeValue: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    sitDelaysExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
