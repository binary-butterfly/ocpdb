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
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.abnormal_traffic_type_enum_g_input import AbnormalTrafficTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.cause_input import CauseInput
from webapp.shared.datex2.v3_7.shared.comment_input import CommentInput
from webapp.shared.datex2.v3_7.shared.confidentiality_value_enum_g_input import ConfidentialityValueEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.probability_of_occurrence_enum_g_input import ProbabilityOfOccurrenceEnumGInput
from webapp.shared.datex2.v3_7.shared.relative_traffic_flow_enum_g_input import RelativeTrafficFlowEnumGInput
from webapp.shared.datex2.v3_7.shared.severity_enum_g_input import SeverityEnumGInput
from webapp.shared.datex2.v3_7.shared.source_input import SourceInput
from webapp.shared.datex2.v3_7.shared.traffic_constriction_type_enum_g_input import TrafficConstrictionTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.traffic_flow_characteristics_enum_g_input import (
    TrafficFlowCharacteristicsEnumGInput,
)
from webapp.shared.datex2.v3_7.shared.traffic_trend_type_enum_g_input import TrafficTrendTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.url_link_input import UrlLinkInput
from webapp.shared.datex2.v3_7.shared.validity_input import ValidityInput

from .impact_input import ImpactInput
from .location_reference_g_input import LocationReferenceGInput


@validataclass
class AbnormalTrafficInput(ValidataclassMixin):
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
    abnormalTrafficType: AbnormalTrafficTypeEnumGInput | UnsetValueType = (
        DataclassValidator(AbnormalTrafficTypeEnumGInput),
        Default(UnsetValue),
    )
    numberOfVehiclesWaiting: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    queueLength: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    relativeTrafficFlow: RelativeTrafficFlowEnumGInput | UnsetValueType = (
        DataclassValidator(RelativeTrafficFlowEnumGInput),
        Default(UnsetValue),
    )
    trafficFlowCharacteristics: TrafficFlowCharacteristicsEnumGInput | UnsetValueType = (
        DataclassValidator(TrafficFlowCharacteristicsEnumGInput),
        Default(UnsetValue),
    )
    trafficTrendType: TrafficTrendTypeEnumGInput | UnsetValueType = (
        DataclassValidator(TrafficTrendTypeEnumGInput),
        Default(UnsetValue),
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
    sitSituationRecordExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    sitTrafficElementExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    sitAbnormalTrafficExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
