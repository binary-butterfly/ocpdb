"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_form_of_way_enum_g_input import OpenlrFormOfWayEnumGInput
from .openlr_functional_road_class_enum_g_input import OpenlrFunctionalRoadClassEnumGInput


@validataclass
class OpenlrLineAttributesInput:
    openlrFunctionalRoadClass: OpenlrFunctionalRoadClassEnumGInput = DataclassValidator(
        OpenlrFunctionalRoadClassEnumGInput
    )
    openlrFormOfWay: OpenlrFormOfWayEnumGInput = DataclassValidator(OpenlrFormOfWayEnumGInput)
    openlrBearing: int = IntegerValidator(min_value=0.0)
    locOpenlrLineAttributesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
