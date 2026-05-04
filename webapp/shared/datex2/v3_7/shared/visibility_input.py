"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .integer_metre_distance_value_input import IntegerMetreDistanceValueInput


@validataclass
class VisibilityInput(ValidataclassMixin):
    minimumVisibilityDistance: IntegerMetreDistanceValueInput = DataclassValidator(IntegerMetreDistanceValueInput)
    comVisibilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
