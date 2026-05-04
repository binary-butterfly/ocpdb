"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    FloatValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.header_information_input import HeaderInformationInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.tmplan_operation_status_enum_g_input import TmplanOperationStatusEnumGInput

from .non_predefined_action_input import NonPredefinedActionInput


@validataclass
class NonPredefinedTmplanOperationInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    creationTime: datetime = DateTimeValidator()
    expiryTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    status: TmplanOperationStatusEnumGInput = DataclassValidator(TmplanOperationStatusEnumGInput)
    statusReason: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    versionTime: datetime = DateTimeValidator()
    involvedRoadOperatorConsensusRate: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    nonPredefinedScenarioDescription: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    nonPredefinedScenarioId: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    nonPredefinedStrategyDescription: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    nonPredefinedStrategyId: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    headerInformation: HeaderInformationInput = DataclassValidator(HeaderInformationInput)
    nonPredefinedAction: list[NonPredefinedActionInput] = ListValidator(DataclassValidator(NonPredefinedActionInput))
    tmpTmplanOperationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpNonPredefinedTmplanOperationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
