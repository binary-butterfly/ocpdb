"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .gml_linear_ring_input import GmlLinearRingInput


@validataclass
class GmlPolygonInput:
    exterior: GmlLinearRingInput = DataclassValidator(GmlLinearRingInput)
    interior: list[GmlLinearRingInput] | UnsetValueType = (
        ListValidator(DataclassValidator(GmlLinearRingInput)),
        Default(UnsetValue),
    )
    locGmlPolygonExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
