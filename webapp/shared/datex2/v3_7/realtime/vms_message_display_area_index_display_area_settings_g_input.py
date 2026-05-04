"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator, IntegerValidator

from .display_area_settings_g_input import DisplayAreaSettingsGInput


@validataclass
class vmsMessageDisplayAreaIndexDisplayAreaSettingsGInput(ValidataclassMixin):
    displayAreaSettings: DisplayAreaSettingsGInput = DataclassValidator(DisplayAreaSettingsGInput)
    displayAreaIndex: int = IntegerValidator()
