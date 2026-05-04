"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator

from .action_definition_versioned_reference_g_input import ActionDefinitionVersionedReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class ActionByReferenceInput(ValidataclassMixin):
    versionTime: datetime = DateTimeValidator()
    actionReference: ActionDefinitionVersionedReferenceGInput = DataclassValidator(
        ActionDefinitionVersionedReferenceGInput
    )
    tmpActionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpActionByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
