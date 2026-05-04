"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .open_all_hours_input import OpenAllHoursInput
from .operating_hours_by_reference_input import OperatingHoursByReferenceInput
from .operating_hours_specification_input import OperatingHoursSpecificationInput
from .undefined_operating_hours_input import UndefinedOperatingHoursInput
from .unknown_operating_hours_input import UnknownOperatingHoursInput


@validataclass
class OperatingHoursGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    afacOperatingHoursByReference: OperatingHoursByReferenceInput | UnsetValueType = (
        DataclassValidator(OperatingHoursByReferenceInput),
        Default(UnsetValue),
    )
    afacUnknownOperatingHours: UnknownOperatingHoursInput | UnsetValueType = (
        DataclassValidator(UnknownOperatingHoursInput),
        Default(UnsetValue),
    )
    afacUndefinedOperatingHours: UndefinedOperatingHoursInput | UnsetValueType = (
        DataclassValidator(UndefinedOperatingHoursInput),
        Default(UnsetValue),
    )
    afacOpenAllHours: OpenAllHoursInput | UnsetValueType = DataclassValidator(OpenAllHoursInput), Default(UnsetValue)
    afacOperatingHoursSpecification: OperatingHoursSpecificationInput | UnsetValueType = (
        DataclassValidator(OperatingHoursSpecificationInput),
        Default(UnsetValue),
    )
