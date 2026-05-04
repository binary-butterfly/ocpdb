"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.vehicle_status_enum_g_input import VehicleStatusEnumGInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class GroupOfVehiclesInvolvedInput(ValidataclassMixin):
    numberOfVehicles: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    vehicleStatus: VehicleStatusEnumGInput | UnsetValueType = (
        DataclassValidator(VehicleStatusEnumGInput),
        Default(UnsetValue),
    )
    vehicleCharacteristics: VehicleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsInput),
        Default(UnsetValue),
    )
    comGroupOfVehiclesInvolvedExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
