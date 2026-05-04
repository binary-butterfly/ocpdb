"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .point_coordinates_input import PointCoordinatesInput
from .tpeg_area_descriptor_input import TpegAreaDescriptorInput
from .tpeg_height_input import TpegHeightInput
from .tpeg_loc01_area_location_subtype_enum_g_input import TpegLoc01AreaLocationSubtypeEnumGInput


@validataclass
class TpegGeometricAreaInput(ValidataclassMixin):
    tpegAreaLocationType: TpegLoc01AreaLocationSubtypeEnumGInput = DataclassValidator(
        TpegLoc01AreaLocationSubtypeEnumGInput
    )
    radius: int = IntegerValidator(min_value=0)
    tpegHeight: TpegHeightInput | UnsetValueType = DataclassValidator(TpegHeightInput), Default(UnsetValue)
    centrePoint: PointCoordinatesInput = DataclassValidator(PointCoordinatesInput)
    name: TpegAreaDescriptorInput | UnsetValueType = DataclassValidator(TpegAreaDescriptorInput), Default(UnsetValue)
    locTpegAreaLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegGeometricAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
