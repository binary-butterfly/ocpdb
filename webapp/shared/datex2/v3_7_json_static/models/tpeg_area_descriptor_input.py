"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .tpeg_loc03_area_descriptor_subtype_enum_g_input import TpegLoc03AreaDescriptorSubtypeEnumGInput


@validataclass
class TpegAreaDescriptorInput(ValidataclassMixin):
    """
    A descriptor for describing an area location.
    """

    descriptor: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    tpegAreaDescriptorType: TpegLoc03AreaDescriptorSubtypeEnumGInput = DataclassValidator(
        TpegLoc03AreaDescriptorSubtypeEnumGInput
    )
    locTpegDescriptorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegAreaDescriptorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
