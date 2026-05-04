"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.delays_input import DelaysInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.pt_schedule_input import PtScheduleInput
from webapp.shared.datex2.v3_7.shared.route_allocation_g_input import RouteAllocationGInput
from webapp.shared.datex2.v3_7.shared.supplementary_positional_description_input import (
    SupplementaryPositionalDescriptionInput,
)
from webapp.shared.datex2.v3_7.shared.traffic_constriction_type_enum_g_input import TrafficConstrictionTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.traffic_regulation_order_versioned_reference_g_input import (
    TrafficRegulationOrderVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.traffic_status_value_input import TrafficStatusValueInput
from webapp.shared.datex2.v3_7.shared.travel_time_data_input import TravelTimeDataInput

from .abnormal_traffic_input import AbnormalTrafficInput
from .capacity_management_measure_input import CapacityManagementMeasureInput
from .itinerary_g_input import ItineraryGInput
from .specific_destination_facility_input import SpecificDestinationFacilityInput


@validataclass
class RouteDescriptionInput(ValidataclassMixin):
    nameOfRoute: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    routeClosed: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    isPublicTransportRoute: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    troReference: list[TrafficRegulationOrderVersionedReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TrafficRegulationOrderVersionedReferenceGInput)),
        Default(UnsetValue),
    )
    priorityIndex: int | UnsetValueType = IntegerValidator(min_value=0.0), Default(UnsetValue)
    capacityAvailable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    signedRerouting: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    entry: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    exit: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    roadOrJunctionNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    trafficConstriction: TrafficConstrictionTypeEnumGInput | UnsetValueType = (
        DataclassValidator(TrafficConstrictionTypeEnumGInput),
        Default(UnsetValue),
    )
    routeLength: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    itinerary: ItineraryGInput | UnsetValueType = DataclassValidator(ItineraryGInput), Default(UnsetValue)
    routeAllocation: list[RouteAllocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RouteAllocationGInput)),
        Default(UnsetValue),
    )
    specificDestinationFacility: SpecificDestinationFacilityInput | UnsetValueType = (
        DataclassValidator(SpecificDestinationFacilityInput),
        Default(UnsetValue),
    )
    ptRouteSchedule: list[PtScheduleInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PtScheduleInput)),
        Default(UnsetValue),
    )
    capacityManagementMeasure: list[CapacityManagementMeasureInput] | UnsetValueType = (
        ListValidator(DataclassValidator(CapacityManagementMeasureInput)),
        Default(UnsetValue),
    )
    supplementaryPositionalDescription: SupplementaryPositionalDescriptionInput | UnsetValueType = (
        DataclassValidator(SupplementaryPositionalDescriptionInput),
        Default(UnsetValue),
    )
    abnormalTraffic: AbnormalTrafficInput | UnsetValueType = (
        DataclassValidator(AbnormalTrafficInput),
        Default(UnsetValue),
    )
    routeDelays: DelaysInput | UnsetValueType = DataclassValidator(DelaysInput), Default(UnsetValue)
    trafficStatus: TrafficStatusValueInput | UnsetValueType = (
        DataclassValidator(TrafficStatusValueInput),
        Default(UnsetValue),
    )
    travelTimeData: list[TravelTimeDataInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TravelTimeDataInput)),
        Default(UnsetValue),
    )
    rerRouteDescriptionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
