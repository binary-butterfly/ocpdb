"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .assigned_right_time_relative_g_input import AssignedRightTimeRelativeGInput
from .extension_type_g_input import ExtensionTypeGInput
from .right_specification_versioned_reference_g_input import RightSpecificationVersionedReferenceGInput


@validataclass
class LinkedRightSpecificationInput(ValidataclassMixin):
    qualifyingRightSpec: RightSpecificationVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(RightSpecificationVersionedReferenceGInput),
        Default(UnsetValue),
    )
    assignedRightTimeRelative: AssignedRightTimeRelativeGInput | UnsetValueType = (
        DataclassValidator(AssignedRightTimeRelativeGInput),
        Default(UnsetValue),
    )
    afacLinkedRightSpecificationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
