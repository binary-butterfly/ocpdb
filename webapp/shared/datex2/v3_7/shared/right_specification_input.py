"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from .credential_g_input import CredentialGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .referenceable_organisation_versioned_reference_g_input import ReferenceableOrganisationVersionedReferenceGInput
from .right_type_enum_g_input import RightTypeEnumGInput
from .validity_input import ValidityInput


@validataclass
class RightSpecificationInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    type: RightTypeEnumGInput | UnsetValueType = DataclassValidator(RightTypeEnumGInput), Default(UnsetValue)
    description: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    financialReference: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    issuer: ReferenceableOrganisationVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(ReferenceableOrganisationVersionedReferenceGInput),
        Default(UnsetValue),
    )
    transferable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    transferableConditions: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    credential: list[CredentialGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(CredentialGInput)),
        Default(UnsetValue),
    )
    validity: ValidityInput | UnsetValueType = DataclassValidator(ValidityInput), Default(UnsetValue)
    afacRightSpecificationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
