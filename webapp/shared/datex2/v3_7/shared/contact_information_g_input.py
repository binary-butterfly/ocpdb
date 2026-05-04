"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .contact_information_input import ContactInformationInput
from .contact_person_input import ContactPersonInput


@validataclass
class ContactInformationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    afacContactInformation: ContactInformationInput | UnsetValueType = (
        DataclassValidator(ContactInformationInput),
        Default(UnsetValue),
    )
    afacContactPerson: ContactPersonInput | UnsetValueType = DataclassValidator(ContactPersonInput), Default(UnsetValue)
