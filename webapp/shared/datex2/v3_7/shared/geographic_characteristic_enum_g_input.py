"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .geographic_characteristic_enum import GeographicCharacteristicEnum


@validataclass
class GeographicCharacteristicEnumGInput(ValidataclassMixin):
    value: GeographicCharacteristicEnum = EnumValidator(GeographicCharacteristicEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
