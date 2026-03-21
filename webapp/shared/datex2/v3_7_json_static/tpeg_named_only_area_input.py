"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .tpeg_area_descriptor_input import TpegAreaDescriptorInput
from .tpeg_height_input import TpegHeightInput
from .tpeg_loc01_area_location_subtype_enum_g_input import TpegLoc01AreaLocationSubtypeEnumGInput


@validataclass
class TpegNamedOnlyAreaInput(ValidataclassMixin):
    """
    An area defined by a well-known name.
    """

    tpegAreaLocationType: TpegLoc01AreaLocationSubtypeEnumGInput = DataclassValidator(
        TpegLoc01AreaLocationSubtypeEnumGInput
    )
    tpegHeight: TpegHeightInput | UnsetValueType = DataclassValidator(TpegHeightInput), Default(UnsetValue)
    name: list[TpegAreaDescriptorInput] = ListValidator(DataclassValidator(TpegAreaDescriptorInput))
    locTpegAreaLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegNamedOnlyAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
