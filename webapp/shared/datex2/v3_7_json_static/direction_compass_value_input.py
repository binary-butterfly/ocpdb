"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .direction_compass_enum_g_input import DirectionCompassEnumGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class DirectionCompassValueInput(ValidataclassMixin):
    """
    A measured or calculated value of direction as a point of the compass.
    """

    directionCompass: DirectionCompassEnumGInput = DataclassValidator(DirectionCompassEnumGInput)
    comDataValueExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    comDirectionCompassValueExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
