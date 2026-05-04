"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .relative_offsets_input import RelativeOffsetsInput
from .times_of_day_input import TimesOfDayInput


@validataclass
class AssignedRightTimeRelativeGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    afacRelativeOffsets: RelativeOffsetsInput | UnsetValueType = (
        DataclassValidator(RelativeOffsetsInput),
        Default(UnsetValue),
    )
    afacTimesOfDay: TimesOfDayInput | UnsetValueType = DataclassValidator(TimesOfDayInput), Default(UnsetValue)
