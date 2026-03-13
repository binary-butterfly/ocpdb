"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .fault_severity_enum_g_input import FaultSeverityEnumGInput
from .fault_urgency_enum_g_input import FaultUrgencyEnumGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class FaultInput:
    faultIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    faultDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    faultCreationTime: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    faultLastUpdateTime: str = StringValidator()
    faultImpactSeverity: FaultSeverityEnumGInput | UnsetValueType = (
        DataclassValidator(FaultSeverityEnumGInput),
        Default(UnsetValue),
    )
    faultUrgencyToRectify: FaultUrgencyEnumGInput | UnsetValueType = (
        DataclassValidator(FaultUrgencyEnumGInput),
        Default(UnsetValue),
    )
    manufacturerFaultCode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    comFaultExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
