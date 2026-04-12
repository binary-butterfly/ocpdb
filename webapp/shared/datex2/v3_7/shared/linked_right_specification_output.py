"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .assigned_right_time_relative_g_output import AssignedRightTimeRelativeGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .right_specification_versioned_reference_g_output import RightSpecificationVersionedReferenceGOutput


@dataclass(kw_only=True)
class LinkedRightSpecificationOutput:
    qualifyingRightSpec: RightSpecificationVersionedReferenceGOutput | None = None
    assignedRightTimeRelative: AssignedRightTimeRelativeGOutput | None = None
    afacLinkedRightSpecificationExtensionG: ExtensionTypeGOutput | None = None
