"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.access_condition_type_enum_g_input import AccessConditionTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.legal_basis_input import LegalBasisInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .location_reference_g_input import LocationReferenceGInput


@validataclass
class AccessConditionInput(ValidataclassMixin):
    negate: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    active: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    accessConditionType: list[AccessConditionTypeEnumGInput] = ListValidator(
        DataclassValidator(AccessConditionTypeEnumGInput)
    )
    otherAccessRestriction: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    legalBasis: LegalBasisInput | UnsetValueType = DataclassValidator(LegalBasisInput), Default(UnsetValue)
    applicableLocation: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    troConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troAccessConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
