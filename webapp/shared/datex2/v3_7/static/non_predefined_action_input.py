"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.situation_record_versioned_reference_g_input import (
    SituationRecordVersionedReferenceGInput,
)

from .operator_action_definition_g_input import OperatorActionDefinitionGInput


@validataclass
class NonPredefinedActionInput(ValidataclassMixin):
    nonPredefinedActionDescription: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    nonPredefinedActionId: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    actionImplementingSituationRecord: SituationRecordVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(SituationRecordVersionedReferenceGInput),
        Default(UnsetValue),
    )
    internationalIdentifier: InternationalIdentifierInput = DataclassValidator(InternationalIdentifierInput)
    operatorActionDefinition: OperatorActionDefinitionGInput | UnsetValueType = (
        DataclassValidator(OperatorActionDefinitionGInput),
        Default(UnsetValue),
    )
    tmpNonPredefinedActionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
