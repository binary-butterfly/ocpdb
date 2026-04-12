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
from webapp.shared.datex2.v3_7.shared.user_type_enum_g_output import UserTypeEnumGOutput
from webapp.shared.datex2.v3_7.shared.vehicle_characteristics_output import VehicleCharacteristicsOutput

from .accessibility_enum_g_output import AccessibilityEnumGOutput
from .amenities_output import AmenitiesOutput
from .associated_facility_g_output import AssociatedFacilityGOutput
from .availability_enum_g_output import AvailabilityEnumGOutput
from .dimension_output import DimensionOutput
from .electric_charging_point_output import ElectricChargingPointOutput
from .external_identifier_output import ExternalIdentifierOutput
from .image_output import ImageOutput
from .organisation_g_output import OrganisationGOutput
from .url_link_output import UrlLinkOutput


@dataclass(kw_only=True)
class ElectricChargingEquipmentOutput:
    idG: str
    versionG: str
    name: MultilingualStringOutput | None = None
    alias: list[MultilingualStringOutput] | None = None
    lastUpdated: datetime | None = None
    description: MultilingualStringOutput | None = None
    accessibility: list[AccessibilityEnumGOutput] | None = None
    additionalInformation: list[MultilingualStringOutput] | None = None
    availability: AvailabilityEnumGOutput | None = None
    quantity: int | None = None
    regularlyCleaned: bool | None = None
    applicableForUser: list[UserTypeEnumGOutput] | None = None
    nearby: bool | None = None
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
    electricChargingPoint: ElectricChargingPointOutput
    afacFacilityObjectExtensionG: ExtensionTypeGOutput | None = None
    afacSupplementalFacilityExtensionG: ExtensionTypeGOutput | None = None
    aegiElectricChargingEquipmentExtensionG: ExtensionTypeGOutput | None = None
