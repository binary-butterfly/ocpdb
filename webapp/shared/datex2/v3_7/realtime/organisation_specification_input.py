"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.organisation_type_enum_g_input import OrganisationTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.overall_period_input import OverallPeriodInput

from .organisation_g_input import OrganisationGInput
from .organisation_unit_input import OrganisationUnitInput


@validataclass
class OrganisationSpecificationInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    lastUpdated: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    name: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    externalCode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
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
    organisationUnit: list[OrganisationUnitInput] = ListValidator(DataclassValidator(OrganisationUnitInput))
    subOrganisation: list[OrganisationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OrganisationGInput)),
        Default(UnsetValue),
    )
    facOrganisationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facOrganisationSpecificationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
