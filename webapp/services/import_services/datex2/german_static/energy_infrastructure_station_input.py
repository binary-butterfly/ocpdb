"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
    RegexValidator,
    StringValidator,
)

from .accessibility_enum_g_input import AccessibilityEnumGInput
from .amenities_input import AmenitiesInput
from .authentication_and_identification_enum_g_input import AuthenticationAndIdentificationEnumGInput
from .dedicated_parking_spaces_input import DedicatedParkingSpacesInput
from .dimension_input import DimensionInput
from .electric_energy_input import ElectricEnergyInput
from .extension_type_g_input import ExtensionTypeGInput
from .external_identifier_input import ExternalIdentifierInput
from .image_input import ImageInput
from .location_reference_g_input import LocationReferenceGInput
from .multilingual_string_input import MultilingualStringInput
from .operating_hours_g_input import OperatingHoursGInput
from .organisation_g_input import OrganisationGInput
from .refill_point_g_input import RefillPointGInput
from .service_type_input import ServiceTypeInput
from .supplemental_facility_g_input import SupplementalFacilityGInput
from .url_link_input import UrlLinkInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput
from .versioned_reference_input import VersionedReferenceInput


@validataclass
class EnergyInfrastructureStationInput:
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
    totalMaximumPower: int = FloatValidator()
    authenticationAndIdentificationMethods: list[AuthenticationAndIdentificationEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AuthenticationAndIdentificationEnumGInput)),
        Default(UnsetValue),
    )
    numberOfRefillPoints: int = IntegerValidator(min_value=0)
    refillPointByReference: list[VersionedReferenceInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VersionedReferenceInput)),
        Default(UnsetValue),
    )
    userInterfaceLanguage: list[str] | UnsetValueType = (
        ListValidator(RegexValidator(pattern=r'^[a-z]{2}$')),
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
    energyDistributor: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    mobilityServiceProvider: list[OrganisationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OrganisationGInput)),
        Default(UnsetValue),
    )
    roamingPlatform: list[OrganisationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OrganisationGInput)),
        Default(UnsetValue),
    )
    serviceType: list[ServiceTypeInput] = ListValidator(DataclassValidator(ServiceTypeInput))
    refillPoint: list[RefillPointGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RefillPointGInput)),
        Default(UnsetValue),
    )
    electricEnergy: list[ElectricEnergyInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ElectricEnergyInput)),
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
    aegiEnergyInfrastructureStationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
