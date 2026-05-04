"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .maintenance_vehicle_actions_enum_g_input import MaintenanceVehicleActionsEnumGInput


@validataclass
class MaintenanceVehiclesInput(ValidataclassMixin):
    numberOfMaintenanceVehicles: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    maintenanceVehicleActions: list[MaintenanceVehicleActionsEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MaintenanceVehicleActionsEnumGInput)),
        Default(UnsetValue),
    )
    sitMaintenanceVehiclesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
