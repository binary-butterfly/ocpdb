"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_last_location_reference_point_input import OpenlrLastLocationReferencePointInput
from .openlr_location_reference_point_input import OpenlrLocationReferencePointInput


@validataclass
class OpenlrClosedLineLocationReferenceInput:
    openlrLocationReferencePoint: list[OpenlrLocationReferencePointInput] = ListValidator(
        DataclassValidator(OpenlrLocationReferencePointInput)
    )
    openlrLastLine: OpenlrLastLocationReferencePointInput = DataclassValidator(OpenlrLastLocationReferencePointInput)
    locOpenlrAreaLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrClosedLineLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
