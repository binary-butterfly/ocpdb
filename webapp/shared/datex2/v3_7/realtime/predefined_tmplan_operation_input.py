"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, FloatValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.header_information_input import HeaderInformationInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.predefined_measure_selected_input import PredefinedMeasureSelectedInput
from webapp.shared.datex2.v3_7.shared.scenario_versioned_reference_g_input import ScenarioVersionedReferenceGInput
from webapp.shared.datex2.v3_7.shared.strategy_versioned_reference_g_input import StrategyVersionedReferenceGInput
from webapp.shared.datex2.v3_7.shared.tmplan_operation_status_enum_g_input import TmplanOperationStatusEnumGInput
from webapp.shared.datex2.v3_7.shared.tmplan_table_versioned_reference_g_input import (
    TmplanTableVersionedReferenceGInput,
)

from .location_reference_g_input import LocationReferenceGInput


@validataclass
class PredefinedTmplanOperationInput(ValidataclassMixin):
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
    tmplanTableReference: TmplanTableVersionedReferenceGInput = DataclassValidator(TmplanTableVersionedReferenceGInput)
    predefinedScenarioReference: ScenarioVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(ScenarioVersionedReferenceGInput),
        Default(UnsetValue),
    )
    predefinedStrategyReference: StrategyVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(StrategyVersionedReferenceGInput),
        Default(UnsetValue),
    )
    headerInformation: HeaderInformationInput = DataclassValidator(HeaderInformationInput)
    predefinedMeasureSelected: PredefinedMeasureSelectedInput | UnsetValueType = (
        DataclassValidator(PredefinedMeasureSelectedInput),
        Default(UnsetValue),
    )
    problemLocationOverride: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    tmpTmplanOperationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpPredefinedTmplanOperationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
