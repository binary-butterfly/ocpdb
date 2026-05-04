"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.cause_input import CauseInput
from webapp.shared.datex2.v3_7.shared.comment_input import CommentInput
from webapp.shared.datex2.v3_7.shared.confidentiality_value_enum_g_input import ConfidentialityValueEnumGInput
from webapp.shared.datex2.v3_7.shared.driving_condition_type_enum_g_input import DrivingConditionTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.humidity_input import HumidityInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.pollution_input import PollutionInput
from webapp.shared.datex2.v3_7.shared.poor_environment_type_enum_g_input import PoorEnvironmentTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.precipitation_detail_input import PrecipitationDetailInput
from webapp.shared.datex2.v3_7.shared.pressure_input import PressureInput
from webapp.shared.datex2.v3_7.shared.probability_of_occurrence_enum_g_input import ProbabilityOfOccurrenceEnumGInput
from webapp.shared.datex2.v3_7.shared.severity_enum_g_input import SeverityEnumGInput
from webapp.shared.datex2.v3_7.shared.source_input import SourceInput
from webapp.shared.datex2.v3_7.shared.temperature_input import TemperatureInput
from webapp.shared.datex2.v3_7.shared.traffic_constriction_type_enum_g_input import TrafficConstrictionTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.url_link_input import UrlLinkInput
from webapp.shared.datex2.v3_7.shared.validity_input import ValidityInput
from webapp.shared.datex2.v3_7.shared.visibility_input import VisibilityInput
from webapp.shared.datex2.v3_7.shared.wind_input import WindInput

from .impact_input import ImpactInput
from .location_reference_g_input import LocationReferenceGInput


@validataclass
class PoorEnvironmentConditionsInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    situationRecordCreationReference: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    situationRecordCreationTime: datetime = DateTimeValidator()
    situationRecordObservationTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    situationRecordVersionTime: datetime = DateTimeValidator()
    situationRecordFirstSupplierVersionTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    confidentialityOverride: ConfidentialityValueEnumGInput | UnsetValueType = (
        DataclassValidator(ConfidentialityValueEnumGInput),
        Default(UnsetValue),
    )
    probabilityOfOccurrence: ProbabilityOfOccurrenceEnumGInput = DataclassValidator(ProbabilityOfOccurrenceEnumGInput)
    severity: SeverityEnumGInput | UnsetValueType = DataclassValidator(SeverityEnumGInput), Default(UnsetValue)
    safetyRelatedMessage: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    trafficConstrictionType: TrafficConstrictionTypeEnumGInput | UnsetValueType = (
        DataclassValidator(TrafficConstrictionTypeEnumGInput),
        Default(UnsetValue),
    )
    drivingConditionType: DrivingConditionTypeEnumGInput | UnsetValueType = (
        DataclassValidator(DrivingConditionTypeEnumGInput),
        Default(UnsetValue),
    )
    poorEnvironmentType: list[PoorEnvironmentTypeEnumGInput] = ListValidator(
        DataclassValidator(PoorEnvironmentTypeEnumGInput)
    )
    source: SourceInput | UnsetValueType = DataclassValidator(SourceInput), Default(UnsetValue)
    validity: ValidityInput = DataclassValidator(ValidityInput)
    impact: ImpactInput | UnsetValueType = DataclassValidator(ImpactInput), Default(UnsetValue)
    cause: CauseInput | UnsetValueType = DataclassValidator(CauseInput), Default(UnsetValue)
    generalPublicComment: list[CommentInput] | UnsetValueType = (
        ListValidator(DataclassValidator(CommentInput)),
        Default(UnsetValue),
    )
    nonGeneralPublicComment: list[CommentInput] | UnsetValueType = (
        ListValidator(DataclassValidator(CommentInput)),
        Default(UnsetValue),
    )
    urlLink: list[UrlLinkInput] | UnsetValueType = ListValidator(DataclassValidator(UrlLinkInput)), Default(UnsetValue)
    locationReference: LocationReferenceGInput = DataclassValidator(LocationReferenceGInput)
    informationManagerOverride: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    impactOnOppositeDirection: ImpactInput | UnsetValueType = DataclassValidator(ImpactInput), Default(UnsetValue)
    precipitationDetail: PrecipitationDetailInput | UnsetValueType = (
        DataclassValidator(PrecipitationDetailInput),
        Default(UnsetValue),
    )
    visibility: VisibilityInput | UnsetValueType = DataclassValidator(VisibilityInput), Default(UnsetValue)
    pollution: PollutionInput | UnsetValueType = DataclassValidator(PollutionInput), Default(UnsetValue)
    temperature: TemperatureInput | UnsetValueType = DataclassValidator(TemperatureInput), Default(UnsetValue)
    wind: WindInput | UnsetValueType = DataclassValidator(WindInput), Default(UnsetValue)
    humidity: HumidityInput | UnsetValueType = DataclassValidator(HumidityInput), Default(UnsetValue)
    pressure: PressureInput | UnsetValueType = DataclassValidator(PressureInput), Default(UnsetValue)
    sitSituationRecordExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    sitTrafficElementExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    sitConditionsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    sitPoorEnvironmentConditionsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
