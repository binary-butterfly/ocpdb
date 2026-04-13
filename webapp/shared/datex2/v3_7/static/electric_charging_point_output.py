"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.location_reference_g_output import LocationReferenceGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_output import OperatingHoursGOutput
from webapp.shared.datex2.v3_7.shared.rates_g_output import RatesGOutput
from webapp.shared.datex2.v3_7.shared.vehicle_characteristics_output import VehicleCharacteristicsOutput

from .accessibility_enum_g_output import AccessibilityEnumGOutput
from .amenities_output import AmenitiesOutput
from .associated_facility_g_output import AssociatedFacilityGOutput
from .charging_mode_enum_g_output import ChargingModeEnumGOutput
from .charging_point_usage_type_enum_g_output import ChargingPointUsageTypeEnumGOutput
from .connector_output import ConnectorOutput
from .current_type_enum_g_output import CurrentTypeEnumGOutput
from .dedicated_parking_spaces_output import DedicatedParkingSpacesOutput
from .delivery_unit_enum_g_output import DeliveryUnitEnumGOutput
from .dimension_output import DimensionOutput
from .energy_product_g_output import EnergyProductGOutput
from .external_identifier_output import ExternalIdentifierOutput
from .image_output import ImageOutput
from .organisation_g_output import OrganisationGOutput
from .reservation_type_enum_g_output import ReservationTypeEnumGOutput
from .smart_recharging_services_enum_g_output import SmartRechargingServicesEnumGOutput
from .url_link_output import UrlLinkOutput
from .vehicle_to_grid_communication_type_enum_g_output import VehicleToGridCommunicationTypeEnumGOutput


@dataclass(kw_only=True)
class ElectricChargingPointOutput:
    idG: str
    versionG: str
    name: MultilingualStringOutput | None = None
    alias: list[MultilingualStringOutput] | None = None
    lastUpdated: datetime | None = None
    description: MultilingualStringOutput | None = None
    accessibility: list[AccessibilityEnumGOutput] | None = None
    additionalInformation: list[MultilingualStringOutput] | None = None
    deliveryUnit: DeliveryUnitEnumGOutput
    maximumDeliveryAmount: float | None = None
    minimumDeliveryAmount: float | None = None
    modelType: MultilingualStringOutput | None = None
    reservation: ReservationTypeEnumGOutput | None = None
    currentType: CurrentTypeEnumGOutput
    usageType: list[ChargingPointUsageTypeEnumGOutput] | None = None
    vehicleToGridCommunicationType: list[VehicleToGridCommunicationTypeEnumGOutput] | None = None
    numberOfConnectors: int | None = None
    availableVoltage: list[float] | None = None
    availableChargingPower: list[float] | None = None
    chargingMode: ChargingModeEnumGOutput | None = None
    smartRechargingServices: list[SmartRechargingServicesEnumGOutput] | None = None
    otherSmartRechargingServices: list[MultilingualStringOutput] | None = None
    externalIdentifier: list[ExternalIdentifierOutput] | None = None
    informationWebsite: list[UrlLinkOutput] | None = None
    photoUrl: list[UrlLinkOutput] | None = None
    photo: list[ImageOutput] | None = None
    operatingHours: OperatingHoursGOutput | None = None
    locationReference: LocationReferenceGOutput | None = None
    owner: OrganisationGOutput | None = None
    operator: OrganisationGOutput | None = None
    helpdesk: OrganisationGOutput | None = None
    associatedFacility: list[AssociatedFacilityGOutput] | None = None
    rates: RatesGOutput | None = None
    applicableForVehicles: list[VehicleCharacteristicsOutput] | None = None
    dimension: DimensionOutput | None = None
    amenities: AmenitiesOutput | None = None
    dedicatedParkingSpaces: list[DedicatedParkingSpacesOutput] | None = None
    energyProduct: list[EnergyProductGOutput] | None = None
    connector: list[ConnectorOutput] | None = None
    afacFacilityObjectExtensionG: ExtensionTypeGOutput | None = None
    afacFacilityExtensionG: ExtensionTypeGOutput | None = None
    aegiRefillPointExtensionG: ExtensionTypeGOutput | None = None
    aegiElectricChargingPointExtensionG: ExtensionTypeGOutput | None = None
