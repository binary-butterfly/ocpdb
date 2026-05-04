"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .action_definition_versioned_reference_g_input import ActionDefinitionVersionedReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput
from .situation_record_versioned_reference_g_input import SituationRecordVersionedReferenceGInput


@validataclass
class PredefinedActionInput(ValidataclassMixin):
    actionImplementingSituationRecord: SituationRecordVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(SituationRecordVersionedReferenceGInput),
        Default(UnsetValue),
    )
    predefinedActionReference: ActionDefinitionVersionedReferenceGInput = DataclassValidator(
        ActionDefinitionVersionedReferenceGInput
    )
    tmpPredefinedActionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
