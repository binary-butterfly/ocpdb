"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .infrastructure_descriptor_enum import InfrastructureDescriptorEnum
from .infrastructure_descriptor_enum_extension_type_g import InfrastructureDescriptorEnumExtensionTypeG


@dataclass(kw_only=True)
class InfrastructureDescriptorEnumGOutput:
    value: InfrastructureDescriptorEnum
    extendedValueG: InfrastructureDescriptorEnumExtensionTypeG | None = None
