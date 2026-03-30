"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, FloatValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class RateLineTaxInput(ValidataclassMixin):
    """
    Class containing details of tax to be applied to a RateLine
    """

    taxValue: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    taxRate: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    taxIncluded: bool = BooleanValidator()
    trigger: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    labelForDisplay: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    facRateLineTaxExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
