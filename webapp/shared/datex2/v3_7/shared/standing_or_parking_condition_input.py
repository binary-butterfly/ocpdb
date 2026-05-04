"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .legal_basis_input import LegalBasisInput
from .standing_or_parking_condition_type_enum_g_input import StandingOrParkingConditionTypeEnumGInput


@validataclass
class StandingOrParkingConditionInput(ValidataclassMixin):
    negate: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    active: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    standingOrParkingConditionType: StandingOrParkingConditionTypeEnumGInput = DataclassValidator(
        StandingOrParkingConditionTypeEnumGInput
    )
    legalBasis: LegalBasisInput | UnsetValueType = DataclassValidator(LegalBasisInput), Default(UnsetValue)
    troConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troStandingOrParkingConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
