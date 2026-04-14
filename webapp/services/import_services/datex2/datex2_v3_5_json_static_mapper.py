"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from decimal import Decimal

from pycountry import countries
from validataclass.helpers import UnsetValue, UnsetValueType

from webapp.models.charging_station import Capability, ServiceType
from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType, ac_1_phase_connector_types
from webapp.models.enums import TariffAudience, TariffDimensionType, TariffType, VehicleCategoryEnum
from webapp.models.evse import EvseStatus
from webapp.models.location import ChargingRateUnit
from webapp.services.import_services.models import (
    BusinessUpdate,
    ChargingStationUpdate,
    ConnectorUpdate,
    EnergyMixUpdate,
    EvseRealtimeUpdate,
    EvseUpdate,
    LocationUpdate,
    MaxPowerUpdate,
    ParkingSpaceUpdate,
    PriceComponentUpdate,
    RestrictionsUpdate,
    TariffAssociationUpdate,
    TariffElementUpdate,
    TariffUpdate,
    TaxPercentageUpdate,
)
from webapp.shared.datex2.v3_5_json_realtime.models.refill_point_status_enum import RefillPointStatusEnum
from webapp.shared.datex2.v3_5_json_realtime.models.refill_point_status_g_input import RefillPointStatusGInput
from webapp.shared.datex2.v3_5_json_static.models.accessibility_enum import AccessibilityEnum
from webapp.shared.datex2.v3_5_json_static.models.address_line_type_enum import AddressLineTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.amenities_input import AmenitiesInput
from webapp.shared.datex2.v3_5_json_static.models.authentication_and_identification_enum import (
    AuthenticationAndIdentificationEnum,
)
from webapp.shared.datex2.v3_5_json_static.models.authentication_and_identification_enum_g_input import (
    AuthenticationAndIdentificationEnumGInput,
)
from webapp.shared.datex2.v3_5_json_static.models.connector_input import ConnectorInput as DatexConnectorInput
from webapp.shared.datex2.v3_5_json_static.models.connector_type_enum import ConnectorTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.current_type_enum import CurrentTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.dedicated_parking_spaces_input import DedicatedParkingSpacesInput
from webapp.shared.datex2.v3_5_json_static.models.electric_charging_point_input import (
    ElectricChargingPointInput,
)
from webapp.shared.datex2.v3_5_json_static.models.energy_infrastructure_site_input import (
    EnergyInfrastructureSiteInput,
)
from webapp.shared.datex2.v3_5_json_static.models.energy_infrastructure_station_input import (
    EnergyInfrastructureStationInput,
)
from webapp.shared.datex2.v3_5_json_static.models.energy_rate_input import EnergyRateInput
from webapp.shared.datex2.v3_5_json_static.models.eu_vehicle_category_enum import EuVehicleCategoryEnum
from webapp.shared.datex2.v3_5_json_static.models.external_identifier_input import ExternalIdentifierInput
from webapp.shared.datex2.v3_5_json_static.models.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_5_json_static.models.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_5_json_static.models.organisation_g_input import OrganisationGInput
from webapp.shared.datex2.v3_5_json_static.models.point_location_input import PointLocationInput
from webapp.shared.datex2.v3_5_json_static.models.price_type_enum import PriceTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.rate_policy_enum import RatePolicyEnum
from webapp.shared.datex2.v3_5_json_static.models.refill_point_g_input import RefillPointGInput
from webapp.shared.datex2.v3_5_json_static.models.service_type_enum import ServiceTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.service_type_input import ServiceTypeInput
from webapp.shared.datex2.v3_5_json_static.models.type_of_identifier_enum import TypeOfIdentifierEnum
from webapp.shared.datex2.v3_5_json_static.models.type_of_identifier_enum_extension_type_g import (
    TypeOfIdentifierEnumExtensionTypeG,
)


class Datex2V35JSONStaticMapper:
    _rate_policy_map: dict[RatePolicyEnum, TariffType] = {
        RatePolicyEnum.ADHOC: TariffType.AD_HOC_PAYMENT,
        RatePolicyEnum.CONTRACT: TariffType.REGULAR,
    }

    _rate_policy_audience_map: dict[RatePolicyEnum, TariffAudience] = {
        RatePolicyEnum.ADHOC: TariffAudience.AD_HOC_PAYMENT,
        RatePolicyEnum.CONTRACT: TariffAudience.EMSP_CONTRACT,
    }

    _price_type_map: dict[PriceTypeEnum, TariffDimensionType] = {
        PriceTypeEnum.PRICEPERKWH: TariffDimensionType.ENERGY,
        PriceTypeEnum.PRICEPERMINUTE: TariffDimensionType.TIME,
        PriceTypeEnum.BASEPRICE: TariffDimensionType.FLAT,
        PriceTypeEnum.FLATRATE: TariffDimensionType.FLAT,
    }

    def map_energy_infrastructure_site_to_location(
        self,
        source: str,
        energy_infrastructure_site: EnergyInfrastructureSiteInput,
    ) -> LocationUpdate | None:
        # Check if all lot/lon required fields are present
        if not energy_infrastructure_site.locationReference:
            return None
        if not energy_infrastructure_site.locationReference.locAreaLocation:
            return None
        if not energy_infrastructure_site.locationReference.locAreaLocation.coordinatesForDisplay:
            return None

        # Check if all address required fields are present
        if not energy_infrastructure_site.locationReference.locPointLocation.locLocationExtensionG:
            return None
        if not energy_infrastructure_site.locationReference.locPointLocation.locLocationExtensionG.FacilityLocation:
            return None
        if not energy_infrastructure_site.locationReference.locPointLocation.locLocationExtensionG.FacilityLocation.address:
            return None
        if not energy_infrastructure_site.locationReference.locPointLocation.locLocationExtensionG.FacilityLocation.address.addressLine:
            return None

        location = LocationUpdate(
            source=source,
            uid=energy_infrastructure_site.idG,
            lat=Decimal(energy_infrastructure_site.locationReference.locAreaLocation.coordinatesForDisplay.latitude),
            lon=Decimal(energy_infrastructure_site.locationReference.locAreaLocation.coordinatesForDisplay.longitude),
            time_zone='Europe/Berlin',
            charging_pool=[],
        )

        name = self.get_multilanguage_string(energy_infrastructure_site.name)
        if name is not UnsetValue:
            location.name = name
        if energy_infrastructure_site.lastUpdated is not UnsetValue:
            location.last_updated = energy_infrastructure_site.lastUpdated

        self._apply_point_location(energy_infrastructure_site.locationReference.locPointLocation, location)
        self._apply_operator(energy_infrastructure_site.operator, location)
        self._apply_operating_hours(energy_infrastructure_site.operatingHours, location)
        self._apply_helpdesk(energy_infrastructure_site.helpdesk, location)
        location.parking_spaces = self._map_dedicated_parking_spaces(
            energy_infrastructure_site.dedicatedParkingSpaces,
            energy_infrastructure_site.amenities,
        )
        if energy_infrastructure_site.energyInfrastructureStation is not UnsetValue:
            for station in energy_infrastructure_site.energyInfrastructureStation:
                self._apply_energy_infrastructure_stations(station, location, source)

        return location

    def _apply_point_location(self, point_location: PointLocationInput | UnsetValueType, location: LocationUpdate):
        if point_location is UnsetValue:
            return

        address_fragments: list[str] = []
        for address_line in point_location.locLocationExtensionG.FacilityLocation.address.addressLine:
            if address_line.type.value == AddressLineTypeEnum.STREET:
                address_fragments.append(self.get_multilanguage_string(address_line.text))
            elif address_line.type.value == AddressLineTypeEnum.HOUSENUMBER:
                address_fragments.append(self.get_multilanguage_string(address_line.text))
        location.address = ' '.join(address_fragments)

        location.postal_code = point_location.locLocationExtensionG.FacilityLocation.address.postcode
        location.city = self.get_multilanguage_string(
            point_location.locLocationExtensionG.FacilityLocation.address.city,
        )
        if point_location.locLocationExtensionG.FacilityLocation.address.countryCode:
            location.country = countries.get(
                alpha_2=point_location.locLocationExtensionG.FacilityLocation.address.countryCode,
            ).alpha_3

        location.time_zone = point_location.locLocationExtensionG.FacilityLocation.timeZone or 'Europe/Berlin'

    def _apply_operator(self, organization: OrganisationGInput | UnsetValueType, location: LocationUpdate):
        if organization is UnsetValue:
            return
        if organization.afacAnOrganisation is UnsetValue:
            return
        location.operator = BusinessUpdate(
            name=self.get_multilanguage_string(organization.afacAnOrganisation.name),
            emobility_uid=self._get_external_identifier(
                organization.afacAnOrganisation.externalIdentifier,
                TypeOfIdentifierEnumExtensionTypeG.OPERATORID,
            ),
        )

    @staticmethod
    def _get_external_identifier(
        external_identifiers: list[ExternalIdentifierInput] | UnsetValueType,
        identifier_type: TypeOfIdentifierEnumExtensionTypeG,
    ) -> str | None:
        if external_identifiers is UnsetValue:
            return None
        for external_identifier in external_identifiers:
            if external_identifier.typeOfIdentifier is UnsetValue:
                continue
            if external_identifier.typeOfIdentifier.value != TypeOfIdentifierEnum.EXTENDEDG:
                continue
            if external_identifier.typeOfIdentifier.extendedValueG is UnsetValue:
                continue
            if external_identifier.typeOfIdentifier.extendedValueG == identifier_type:
                return external_identifier.identifier
        return None

    def _apply_operating_hours(self, operating_hours: OperatingHoursGInput | UnsetValueType, location: LocationUpdate):
        if operating_hours is UnsetValue:
            return
        if operating_hours.afacOpenAllHours is not UnsetValue:
            location.twentyfourseven = True

    def _apply_helpdesk(self, helpdesk: OrganisationGInput | UnsetValueType, location: LocationUpdate):
        if helpdesk is UnsetValue:
            return
        if helpdesk.afacReferenceableOrganisation is UnsetValue:
            return
        if helpdesk.afacReferenceableOrganisation.organisationUnit is UnsetValue:
            return
        for unit in helpdesk.afacReferenceableOrganisation.organisationUnit:
            if unit.contactInformation is UnsetValue:
                continue
            for contact_info in unit.contactInformation:
                if contact_info.afacContactInformation is UnsetValue:
                    continue
                if contact_info.afacContactInformation.telephoneNumber is not UnsetValue:
                    location.help_phone = contact_info.afacContactInformation.telephoneNumber
                    return

    def _apply_energy_infrastructure_stations(
        self,
        energy_infrastructure_station: EnergyInfrastructureStationInput,
        location: LocationUpdate,
        source: str,
    ):
        if energy_infrastructure_station.refillPoint is UnsetValue:
            return

        charge_station = ChargingStationUpdate(
            uid=energy_infrastructure_station.idG,
            last_updated=energy_infrastructure_station.lastUpdated or location.last_updated,
            evses=[],
            max_power=MaxPowerUpdate(
                unit=ChargingRateUnit.W,
                value=energy_infrastructure_station.totalMaximumPower,
            ),
        )

        charge_station.name = self.get_multilanguage_string(energy_infrastructure_station.name)
        charge_station.capabilities = self._map_capabilities(
            energy_infrastructure_station.authenticationAndIdentificationMethods,
        )
        charge_station.service_type = self._map_service_type(energy_infrastructure_station.serviceType)
        if (
            energy_infrastructure_station.userInterfaceLanguage is not UnsetValue
            and energy_infrastructure_station.userInterfaceLanguage
        ):
            charge_station.user_interface_languages = energy_infrastructure_station.userInterfaceLanguage

        charge_station.parking_spaces = self._map_dedicated_parking_spaces(
            energy_infrastructure_station.dedicatedParkingSpaces,
            energy_infrastructure_station.amenities,
        )

        location.charging_pool.append(charge_station)

        for refill_point in energy_infrastructure_station.refillPoint:
            self._apply_refill_point(refill_point, charge_station, location, source)

    def _apply_refill_point(
        self,
        refill_point: RefillPointGInput,
        charge_station: ChargingStationUpdate,
        location: LocationUpdate,
        source: str,
    ):
        if refill_point.aegiElectricChargingPoint is UnsetValue:
            return

        evse = EvseUpdate(
            uid=refill_point.aegiElectricChargingPoint.idG,
            evse_id=refill_point.aegiElectricChargingPoint.idG,
            last_updated=refill_point.aegiElectricChargingPoint.lastUpdated or charge_station.last_updated,
            connectors=[],
        )
        charge_station.evses.append(evse)

        self._apply_energy_mix(refill_point.aegiElectricChargingPoint, location)

        if refill_point.aegiElectricChargingPoint.connector is UnsetValue:
            return

        evse.connectors = []
        for i, connector in enumerate(refill_point.aegiElectricChargingPoint.connector):
            self._apply_connector(connector, i, refill_point.aegiElectricChargingPoint, evse)

        self._apply_energy_rates(refill_point.aegiElectricChargingPoint, evse, source)

    def _apply_connector(
        self,
        connector_input: DatexConnectorInput,
        i: int,
        charging_point: ElectricChargingPointInput,
        evse: EvseUpdate,
    ):
        standard = self._map_standard(connector_input.connectorType.value)
        power_type = self._map_power_type(charging_point.currentType.value, standard)

        max_electric_power = int(connector_input.maxPowerAtSocket)
        max_voltage = int(connector_input.voltage) if connector_input.voltage is not UnsetValue else None
        max_amperage = int(connector_input.maximumCurrent) if connector_input.maximumCurrent is not UnsetValue else None

        if (
            max_voltage is None
            and charging_point.availableVoltage is not UnsetValue
            and charging_point.availableVoltage
        ):
            max_voltage = int(charging_point.availableVoltage[0])

        if max_electric_power == 0 and (
            charging_point.availableChargingPower is not UnsetValue and charging_point.availableChargingPower
        ):
            max_electric_power = int(charging_point.availableChargingPower[0])

        if max_amperage is None and max_voltage and max_electric_power:
            max_amperage = int(max_electric_power / max_voltage)

        connector = ConnectorUpdate(
            uid=str(i),
            standard=standard,
            format=ConnectorFormat.CABLE if power_type == PowerType.DC else ConnectorFormat.SOCKET,
            power_type=power_type,
            max_electric_power=max_electric_power,
            max_voltage=max_voltage,
            max_amperage=max_amperage,
            last_updated=charging_point.lastUpdated or evse.last_updated,
        )
        evse.connectors.append(connector)

    def _apply_energy_mix(self, charging_point: ElectricChargingPointInput, location: LocationUpdate):
        if charging_point.electricEnergy is UnsetValue:
            return
        for electric_energy in charging_point.electricEnergy:
            if electric_energy.isGreenEnergy is not UnsetValue:
                if location.energy_mix is None:
                    location.energy_mix = EnergyMixUpdate(is_green_energy=electric_energy.isGreenEnergy)
                else:
                    location.energy_mix.is_green_energy = electric_energy.isGreenEnergy
                return

    def _apply_energy_rates(
        self,
        charging_point: ElectricChargingPointInput,
        evse: EvseUpdate,
        source: str,
    ):
        if charging_point.electricEnergy is UnsetValue:
            return
        for electric_energy in charging_point.electricEnergy:
            if electric_energy.energyRate is UnsetValue:
                continue
            for energy_rate in electric_energy.energyRate:
                tariff_uid = f'{evse.uid}:{energy_rate.idG}'
                tariff_update = self._map_energy_rate(energy_rate, tariff_uid, source)

                audience = self._rate_policy_audience_map.get(energy_rate.ratePolicy.value)

                evse.tariff_association = [
                    TariffAssociationUpdate(
                        uid=tariff_uid,
                        source=source,
                        audience=audience,
                        start_date_time=energy_rate.lastUpdated,
                        last_updated=energy_rate.lastUpdated,
                        tariff=tariff_update,
                    )
                ]

    def _map_energy_rate(self, energy_rate: EnergyRateInput, tariff_uid: str, source: str) -> TariffUpdate:
        tariff_type = self._rate_policy_map.get(energy_rate.ratePolicy.value)
        currency = energy_rate.applicableCurrency[0] if energy_rate.applicableCurrency else None

        tariff_elements: list[TariffElementUpdate] = []
        if energy_rate.energyPrice is not UnsetValue:
            for energy_price in energy_rate.energyPrice:
                price_component = PriceComponentUpdate(
                    type=self._price_type_map.get(energy_price.priceType.value),
                    price=Decimal(round(energy_price.value, 4)),
                )
                if energy_price.taxRate is not UnsetValue:
                    price_component.taxes = [
                        TaxPercentageUpdate(
                            name='VAT',
                            percentage=Decimal(energy_price.taxRate),
                        ),
                    ]

                tariff_element = TariffElementUpdate(
                    price_components=[price_component],
                )

                if energy_price.timeBasedApplicability is not UnsetValue and (
                    energy_price.timeBasedApplicability.fromMinute is not UnsetValue
                    or energy_price.timeBasedApplicability.toMinute is not UnsetValue
                ):
                    restriction = RestrictionsUpdate()
                    if energy_price.timeBasedApplicability.fromMinute is not UnsetValue:
                        restriction.min_duration = int(energy_price.timeBasedApplicability.fromMinute * 60)
                    if energy_price.timeBasedApplicability.toMinute is not UnsetValue:
                        restriction.max_duration = int(energy_price.timeBasedApplicability.toMinute * 60)

                    tariff_element.restrictions = restriction

                tariff_elements.append(tariff_element)

        return TariffUpdate(
            uid=tariff_uid,
            source=source,
            currency=currency,
            type=tariff_type,
            last_updated=energy_rate.lastUpdated,
            elements=tariff_elements,
        )

    _authentication_to_capability_map: dict[AuthenticationAndIdentificationEnum, Capability] = {
        AuthenticationAndIdentificationEnum.CREDITCARD: Capability.CREDIT_CARD_PAYABLE,
        AuthenticationAndIdentificationEnum.DEBITCARD: Capability.DEBIT_CARD_PAYABLE,
        AuthenticationAndIdentificationEnum.MIFARECLASSIC: Capability.RFID_READER,
        AuthenticationAndIdentificationEnum.MIFAREDESFIRE: Capability.RFID_READER,
        AuthenticationAndIdentificationEnum.RFID: Capability.RFID_READER,
        AuthenticationAndIdentificationEnum.ACTIVERFIDCHIP: Capability.RFID_READER,
        AuthenticationAndIdentificationEnum.NFC: Capability.CONTACTLESS_CARD_SUPPORT,
        AuthenticationAndIdentificationEnum.OVERTHEAIR: Capability.REMOTE_START_STOP_CAPABLE,
        AuthenticationAndIdentificationEnum.APPS: Capability.REMOTE_START_STOP_CAPABLE,
        AuthenticationAndIdentificationEnum.PLC: Capability.IEC15118,
        AuthenticationAndIdentificationEnum.CASHPAYMENT: Capability.CASH,
        AuthenticationAndIdentificationEnum.PINPAD: Capability.PED_TERMINAL,
        AuthenticationAndIdentificationEnum.CALYPSO: Capability.CHIP_CARD_SUPPORT,
    }

    @classmethod
    def _map_capabilities(
        cls,
        methods: list[AuthenticationAndIdentificationEnumGInput] | UnsetValueType,
    ) -> list[Capability] | None:
        if methods is UnsetValue:
            return None
        capabilities: set[Capability] = set()
        for method in methods:
            capability = cls._authentication_to_capability_map.get(method.value)
            if capability is not None:
                capabilities.add(capability)
        return sorted(capabilities, key=lambda c: c.value) if capabilities else None

    _service_type_map: dict[ServiceTypeEnum, ServiceType] = {
        ServiceTypeEnum.PHYSICALATTENDANCE: ServiceType.PHYSICAL_ATTENDANCE,
        ServiceTypeEnum.UNATTENDED: ServiceType.UNATTENDED,
    }

    @classmethod
    def _map_service_type(cls, service_types: list[ServiceTypeInput]) -> ServiceType | None:
        for service_type_input in service_types:
            service_type = cls._service_type_map.get(service_type_input.serviceType.value)
            if service_type is not None:
                return service_type
        return None

    _eu_vehicle_category_map: dict[EuVehicleCategoryEnum, VehicleCategoryEnum] = {
        EuVehicleCategoryEnum.L1: VehicleCategoryEnum.L1,
        EuVehicleCategoryEnum.L2: VehicleCategoryEnum.L2,
        EuVehicleCategoryEnum.L3: VehicleCategoryEnum.L3,
        EuVehicleCategoryEnum.L4: VehicleCategoryEnum.L4,
        EuVehicleCategoryEnum.L5: VehicleCategoryEnum.L5,
        EuVehicleCategoryEnum.L6: VehicleCategoryEnum.L6,
        EuVehicleCategoryEnum.L7: VehicleCategoryEnum.L7,
        EuVehicleCategoryEnum.M: VehicleCategoryEnum.M,
        EuVehicleCategoryEnum.M1: VehicleCategoryEnum.M1,
        EuVehicleCategoryEnum.M2: VehicleCategoryEnum.M2,
        EuVehicleCategoryEnum.M3: VehicleCategoryEnum.M3,
        EuVehicleCategoryEnum.N: VehicleCategoryEnum.N,
        EuVehicleCategoryEnum.N1: VehicleCategoryEnum.N1,
        EuVehicleCategoryEnum.N1CLASSI: VehicleCategoryEnum.N1,
        EuVehicleCategoryEnum.N1CLASSII: VehicleCategoryEnum.N1,
        EuVehicleCategoryEnum.N1CLASSIII: VehicleCategoryEnum.N1,
        EuVehicleCategoryEnum.N1CLASSIIIANDN2: VehicleCategoryEnum.N1,
        EuVehicleCategoryEnum.N2: VehicleCategoryEnum.N2,
        EuVehicleCategoryEnum.N3: VehicleCategoryEnum.N3,
        EuVehicleCategoryEnum.O: VehicleCategoryEnum.O,
        EuVehicleCategoryEnum.O1: VehicleCategoryEnum.O1,
        EuVehicleCategoryEnum.O2: VehicleCategoryEnum.O2,
        EuVehicleCategoryEnum.O3: VehicleCategoryEnum.O3,
        EuVehicleCategoryEnum.O4: VehicleCategoryEnum.O4,
        EuVehicleCategoryEnum.R1: VehicleCategoryEnum.R1,
        EuVehicleCategoryEnum.R2: VehicleCategoryEnum.R2,
        EuVehicleCategoryEnum.R3: VehicleCategoryEnum.R3,
        EuVehicleCategoryEnum.R4: VehicleCategoryEnum.R4,
        EuVehicleCategoryEnum.T1: VehicleCategoryEnum.T1,
        EuVehicleCategoryEnum.T2: VehicleCategoryEnum.T2,
        EuVehicleCategoryEnum.T3: VehicleCategoryEnum.T3,
        EuVehicleCategoryEnum.T4: VehicleCategoryEnum.T4,
        EuVehicleCategoryEnum.T41: VehicleCategoryEnum.T41,
        EuVehicleCategoryEnum.T42: VehicleCategoryEnum.T42,
        EuVehicleCategoryEnum.T43: VehicleCategoryEnum.T43,
    }

    _accessible_values: set[AccessibilityEnum] = {
        AccessibilityEnum.BARRIERFREEACCESSIBLE,
        AccessibilityEnum.DISABILITYACCESSIBLE,
        AccessibilityEnum.WHEELCHAIRACCESSIBLE,
    }

    def _map_dedicated_parking_spaces(
        self,
        dedicated_parking_spaces: list[DedicatedParkingSpacesInput] | UnsetValueType,
        station_amenities: AmenitiesInput | UnsetValueType,
    ) -> list[ParkingSpaceUpdate] | None:
        if dedicated_parking_spaces is UnsetValue:
            return None

        result: list[ParkingSpaceUpdate] = []
        for parking_input in dedicated_parking_spaces:
            vehicle_types = self._map_vehicle_types(parking_input)

            parking_space = ParkingSpaceUpdate(
                vehicle_types=vehicle_types,
                parking_space_count=parking_input.numberOfSpaces,
            )

            self._apply_vehicle_dimensions(parking_input, parking_space)
            self._apply_parking_amenities(parking_input.amenities, station_amenities, parking_space)

            if parking_input.accessibility is not UnsetValue:
                for accessibility in parking_input.accessibility:
                    if accessibility.value in self._accessible_values:
                        parking_space.is_accessible = True
                        break

            result.append(parking_space)

        return self._deduplicate_parking_spaces(result) or None

    @staticmethod
    def _deduplicate_parking_spaces(parking_spaces: list[ParkingSpaceUpdate]) -> list[ParkingSpaceUpdate]:
        deduplicated: list[ParkingSpaceUpdate] = []
        for ps in parking_spaces:
            for existing in deduplicated:
                if (
                    existing.vehicle_types == ps.vehicle_types
                    and existing.max_weight == ps.max_weight
                    and existing.max_height == ps.max_height
                    and existing.max_length == ps.max_length
                    and existing.max_width == ps.max_width
                    and existing.has_roof == ps.has_roof
                    and existing.is_illuminated == ps.is_illuminated
                    and existing.is_accessible == ps.is_accessible
                ):
                    existing.parking_space_count += ps.parking_space_count
                    break
            else:
                deduplicated.append(ps)
        return deduplicated

    def _map_vehicle_types(
        self,
        parking_input: DedicatedParkingSpacesInput,
    ) -> list[VehicleCategoryEnum]:
        if parking_input.applicableForVehicles is UnsetValue:
            return []

        vehicle_types: list[VehicleCategoryEnum] = []
        for vehicle_chars in parking_input.applicableForVehicles:
            if vehicle_chars.comVehicleCharacteristicsExtensionG is UnsetValue:
                continue
            extended = vehicle_chars.comVehicleCharacteristicsExtensionG.VehicleCharacteristicsExtended
            if extended is UnsetValue:
                continue
            for eu_category in extended.euVehicleCategory:
                mapped = self._eu_vehicle_category_map.get(eu_category.value)
                if mapped is not None and mapped not in vehicle_types:
                    vehicle_types.append(mapped)

        return vehicle_types

    @staticmethod
    def _apply_vehicle_dimensions(
        parking_input: DedicatedParkingSpacesInput,
        parking_space: ParkingSpaceUpdate,
    ):
        if parking_input.applicableForVehicles is UnsetValue:
            return

        for vehicle_chars in parking_input.applicableForVehicles:
            if vehicle_chars.grossWeightCharacteristic is not UnsetValue:
                for weight in vehicle_chars.grossWeightCharacteristic:
                    parking_space.max_weight = int(weight.grossVehicleWeight * 1000)
                    break

            if vehicle_chars.heightCharacteristic is not UnsetValue:
                for height in vehicle_chars.heightCharacteristic:
                    parking_space.max_height = int(height.vehicleHeight * 100)
                    break

            if vehicle_chars.lengthCharacteristic is not UnsetValue:
                for length in vehicle_chars.lengthCharacteristic:
                    parking_space.max_length = int(length.vehicleLength * 100)
                    break

            if vehicle_chars.widthCharacteristic is not UnsetValue:
                for width in vehicle_chars.widthCharacteristic:
                    parking_space.max_width = int(width.vehicleWidth * 100)
                    break

    @staticmethod
    def _apply_parking_amenities(
        parking_amenities: AmenitiesInput | UnsetValueType,
        station_amenities: AmenitiesInput | UnsetValueType,
        parking_space: ParkingSpaceUpdate,
    ):
        amenities = parking_amenities if parking_amenities is not UnsetValue else station_amenities
        if amenities is UnsetValue:
            return

        if amenities.roofed is not UnsetValue:
            parking_space.has_roof = amenities.roofed
        if amenities.illuminated is not UnsetValue:
            parking_space.is_illuminated = amenities.illuminated

    @staticmethod
    def _map_power_type(current_type: CurrentTypeEnum, standard: ConnectorType):
        if current_type == CurrentTypeEnum.DC:
            return PowerType.DC

        if current_type == CurrentTypeEnum.EXTENDEDG:
            return PowerType.AC_3_PHASE

        if standard in ac_1_phase_connector_types:
            return PowerType.AC_1_PHASE

        return PowerType.AC_3_PHASE

    @staticmethod
    def _map_standard(connector_type: ConnectorTypeEnum) -> ConnectorType | None:
        return {
            ConnectorTypeEnum.CEE3: ConnectorType.IEC_60309_2_single_16,
            ConnectorTypeEnum.CEE5: ConnectorType.IEC_60309_2_three_32,
            ConnectorTypeEnum.CHADEMO: ConnectorType.CHADEMO,
            ConnectorTypeEnum.DOMESTICA: ConnectorType.DOMESTIC_A,
            ConnectorTypeEnum.DOMESTICB: ConnectorType.DOMESTIC_B,
            ConnectorTypeEnum.DOMESTICC: ConnectorType.DOMESTIC_C,
            ConnectorTypeEnum.DOMESTICD: ConnectorType.DOMESTIC_D,
            ConnectorTypeEnum.DOMESTICE: ConnectorType.DOMESTIC_E,
            ConnectorTypeEnum.DOMESTICF: ConnectorType.DOMESTIC_F,
            ConnectorTypeEnum.DOMESTICG: ConnectorType.DOMESTIC_G,
            ConnectorTypeEnum.DOMESTICH: ConnectorType.DOMESTIC_H,
            ConnectorTypeEnum.DOMESTICI: ConnectorType.DOMESTIC_I,
            ConnectorTypeEnum.DOMESTICJ: ConnectorType.DOMESTIC_J,
            ConnectorTypeEnum.DOMESTICK: ConnectorType.DOMESTIC_K,
            ConnectorTypeEnum.DOMESTICL: ConnectorType.DOMESTIC_L,
            ConnectorTypeEnum.IEC60309X2THREE16: ConnectorType.IEC_60309_2_three_16,
            ConnectorTypeEnum.IEC60309X2THREE32: ConnectorType.IEC_60309_2_three_32,
            ConnectorTypeEnum.IEC60309X2THREE64: ConnectorType.IEC_60309_2_three_64,
            ConnectorTypeEnum.IEC60309X2SINGLE16: ConnectorType.IEC_60309_2_single_16,
            ConnectorTypeEnum.IEC62196T1: ConnectorType.IEC_62196_T1,
            ConnectorTypeEnum.IEC62196T1COMBO: ConnectorType.IEC_62196_T1_COMBO,
            ConnectorTypeEnum.IEC62196T2: ConnectorType.IEC_62196_T2,
            ConnectorTypeEnum.IEC62196T2COMBO: ConnectorType.IEC_62196_T2_COMBO,
            ConnectorTypeEnum.PANTOGRAPHBOTTOMUP: ConnectorType.PANTOGRAPH_BOTTOM_UP,
            ConnectorTypeEnum.PANTOGRAPHTOPDOWN: ConnectorType.PANTOGRAPH_TOP_DOWN,
            ConnectorTypeEnum.TESLACONNECTOREUROPE: ConnectorType.TESLA_S,
            ConnectorTypeEnum.TESLACONNECTORAMERICA: ConnectorType.TESLA_S,
            ConnectorTypeEnum.TESLAR: ConnectorType.TESLA_R,
            ConnectorTypeEnum.TESLAS: ConnectorType.TESLA_S,
        }.get(connector_type, None)

    _refill_point_status_map: dict[RefillPointStatusEnum, EvseStatus] = {
        RefillPointStatusEnum.AVAILABLE: EvseStatus.AVAILABLE,
        RefillPointStatusEnum.BLOCKED: EvseStatus.BLOCKED,
        RefillPointStatusEnum.CHARGING: EvseStatus.CHARGING,
        RefillPointStatusEnum.FAULTED: EvseStatus.OUTOFORDER,
        RefillPointStatusEnum.INOPERATIVE: EvseStatus.INOPERATIVE,
        RefillPointStatusEnum.OCCUPIED: EvseStatus.CHARGING,
        RefillPointStatusEnum.OUTOFORDER: EvseStatus.OUTOFORDER,
        RefillPointStatusEnum.OUTOFSTOCK: EvseStatus.OUTOFORDER,
        RefillPointStatusEnum.PLANNED: EvseStatus.PLANNED,
        RefillPointStatusEnum.REMOVED: EvseStatus.REMOVED,
        RefillPointStatusEnum.RESERVED: EvseStatus.RESERVED,
        RefillPointStatusEnum.UNAVAILABLE: EvseStatus.INOPERATIVE,
        RefillPointStatusEnum.UNKNOWN: EvseStatus.UNKNOWN,
    }

    def map_energy_infrastructure_station_status(
        self,
        refill_point_status_g: RefillPointStatusGInput,
    ) -> EvseRealtimeUpdate | None:
        refill_point_status = refill_point_status_g.aegiRefillPointStatus
        if refill_point_status is UnsetValue:
            refill_point_status = refill_point_status_g.aegiElectricChargingPointStatus
        if refill_point_status is UnsetValue:
            return None

        status = self._refill_point_status_map.get(refill_point_status.status.value)
        if status is None:
            return None

        return EvseRealtimeUpdate(
            uid=refill_point_status.reference.idG,
            evse_id=refill_point_status.reference.idG,
            status=status,
            last_updated=None if refill_point_status.lastUpdated is UnsetValue else refill_point_status.lastUpdated,
        )

    @staticmethod
    def get_multilanguage_string(values: MultilingualStringInput | UnsetValueType) -> str | UnsetValueType:
        if values is UnsetValue:
            return UnsetValue

        item = next(iter(values.values), UnsetValue)

        if item is UnsetValue:
            return UnsetValue

        return item.value
