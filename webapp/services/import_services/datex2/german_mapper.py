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

from datetime import datetime

from pycountry import countries
from validataclass.helpers import UnsetValue, UnsetValueType

from webapp.models.charging_station import Capability, ServiceType
from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType, ac_1_phase_connector_types
from webapp.models.evse import EvseStatus
from webapp.models.location import ChargingRateUnit
from webapp.services.import_services.datex2.german_realtime.refill_point_status_enum import RefillPointStatusEnum
from webapp.services.import_services.datex2.german_realtime.refill_point_status_g_input import RefillPointStatusGInput
from webapp.services.import_services.datex2.german_static.address_line_type_enum import AddressLineTypeEnum
from webapp.services.import_services.datex2.german_static.authentication_and_identification_enum import (
    AuthenticationAndIdentificationEnum,
)
from webapp.services.import_services.datex2.german_static.authentication_and_identification_enum_g_input import (
    AuthenticationAndIdentificationEnumGInput,
)
from webapp.services.import_services.datex2.german_static.connector_input import ConnectorInput as DatexConnectorInput
from webapp.services.import_services.datex2.german_static.connector_type_enum import ConnectorTypeEnum
from webapp.services.import_services.datex2.german_static.current_type_enum import CurrentTypeEnum
from webapp.services.import_services.datex2.german_static.electric_charging_point_input import (
    ElectricChargingPointInput,
)
from webapp.services.import_services.datex2.german_static.energy_infrastructure_site_input import (
    EnergyInfrastructureSiteInput,
)
from webapp.services.import_services.datex2.german_static.energy_infrastructure_station_input import (
    EnergyInfrastructureStationInput,
)
from webapp.services.import_services.datex2.german_static.external_identifier_input import ExternalIdentifierInput
from webapp.services.import_services.datex2.german_static.multilingual_string_input import MultilingualStringInput
from webapp.services.import_services.datex2.german_static.operating_hours_g_input import OperatingHoursGInput
from webapp.services.import_services.datex2.german_static.organisation_g_input import OrganisationGInput
from webapp.services.import_services.datex2.german_static.point_location_input import PointLocationInput
from webapp.services.import_services.datex2.german_static.refill_point_g_input import RefillPointGInput
from webapp.services.import_services.datex2.german_static.service_type_enum import ServiceTypeEnum
from webapp.services.import_services.datex2.german_static.service_type_input import ServiceTypeInput
from webapp.services.import_services.datex2.german_static.type_of_identifier_enum import TypeOfIdentifierEnum
from webapp.services.import_services.datex2.german_static.type_of_identifier_enum_extension_type_g import (
    TypeOfIdentifierEnumExtensionTypeG,
)
from webapp.services.import_services.models import (
    BusinessUpdate,
    ChargingStationUpdate,
    ConnectorUpdate,
    EnergyMixUpdate,
    EvseRealtimeUpdate,
    EvseUpdate,
    LocationUpdate,
    MaxPowerUpdate,
)


class GermanStaticDatexMapper:
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
            lat=energy_infrastructure_site.locationReference.locAreaLocation.coordinatesForDisplay.latitude,
            lon=energy_infrastructure_site.locationReference.locAreaLocation.coordinatesForDisplay.longitude,
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
        if energy_infrastructure_site.energyInfrastructureStation is not UnsetValue:
            for station in energy_infrastructure_site.energyInfrastructureStation:
                self._apply_energy_infrastructure_stations(station, location)

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
    ):
        if energy_infrastructure_station.refillPoint is UnsetValue:
            return

        charge_station = ChargingStationUpdate(
            uid=energy_infrastructure_station.idG,
            last_updated=energy_infrastructure_station.lastUpdated or location.last_updated,
            evses=[],
            max_power=MaxPowerUpdate(
                unit=ChargingRateUnit.KW,
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

        location.charging_pool.append(charge_station)

        for refill_point in energy_infrastructure_station.refillPoint:
            self._apply_refill_point(refill_point, charge_station, location)

    def _apply_refill_point(
        self, refill_point: RefillPointGInput, charge_station: ChargingStationUpdate, location: LocationUpdate
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

    def _apply_connector(
        self, connector_input: DatexConnectorInput, i: int, charging_point: ElectricChargingPointInput, evse: EvseUpdate
    ):
        standard = self._map_standard(connector_input.connectorType.value)
        power_type = self._map_power_type(charging_point.currentType.value, standard)

        max_electric_power = int(connector_input.maxPowerAtSocket * 1000)
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
            max_electric_power = int(charging_point.availableChargingPower[0] * 1000)

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
    def _map_standard(connector_type: ConnectorTypeEnum) -> ConnectorType | UnsetValueType:
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
        }.get(connector_type, UnsetValue)

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

        last_updated = None
        if refill_point_status.lastUpdated is not UnsetValue:
            last_updated = datetime.fromisoformat(refill_point_status.lastUpdated)

        return EvseRealtimeUpdate(
            uid=refill_point_status.reference.idG,
            evse_id=refill_point_status.reference.idG,
            status=status,
            last_updated=last_updated,
        )

    @staticmethod
    def get_multilanguage_string(values: MultilingualStringInput | UnsetValueType) -> str | UnsetValueType:
        if values is UnsetValue:
            return UnsetValue

        item = next(iter(values.values), UnsetValue)

        if item is UnsetValue:
            return UnsetValue

        return item.value
