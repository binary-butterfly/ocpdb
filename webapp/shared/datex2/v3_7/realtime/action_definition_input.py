"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.activation_delay_input import ActivationDelayInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .operator_action_definition_g_input import OperatorActionDefinitionGInput


@validataclass
class ActionDefinitionInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    versionTime: datetime = DateTimeValidator()
    externalIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    description: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    actionImplementer: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    operatorActionDefinition: OperatorActionDefinitionGInput | UnsetValueType = (
        DataclassValidator(OperatorActionDefinitionGInput),
        Default(UnsetValue),
    )
    activationDelay: ActivationDelayInput | UnsetValueType = (
        DataclassValidator(ActivationDelayInput),
        Default(UnsetValue),
    )
    tmpActionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpActionDefinitionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
