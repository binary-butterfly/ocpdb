"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, IntegerValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.reference_input import ReferenceInput

from .point_location_g_input import PointLocationGInput


@validataclass
class TrafficSignalInput(ValidataclassMixin):
    index: int = IntegerValidator()
    externalId: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    greenTimeAdjustmentOverride: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    cycleLengthOverride: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    signalGroup: ReferenceInput | UnsetValueType = DataclassValidator(ReferenceInput), Default(UnsetValue)
    notionalMidPoint: PointLocationGInput | UnsetValueType = (
        DataclassValidator(PointLocationGInput),
        Default(UnsetValue),
    )
    rerTrafficSignalExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
