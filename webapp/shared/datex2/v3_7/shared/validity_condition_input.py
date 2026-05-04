"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .legal_basis_input import LegalBasisInput
from .validity_input import ValidityInput


@validataclass
class ValidityConditionInput(ValidataclassMixin):
    negate: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legalBasis: LegalBasisInput | UnsetValueType = DataclassValidator(LegalBasisInput), Default(UnsetValue)
    validity: ValidityInput = DataclassValidator(ValidityInput)
    rerConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    rerValidityConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
