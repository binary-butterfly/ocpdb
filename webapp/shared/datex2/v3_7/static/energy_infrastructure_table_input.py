"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .energy_infrastructure_site_input import EnergyInfrastructureSiteInput


@validataclass
class EnergyInfrastructureTableInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    tableName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    energyInfrastructureSite: list[EnergyInfrastructureSiteInput] = ListValidator(
        DataclassValidator(EnergyInfrastructureSiteInput)
    )
    aegiEnergyInfrastructureTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
