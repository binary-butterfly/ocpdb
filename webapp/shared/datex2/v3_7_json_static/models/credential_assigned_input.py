"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .credential_type_enum_g_input import CredentialTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .organisation_versioned_reference_g_input import OrganisationVersionedReferenceGInput


@validataclass
class CredentialAssignedInput(ValidataclassMixin):
    """
    Information concerning a specific credential that is used for verification for one AssignedRight. Specialisation of a general credential.
    """

    type: CredentialTypeEnumGInput = DataclassValidator(CredentialTypeEnumGInput)
    otherType: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    localIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    issuer: OrganisationVersionedReferenceGInput = DataclassValidator(OrganisationVersionedReferenceGInput)
    facCredentialExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facCredentialAssignedExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
