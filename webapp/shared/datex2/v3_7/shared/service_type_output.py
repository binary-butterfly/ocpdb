"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .overall_period_output import OverallPeriodOutput
from .service_type_enum_g_output import ServiceTypeEnumGOutput


@dataclass(kw_only=True)
class ServiceTypeOutput:
    serviceType: ServiceTypeEnumGOutput
    overallPeriod: OverallPeriodOutput | None = None
    aegiServiceTypeExtensionG: ExtensionTypeGOutput | None = None
