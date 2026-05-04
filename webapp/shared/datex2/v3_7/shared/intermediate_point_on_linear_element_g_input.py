"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator, IntegerValidator

from .referent_input import ReferentInput


@validataclass
class intermediatePointOnLinearElementGInput(ValidataclassMixin):
    referent: ReferentInput = DataclassValidator(ReferentInput)
    index: int = IntegerValidator()
