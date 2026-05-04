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
    ListValidator,
    RegexValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.predefined_condition_publication_versioned_reference_g_input import (
    PredefinedConditionPublicationVersionedReferenceGInput,
)

from .ad_hoc_traffic_regulations_input import AdHocTrafficRegulationsInput
from .dynamic_traffic_regulations_input import DynamicTrafficRegulationsInput
from .traffic_regulations_by_authorised_actors_input import TrafficRegulationsByAuthorisedActorsInput
from .traffic_regulations_from_competent_authorities_input import TrafficRegulationsFromCompetentAuthoritiesInput
from .traffic_regulations_without_traffic_regulation_order_input import (
    TrafficRegulationsWithoutTrafficRegulationOrderInput,
)


@validataclass
class TrafficRegulationPublicationInput(ValidataclassMixin):
    idG: str = StringValidator()
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    feedDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    feedType: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    publicationTime: datetime = DateTimeValidator()
    predefinedConditionPublicationReference: (
        list[PredefinedConditionPublicationVersionedReferenceGInput] | UnsetValueType
    ) = ListValidator(DataclassValidator(PredefinedConditionPublicationVersionedReferenceGInput)), Default(UnsetValue)
    publicationCreator: InternationalIdentifierInput = DataclassValidator(InternationalIdentifierInput)
    trafficRegulationsFromCompetentAuthorities: TrafficRegulationsFromCompetentAuthoritiesInput | UnsetValueType = (
        DataclassValidator(TrafficRegulationsFromCompetentAuthoritiesInput),
        Default(UnsetValue),
    )
    trafficRegulationsByAuthorisedActors: TrafficRegulationsByAuthorisedActorsInput | UnsetValueType = (
        DataclassValidator(TrafficRegulationsByAuthorisedActorsInput),
        Default(UnsetValue),
    )
    adHocTrafficRegulations: AdHocTrafficRegulationsInput | UnsetValueType = (
        DataclassValidator(AdHocTrafficRegulationsInput),
        Default(UnsetValue),
    )
    dynamicTrafficRegulations: DynamicTrafficRegulationsInput | UnsetValueType = (
        DataclassValidator(DynamicTrafficRegulationsInput),
        Default(UnsetValue),
    )
    trafficRegulationsWithoutTrafficRegulationOrder: (
        TrafficRegulationsWithoutTrafficRegulationOrderInput | UnsetValueType
    ) = DataclassValidator(TrafficRegulationsWithoutTrafficRegulationOrderInput), Default(UnsetValue)
    comPayloadPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troTrafficRegulationPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
