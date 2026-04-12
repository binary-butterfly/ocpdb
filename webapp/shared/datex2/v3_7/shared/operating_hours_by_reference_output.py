"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .closure_information_output import ClosureInformationOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .operating_hours_specification_versioned_reference_g_output import (
    OperatingHoursSpecificationVersionedReferenceGOutput,
)
from .operating_hours_table_versioned_reference_g_output import OperatingHoursTableVersionedReferenceGOutput


@dataclass(kw_only=True)
class OperatingHoursByReferenceOutput:
    operatingHoursReference: OperatingHoursSpecificationVersionedReferenceGOutput
    operatingHoursTableReference: OperatingHoursTableVersionedReferenceGOutput | None = None
    closureInformation: ClosureInformationOutput | None = None
    afacOperatingHoursExtensionG: ExtensionTypeGOutput | None = None
    afacOperatingHoursByReferenceExtensionG: ExtensionTypeGOutput | None = None
