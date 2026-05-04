"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .linear_element_by_code_input import LinearElementByCodeInput
from .linear_element_by_line_string_input import LinearElementByLineStringInput
from .linear_element_by_points_input import LinearElementByPointsInput
from .linear_element_input import LinearElementInput


@validataclass
class LinearElementGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locLinearElement: LinearElementInput | UnsetValueType = DataclassValidator(LinearElementInput), Default(UnsetValue)
    locLinearElementByLineString: LinearElementByLineStringInput | UnsetValueType = (
        DataclassValidator(LinearElementByLineStringInput),
        Default(UnsetValue),
    )
    locLinearElementByPoints: LinearElementByPointsInput | UnsetValueType = (
        DataclassValidator(LinearElementByPointsInput),
        Default(UnsetValue),
    )
    locLinearElementByCode: LinearElementByCodeInput | UnsetValueType = (
        DataclassValidator(LinearElementByCodeInput),
        Default(UnsetValue),
    )
