"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.validators import StringValidator


@validataclass
class EnergyRateReferenceGInput:
    targetClass: str = StringValidator(), Default('EnergyRate')
    idG: str = StringValidator()
