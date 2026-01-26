"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .named_area_g_input import NamedAreaGInput
from .public_event_type_enum_g_input import PublicEventTypeEnumGInput
from .special_day_type_enum_g_input import SpecialDayTypeEnumGInput


@validataclass
class SpecialDayInput:
    intersectWithApplicableDays: bool = BooleanValidator()
    specialDayType: SpecialDayTypeEnumGInput = DataclassValidator(SpecialDayTypeEnumGInput)
    publicEvent: PublicEventTypeEnumGInput | UnsetValueType = (
        DataclassValidator(PublicEventTypeEnumGInput),
        Default(UnsetValue),
    )
    namedArea: list[NamedAreaGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(NamedAreaGInput)),
        Default(UnsetValue),
    )
    comSpecialDayExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
