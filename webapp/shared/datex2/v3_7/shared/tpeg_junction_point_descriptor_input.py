"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .tpeg_loc03_junction_point_descriptor_subtype_enum_g_input import TpegLoc03JunctionPointDescriptorSubtypeEnumGInput


@validataclass
class TpegJunctionPointDescriptorInput(ValidataclassMixin):
    descriptor: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    tpegJunctionPointDescriptorType: TpegLoc03JunctionPointDescriptorSubtypeEnumGInput = DataclassValidator(
        TpegLoc03JunctionPointDescriptorSubtypeEnumGInput
    )
    locTpegDescriptorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegPointDescriptorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegJunctionPointDescriptorExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
