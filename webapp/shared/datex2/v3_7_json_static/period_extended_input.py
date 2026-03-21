"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .fuzzy_period_input import FuzzyPeriodInput


@validataclass
class PeriodExtendedInput(ValidataclassMixin):
    """
    Extension class for Period.
    """

    fuzzyPeriod: list[FuzzyPeriodInput] | UnsetValueType = (
        ListValidator(DataclassValidator(FuzzyPeriodInput)),
        Default(UnsetValue),
    )
