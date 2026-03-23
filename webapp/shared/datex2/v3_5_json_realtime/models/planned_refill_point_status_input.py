"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .overall_period_input import OverallPeriodInput
from .refill_point_status_enum_g_input import RefillPointStatusEnumGInput


@validataclass
class PlannedRefillPointStatusInput(ValidataclassMixin):
    """
    Planned status information for a refill point, for example reservatons
    """

    status: RefillPointStatusEnumGInput = DataclassValidator(RefillPointStatusEnumGInput)
    overallPeriod: OverallPeriodInput = DataclassValidator(OverallPeriodInput)
    aegiPlannedRefillPointStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
