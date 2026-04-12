"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput

from .catalogue_information_output import CatalogueInformationOutput
from .device_component_enum_g_output import DeviceComponentEnumGOutput
from .fault_impact_on_data_enum_g_output import FaultImpactOnDataEnumGOutput
from .fault_severity_enum_g_output import FaultSeverityEnumGOutput
from .fault_type_enum_g_output import FaultTypeEnumGOutput
from .fault_urgency_enum_g_output import FaultUrgencyEnumGOutput


@dataclass(kw_only=True)
class DeviceFaultOutput:
    idG: str
    faultIdentifier: str | None = None
    faultDescription: MultilingualStringOutput | None = None
    faultCreationTime: datetime | None = None
    faultLastUpdateTime: datetime
    faultImpactSeverity: FaultSeverityEnumGOutput | None = None
    faultUrgencyToRectify: FaultUrgencyEnumGOutput | None = None
    manufacturerFaultCode: str | None = None
    faultType: FaultTypeEnumGOutput
    faultInstructions: MultilingualStringOutput | None = None
    faultImpactOnData: list[FaultImpactOnDataEnumGOutput] | None = None
    faultComponent: str | None = None
    faultComponentType: DeviceComponentEnumGOutput | None = None
    faultObjectInformation: CatalogueInformationOutput | None = None
    comFaultExtensionG: ExtensionTypeGOutput | None = None
    fstDeviceFaultExtensionG: ExtensionTypeGOutput | None = None
