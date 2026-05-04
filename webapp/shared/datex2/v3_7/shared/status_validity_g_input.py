"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .validity_by_offset_input import ValidityByOffsetInput
from .validity_by_period_input import ValidityByPeriodInput
from .validity_by_time_input import ValidityByTimeInput


@validataclass
class StatusValidityGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    prkValidityByPeriod: ValidityByPeriodInput | UnsetValueType = (
        DataclassValidator(ValidityByPeriodInput),
        Default(UnsetValue),
    )
    prkValidityByTime: ValidityByTimeInput | UnsetValueType = (
        DataclassValidator(ValidityByTimeInput),
        Default(UnsetValue),
    )
    prkValidityByOffset: ValidityByOffsetInput | UnsetValueType = (
        DataclassValidator(ValidityByOffsetInput),
        Default(UnsetValue),
    )
