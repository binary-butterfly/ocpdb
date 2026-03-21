"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_functional_road_class_enum_g_input import OpenlrFunctionalRoadClassEnumGInput


@validataclass
class OpenlrPathAttributesInput(ValidataclassMixin):
    """
    Properties of the path from the associated location reference point to the next location reference point, which are specified to assist correct identification of the point in an external map data source.
    """

    openlrLowestFrcToNextLRPoint: OpenlrFunctionalRoadClassEnumGInput = DataclassValidator(
        OpenlrFunctionalRoadClassEnumGInput
    )
    openlrDistanceToNextLRPoint: int = IntegerValidator(min_value=0)
    locOpenlrPathAttributesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
