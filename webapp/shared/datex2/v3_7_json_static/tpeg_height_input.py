"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .extension_type_g_input import ExtensionTypeGInput
from .tpeg_loc04_height_type_enum_g_input import TpegLoc04HeightTypeEnumGInput


@validataclass
class TpegHeightInput(ValidataclassMixin):
    """
    Height information which provides additional discrimination for the applicable area.
    """

    height: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    heightType: TpegLoc04HeightTypeEnumGInput = DataclassValidator(TpegLoc04HeightTypeEnumGInput)
    locTpegHeightExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
