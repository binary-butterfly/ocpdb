"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .smart_recharging_services_enum import SmartRechargingServicesEnum


@dataclass(kw_only=True)
class SmartRechargingServicesEnumGOutput:
    value: SmartRechargingServicesEnum
    extendedValueG: str | None = None
