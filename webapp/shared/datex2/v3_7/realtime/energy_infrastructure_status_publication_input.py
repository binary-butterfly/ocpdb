"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    ListValidator,
    RegexValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.energy_infrastructure_table_versioned_reference_g_input import (
    EnergyInfrastructureTableVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.header_information_input import HeaderInformationInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .energy_infrastructure_site_status_input import EnergyInfrastructureSiteStatusInput


@validataclass
class EnergyInfrastructureStatusPublicationInput(ValidataclassMixin):
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    feedDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    feedType: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    publicationTime: datetime = DateTimeValidator()
    tableReference: list[EnergyInfrastructureTableVersionedReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyInfrastructureTableVersionedReferenceGInput)),
        Default(UnsetValue),
    )
    publicationCreator: InternationalIdentifierInput = DataclassValidator(InternationalIdentifierInput)
    headerInformation: HeaderInformationInput | UnsetValueType = (
        DataclassValidator(HeaderInformationInput),
        Default(UnsetValue),
    )
    energyInfrastructureSiteStatus: list[EnergyInfrastructureSiteStatusInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyInfrastructureSiteStatusInput)),
        Default(UnsetValue),
    )
    comPayloadPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    aegiEnergyInfrastructureStatusPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
