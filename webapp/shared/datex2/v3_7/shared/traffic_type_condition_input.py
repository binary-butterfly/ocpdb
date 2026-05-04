"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .legal_basis_input import LegalBasisInput
from .traffic_type_enum_g_input import TrafficTypeEnumGInput


@validataclass
class TrafficTypeConditionInput(ValidataclassMixin):
    negate: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    trafficType: list[TrafficTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TrafficTypeEnumGInput)),
        Default(UnsetValue),
    )
    legalBasis: LegalBasisInput | UnsetValueType = DataclassValidator(LegalBasisInput), Default(UnsetValue)
    rerConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    rerTrafficTypeConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
