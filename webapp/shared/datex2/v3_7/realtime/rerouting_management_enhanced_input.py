"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.rerouting_type_enum_g_input import ReroutingTypeEnumGInput

from .location_g_input import LocationGInput
from .route_description_input import RouteDescriptionInput


@validataclass
class ReroutingManagementEnhancedInput(ValidataclassMixin):
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    type: ReroutingTypeEnumGInput | UnsetValueType = DataclassValidator(ReroutingTypeEnumGInput), Default(UnsetValue)
    bindingTrafficRegulation: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    preventiveMeasure: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    routingOrigin: list[LocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationGInput)),
        Default(UnsetValue),
    )
    routingThrough: list[LocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationGInput)),
        Default(UnsetValue),
    )
    routingDestination: list[LocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationGInput)),
        Default(UnsetValue),
    )
    originalRoute: RouteDescriptionInput | UnsetValueType = (
        DataclassValidator(RouteDescriptionInput),
        Default(UnsetValue),
    )
    alternativeRoute: list[RouteDescriptionInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RouteDescriptionInput)),
        Default(UnsetValue),
    )
