"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .duration_value_input import DurationValueInput


@validataclass
class DataValueGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    comxDurationValue: DurationValueInput | UnsetValueType = DataclassValidator(DurationValueInput), Default(UnsetValue)
