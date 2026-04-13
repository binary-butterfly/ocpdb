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
from webapp.shared.datex2.v3_7.shared.service_type_output import ServiceTypeOutput
from webapp.shared.datex2.v3_7.shared.vehicle_characteristics_output import VehicleCharacteristicsOutput

from .accessibility_enum_g_output import AccessibilityEnumGOutput
from .amenities_output import AmenitiesOutput
from .associated_facility_g_output import AssociatedFacilityGOutput
from .authentication_and_identification_enum_g_output import AuthenticationAndIdentificationEnumGOutput
from .dedicated_parking_spaces_output import DedicatedParkingSpacesOutput
from .dimension_output import DimensionOutput
from .energy_product_g_output import EnergyProductGOutput
from .external_identifier_output import ExternalIdentifierOutput
from .image_output import ImageOutput
from .organisation_g_output import OrganisationGOutput
from .refill_point_g_output import RefillPointGOutput
from .supplemental_facility_g_output import SupplementalFacilityGOutput
from .url_link_output import UrlLinkOutput


@dataclass(kw_only=True)
class EnergyInfrastructureStationOutput:
    idG: str
    versionG: str
    name: MultilingualStringOutput | None = None
    alias: list[MultilingualStringOutput] | None = None
    lastUpdated: datetime | None = None
    description: MultilingualStringOutput | None = None
    accessibility: list[AccessibilityEnumGOutput] | None = None
    additionalInformation: list[MultilingualStringOutput] | None = None
    totalMaximumPower: float | None = None
    authenticationAndIdentificationMethods: list[AuthenticationAndIdentificationEnumGOutput] | None = None
    numberOfRefillPoints: int | None = None
    userInterfaceLanguage: list[str] | None = None
    renewableSources: bool | None = None
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
    supplementalFacility: list[SupplementalFacilityGOutput] | None = None
    dedicatedParkingSpaces: list[DedicatedParkingSpacesOutput] | None = None
    energyDistributor: OrganisationGOutput | None = None
    mobilityServiceProvider: list[OrganisationGOutput] | None = None
    roamingPlatform: list[OrganisationGOutput] | None = None
    serviceType: list[ServiceTypeOutput] | None = None
    refillPoint: list[RefillPointGOutput] | None = None
    energyProduct: list[EnergyProductGOutput] | None = None
    afacFacilityObjectExtensionG: ExtensionTypeGOutput | None = None
    afacFacilityExtensionG: ExtensionTypeGOutput | None = None
    aegiEnergyInfrastructureStationExtensionG: ExtensionTypeGOutput | None = None
