"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, FloatValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .position_confidence_coded_error_enum_g_input import PositionConfidenceCodedErrorEnumGInput


@validataclass
class PositionConfidenceEllipseInput:
    semiMajorAxisLength: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    semiMajorAxisLengthCodedError: PositionConfidenceCodedErrorEnumGInput | UnsetValueType = (
        DataclassValidator(PositionConfidenceCodedErrorEnumGInput),
        Default(UnsetValue),
    )
    semiMinorAxisLength: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    semiMinorAxisLengthCodedError: PositionConfidenceCodedErrorEnumGInput | UnsetValueType = (
        DataclassValidator(PositionConfidenceCodedErrorEnumGInput),
        Default(UnsetValue),
    )
    semiMajorAxisOrientation: int | UnsetValueType = IntegerValidator(min_value=0.0), Default(UnsetValue)
    semiMajorAxisOrientationError: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    locPositionConfidenceEllipseExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
