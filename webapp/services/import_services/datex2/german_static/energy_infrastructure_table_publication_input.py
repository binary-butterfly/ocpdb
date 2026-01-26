"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, RegexValidator, StringValidator

from .energy_infrastructure_table_input import EnergyInfrastructureTableInput
from .extension_type_g_input import ExtensionTypeGInput
from .header_information_input import HeaderInformationInput
from .international_identifier_input import InternationalIdentifierInput


@validataclass
class EnergyInfrastructureTablePublicationInput:
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    publicationTime: str = StringValidator()
    publicationCreator: InternationalIdentifierInput = DataclassValidator(InternationalIdentifierInput)
    headerInformation: HeaderInformationInput | UnsetValueType = (
        DataclassValidator(HeaderInformationInput),
        Default(UnsetValue),
    )
    energyInfrastructureTable: list[EnergyInfrastructureTableInput] = ListValidator(
        DataclassValidator(EnergyInfrastructureTableInput)
    )
    comPayloadPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    aegiEnergyInfrastructureTablePublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
