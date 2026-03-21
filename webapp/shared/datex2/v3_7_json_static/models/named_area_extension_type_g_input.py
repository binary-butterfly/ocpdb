"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .named_area_extended_input import NamedAreaExtendedInput


@validataclass
class NamedAreaExtensionTypeGInput(ValidataclassMixin):
    NamedAreaExtended: NamedAreaExtendedInput | UnsetValueType = (
        DataclassValidator(NamedAreaExtendedInput),
        Default(UnsetValue),
    )
