"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .altitude_accuracy_enum_g_input import AltitudeAccuracyEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .position_confidence_coded_error_enum_g_input import PositionConfidenceCodedErrorEnumGInput


@validataclass
class AltitudeConfidenceInput:
    altitudeAccuracyCodedValue: AltitudeAccuracyEnumGInput | UnsetValueType = (
        DataclassValidator(AltitudeAccuracyEnumGInput),
        Default(UnsetValue),
    )
    altitudeAccuracyCodedError: PositionConfidenceCodedErrorEnumGInput | UnsetValueType = (
        DataclassValidator(PositionConfidenceCodedErrorEnumGInput),
        Default(UnsetValue),
    )
    locAltitudeConfidenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
