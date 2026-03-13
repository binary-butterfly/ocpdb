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
    StringValidator,
)

from .accessibility_enum_g_input import AccessibilityEnumGInput
from .amenities_input import AmenitiesInput
from .charging_mode_enum_g_input import ChargingModeEnumGInput
from .charging_point_usage_type_enum_g_input import ChargingPointUsageTypeEnumGInput
from .connector_input import ConnectorInput
from .current_type_enum_g_input import CurrentTypeEnumGInput
from .dedicated_parking_spaces_input import DedicatedParkingSpacesInput
from .delivery_unit_enum_g_input import DeliveryUnitEnumGInput
from .dimension_input import DimensionInput
from .electric_energy_input import ElectricEnergyInput
from .extension_type_g_input import ExtensionTypeGInput
from .external_identifier_input import ExternalIdentifierInput
from .image_input import ImageInput
from .location_reference_g_input import LocationReferenceGInput
from .multilingual_string_input import MultilingualStringInput
from .operating_hours_g_input import OperatingHoursGInput
from .organisation_g_input import OrganisationGInput
from .reservation_type_enum_g_input import ReservationTypeEnumGInput
from .smart_recharging_services_enum_g_input import SmartRechargingServicesEnumGInput
from .supplemental_facility_g_input import SupplementalFacilityGInput
from .url_link_input import UrlLinkInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput
from .vehicle_to_grid_communication_type_enum_g_input import VehicleToGridCommunicationTypeEnumGInput


@validataclass
class ElectricChargingPointInput:
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
    deliveryUnit: DeliveryUnitEnumGInput = DataclassValidator(DeliveryUnitEnumGInput)
    modelType: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    reservation: ReservationTypeEnumGInput | UnsetValueType = (
        DataclassValidator(ReservationTypeEnumGInput),
        Default(UnsetValue),
    )
    currentType: CurrentTypeEnumGInput = DataclassValidator(CurrentTypeEnumGInput)
    usageType: list[ChargingPointUsageTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ChargingPointUsageTypeEnumGInput)),
        Default(UnsetValue),
    )
    vehicleToGridCommunicationType: list[VehicleToGridCommunicationTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleToGridCommunicationTypeEnumGInput)),
        Default(UnsetValue),
    )
    numberOfConnectors: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    availableVoltage: list[int] | UnsetValueType = ListValidator(FloatValidator()), Default(UnsetValue)
    availableChargingPower: list[int] | UnsetValueType = ListValidator(FloatValidator()), Default(UnsetValue)
    chargingMode: ChargingModeEnumGInput | UnsetValueType = (
        DataclassValidator(ChargingModeEnumGInput),
        Default(UnsetValue),
    )
    smartRechargingServices: list[SmartRechargingServicesEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SmartRechargingServicesEnumGInput)),
        Default(UnsetValue),
    )
    otherSmartRechargingServices: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
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
    connector: list[ConnectorInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ConnectorInput)),
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
    aegiRefillPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    aegiElectricChargingPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
