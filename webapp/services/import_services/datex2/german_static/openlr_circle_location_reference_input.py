"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_geo_coordinate_input import OpenlrGeoCoordinateInput


@validataclass
class OpenlrCircleLocationReferenceInput:
    openlrRadius: int = IntegerValidator(min_value=0)
    openlrGeoCoordinate: OpenlrGeoCoordinateInput = DataclassValidator(OpenlrGeoCoordinateInput)
    locOpenlrAreaLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrCircleLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
