"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator, IntegerValidator

from .display_area_g_input import DisplayAreaGInput


@validataclass
class vmsConfigurationDisplayAreaIndexDisplayAreaGInput(ValidataclassMixin):
    displayArea: DisplayAreaGInput = DataclassValidator(DisplayAreaGInput)
    displayAreaIndex: int = IntegerValidator()
