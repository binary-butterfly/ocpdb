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

from webapp.shared.datex2.v3_7.shared.accident_cause_enum_g_input import AccidentCauseEnumGInput
from webapp.shared.datex2.v3_7.shared.accident_extension_type_g_input import AccidentExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.accident_type_enum_g_input import AccidentTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.cause_input import CauseInput
from webapp.shared.datex2.v3_7.shared.collision_type_enum_g_input import CollisionTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.comment_input import CommentInput
from webapp.shared.datex2.v3_7.shared.confidentiality_value_enum_g_input import ConfidentialityValueEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.group_of_people_involved_input import GroupOfPeopleInvolvedInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.probability_of_occurrence_enum_g_input import ProbabilityOfOccurrenceEnumGInput
from webapp.shared.datex2.v3_7.shared.severity_enum_g_input import SeverityEnumGInput
from webapp.shared.datex2.v3_7.shared.source_input import SourceInput
from webapp.shared.datex2.v3_7.shared.traffic_constriction_type_enum_g_input import TrafficConstrictionTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.url_link_input import UrlLinkInput
from webapp.shared.datex2.v3_7.shared.validity_input import ValidityInput

from .group_of_vehicles_involved_input import GroupOfVehiclesInvolvedInput
from .impact_input import ImpactInput
from .location_reference_g_input import LocationReferenceGInput
from .vehicle_input import VehicleInput


@validataclass
class AccidentInput(ValidataclassMixin):
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
    accidentCause: AccidentCauseEnumGInput | UnsetValueType = (
        DataclassValidator(AccidentCauseEnumGInput),
        Default(UnsetValue),
    )
    accidentType: list[AccidentTypeEnumGInput] = ListValidator(DataclassValidator(AccidentTypeEnumGInput))
    collisionType: CollisionTypeEnumGInput | UnsetValueType = (
        DataclassValidator(CollisionTypeEnumGInput),
        Default(UnsetValue),
    )
    totalNumberOfPeopleInvolved: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    totalNumberOfVehiclesInvolved: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
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
    vehicleInvolved: list[VehicleInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleInput)),
        Default(UnsetValue),
    )
    groupOfVehiclesInvolved: list[GroupOfVehiclesInvolvedInput] | UnsetValueType = (
        ListValidator(DataclassValidator(GroupOfVehiclesInvolvedInput)),
        Default(UnsetValue),
    )
    groupOfPeopleInvolved: list[GroupOfPeopleInvolvedInput] | UnsetValueType = (
        ListValidator(DataclassValidator(GroupOfPeopleInvolvedInput)),
        Default(UnsetValue),
    )
    sitSituationRecordExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    sitTrafficElementExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    sitAccidentExtensionG: AccidentExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(AccidentExtensionTypeGInput),
        Default(UnsetValue),
    )
