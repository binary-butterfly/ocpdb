"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class PositionAccuracyInput:
    accuracyPercentile50: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    accuracyPercentile75: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    accuracyPercentile95: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    locPositionAccuracyExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
