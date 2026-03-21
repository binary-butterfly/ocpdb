"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .refund_type_enum_g_input import RefundTypeEnumGInput
from .surcharge_type_enum_g_input import SurchargeTypeEnumGInput


@validataclass
class SurchargeInput(ValidataclassMixin):
    """
    Free-text description of the condition that leads to a surcharge being applied
    """

    surchargeType: SurchargeTypeEnumGInput = DataclassValidator(SurchargeTypeEnumGInput)
    value: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    rate: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    trigger: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    refund: RefundTypeEnumGInput | UnsetValueType = DataclassValidator(RefundTypeEnumGInput), Default(UnsetValue)
    labelForDisplay: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    facSurchargeExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
