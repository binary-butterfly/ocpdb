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

from webapp.models.business import Business
from webapp.models.charging_station import Capability, ChargingStation
from webapp.models.connector import Connector, ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import Evse
from webapp.models.location import Location
from webapp.shared.datex2.v3_7.shared.address_line_output import AddressLineOutput
from webapp.shared.datex2.v3_7.shared.address_line_type_enum import AddressLineTypeEnum
from webapp.shared.datex2.v3_7.shared.address_line_type_enum_g_output import AddressLineTypeEnumGOutput
from webapp.shared.datex2.v3_7.shared.address_output import AddressOutput
from webapp.shared.datex2.v3_7.shared.afir_facility_location_output import AfirFacilityLocationOutput
from webapp.shared.datex2.v3_7.shared.international_identifier_output import InternationalIdentifierOutput
from webapp.shared.datex2.v3_7.shared.location_extension_type_g_output import LocationExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.location_reference_g_output import LocationReferenceGOutput
from webapp.shared.datex2.v3_7.shared.multi_lingual_string_value_output import MultiLingualStringValueOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput
from webapp.shared.datex2.v3_7.shared.open_all_hours_output import OpenAllHoursOutput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_output import OperatingHoursGOutput
from webapp.shared.datex2.v3_7.shared.point_by_coordinates_output import PointByCoordinatesOutput
from webapp.shared.datex2.v3_7.shared.point_coordinates_output import PointCoordinatesOutput
from webapp.shared.datex2.v3_7.shared.point_location_output import PointLocationOutput
from webapp.shared.datex2.v3_7.static.authentication_and_identification_enum import (
    AuthenticationAndIdentificationEnum,
)
from webapp.shared.datex2.v3_7.static.authentication_and_identification_enum_g_output import (
    AuthenticationAndIdentificationEnumGOutput,
)
from webapp.shared.datex2.v3_7.static.connector_format_type_enum import ConnectorFormatTypeEnum
from webapp.shared.datex2.v3_7.static.connector_format_type_enum_g_output import ConnectorFormatTypeEnumGOutput
from webapp.shared.datex2.v3_7.static.connector_output import ConnectorOutput
from webapp.shared.datex2.v3_7.static.connector_type_enum import ConnectorTypeEnum
from webapp.shared.datex2.v3_7.static.connector_type_enum_g_output import ConnectorTypeEnumGOutput
from webapp.shared.datex2.v3_7.static.current_type_enum import CurrentTypeEnum
from webapp.shared.datex2.v3_7.static.current_type_enum_g_output import CurrentTypeEnumGOutput
from webapp.shared.datex2.v3_7.static.d_a_t_e_x_i_i3_d2_payload_output import DATEXII3D2PayloadOutput
from webapp.shared.datex2.v3_7.static.delivery_unit_enum import DeliveryUnitEnum
from webapp.shared.datex2.v3_7.static.delivery_unit_enum_g_output import DeliveryUnitEnumGOutput
from webapp.shared.datex2.v3_7.static.electric_charging_point_output import ElectricChargingPointOutput
from webapp.shared.datex2.v3_7.static.electric_energy_output import ElectricEnergyOutput
from webapp.shared.datex2.v3_7.static.energy_infrastructure_site_output import EnergyInfrastructureSiteOutput
from webapp.shared.datex2.v3_7.static.energy_infrastructure_station_output import EnergyInfrastructureStationOutput
from webapp.shared.datex2.v3_7.static.energy_infrastructure_table_output import EnergyInfrastructureTableOutput
from webapp.shared.datex2.v3_7.static.energy_infrastructure_table_publication_output import (
    EnergyInfrastructureTablePublicationOutput,
)
from webapp.shared.datex2.v3_7.static.energy_product_g_output import EnergyProductGOutput
from webapp.shared.datex2.v3_7.static.organisation_g_output import OrganisationGOutput
from webapp.shared.datex2.v3_7.static.organisation_unit_output import OrganisationUnitOutput
from webapp.shared.datex2.v3_7.static.payload_publication_g_output import PayloadPublicationGOutput
from webapp.shared.datex2.v3_7.static.referenceable_organisation_output import ReferenceableOrganisationOutput
from webapp.shared.datex2.v3_7.static.refill_point_g_output import RefillPointGOutput


class DatexV37JSONStaticExportMapper:
    _connector_type_map: dict[ConnectorType, ConnectorTypeEnum] = {
        ConnectorType.CHADEMO: ConnectorTypeEnum.CHADEMO,
        ConnectorType.DOMESTIC_A: ConnectorTypeEnum.DOMESTICATYPE,
        ConnectorType.DOMESTIC_B: ConnectorTypeEnum.DOMESTICBTYPE,
        ConnectorType.DOMESTIC_C: ConnectorTypeEnum.DOMESTICCTYPE,
        ConnectorType.DOMESTIC_D: ConnectorTypeEnum.DOMESTICDTYPE,
        ConnectorType.DOMESTIC_E: ConnectorTypeEnum.DOMESTICETYPE,
        ConnectorType.DOMESTIC_F: ConnectorTypeEnum.DOMESTICFTYPE,
        ConnectorType.DOMESTIC_G: ConnectorTypeEnum.DOMESTICGTYPE,
        ConnectorType.DOMESTIC_H: ConnectorTypeEnum.DOMESTICHTYPE,
        ConnectorType.DOMESTIC_I: ConnectorTypeEnum.DOMESTICITYPE,
        ConnectorType.DOMESTIC_J: ConnectorTypeEnum.DOMESTICJTYPE,
        ConnectorType.DOMESTIC_K: ConnectorTypeEnum.DOMESTICKTYPE,
        ConnectorType.DOMESTIC_L: ConnectorTypeEnum.DOMESTICLTYPE,
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

    _power_type_to_current_type_map: dict[PowerType, CurrentTypeEnum] = {
        PowerType.DC: CurrentTypeEnum.DC,
        PowerType.AC_1_PHASE: CurrentTypeEnum.AC,
        PowerType.AC_3_PHASE: CurrentTypeEnum.AC,
    }

    _connector_format_map: dict[ConnectorFormat, ConnectorFormatTypeEnum] = {
        ConnectorFormat.SOCKET: ConnectorFormatTypeEnum.SOCKET,
        ConnectorFormat.CABLE: ConnectorFormatTypeEnum.CABLEMODE3,
    }

    def map_locations_to_static_payload(self, locations: list[Location]) -> DATEXII3D2PayloadOutput:
        now = datetime.now(tz=timezone.utc)

        sites = []
        for location in locations:
            site = self._map_location_to_site(location)
            if site is not None:
                sites.append(site)

        payload = PayloadPublicationGOutput(
            modelBaseVersionG='3',
            versionG='3.7',
            profileNameG='Afir Energy Infrastructure',
            profileVersionG='01-00-00',
            aegiEnergyInfrastructureTablePublication=EnergyInfrastructureTablePublicationOutput(
                lang='de',
                publicationTime=now,
                publicationCreator=InternationalIdentifierOutput(
                    country='DE',
                    nationalIdentifier='OCPDB',
                ),
                energyInfrastructureTable=[
                    EnergyInfrastructureTableOutput(
                        idG='1',
                        versionG='1',
                        energyInfrastructureSite=sites,
                    ),
                ],
            ),
        )
        return DATEXII3D2PayloadOutput(payload=payload)

    def _map_location_to_site(self, location: Location) -> EnergyInfrastructureSiteOutput | None:
        if location.lat is None or location.lon is None:
            return None

        version_g = location.last_updated.isoformat()

        location_reference = self._build_location_reference(location)

        stations = []
        for charging_station in location.charging_pool:
            station = self._map_charging_station_to_station(charging_station, location)
            stations.append(station)

        site = EnergyInfrastructureSiteOutput(
            idG=location.uid,
            versionG=version_g,
            locationReference=location_reference,
            energyInfrastructureStation=stations,
        )

        if location.name:
            site.name = self._build_multilingual_string(location.name)

        if location.twentyfourseven:
            site.operatingHours = OperatingHoursGOutput(afacOpenAllHours=OpenAllHoursOutput())

        if location.operator:
            site.operator = self._build_operator(location.operator)

        return site

    def _map_charging_station_to_station(
        self,
        charging_station: ChargingStation,
        location: Location,
    ) -> EnergyInfrastructureStationOutput:
        version_g = charging_station.last_updated.isoformat()

        refill_points = []
        for evse in charging_station.evses:
            refill_point = self._map_evse_to_refill_point(evse, location)
            refill_points.append(refill_point)

        station = EnergyInfrastructureStationOutput(
            idG=charging_station.uid,
            versionG=version_g,
            refillPoint=refill_points,
        )

        if charging_station.lat and charging_station.lon:
            station.locationReference = self._build_location_reference(location)

        capabilities = charging_station.capabilities
        if capabilities:
            auth_methods = self._map_capabilities_to_auth_methods(capabilities)
            if auth_methods:
                station.authenticationAndIdentificationMethods = auth_methods

        return station

    def _map_evse_to_refill_point(self, evse: Evse, location: Location) -> RefillPointGOutput:
        version_g = evse.last_updated.isoformat()

        current_type = CurrentTypeEnum.AC
        if evse.connectors:
            first_connector = evse.connectors[0]
            if first_connector.power_type:
                current_type = self._power_type_to_current_type_map.get(first_connector.power_type, CurrentTypeEnum.AC)

        datex_connectors: list[ConnectorOutput] = []
        voltages: list[float] = []
        powers: list[float] = []
        for connector in evse.connectors:
            datex_connector = self._map_connector(connector)
            if datex_connector is not None:
                datex_connectors.append(datex_connector)
            if connector.max_voltage:
                voltages.append(float(connector.max_voltage))
            if connector.max_electric_power:
                powers.append(float(connector.max_electric_power))

        charging_point = ElectricChargingPointOutput(
            idG=evse.uid,
            versionG=version_g,
            deliveryUnit=DeliveryUnitEnumGOutput(value=DeliveryUnitEnum.KWH),
            currentType=CurrentTypeEnumGOutput(value=current_type),
            connector=datex_connectors,
        )

        if voltages:
            charging_point.availableVoltage = voltages

        if powers:
            charging_point.availableChargingPower = powers

        if location.energy_mix and location.energy_mix.get('is_green_energy') is not None:
            charging_point.energyProduct = [
                EnergyProductGOutput(
                    aegiElectricEnergy=ElectricEnergyOutput(
                        isGreenEnergy=location.energy_mix['is_green_energy'],
                    ),
                ),
            ]

        return RefillPointGOutput(aegiElectricChargingPoint=charging_point)

    def _map_connector(self, connector: Connector) -> ConnectorOutput | None:
        if connector.standard is None:
            return None

        connector_type_enum = self._connector_type_map.get(connector.standard)
        if connector_type_enum is None:
            return None

        max_power_kw = float(connector.max_electric_power) if connector.max_electric_power else 0.0

        datex_connector = ConnectorOutput(
            connectorType=ConnectorTypeEnumGOutput(value=connector_type_enum),
            maxPowerAtSocket=max_power_kw,
        )

        if connector.max_voltage:
            datex_connector.voltage = float(connector.max_voltage)

        if connector.max_amperage:
            datex_connector.maximumCurrent = float(connector.max_amperage)

        if connector.format:
            format_enum = self._connector_format_map.get(connector.format)
            if format_enum:
                datex_connector.connectorFormat = ConnectorFormatTypeEnumGOutput(value=format_enum)

        return datex_connector

    def _build_location_reference(self, location: Location) -> LocationReferenceGOutput:
        coordinates = PointCoordinatesOutput(
            latitude=float(location.lat),
            longitude=float(location.lon),
        )

        point_location = PointLocationOutput(
            pointByCoordinates=PointByCoordinatesOutput(pointCoordinates=coordinates),
            locLocationExtensionG=LocationExtensionTypeGOutput(
                AfirFacilityLocation=self._build_facility_location(location),
            ),
        )

        return LocationReferenceGOutput(locPointLocation=point_location)

    def _build_facility_location(
        self,
        location: Location,
        include_timezone: bool = False,
    ) -> AfirFacilityLocationOutput:
        address = self._build_address(location)
        facility = AfirFacilityLocationOutput(address=address)

        if include_timezone and location.time_zone:
            facility.timeZone = location.time_zone

        return facility

    def _build_address(self, location: Location) -> AddressOutput:
        address = AddressOutput()

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
                    AddressLineOutput(
                        order=1,
                        type=AddressLineTypeEnumGOutput(value=AddressLineTypeEnum.STREET),
                        text=self._build_multilingual_string(street),
                    )
                )
            if house_number:
                address_lines.append(
                    AddressLineOutput(
                        order=2,
                        type=AddressLineTypeEnumGOutput(value=AddressLineTypeEnum.HOUSENUMBER),
                        text=self._build_multilingual_string(house_number),
                    )
                )
            if address_lines:
                address.addressLine = address_lines

        return address

    @staticmethod
    def _build_operator(business: Business) -> OrganisationGOutput:
        org = ReferenceableOrganisationOutput(
            idG=business.emobility_uid or f'OP-{business.id}',
            versionG='1',
            name=DatexV37JSONStaticExportMapper._build_multilingual_string(business.name),
            organisationUnit=[OrganisationUnitOutput()],
        )

        return OrganisationGOutput(afacReferenceableOrganisation=org)

    def _map_capabilities_to_auth_methods(
        self,
        capabilities: list[Capability],
    ) -> list[AuthenticationAndIdentificationEnumGOutput]:
        methods = []
        for capability in capabilities:
            method = self._capability_to_auth_method_map.get(capability)
            if method:
                methods.append(AuthenticationAndIdentificationEnumGOutput(value=method))
        return methods

    @staticmethod
    def _build_multilingual_string(text: str, lang: str = 'de') -> MultilingualStringOutput:
        return MultilingualStringOutput(
            values=[MultiLingualStringValueOutput(lang=lang, value=text)],
        )

    @staticmethod
    def _split_address(address: str) -> tuple[str | None, str | None]:
        if not address:
            return None, None
        match = re.match(r'^(.+)\s+(\d+\S*)$', address)
        if match:
            return match.group(1), match.group(2)
        return address, None
