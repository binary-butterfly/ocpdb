"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, IntegerValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.legal_basis_input import LegalBasisInput


@validataclass
class OccupantConditionInput(ValidataclassMixin):
    negate: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    disabledWithPermit: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    numberOfOccupants: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    legalBasis: LegalBasisInput | UnsetValueType = DataclassValidator(LegalBasisInput), Default(UnsetValue)
    rerConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    rerOccupantConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
