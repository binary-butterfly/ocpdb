"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.capacity_management_action_enum_g_input import CapacityManagementActionEnumGInput
from webapp.shared.datex2.v3_7.shared.capacity_management_measure_enum_g_input import (
    CapacityManagementMeasureEnumGInput,
)
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .location_reference_g_input import LocationReferenceGInput
from .traffic_signal_input import TrafficSignalInput


@validataclass
class CapacityManagementMeasureInput(ValidataclassMixin):
    measure: CapacityManagementMeasureEnumGInput = DataclassValidator(CapacityManagementMeasureEnumGInput)
    action: list[CapacityManagementActionEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(CapacityManagementActionEnumGInput)),
        Default(UnsetValue),
    )
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    defaultGreenTimeAdjustment: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    defaultCycleLength: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    recommendedSpeed: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    affectedLocation: list[LocationReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationReferenceGInput)),
        Default(UnsetValue),
    )
    trafficSignal: list[TrafficSignalInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TrafficSignalInput)),
        Default(UnsetValue),
    )
    rerCapacityManagementMeasureExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
