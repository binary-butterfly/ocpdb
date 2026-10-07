"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .traffic_type_enum import TrafficTypeEnum
from .traffic_type_enum_extension_type_g import TrafficTypeEnumExtensionTypeG


@validataclass(reject_unknown_fields=True)
class TrafficTypeEnumGInput(ValidataclassMixin):
    value: TrafficTypeEnum = EnumValidator(TrafficTypeEnum)
    extendedValueG: TrafficTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(TrafficTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
