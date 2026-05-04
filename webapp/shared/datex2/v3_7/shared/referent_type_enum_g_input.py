"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .referent_type_enum import ReferentTypeEnum


@validataclass
class ReferentTypeEnumGInput(ValidataclassMixin):
    value: ReferentTypeEnum = EnumValidator(ReferentTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
