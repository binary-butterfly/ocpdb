"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.activation_status_enum_g_input import ActivationStatusEnumGInput
from webapp.shared.datex2.v3_7.shared.activation_type_enum_g_input import ActivationTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.alternative_mobility_options_input import AlternativeMobilityOptionsInput
from webapp.shared.datex2.v3_7.shared.controlled_zone_summary_input import ControlledZoneSummaryInput
from webapp.shared.datex2.v3_7.shared.controlled_zone_table_publication_versioned_reference_g_input import (
    ControlledZoneTablePublicationVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.controlled_zone_type_enum_g_input import ControlledZoneTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .controlled_zone_regulation_input import ControlledZoneRegulationInput
from .rates_g_input import RatesGInput
from .traffic_regulation_order_g_input import TrafficRegulationOrderGInput


@validataclass
class ControlledZoneInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    controlledZoneType: list[ControlledZoneTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ControlledZoneTypeEnumGInput)),
        Default(UnsetValue),
    )
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    recordVersionTime: datetime = DateTimeValidator()
    activationType: ActivationTypeEnumGInput | UnsetValueType = (
        DataclassValidator(ActivationTypeEnumGInput),
        Default(UnsetValue),
    )
    status: ActivationStatusEnumGInput = DataclassValidator(ActivationStatusEnumGInput)
    dynamicActivationPublicationSource: ControlledZoneTablePublicationVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(ControlledZoneTablePublicationVersionedReferenceGInput),
        Default(UnsetValue),
    )
    controlledZoneSummary: ControlledZoneSummaryInput | UnsetValueType = (
        DataclassValidator(ControlledZoneSummaryInput),
        Default(UnsetValue),
    )
    trafficRegulationOrder: list[TrafficRegulationOrderGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TrafficRegulationOrderGInput)),
        Default(UnsetValue),
    )
    controlledZoneRegulation: list[ControlledZoneRegulationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ControlledZoneRegulationInput)),
        Default(UnsetValue),
    )
    tariffInformation: list[RatesGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RatesGInput)),
        Default(UnsetValue),
    )
    alternativeMobilityOptions: list[AlternativeMobilityOptionsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AlternativeMobilityOptionsInput)),
        Default(UnsetValue),
    )
    czControlledZoneExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
