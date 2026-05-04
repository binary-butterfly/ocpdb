"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .overall_period_input import OverallPeriodInput
from .validity_status_enum_g_input import ValidityStatusEnumGInput


@validataclass
class ValidityInput(ValidataclassMixin):
    validityStatus: ValidityStatusEnumGInput = DataclassValidator(ValidityStatusEnumGInput)
    overrunning: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    validityTimeSpecification: OverallPeriodInput = DataclassValidator(OverallPeriodInput)
    comValidityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
