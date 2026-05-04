"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.accessibility_enum_g_input import AccessibilityEnumGInput
from webapp.shared.datex2.v3_7.shared.amenities_input import AmenitiesInput
from webapp.shared.datex2.v3_7.shared.associated_facility_g_input import AssociatedFacilityGInput
from webapp.shared.datex2.v3_7.shared.charging_mode_enum_g_input import ChargingModeEnumGInput
from webapp.shared.datex2.v3_7.shared.charging_point_usage_type_enum_g_input import ChargingPointUsageTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.connector_input import ConnectorInput
from webapp.shared.datex2.v3_7.shared.current_type_enum_g_input import CurrentTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.delivery_unit_enum_g_input import DeliveryUnitEnumGInput
from webapp.shared.datex2.v3_7.shared.dimension_input import DimensionInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.external_identifier_input import ExternalIdentifierInput
from webapp.shared.datex2.v3_7.shared.image_input import ImageInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_7.shared.reservation_type_enum_g_input import ReservationTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.smart_recharging_services_enum_g_input import SmartRechargingServicesEnumGInput
from webapp.shared.datex2.v3_7.shared.url_link_input import UrlLinkInput
from webapp.shared.datex2.v3_7.shared.vehicle_to_grid_communication_type_enum_g_input import (
    VehicleToGridCommunicationTypeEnumGInput,
)

from .dedicated_parking_spaces_input import DedicatedParkingSpacesInput
from .energy_product_g_input import EnergyProductGInput
from .location_reference_g_input import LocationReferenceGInput
from .organisation_g_input import OrganisationGInput
from .rates_g_input import RatesGInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class ElectricChargingPointInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    alias: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
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
    deliveryUnit: DeliveryUnitEnumGInput = DataclassValidator(DeliveryUnitEnumGInput)
    maximumDeliveryAmount: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    minimumDeliveryAmount: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
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
    availableVoltage: list[float] | UnsetValueType = (
        ListValidator(FloatValidator(allow_integers=True)),
        Default(UnsetValue),
    )
    availableChargingPower: list[float] | UnsetValueType = (
        ListValidator(FloatValidator(allow_integers=True)),
        Default(UnsetValue),
    )
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
    amenities: AmenitiesInput | UnsetValueType = DataclassValidator(AmenitiesInput), Default(UnsetValue)
    dedicatedParkingSpaces: list[DedicatedParkingSpacesInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DedicatedParkingSpacesInput)),
        Default(UnsetValue),
    )
    energyProduct: list[EnergyProductGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyProductGInput)),
        Default(UnsetValue),
    )
    connector: list[ConnectorInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ConnectorInput)),
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
