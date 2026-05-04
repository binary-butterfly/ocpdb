"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.integer_metre_distance_value_input import IntegerMetreDistanceValueInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.public_transport_schedule_input import PublicTransportScheduleInput
from webapp.shared.datex2.v3_7.shared.special_location_enum_g_input import SpecialLocationEnumGInput

from .location_reference_g_input import LocationReferenceGInput


@validataclass
class PublicTransportStopInput(ValidataclassMixin):
    name: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    specialLocation: SpecialLocationEnumGInput | UnsetValueType = (
        DataclassValidator(SpecialLocationEnumGInput),
        Default(UnsetValue),
    )
    locationReference: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    distanceFromOrigin: IntegerMetreDistanceValueInput | UnsetValueType = (
        DataclassValidator(IntegerMetreDistanceValueInput),
        Default(UnsetValue),
    )
    publicTransportSchedule: list[PublicTransportScheduleInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PublicTransportScheduleInput)),
        Default(UnsetValue),
    )
    prkRelatedLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkPublicTransportStopExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
