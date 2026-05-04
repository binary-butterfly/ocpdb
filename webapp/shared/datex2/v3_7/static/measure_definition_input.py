"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.activation_conditions_input import ActivationConditionsInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.organisation_reference_g_input import OrganisationReferenceGInput
from webapp.shared.datex2.v3_7.shared.response_type_input import ResponseTypeInput

from .action_g_input import ActionGInput


@validataclass
class MeasureDefinitionInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    versionTime: datetime = DateTimeValidator()
    externalIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    description: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    responsibleRoadOperator: OrganisationReferenceGInput = DataclassValidator(OrganisationReferenceGInput)
    shortName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    action: list[ActionGInput] = ListValidator(DataclassValidator(ActionGInput))
    responseType: ResponseTypeInput | UnsetValueType = DataclassValidator(ResponseTypeInput), Default(UnsetValue)
    activationConditions: ActivationConditionsInput | UnsetValueType = (
        DataclassValidator(ActivationConditionsInput),
        Default(UnsetValue),
    )
    tmpMeasureExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpMeasureDefinitionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
