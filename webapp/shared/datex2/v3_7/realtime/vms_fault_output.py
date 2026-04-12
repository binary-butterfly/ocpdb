"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput

from .fault_severity_enum_g_output import FaultSeverityEnumGOutput
from .fault_urgency_enum_g_output import FaultUrgencyEnumGOutput
from .vms_fault_enum_g_output import VmsFaultEnumGOutput


@dataclass(kw_only=True)
class VmsFaultOutput:
    faultIdentifier: str | None = None
    faultDescription: MultilingualStringOutput | None = None
    faultCreationTime: datetime | None = None
    faultLastUpdateTime: datetime
    faultImpactSeverity: FaultSeverityEnumGOutput | None = None
    faultUrgencyToRectify: FaultUrgencyEnumGOutput | None = None
    manufacturerFaultCode: str | None = None
    vmsFault: VmsFaultEnumGOutput
    comFaultExtensionG: ExtensionTypeGOutput | None = None
    vmsVmsFaultExtensionG: ExtensionTypeGOutput | None = None
