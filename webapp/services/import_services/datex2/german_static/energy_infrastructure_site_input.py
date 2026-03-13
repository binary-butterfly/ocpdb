"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .accessibility_enum_g_input import AccessibilityEnumGInput
from .amenities_input import AmenitiesInput
from .dedicated_parking_spaces_input import DedicatedParkingSpacesInput
from .dimension_input import DimensionInput
from .energy_infrastructure_site_type_enum_g_input import EnergyInfrastructureSiteTypeEnumGInput
from .energy_infrastructure_station_input import EnergyInfrastructureStationInput
from .extension_type_g_input import ExtensionTypeGInput
from .external_identifier_input import ExternalIdentifierInput
from .image_input import ImageInput
from .location_g_input import LocationGInput
from .location_reference_g_input import LocationReferenceGInput
from .multilingual_string_input import MultilingualStringInput
from .operating_hours_g_input import OperatingHoursGInput
from .organisation_g_input import OrganisationGInput
from .service_type_input import ServiceTypeInput
from .supplemental_facility_g_input import SupplementalFacilityGInput
from .url_link_input import UrlLinkInput
from .user_type_enum_g_input import UserTypeEnumGInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class EnergyInfrastructureSiteInput:
    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    alias: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    lastUpdated: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    accessibility: list[AccessibilityEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AccessibilityEnumGInput)),
        Default(UnsetValue),
    )
    additionalInformation: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    typeOfSite: EnergyInfrastructureSiteTypeEnumGInput | UnsetValueType = (
        DataclassValidator(EnergyInfrastructureSiteTypeEnumGInput),
        Default(UnsetValue),
    )
    brand: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    exclusiveUsers: list[UserTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(UserTypeEnumGInput)),
        Default(UnsetValue),
    )
    preferredUsers: list[UserTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(UserTypeEnumGInput)),
        Default(UnsetValue),
    )
    externalIdentifier: list[ExternalIdentifierInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ExternalIdentifierInput)),
        Default(UnsetValue),
    )
    informationWebsite: list[UrlLinkInput] | UnsetValueType = (
        ListValidator(DataclassValidator(UrlLinkInput)),
        Default(UnsetValue),
    )
    photoUrl: list[UrlLinkInput] | UnsetValueType = ListValidator(DataclassValidator(UrlLinkInput)), Default(UnsetValue)
    photo: list[ImageInput] | UnsetValueType = ListValidator(DataclassValidator(ImageInput)), Default(UnsetValue)
    operatingHours: OperatingHoursGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursGInput),
        Default(UnsetValue),
    )
    locationReference: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    owner: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    operator: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    helpdesk: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    applicableForVehicles: list[VehicleCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleCharacteristicsInput)),
        Default(UnsetValue),
    )
    dimension: DimensionInput | UnsetValueType = DataclassValidator(DimensionInput), Default(UnsetValue)
    amenities: AmenitiesInput | UnsetValueType = DataclassValidator(AmenitiesInput), Default(UnsetValue)
    supplementalFacility: list[SupplementalFacilityGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SupplementalFacilityGInput)),
        Default(UnsetValue),
    )
    dedicatedParkingSpaces: list[DedicatedParkingSpacesInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DedicatedParkingSpacesInput)),
        Default(UnsetValue),
    )
    serviceType: list[ServiceTypeInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ServiceTypeInput)),
        Default(UnsetValue),
    )
    entrance: list[LocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationGInput)),
        Default(UnsetValue),
    )
    exit: list[LocationGInput] | UnsetValueType = ListValidator(DataclassValidator(LocationGInput)), Default(UnsetValue)
    energyInfrastructureStation: list[EnergyInfrastructureStationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyInfrastructureStationInput)),
        Default(UnsetValue),
    )
    energyDistributor: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    mobilityServiceProvider: list[OrganisationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OrganisationGInput)),
        Default(UnsetValue),
    )
    roamingPlatfom: list[OrganisationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OrganisationGInput)),
        Default(UnsetValue),
    )
    afacFacilityObjectExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacFacilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    aegiEnergyInfrastructureSiteExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
