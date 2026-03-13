"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from .accessibility_enum_g_input import AccessibilityEnumGInput
from .amenities_input import AmenitiesInput
from .availability_enum_g_input import AvailabilityEnumGInput
from .dimension_input import DimensionInput
from .extension_type_g_input import ExtensionTypeGInput
from .external_identifier_input import ExternalIdentifierInput
from .image_input import ImageInput
from .location_reference_g_input import LocationReferenceGInput
from .multilingual_string_input import MultilingualStringInput
from .operating_hours_g_input import OperatingHoursGInput
from .organisation_g_input import OrganisationGInput
from .service_facility_type_enum_g_input import ServiceFacilityTypeEnumGInput
from .url_link_input import UrlLinkInput
from .user_type_enum_g_input import UserTypeEnumGInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class SupplementalServiceFacilityInput:
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
    availability: AvailabilityEnumGInput | UnsetValueType = (
        DataclassValidator(AvailabilityEnumGInput),
        Default(UnsetValue),
    )
    quantity: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    regularlyCleaned: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    applicableForUser: list[UserTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(UserTypeEnumGInput)),
        Default(UnsetValue),
    )
    nearby: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    serviceFacilityType: ServiceFacilityTypeEnumGInput = DataclassValidator(ServiceFacilityTypeEnumGInput)
    numberOfSubitems: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    distanceFromOriginFacility: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
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
    afacFacilityObjectExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacSupplementalFacilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacSupplementalServiceFacilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
