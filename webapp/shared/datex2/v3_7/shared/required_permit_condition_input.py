"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .legal_basis_input import LegalBasisInput
from .multilingual_string_input import MultilingualStringInput
from .permit_information_versioned_reference_g_input import PermitInformationVersionedReferenceGInput
from .permit_type_enum_g_input import PermitTypeEnumGInput


@validataclass
class RequiredPermitConditionInput(ValidataclassMixin):
    negate: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    active: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    identifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    issuingAuthority: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    permitCharacteristics: PermitInformationVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(PermitInformationVersionedReferenceGInput),
        Default(UnsetValue),
    )
    permitType: list[PermitTypeEnumGInput] = ListValidator(DataclassValidator(PermitTypeEnumGInput))
    legalBasis: LegalBasisInput | UnsetValueType = DataclassValidator(LegalBasisInput), Default(UnsetValue)
    troConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troRequiredPermitConditionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
