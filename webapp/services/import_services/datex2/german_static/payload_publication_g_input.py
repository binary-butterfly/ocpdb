"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .energy_infrastructure_table_publication_input import EnergyInfrastructureTablePublicationInput


@validataclass
class PayloadPublicationGInput:
    versionG: str | UnsetValueType = StringValidator(), Default('3.5')
    modelBaseVersionG: str = StringValidator(), Default('3')
    extensionNameG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    extensionVersionG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    profileNameG: str | UnsetValueType = StringValidator(), Default('AFIR Energy InfrastructureG')
    profileVersionG: str | UnsetValueType = StringValidator(), Default('01-00-00G')
    aegiEnergyInfrastructureTablePublication: EnergyInfrastructureTablePublicationInput | UnsetValueType = (
        DataclassValidator(EnergyInfrastructureTablePublicationInput),
        Default(UnsetValue),
    )
