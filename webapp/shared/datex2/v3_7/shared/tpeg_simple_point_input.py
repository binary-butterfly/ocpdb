"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .direction_enum_g_input import DirectionEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .tpeg_loc01_simple_point_location_subtype_enum_g_input import TpegLoc01SimplePointLocationSubtypeEnumGInput
from .tpeg_point_g_input import TpegPointGInput


@validataclass
class TpegSimplePointInput(ValidataclassMixin):
    tpegDirection: DirectionEnumGInput = DataclassValidator(DirectionEnumGInput)
    tpegSimplePointLocationType: TpegLoc01SimplePointLocationSubtypeEnumGInput = DataclassValidator(
        TpegLoc01SimplePointLocationSubtypeEnumGInput
    )
    point: TpegPointGInput = DataclassValidator(TpegPointGInput)
    locTpegPointLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegSimplePointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
