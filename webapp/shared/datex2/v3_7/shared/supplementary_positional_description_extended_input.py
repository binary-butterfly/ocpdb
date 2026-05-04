"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .house_number_side_enum_g_input import HouseNumberSideEnumGInput


@validataclass
class SupplementaryPositionalDescriptionExtendedInput(ValidataclassMixin):
    houseNumberSide: HouseNumberSideEnumGInput | UnsetValueType = (
        DataclassValidator(HouseNumberSideEnumGInput),
        Default(UnsetValue),
    )
