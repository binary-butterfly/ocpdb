"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .device_component_enum import DeviceComponentEnum


@dataclass(kw_only=True)
class DeviceComponentEnumGOutput:
    value: DeviceComponentEnum
    extendedValueG: str | None = None
