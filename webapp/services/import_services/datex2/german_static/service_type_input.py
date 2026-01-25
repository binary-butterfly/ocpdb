"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .overall_period_input import OverallPeriodInput
from .service_type_enum_g_input import ServiceTypeEnumGInput


@validataclass
class ServiceTypeInput:
    serviceType: ServiceTypeEnumGInput = DataclassValidator(ServiceTypeEnumGInput)
    overallPeriod: OverallPeriodInput | UnsetValueType = DataclassValidator(OverallPeriodInput), Default(UnsetValue)
    aegiServiceTypeExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
