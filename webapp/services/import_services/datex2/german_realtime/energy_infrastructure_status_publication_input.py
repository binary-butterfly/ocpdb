"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, RegexValidator, StringValidator

from .energy_infrastructure_site_status_input import EnergyInfrastructureSiteStatusInput
from .energy_infrastructure_table_versioned_reference_g_input import EnergyInfrastructureTableVersionedReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput
from .header_information_input import HeaderInformationInput
from .international_identifier_input import InternationalIdentifierInput


@validataclass
class EnergyInfrastructureStatusPublicationInput:
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    publicationTime: str = StringValidator()
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
