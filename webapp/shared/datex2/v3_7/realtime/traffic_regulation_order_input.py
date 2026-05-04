"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.legal_basis_input import LegalBasisInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.reason_for_regulation_enum_g_input import ReasonForRegulationEnumGInput
from webapp.shared.datex2.v3_7.shared.traffic_regulation_order_status_enum_g_input import (
    TrafficRegulationOrderStatusEnumGInput,
)
from webapp.shared.datex2.v3_7.shared.validity_input import ValidityInput

from .location_reference_g_input import LocationReferenceGInput
from .traffic_regulation_g_input import TrafficRegulationGInput


@validataclass
class TrafficRegulationOrderInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    issuingAuthority: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    reason: list[ReasonForRegulationEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ReasonForRegulationEnumGInput)),
        Default(UnsetValue),
    )
    regulationId: str = StringValidator()
    status: TrafficRegulationOrderStatusEnumGInput = DataclassValidator(TrafficRegulationOrderStatusEnumGInput)
    implementedValidity: ValidityInput | UnsetValueType = DataclassValidator(ValidityInput), Default(UnsetValue)
    validityByOrder: ValidityInput | UnsetValueType = DataclassValidator(ValidityInput), Default(UnsetValue)
    implementedLocation: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    locationByOrder: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    trafficRegulation: list[TrafficRegulationGInput] = ListValidator(DataclassValidator(TrafficRegulationGInput))
    legalBasis: LegalBasisInput | UnsetValueType = DataclassValidator(LegalBasisInput), Default(UnsetValue)
    troTrafficRegulationOrderExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
