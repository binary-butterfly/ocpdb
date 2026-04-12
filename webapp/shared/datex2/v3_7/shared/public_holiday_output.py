"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .named_area_g_output import NamedAreaGOutput
from .public_event_type_enum_g_output import PublicEventTypeEnumGOutput
from .special_day_type_enum_g_output import SpecialDayTypeEnumGOutput


@dataclass(kw_only=True)
class PublicHolidayOutput:
    intersectWithApplicableDays: bool
    specialDayType: SpecialDayTypeEnumGOutput
    publicEvent: PublicEventTypeEnumGOutput | None = None
    publicHolidayName: MultilingualStringOutput
    namedArea: list[NamedAreaGOutput] | None = None
    comSpecialDayExtensionG: ExtensionTypeGOutput | None = None
    comPublicHolidayExtensionG: ExtensionTypeGOutput | None = None
