"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.multi_page_display_input import MultiPageDisplayInput
from webapp.shared.datex2.v3_7.shared.supplementary_pictogram_input import SupplementaryPictogramInput
from webapp.shared.datex2.v3_7.shared.supplementary_text_input import SupplementaryTextInput
from webapp.shared.datex2.v3_7.shared.text_display_input import TextDisplayInput

from .pictogram_display_input import PictogramDisplayInput


@validataclass
class DisplayAreaSettingsGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    vmsTextDisplay: TextDisplayInput | UnsetValueType = DataclassValidator(TextDisplayInput), Default(UnsetValue)
    vmsSupplementaryPictogram: SupplementaryPictogramInput | UnsetValueType = (
        DataclassValidator(SupplementaryPictogramInput),
        Default(UnsetValue),
    )
    vmsSupplementaryText: SupplementaryTextInput | UnsetValueType = (
        DataclassValidator(SupplementaryTextInput),
        Default(UnsetValue),
    )
    vmsPictogramDisplay: PictogramDisplayInput | UnsetValueType = (
        DataclassValidator(PictogramDisplayInput),
        Default(UnsetValue),
    )
    vmsMultiPageDisplay: MultiPageDisplayInput | UnsetValueType = (
        DataclassValidator(MultiPageDisplayInput),
        Default(UnsetValue),
    )
