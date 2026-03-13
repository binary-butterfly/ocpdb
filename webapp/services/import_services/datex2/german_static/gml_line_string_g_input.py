"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .gml_line_string_input import GmlLineStringInput
from .gml_linear_ring_input import GmlLinearRingInput


@validataclass
class GmlLineStringGInput:
    locGmlLineString: GmlLineStringInput | UnsetValueType = DataclassValidator(GmlLineStringInput), Default(UnsetValue)
    locGmlLinearRing: GmlLinearRingInput | UnsetValueType = DataclassValidator(GmlLinearRingInput), Default(UnsetValue)
