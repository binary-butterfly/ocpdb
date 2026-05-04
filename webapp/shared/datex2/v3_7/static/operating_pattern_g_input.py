"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .operating_restriction_input import OperatingRestrictionInput
from .usage_scenario_input import UsageScenarioInput


@validataclass
class OperatingPatternGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    prkUsageScenario: UsageScenarioInput | UnsetValueType = DataclassValidator(UsageScenarioInput), Default(UnsetValue)
    prkOperatingRestriction: OperatingRestrictionInput | UnsetValueType = (
        DataclassValidator(OperatingRestrictionInput),
        Default(UnsetValue),
    )
