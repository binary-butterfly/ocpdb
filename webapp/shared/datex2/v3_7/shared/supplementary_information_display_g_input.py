"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .supplementary_pictogram_input import SupplementaryPictogramInput
from .supplementary_text_input import SupplementaryTextInput


@validataclass
class SupplementaryInformationDisplayGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    vmsSupplementaryPictogram: SupplementaryPictogramInput | UnsetValueType = (
        DataclassValidator(SupplementaryPictogramInput),
        Default(UnsetValue),
    )
    vmsSupplementaryText: SupplementaryTextInput | UnsetValueType = (
        DataclassValidator(SupplementaryTextInput),
        Default(UnsetValue),
    )
