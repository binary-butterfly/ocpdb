"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .setting_reason_enum import SettingReasonEnum


@validataclass
class SettingReasonEnumGInput(ValidataclassMixin):
    value: SettingReasonEnum = EnumValidator(SettingReasonEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
