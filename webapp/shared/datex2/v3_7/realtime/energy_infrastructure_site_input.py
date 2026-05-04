"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.accessibility_enum_g_input import AccessibilityEnumGInput
from webapp.shared.datex2.v3_7.shared.associated_facility_g_input import AssociatedFacilityGInput
from webapp.shared.datex2.v3_7.shared.dimension_input import DimensionInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.image_input import ImageInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_7.shared.url_link_input import UrlLinkInput
from webapp.shared.datex2.v3_7.shared.user_type_enum_g_input import UserTypeEnumGInput

from .energy_infrastructure_site_type_enum_g_input import EnergyInfrastructureSiteTypeEnumGInput
from .energy_infrastructure_station_input import EnergyInfrastructureStationInput
from .location_g_input import LocationGInput
from .location_reference_g_input import LocationReferenceGInput
from .organisation_g_input import OrganisationGInput
from .rates_g_input import RatesGInput
from .supplemental_facility_g_input import SupplementalFacilityGInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class EnergyInfrastructureSiteInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    alias: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    externalIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    lastUpdated: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
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
    associatedFacility: list[AssociatedFacilityGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AssociatedFacilityGInput)),
        Default(UnsetValue),
    )
    rates: RatesGInput | UnsetValueType = DataclassValidator(RatesGInput), Default(UnsetValue)
    applicableForVehicles: list[VehicleCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleCharacteristicsInput)),
        Default(UnsetValue),
    )
    dimension: DimensionInput | UnsetValueType = DataclassValidator(DimensionInput), Default(UnsetValue)
    supplementalFacility: list[SupplementalFacilityGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SupplementalFacilityGInput)),
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
    facFacilityObjectExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facFacilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    egiEnergyInfrastructureSiteExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
