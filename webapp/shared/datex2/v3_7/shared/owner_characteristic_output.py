"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .location_reference_g_output import LocationReferenceGOutput
from .owner_type_enum_g_output import OwnerTypeEnumGOutput


@dataclass(kw_only=True)
class OwnerCharacteristicOutput:
    ownerType: OwnerTypeEnumGOutput
    locationOfResidency: LocationReferenceGOutput | None = None
    comxOwnerCharacteristicExtensionG: ExtensionTypeGOutput | None = None
