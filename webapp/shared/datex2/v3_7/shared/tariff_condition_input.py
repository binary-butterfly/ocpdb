"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .legal_basis_input import LegalBasisInput


@validataclass
class TariffConditionInput(ValidataclassMixin):
    negate: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    active: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    tariffPaid: bool = BooleanValidator()
    legalBasis: LegalBasisInput | UnsetValueType = DataclassValidator(LegalBasisInput), Default(UnsetValue)
    troConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    czTariffConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
