"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .direction_enum_g_input import DirectionEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .tpeg_loc01_framed_point_location_subtype_enum_g_input import TpegLoc01FramedPointLocationSubtypeEnumGInput
from .tpeg_non_junction_point_input import TpegNonJunctionPointInput
from .tpeg_point_g_input import TpegPointGInput


@validataclass
class TpegFramedPointInput(ValidataclassMixin):
    tpegDirection: DirectionEnumGInput = DataclassValidator(DirectionEnumGInput)
    tpegFramedPointLocationType: TpegLoc01FramedPointLocationSubtypeEnumGInput = DataclassValidator(
        TpegLoc01FramedPointLocationSubtypeEnumGInput
    )
    framedPoint: TpegNonJunctionPointInput = DataclassValidator(TpegNonJunctionPointInput)
    to: TpegPointGInput = DataclassValidator(TpegPointGInput)
    from_: TpegPointGInput = DataclassValidator(TpegPointGInput)
    locTpegPointLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegFramedPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )

    @staticmethod
    def __pre_validate__(input_data: dict) -> dict:
        field_mapping = {
            'from': 'from_',
        }

        for from_key, to_key in field_mapping.items():
            if from_key in input_data:
                input_data[to_key] = input_data.pop(from_key)

        return input_data
