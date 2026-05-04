"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .credential_assigned_input import CredentialAssignedInput
from .credential_input import CredentialInput


@validataclass
class CredentialGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    afacCredential: CredentialInput | UnsetValueType = DataclassValidator(CredentialInput), Default(UnsetValue)
    afacCredentialAssigned: CredentialAssignedInput | UnsetValueType = (
        DataclassValidator(CredentialAssignedInput),
        Default(UnsetValue),
    )
