"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .point_coordinates_input import PointCoordinatesInput
from .tpeg_other_point_descriptor_input import TpegOtherPointDescriptorInput


@validataclass
class TpegNonJunctionPointInput(ValidataclassMixin):
    pointCoordinates: PointCoordinatesInput = DataclassValidator(PointCoordinatesInput)
    name: list[TpegOtherPointDescriptorInput] = ListValidator(DataclassValidator(TpegOtherPointDescriptorInput))
    locTpegPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locTpegNonJunctionPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
