"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .gdd_service_category_enum import GddServiceCategoryEnum


@validataclass
class GddServiceCategoryEnumGInput(ValidataclassMixin):
    value: GddServiceCategoryEnum = EnumValidator(GddServiceCategoryEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
