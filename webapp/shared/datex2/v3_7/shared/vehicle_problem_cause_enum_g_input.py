"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .vehicle_problem_cause_enum import VehicleProblemCauseEnum


@validataclass
class VehicleProblemCauseEnumGInput(ValidataclassMixin):
    value: VehicleProblemCauseEnum = EnumValidator(VehicleProblemCauseEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
