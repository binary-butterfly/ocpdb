"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .point_coordinates_input import PointCoordinatesInput
from .tpeg_ilc_point_descriptor_input import TpegIlcPointDescriptorInput
from .tpeg_junction_point_descriptor_input import TpegJunctionPointDescriptorInput
from .tpeg_other_point_descriptor_input import TpegOtherPointDescriptorInput


@validataclass
class TpegJunctionInput(ValidataclassMixin):
    pointCoordinates: PointCoordinatesInput = DataclassValidator(PointCoordinatesInput)
    name: TpegJunctionPointDescriptorInput | UnsetValueType = (
        DataclassValidator(TpegJunctionPointDescriptorInput),
        Default(UnsetValue),
    )
    ilc: list[TpegIlcPointDescriptorInput] = ListValidator(DataclassValidator(TpegIlcPointDescriptorInput))
    otherName: list[TpegOtherPointDescriptorInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TpegOtherPointDescriptorInput)),
        Default(UnsetValue),
    )
    locTpegPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegJunctionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
