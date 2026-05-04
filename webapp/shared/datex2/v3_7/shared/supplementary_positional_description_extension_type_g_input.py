"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .supplementary_positional_description_extended_input import SupplementaryPositionalDescriptionExtendedInput


@validataclass
class SupplementaryPositionalDescriptionExtensionTypeGInput(ValidataclassMixin):
    SupplementaryPositionalDescriptionExtended: SupplementaryPositionalDescriptionExtendedInput | UnsetValueType = (
        DataclassValidator(SupplementaryPositionalDescriptionExtendedInput),
        Default(UnsetValue),
    )
