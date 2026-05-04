"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .tpeg_loc03_ilc_point_descriptor_subtype_enum_g_input import TpegLoc03IlcPointDescriptorSubtypeEnumGInput


@validataclass
class TpegIlcPointDescriptorInput(ValidataclassMixin):
    descriptor: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    tpegIlcPointDescriptorType: TpegLoc03IlcPointDescriptorSubtypeEnumGInput = DataclassValidator(
        TpegLoc03IlcPointDescriptorSubtypeEnumGInput
    )
    locTpegDescriptorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegPointDescriptorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegIlcPointDescriptorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
