"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.delays_input import DelaysInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class ClassifiedDelayInput(ValidataclassMixin):
    delays: DelaysInput = DataclassValidator(DelaysInput)
    vehicleCharacteristics: VehicleCharacteristicsInput = DataclassValidator(VehicleCharacteristicsInput)
    ubxClassifiedDelayExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
