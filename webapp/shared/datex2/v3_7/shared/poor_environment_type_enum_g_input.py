"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .poor_environment_type_enum import PoorEnvironmentTypeEnum


@validataclass
class PoorEnvironmentTypeEnumGInput(ValidataclassMixin):
    value: PoorEnvironmentTypeEnum = EnumValidator(PoorEnvironmentTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
