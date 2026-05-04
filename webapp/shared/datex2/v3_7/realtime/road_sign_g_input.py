"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .main_sign_input import MainSignInput
from .supplementary_panel_input import SupplementaryPanelInput


@validataclass
class RoadSignGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    troSupplementaryPanel: SupplementaryPanelInput | UnsetValueType = (
        DataclassValidator(SupplementaryPanelInput),
        Default(UnsetValue),
    )
    troMainSign: MainSignInput | UnsetValueType = DataclassValidator(MainSignInput), Default(UnsetValue)
