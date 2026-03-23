"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .energy_infrastructure_status_publication_input import EnergyInfrastructureStatusPublicationInput


@validataclass
class PayloadPublicationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    versionG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    modelBaseVersionG: str = StringValidator()
    extensionNameG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    extensionVersionG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    profileNameG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    profileVersionG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    aegiEnergyInfrastructureStatusPublication: EnergyInfrastructureStatusPublicationInput | UnsetValueType = (
        DataclassValidator(EnergyInfrastructureStatusPublicationInput),
        Default(UnsetValue),
    )
