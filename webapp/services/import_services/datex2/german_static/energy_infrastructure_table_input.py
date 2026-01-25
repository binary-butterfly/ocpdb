"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import AnythingValidator, DataclassValidator, ListValidator, StringValidator

from .energy_infrastructure_site_input import EnergyInfrastructureSiteInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class EnergyInfrastructureTableInput:
    idG: str = StringValidator()
    versionG: str = StringValidator()
    tableName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    energyInfrastructureSite: list[EnergyInfrastructureSiteInput] = ListValidator(
        AnythingValidator(allowed_types=[dict]),
    )
    aegiEnergyInfrastructureTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
