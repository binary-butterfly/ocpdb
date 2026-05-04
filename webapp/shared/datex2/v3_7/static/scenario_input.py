"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.cause_type_enum_g_input import CauseTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.detailed_cause_type_input import DetailedCauseTypeInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.organisation_reference_g_input import OrganisationReferenceGInput
from webapp.shared.datex2.v3_7.shared.overall_period_input import OverallPeriodInput

from .impact_kind_input import ImpactKindInput
from .location_reference_g_input import LocationReferenceGInput
from .strategy_g_input import StrategyGInput


@validataclass
class ScenarioInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    externalIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    versionTime: datetime = DateTimeValidator()
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    situationType: list[CauseTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(CauseTypeEnumGInput)),
        Default(UnsetValue),
    )
    emergencyServicesAccessibility: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    name: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    scenarioDirector: OrganisationReferenceGInput | UnsetValueType = (
        DataclassValidator(OrganisationReferenceGInput),
        Default(UnsetValue),
    )
    situationFilter: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    strategy: list[StrategyGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(StrategyGInput)),
        Default(UnsetValue),
    )
    impactKind: ImpactKindInput | UnsetValueType = DataclassValidator(ImpactKindInput), Default(UnsetValue)
    problemLocation: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    scheduledScenarioValidity: OverallPeriodInput | UnsetValueType = (
        DataclassValidator(OverallPeriodInput),
        Default(UnsetValue),
    )
    situationTypeDetail: list[DetailedCauseTypeInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DetailedCauseTypeInput)),
        Default(UnsetValue),
    )
    tmpScenarioExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
