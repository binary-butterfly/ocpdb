"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .open_all_hours_output import OpenAllHoursOutput
from .operating_hours_by_reference_output import OperatingHoursByReferenceOutput
from .operating_hours_specification_output import OperatingHoursSpecificationOutput
from .undefined_operating_hours_output import UndefinedOperatingHoursOutput
from .unknown_operating_hours_output import UnknownOperatingHoursOutput


@dataclass(kw_only=True)
class OperatingHoursGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    afacOperatingHoursByReference: OperatingHoursByReferenceOutput | None = None
    afacUnknownOperatingHours: UnknownOperatingHoursOutput | None = None
    afacUndefinedOperatingHours: UndefinedOperatingHoursOutput | None = None
    afacOpenAllHours: OpenAllHoursOutput | None = None
    afacOperatingHoursSpecification: OperatingHoursSpecificationOutput | None = None
