"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .display_area_input import DisplayAreaInput
from .pictogram_display_area_input import PictogramDisplayAreaInput
from .supplementary_panel_area_input import SupplementaryPanelAreaInput
from .text_display_area_input import TextDisplayAreaInput


@validataclass
class DisplayAreaGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    vmsDisplayArea: DisplayAreaInput | UnsetValueType = DataclassValidator(DisplayAreaInput), Default(UnsetValue)
    vmsSupplementaryPanelArea: SupplementaryPanelAreaInput | UnsetValueType = (
        DataclassValidator(SupplementaryPanelAreaInput),
        Default(UnsetValue),
    )
    vmsPictogramDisplayArea: PictogramDisplayAreaInput | UnsetValueType = (
        DataclassValidator(PictogramDisplayAreaInput),
        Default(UnsetValue),
    )
    vmsTextDisplayArea: TextDisplayAreaInput | UnsetValueType = (
        DataclassValidator(TextDisplayAreaInput),
        Default(UnsetValue),
    )
