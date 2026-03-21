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

import re
from datetime import datetime, timezone

from pycountry import countries
from validataclass.helpers import UnsetValue

from webapp.models.business import Business
from webapp.models.charging_station import Capability, ChargingStation, ServiceType
from webapp.models.connector import Connector, ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import Evse
from webapp.models.location import Location
from webapp.shared.datex2.v3_5_json_static.address_input import AddressInput
from webapp.shared.datex2.v3_5_json_static.address_line_input import AddressLineInput
from webapp.shared.datex2.v3_5_json_static.address_line_type_enum import AddressLineTypeEnum
from webapp.shared.datex2.v3_5_json_static.address_line_type_enum_g_input import AddressLineTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.an_organisation_input import AnOrganisationInput
from webapp.shared.datex2.v3_5_json_static.area_location_input import AreaLocationInput
from webapp.shared.datex2.v3_5_json_static.authentication_and_identification_enum import (
    AuthenticationAndIdentificationEnum,
)
from webapp.shared.datex2.v3_5_json_static.authentication_and_identification_enum_g_input import (
    AuthenticationAndIdentificationEnumGInput,
)
from webapp.shared.datex2.v3_5_json_static.connector_format_type_enum import ConnectorFormatTypeEnum
from webapp.shared.datex2.v3_5_json_static.connector_format_type_enum_g_input import ConnectorFormatTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.connector_input import ConnectorInput as DatexConnectorInput
from webapp.shared.datex2.v3_5_json_static.connector_type_enum import ConnectorTypeEnum
from webapp.shared.datex2.v3_5_json_static.connector_type_enum_g_input import ConnectorTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.contact_information_g_input import ContactInformationGInput
from webapp.shared.datex2.v3_5_json_static.contact_information_input import ContactInformationInput
from webapp.shared.datex2.v3_5_json_static.current_type_enum import CurrentTypeEnum
from webapp.shared.datex2.v3_5_json_static.current_type_enum_g_input import CurrentTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.d_a_t_e_x_i_i3_d2_payload_input import DATEXII3D2PayloadInput
from webapp.shared.datex2.v3_5_json_static.delivery_unit_enum import DeliveryUnitEnum
from webapp.shared.datex2.v3_5_json_static.delivery_unit_enum_g_input import DeliveryUnitEnumGInput
from webapp.shared.datex2.v3_5_json_static.electric_charging_point_input import ElectricChargingPointInput
from webapp.shared.datex2.v3_5_json_static.electric_energy_input import ElectricEnergyInput
from webapp.shared.datex2.v3_5_json_static.energy_infrastructure_site_input import EnergyInfrastructureSiteInput
from webapp.shared.datex2.v3_5_json_static.energy_infrastructure_station_input import EnergyInfrastructureStationInput
from webapp.shared.datex2.v3_5_json_static.energy_infrastructure_table_input import EnergyInfrastructureTableInput
from webapp.shared.datex2.v3_5_json_static.energy_infrastructure_table_publication_input import (
    EnergyInfrastructureTablePublicationInput,
)
from webapp.shared.datex2.v3_5_json_static.external_identifier_input import ExternalIdentifierInput
from webapp.shared.datex2.v3_5_json_static.facility_location_input import FacilityLocationInput
from webapp.shared.datex2.v3_5_json_static.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_5_json_static.location_extension_type_g_input import LocationExtensionTypeGInput
from webapp.shared.datex2.v3_5_json_static.location_reference_g_input import LocationReferenceGInput
from webapp.shared.datex2.v3_5_json_static.multi_lingual_string_value_input import MultiLingualStringValueInput
from webapp.shared.datex2.v3_5_json_static.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_5_json_static.open_all_hours_input import OpenAllHoursInput
from webapp.shared.datex2.v3_5_json_static.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_5_json_static.organisation_g_input import OrganisationGInput
from webapp.shared.datex2.v3_5_json_static.organisation_unit_input import OrganisationUnitInput
from webapp.shared.datex2.v3_5_json_static.payload_publication_g_input import PayloadPublicationGInput
from webapp.shared.datex2.v3_5_json_static.point_coordinates_input import PointCoordinatesInput
from webapp.shared.datex2.v3_5_json_static.point_location_input import PointLocationInput
from webapp.shared.datex2.v3_5_json_static.referenceable_organisation_input import ReferenceableOrganisationInput
from webapp.shared.datex2.v3_5_json_static.refill_point_g_input import RefillPointGInput
from webapp.shared.datex2.v3_5_json_static.service_type_enum import ServiceTypeEnum
from webapp.shared.datex2.v3_5_json_static.service_type_enum_g_input import ServiceTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.service_type_input import ServiceTypeInput
from webapp.shared.datex2.v3_5_json_static.type_of_identifier_enum import TypeOfIdentifierEnum
from webapp.shared.datex2.v3_5_json_static.type_of_identifier_enum_extension_type_g import (
    TypeOfIdentifierEnumExtensionTypeG,
)
from webapp.shared.datex2.v3_5_json_static.type_of_identifier_enum_g_input import TypeOfIdentifierEnumGInput


class DatexV35JSONStaticExportMapper:
    _connector_type_map: dict[ConnectorType, ConnectorTypeEnum] = {
        ConnectorType.CHADEMO: ConnectorTypeEnum.CHADEMO,
        ConnectorType.DOMESTIC_A: ConnectorTypeEnum.DOMESTICA,
        ConnectorType.DOMESTIC_B: ConnectorTypeEnum.DOMESTICB,
        ConnectorType.DOMESTIC_C: ConnectorTypeEnum.DOMESTICC,
        ConnectorType.DOMESTIC_D: ConnectorTypeEnum.DOMESTICD,
        ConnectorType.DOMESTIC_E: ConnectorTypeEnum.DOMESTICE,
        ConnectorType.DOMESTIC_F: ConnectorTypeEnum.DOMESTICF,
        ConnectorType.DOMESTIC_G: ConnectorTypeEnum.DOMESTICG,
        ConnectorType.DOMESTIC_H: ConnectorTypeEnum.DOMESTICH,
        ConnectorType.DOMESTIC_I: ConnectorTypeEnum.DOMESTICI,
        ConnectorType.DOMESTIC_J: ConnectorTypeEnum.DOMESTICJ,
        ConnectorType.DOMESTIC_K: ConnectorTypeEnum.DOMESTICK,
        ConnectorType.DOMESTIC_L: ConnectorTypeEnum.DOMESTICL,
        ConnectorType.IEC_60309_2_single_16: ConnectorTypeEnum.IEC60309X2SINGLE16,
        ConnectorType.IEC_60309_2_three_16: ConnectorTypeEnum.IEC60309X2THREE16,
        ConnectorType.IEC_60309_2_three_32: ConnectorTypeEnum.IEC60309X2THREE32,
        ConnectorType.IEC_60309_2_three_64: ConnectorTypeEnum.IEC60309X2THREE64,
        ConnectorType.IEC_62196_T1: ConnectorTypeEnum.IEC62196T1,
        ConnectorType.IEC_62196_T1_COMBO: ConnectorTypeEnum.IEC62196T1COMBO,
        ConnectorType.IEC_62196_T2: ConnectorTypeEnum.IEC62196T2,
        ConnectorType.IEC_62196_T2_COMBO: ConnectorTypeEnum.IEC62196T2COMBO,
        ConnectorType.IEC_62196_T3A: ConnectorTypeEnum.IEC62196T3A,
        ConnectorType.IEC_62196_T3C: ConnectorTypeEnum.IEC62196T3C,
        ConnectorType.PANTOGRAPH_BOTTOM_UP: ConnectorTypeEnum.PANTOGRAPHBOTTOMUP,
        ConnectorType.PANTOGRAPH_TOP_DOWN: ConnectorTypeEnum.PANTOGRAPHTOPDOWN,
        ConnectorType.TESLA_R: ConnectorTypeEnum.TESLAR,
        ConnectorType.TESLA_S: ConnectorTypeEnum.TESLAS,
    }

    _capability_to_auth_method_map: dict[Capability, AuthenticationAndIdentificationEnum] = {
        Capability.CREDIT_CARD_PAYABLE: AuthenticationAndIdentificationEnum.CREDITCARD,
        Capability.DEBIT_CARD_PAYABLE: AuthenticationAndIdentificationEnum.DEBITCARD,
        Capability.RFID_READER: AuthenticationAndIdentificationEnum.RFID,
        Capability.CONTACTLESS_CARD_SUPPORT: AuthenticationAndIdentificationEnum.NFC,
        Capability.REMOTE_START_STOP_CAPABLE: AuthenticationAndIdentificationEnum.OVERTHEAIR,
        Capability.IEC15118: AuthenticationAndIdentificationEnum.PLC,
        Capability.CASH: AuthenticationAndIdentificationEnum.CASHPAYMENT,
        Capability.PED_TERMINAL: AuthenticationAndIdentificationEnum.PINPAD,
        Capability.CHIP_CARD_SUPPORT: AuthenticationAndIdentificationEnum.CALYPSO,
    }

    _service_type_map: dict[ServiceType, ServiceTypeEnum] = {
        ServiceType.PHYSICAL_ATTENDANCE: ServiceTypeEnum.PHYSICALATTENDANCE,
        ServiceType.UNATTENDED: ServiceTypeEnum.UNATTENDED,
    }

    _power_type_to_current_type_map: dict[PowerType, CurrentTypeEnum] = {
        PowerType.DC: CurrentTypeEnum.DC,
        PowerType.AC_1_PHASE: CurrentTypeEnum.AC,
        PowerType.AC_3_PHASE: CurrentTypeEnum.AC,
    }

    _connector_format_map: dict[ConnectorFormat, ConnectorFormatTypeEnum] = {
        ConnectorFormat.SOCKET: ConnectorFormatTypeEnum.SOCKET,
        ConnectorFormat.CABLE: ConnectorFormatTypeEnum.CABLEMODE3,
    }

    def map_locations_to_static_payload(self, locations: list[Location]) -> DATEXII3D2PayloadInput:
        now = datetime.now(tz=timezone.utc).isoformat()

        sites = []
        for location in locations:
            site = self._map_location_to_site(location)
            if site is not None:
                sites.append(site)

        payload = PayloadPublicationGInput(
            modelBaseVersionG='3',
            versionG='3.5',
            profileNameG='Afir Energy Infrastructure',
            profileVersionG='01-00-00',
            aegiEnergyInfrastructureTablePublication=EnergyInfrastructureTablePublicationInput(
                lang='de',
                publicationTime=now,
                publicationCreator=InternationalIdentifierInput(
                    country='DE',
                    nationalIdentifier='OCPDB',
                ),
                energyInfrastructureTable=[
                    EnergyInfrastructureTableInput(
                        idG='1',
                        versionG='1',
                        energyInfrastructureSite=sites,
                    ),
                ],
            ),
        )
        return DATEXII3D2PayloadInput(payload=payload)

    def _map_location_to_site(self, location: Location) -> EnergyInfrastructureSiteInput | None:
        if location.lat is None or location.lon is None:
            return None

        version_g = location.last_updated.isoformat()

        location_reference = self._build_site_location_reference(location)

        stations = []
        for charging_station in location.charging_pool:
            station = self._map_charging_station_to_station(charging_station, location)
            stations.append(station)

        site = EnergyInfrastructureSiteInput(
            idG=location.uid,
            versionG=version_g,
            locationReference=location_reference,
            energyInfrastructureStation=stations,
        )

        if location.name:
            site.additionalInformation = [self._build_multilingual_string(location.name)]

        if location.twentyfourseven:
            site.operatingHours = OperatingHoursGInput(afacOpenAllHours=OpenAllHoursInput())

        if location.operator:
            site.operator = self._build_operator(location.operator)

        if location.help_phone:
            site.helpdesk = self._build_helpdesk(location.help_phone, version_g, location.operator)

        return site

    def _map_charging_station_to_station(
        self,
        charging_station: ChargingStation,
        location: Location,
    ) -> EnergyInfrastructureStationInput:
        version_g = charging_station.last_updated.isoformat()

        refill_points = []
        for evse in charging_station.evses:
            refill_point = self._map_evse_to_refill_point(evse, location)
            refill_points.append(refill_point)

        service_type_list = []
        if charging_station.service_type:
            datex_service_type = self._service_type_map.get(charging_station.service_type)
            if datex_service_type:
                service_type_list = [
                    ServiceTypeInput(serviceType=ServiceTypeEnumGInput(value=datex_service_type)),
                ]

        station = EnergyInfrastructureStationInput(
            idG=charging_station.uid,
            versionG=version_g,
            numberOfRefillPoints=len(charging_station.evses),
            totalMaximumPower=charging_station.max_power_value
            if charging_station.max_power_value is not None
            else UnsetValue,
            serviceType=service_type_list,
            refillPoint=refill_points,
        )

        if charging_station.lat and charging_station.lon:
            station.locationReference = self._build_station_location_reference(location)

        capabilities = charging_station.capabilities
        if capabilities:
            auth_methods = self._map_capabilities_to_auth_methods(capabilities)
            if auth_methods:
                station.authenticationAndIdentificationMethods = auth_methods

        if charging_station.user_interface_languages:
            station.userInterfaceLanguage = charging_station.user_interface_languages

        return station

    def _map_evse_to_refill_point(self, evse: Evse, location: Location) -> RefillPointGInput:
        version_g = evse.last_updated.isoformat()

        current_type = CurrentTypeEnum.AC
        if evse.connectors:
            first_connector = evse.connectors[0]
            if first_connector.power_type:
                current_type = self._power_type_to_current_type_map.get(first_connector.power_type, CurrentTypeEnum.AC)

        datex_connectors = []
        voltages = []
        powers = []
        for connector in evse.connectors:
            datex_connector = self._map_connector(connector)
            if datex_connector is not None:
                datex_connectors.append(datex_connector)
            if connector.max_voltage:
                voltages.append(float(connector.max_voltage))
            if connector.max_electric_power:
                powers.append(connector.max_electric_power / 1000.0)

        charging_point = ElectricChargingPointInput(
            idG=evse.uid,
            versionG=version_g,
            deliveryUnit=DeliveryUnitEnumGInput(value=DeliveryUnitEnum.KWH),
            currentType=CurrentTypeEnumGInput(value=current_type),
            numberOfConnectors=len(evse.connectors),
            connector=datex_connectors,
        )

        if voltages:
            charging_point.availableVoltage = voltages

        if powers:
            charging_point.availableChargingPower = powers

        if location.energy_mix and location.energy_mix.get('is_green_energy') is not None:
            charging_point.electricEnergy = [
                ElectricEnergyInput(isGreenEnergy=location.energy_mix['is_green_energy']),
            ]

        return RefillPointGInput(aegiElectricChargingPoint=charging_point)

    def _map_connector(self, connector: Connector) -> DatexConnectorInput | None:
        if connector.standard is None:
            return None

        connector_type_enum = self._connector_type_map.get(connector.standard)
        max_power_kw = (connector.max_electric_power / 1000.0) if connector.max_electric_power else 0.0

        datex_connector = DatexConnectorInput(
            connectorType=ConnectorTypeEnumGInput(value=connector_type_enum) if connector_type_enum else UnsetValue,
            maxPowerAtSocket=max_power_kw,
        )

        if connector.max_voltage:
            datex_connector.voltage = float(connector.max_voltage)

        if connector.max_amperage:
            datex_connector.maximumCurrent = float(connector.max_amperage)

        if connector.format:
            format_enum = self._connector_format_map.get(connector.format)
            if format_enum:
                datex_connector.connectorFormat = ConnectorFormatTypeEnumGInput(value=format_enum)

        return datex_connector

    def _build_site_location_reference(self, location: Location) -> LocationReferenceGInput:
        coordinates = PointCoordinatesInput(
            latitude=float(location.lat),
            longitude=float(location.lon),
        )

        return LocationReferenceGInput(
            locAreaLocation=AreaLocationInput(coordinatesForDisplay=coordinates),
            locPointLocation=PointLocationInput(
                locLocationExtensionG=LocationExtensionTypeGInput(
                    FacilityLocation=self._build_facility_location(location),
                ),
            ),
        )

    def _build_station_location_reference(self, charging_station: ChargingStation) -> LocationReferenceGInput:
        coordinates = PointCoordinatesInput(
            latitude=float(charging_station.lat),
            longitude=float(charging_station.lon),
        )

        return LocationReferenceGInput(
            locPointLocation=PointLocationInput(
                coordinatesForDisplay=coordinates,
                locLocationExtensionG=LocationExtensionTypeGInput(
                    FacilityLocation=self._build_facility_location(coordinates, include_timezone=True),
                ),
            ),
        )

    def _build_facility_location(
        self,
        location: Location,
        include_timezone: bool = False,
    ) -> FacilityLocationInput:
        address = self._build_address(location)
        facility = FacilityLocationInput(address=address)

        if include_timezone and location.time_zone:
            facility.timeZone = location.time_zone

        return facility

    def _build_address(self, location: Location) -> AddressInput:
        address = AddressInput()

        if location.postal_code:
            address.postcode = location.postal_code

        if location.city:
            address.city = self._build_multilingual_string(location.city)

        if location.country:
            try:
                country = countries.get(alpha_3=location.country)
                if country:
                    address.countryCode = country.alpha_2
            except (KeyError, LookupError):
                pass

        if location.address:
            street, house_number = self._split_address(location.address)
            address_lines = []
            if street:
                address_lines.append(
                    AddressLineInput(
                        order=1,
                        type=AddressLineTypeEnumGInput(value=AddressLineTypeEnum.STREET),
                        text=self._build_multilingual_string(street),
                    )
                )
            if house_number:
                address_lines.append(
                    AddressLineInput(
                        order=2,
                        type=AddressLineTypeEnumGInput(value=AddressLineTypeEnum.HOUSENUMBER),
                        text=self._build_multilingual_string(house_number),
                    )
                )
            if address_lines:
                address.addressLine = address_lines

        return address

    @staticmethod
    def _build_operator(business: Business) -> OrganisationGInput:
        org = AnOrganisationInput(
            name=DatexV35JSONStaticExportMapper._build_multilingual_string(business.name),
        )

        if business.emobility_uid:
            org.externalIdentifier = [
                ExternalIdentifierInput(
                    identifier=business.emobility_uid,
                    typeOfIdentifier=TypeOfIdentifierEnumGInput(
                        value=TypeOfIdentifierEnum.EXTENDEDG,
                        extendedValueG=TypeOfIdentifierEnumExtensionTypeG.OPERATORID,
                    ),
                ),
            ]

        return OrganisationGInput(afacAnOrganisation=org)

    @staticmethod
    def _build_helpdesk(
        phone: str,
        version_g: str,
        operator: Business | None,
    ) -> OrganisationGInput:
        name = DatexV35JSONStaticExportMapper._build_multilingual_string(operator.name if operator else 'Helpdesk')

        return OrganisationGInput(
            afacReferenceableOrganisation=ReferenceableOrganisationInput(
                idG='HELP',
                versionG=version_g,
                name=name,
                organisationUnit=[
                    OrganisationUnitInput(
                        contactInformation=[
                            ContactInformationGInput(
                                afacContactInformation=ContactInformationInput(
                                    telephoneNumber=phone,
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

    def _map_capabilities_to_auth_methods(
        self,
        capabilities: list[Capability],
    ) -> list[AuthenticationAndIdentificationEnumGInput]:
        methods = []
        for capability in capabilities:
            method = self._capability_to_auth_method_map.get(capability)
            if method:
                methods.append(AuthenticationAndIdentificationEnumGInput(value=method))
        return methods

    @staticmethod
    def _build_multilingual_string(text: str, lang: str = 'de') -> MultilingualStringInput:
        return MultilingualStringInput(
            values=[MultiLingualStringValueInput(lang=lang, value=text)],
        )

    @staticmethod
    def _split_address(address: str) -> tuple[str | None, str | None]:
        if not address:
            return None, None
        match = re.match(r'^(.+)\s+(\d+\S*)$', address)
        if match:
            return match.group(1), match.group(2)
        return address, None
