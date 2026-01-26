"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .external_identifier_input import ExternalIdentifierInput
from .multilingual_string_input import MultilingualStringInput
from .organisation_type_enum_g_input import OrganisationTypeEnumGInput
from .organisation_unit_input import OrganisationUnitInput
from .overall_period_input import OverallPeriodInput


@validataclass
class ReferenceableOrganisationInput:
    idG: str = StringValidator()
    versionG: str = StringValidator()
    lastUpdated: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    name: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    legalName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    linkToGeneralInformation: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    linkToLogo: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    linkToWebform: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    available24hours: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    responsibility: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    publishingAgreement: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    type: OrganisationTypeEnumGInput | UnsetValueType = (
        DataclassValidator(OrganisationTypeEnumGInput),
        Default(UnsetValue),
    )
    nationalOrganisationNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    nationalRegister: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    vatIdentificationNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    generalTimeValidity: OverallPeriodInput | UnsetValueType = (
        DataclassValidator(OverallPeriodInput),
        Default(UnsetValue),
    )
    organisationUnit: list[OrganisationUnitInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OrganisationUnitInput)),
        Default(UnsetValue),
    )
    externalIdentifier: list[ExternalIdentifierInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ExternalIdentifierInput)),
        Default(UnsetValue),
    )
    afacOrganisationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacAnOrganisationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacReferenceableOrganisationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
