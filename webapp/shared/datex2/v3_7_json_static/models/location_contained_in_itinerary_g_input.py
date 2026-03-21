"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator, IntegerValidator

from .location_g_input import LocationGInput


@validataclass
class locationContainedInItineraryGInput(ValidataclassMixin):
    location: LocationGInput = DataclassValidator(LocationGInput)
    index: int = IntegerValidator()
