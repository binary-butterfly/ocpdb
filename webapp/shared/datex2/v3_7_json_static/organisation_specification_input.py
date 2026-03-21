"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .organisation_unit_input import OrganisationUnitInput


@validataclass
class OrganisationSpecificationInput(ValidataclassMixin):
    """
    Specification of an organisation. It must contain at least one unit.
    """

    idG: str = StringValidator()
    versionG: str = StringValidator()
    lastUpdated: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    name: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    externalCode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    legalName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    linkToGeneralInformation: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    nationalOrganisationNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    nationalRegister: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    vatIdentificationNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    organisationUnit: list[OrganisationUnitInput] = ListValidator(DataclassValidator(OrganisationUnitInput))
    facOrganisationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facOrganisationSpecificationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
