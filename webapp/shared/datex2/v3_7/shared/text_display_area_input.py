"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from .display_geometry_input import DisplayGeometryInput
from .extension_type_g_input import ExtensionTypeGInput
from .lane_input import LaneInput
from .position_x_absolute_enum_g_input import PositionXAbsoluteEnumGInput
from .position_x_relative_enum_g_input import PositionXRelativeEnumGInput
from .position_y_absolute_enum_g_input import PositionYAbsoluteEnumGInput
from .position_y_relative_enum_g_input import PositionYRelativeEnumGInput


@validataclass
class TextDisplayAreaInput(ValidataclassMixin):
    sequencingCapable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    maxNumberOfSequentialPages: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    positionXAbsolute: PositionXAbsoluteEnumGInput | UnsetValueType = (
        DataclassValidator(PositionXAbsoluteEnumGInput),
        Default(UnsetValue),
    )
    positionXRelativeToPrevious: PositionXRelativeEnumGInput | UnsetValueType = (
        DataclassValidator(PositionXRelativeEnumGInput),
        Default(UnsetValue),
    )
    positionYAbsolute: PositionYAbsoluteEnumGInput | UnsetValueType = (
        DataclassValidator(PositionYAbsoluteEnumGInput),
        Default(UnsetValue),
    )
    positionYRelativeToPrevious: PositionYRelativeEnumGInput | UnsetValueType = (
        DataclassValidator(PositionYRelativeEnumGInput),
        Default(UnsetValue),
    )
    proportionalFont: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    maxNumberOfCharacters: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    maxNumberOfRows: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    textCodeListIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    maxFontHeight: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    minFontHeight: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    maxFontWidth: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    minFontWidth: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    maxFontSpacing: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    minFontSpacing: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    displayGeometry: DisplayGeometryInput | UnsetValueType = (
        DataclassValidator(DisplayGeometryInput),
        Default(UnsetValue),
    )
    overriddenLaneAssociation: list[LaneInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LaneInput)),
        Default(UnsetValue),
    )
    vmsDisplayAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsTextDisplayAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
