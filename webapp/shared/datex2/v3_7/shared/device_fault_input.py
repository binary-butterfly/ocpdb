"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator, StringValidator

from .catalogue_information_input import CatalogueInformationInput
from .device_component_enum_g_input import DeviceComponentEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .fault_impact_on_data_enum_g_input import FaultImpactOnDataEnumGInput
from .fault_severity_enum_g_input import FaultSeverityEnumGInput
from .fault_type_enum_g_input import FaultTypeEnumGInput
from .fault_urgency_enum_g_input import FaultUrgencyEnumGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class DeviceFaultInput(ValidataclassMixin):
    idG: str = StringValidator()
    faultIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    faultDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    faultCreationTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    faultLastUpdateTime: datetime = DateTimeValidator()
    faultImpactSeverity: FaultSeverityEnumGInput | UnsetValueType = (
        DataclassValidator(FaultSeverityEnumGInput),
        Default(UnsetValue),
    )
    faultUrgencyToRectify: FaultUrgencyEnumGInput | UnsetValueType = (
        DataclassValidator(FaultUrgencyEnumGInput),
        Default(UnsetValue),
    )
    manufacturerFaultCode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    faultType: FaultTypeEnumGInput = DataclassValidator(FaultTypeEnumGInput)
    faultInstructions: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    faultImpactOnData: list[FaultImpactOnDataEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(FaultImpactOnDataEnumGInput)),
        Default(UnsetValue),
    )
    faultComponent: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    faultComponentType: DeviceComponentEnumGInput | UnsetValueType = (
        DataclassValidator(DeviceComponentEnumGInput),
        Default(UnsetValue),
    )
    faultObjectInformation: CatalogueInformationInput | UnsetValueType = (
        DataclassValidator(CatalogueInformationInput),
        Default(UnsetValue),
    )
    comFaultExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    fstDeviceFaultExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
