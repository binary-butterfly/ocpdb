"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .parking_place_status_enum_g_input import ParkingPlaceStatusEnumGInput
from .rgb_colour_input import RgbColourInput
from .thresholds_g_input import ThresholdsGInput


@validataclass
class StatusConfigurationInput(ValidataclassMixin):
    parkingStatus: ParkingPlaceStatusEnumGInput = DataclassValidator(ParkingPlaceStatusEnumGInput)
    thresholds: ThresholdsGInput = DataclassValidator(ThresholdsGInput)
    statusColourMapping: RgbColourInput | UnsetValueType = DataclassValidator(RgbColourInput), Default(UnsetValue)
    prkStatusConfigurationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
