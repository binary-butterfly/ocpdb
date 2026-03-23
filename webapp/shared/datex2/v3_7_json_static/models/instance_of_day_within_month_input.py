"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .day_enum_g_input import DayEnumGInput
from .day_week_month_extension_type_g_input import DayWeekMonthExtensionTypeGInput
from .extension_type_g_input import ExtensionTypeGInput
from .instance_of_day_enum_g_input import InstanceOfDayEnumGInput
from .month_of_year_enum_g_input import MonthOfYearEnumGInput


@validataclass
class InstanceOfDayWithinMonthInput(ValidataclassMixin):
    """
    Specification of periods defined by the instance of a specific weekday within a month (e.g. 3rd Tuesday in May)
    """

    applicableDay: list[DayEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DayEnumGInput)),
        Default(UnsetValue),
    )
    applicableMonth: list[MonthOfYearEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MonthOfYearEnumGInput)),
        Default(UnsetValue),
    )
    applicableInstanceOfDayWithinMonth: list[InstanceOfDayEnumGInput] = ListValidator(
        DataclassValidator(InstanceOfDayEnumGInput)
    )
    comDayWeekMonthExtensionG: DayWeekMonthExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(DayWeekMonthExtensionTypeGInput),
        Default(UnsetValue),
    )
    comInstanceOfDayWithinMonthExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
