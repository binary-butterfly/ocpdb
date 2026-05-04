"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .direction_enum_g_input import DirectionEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .tpeg_loc01_linear_location_subtype_enum_g_input import TpegLoc01LinearLocationSubtypeEnumGInput
from .tpeg_point_g_input import TpegPointGInput


@validataclass
class TpegLinearLocationInput(ValidataclassMixin):
    tpegDirection: DirectionEnumGInput = DataclassValidator(DirectionEnumGInput)
    tpegLinearLocationType: TpegLoc01LinearLocationSubtypeEnumGInput = DataclassValidator(
        TpegLoc01LinearLocationSubtypeEnumGInput
    )
    to: TpegPointGInput = DataclassValidator(TpegPointGInput)
    from_: TpegPointGInput = DataclassValidator(TpegPointGInput)
    locTpegLinearLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
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
