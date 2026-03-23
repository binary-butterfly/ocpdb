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
from webapp.models.enums import TariffType
from webapp.models.evse import Evse
from webapp.models.location import Location
from webapp.models.tariff import Tariff
from webapp.shared.datex2.v3_5_json_static.models.address_input import AddressInput
from webapp.shared.datex2.v3_5_json_static.models.address_line_input import AddressLineInput
from webapp.shared.datex2.v3_5_json_static.models.address_line_type_enum import AddressLineTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.address_line_type_enum_g_input import AddressLineTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.models.an_organisation_input import AnOrganisationInput
from webapp.shared.datex2.v3_5_json_static.models.area_location_input import AreaLocationInput
from webapp.shared.datex2.v3_5_json_static.models.authentication_and_identification_enum import (
    AuthenticationAndIdentificationEnum,
)
from webapp.shared.datex2.v3_5_json_static.models.authentication_and_identification_enum_g_input import (
    AuthenticationAndIdentificationEnumGInput,
)
from webapp.shared.datex2.v3_5_json_static.models.connector_format_type_enum import ConnectorFormatTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.connector_format_type_enum_g_input import (
    ConnectorFormatTypeEnumGInput,
)
from webapp.shared.datex2.v3_5_json_static.models.connector_input import (
    ConnectorInput,
)
from webapp.shared.datex2.v3_5_json_static.models.connector_input import (
    ConnectorInput as DatexConnectorInput,
)
from webapp.shared.datex2.v3_5_json_static.models.connector_type_enum import ConnectorTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.connector_type_enum_g_input import ConnectorTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.models.contact_information_g_input import ContactInformationGInput
from webapp.shared.datex2.v3_5_json_static.models.contact_information_input import ContactInformationInput
from webapp.shared.datex2.v3_5_json_static.models.current_type_enum import CurrentTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.current_type_enum_g_input import CurrentTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.models.d_a_t_e_x_i_i3_d2_payload_input import DATEXII3D2PayloadInput
from webapp.shared.datex2.v3_5_json_static.models.delivery_unit_enum import DeliveryUnitEnum
from webapp.shared.datex2.v3_5_json_static.models.delivery_unit_enum_g_input import DeliveryUnitEnumGInput
from webapp.shared.datex2.v3_5_json_static.models.electric_charging_point_input import ElectricChargingPointInput
from webapp.shared.datex2.v3_5_json_static.models.electric_energy_input import ElectricEnergyInput
from webapp.shared.datex2.v3_5_json_static.models.energy_infrastructure_site_input import EnergyInfrastructureSiteInput
from webapp.shared.datex2.v3_5_json_static.models.energy_infrastructure_station_input import (
    EnergyInfrastructureStationInput,
)
from webapp.shared.datex2.v3_5_json_static.models.energy_infrastructure_table_input import (
    EnergyInfrastructureTableInput,
)
from webapp.shared.datex2.v3_5_json_static.models.energy_infrastructure_table_publication_input import (
    EnergyInfrastructureTablePublicationInput,
)
from webapp.shared.datex2.v3_5_json_static.models.energy_price_input import EnergyPriceInput
from webapp.shared.datex2.v3_5_json_static.models.energy_rate_input import EnergyRateInput
from webapp.shared.datex2.v3_5_json_static.models.external_identifier_input import ExternalIdentifierInput
from webapp.shared.datex2.v3_5_json_static.models.facility_location_input import FacilityLocationInput
from webapp.shared.datex2.v3_5_json_static.models.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_5_json_static.models.location_extension_type_g_input import LocationExtensionTypeGInput
from webapp.shared.datex2.v3_5_json_static.models.location_reference_g_input import LocationReferenceGInput
from webapp.shared.datex2.v3_5_json_static.models.multi_lingual_string_value_input import MultiLingualStringValueInput
from webapp.shared.datex2.v3_5_json_static.models.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_5_json_static.models.open_all_hours_input import OpenAllHoursInput
from webapp.shared.datex2.v3_5_json_static.models.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_5_json_static.models.organisation_g_input import OrganisationGInput
from webapp.shared.datex2.v3_5_json_static.models.organisation_unit_input import OrganisationUnitInput
from webapp.shared.datex2.v3_5_json_static.models.payload_publication_g_input import PayloadPublicationGInput
from webapp.shared.datex2.v3_5_json_static.models.point_coordinates_input import PointCoordinatesInput
from webapp.shared.datex2.v3_5_json_static.models.point_location_input import PointLocationInput
from webapp.shared.datex2.v3_5_json_static.models.price_type_enum import PriceTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.price_type_enum_g_input import PriceTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.models.rate_policy_enum import RatePolicyEnum
from webapp.shared.datex2.v3_5_json_static.models.rate_policy_enum_g_input import RatePolicyEnumGInput
from webapp.shared.datex2.v3_5_json_static.models.referenceable_organisation_input import ReferenceableOrganisationInput
from webapp.shared.datex2.v3_5_json_static.models.refill_point_g_input import RefillPointGInput
from webapp.shared.datex2.v3_5_json_static.models.service_type_enum import ServiceTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.service_type_enum_g_input import ServiceTypeEnumGInput
from webapp.shared.datex2.v3_5_json_static.models.service_type_input import ServiceTypeInput
from webapp.shared.datex2.v3_5_json_static.models.time_based_applicability_input import TimeBasedApplicabilityInput
from webapp.shared.datex2.v3_5_json_static.models.type_of_identifier_enum import TypeOfIdentifierEnum
from webapp.shared.datex2.v3_5_json_static.models.type_of_identifier_enum_extension_type_g import (
    TypeOfIdentifierEnumExtensionTypeG,
)
from webapp.shared.datex2.v3_5_json_static.models.type_of_identifier_enum_g_input import TypeOfIdentifierEnumGInput


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

    _tariff_type_to_rate_policy_map: dict[TariffType, RatePolicyEnum] = {
        TariffType.AD_HOC_PAYMENT: RatePolicyEnum.ADHOC,
        TariffType.REGULAR: RatePolicyEnum.CONTRACT,
    }

    _price_component_type_to_price_type_map: dict[str, PriceTypeEnum] = {
        'ENERGY': PriceTypeEnum.PRICEPERKWH,
        'TIME': PriceTypeEnum.PRICEPERMINUTE,
        'FLAT': PriceTypeEnum.FLATRATE,
        'PARKING_TIME': PriceTypeEnum.PRICEPERMINUTE,
    }

    def map_locations_to_static_payload(
        self,
        locations: list[Location],
        evse_tariffs: dict[str, list['Tariff']] | None = None,
    ) -> DATEXII3D2PayloadInput:
        now = datetime.now(tz=timezone.utc).isoformat()
        evse_tariffs = evse_tariffs or {}

        sites = []
        for location in locations:
            site = self._map_location_to_site(location, evse_tariffs)
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

    def _map_location_to_site(
        self,
        location: Location,
        evse_tariffs: dict[str, list['Tariff']],
    ) -> EnergyInfrastructureSiteInput | None:
        if location.lat is None or location.lon is None:
            return None

        version_g = location.last_updated.isoformat()

        location_reference = self._build_site_location_reference(location)

        stations = []
        for charging_station in location.charging_pool:
            station = self._map_charging_station_to_station(charging_station, location, evse_tariffs)
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
        evse_tariffs: dict[str, list['Tariff']],
    ) -> EnergyInfrastructureStationInput:
        version_g = charging_station.last_updated.isoformat()

        refill_points = []
        for evse in charging_station.evses:
            refill_point = self._map_evse_to_refill_point(evse, location, evse_tariffs)
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

    def _map_evse_to_refill_point(
        self,
        evse: Evse,
        location: Location,
        evse_tariffs: dict[str, list['Tariff']],
    ) -> RefillPointGInput:
        version_g = evse.last_updated.isoformat()

        current_type = CurrentTypeEnum.AC
        if evse.connectors:
            first_connector = evse.connectors[0]
            if first_connector.power_type:
                current_type = self._power_type_to_current_type_map.get(first_connector.power_type, CurrentTypeEnum.AC)

        datex_connectors: list[ConnectorInput] = []
        voltages: list[int] = []
        powers: list[int] = []
        for connector in evse.connectors:
            datex_connector = self._map_connector(connector)
            if datex_connector is not None:
                datex_connectors.append(datex_connector)
            if connector.max_voltage:
                voltages.append(connector.max_voltage)
            if connector.max_electric_power:
                powers.append(connector.max_electric_power)

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

        is_green = location.energy_mix.get('is_green_energy') if location.energy_mix else None
        tariffs = evse_tariffs.get(evse.uid, [])

        if tariffs:
            energy_rates = [self._map_tariff_to_energy_rate(tariff) for tariff in tariffs]
            electric_energy = ElectricEnergyInput(energyRate=energy_rates)
            if is_green is not None:
                electric_energy.isGreenEnergy = is_green
            charging_point.electricEnergy = [electric_energy]
        elif is_green is not None:
            charging_point.electricEnergy = [ElectricEnergyInput(isGreenEnergy=is_green)]

        return RefillPointGInput(aegiElectricChargingPoint=charging_point)

    def _map_connector(self, connector: Connector) -> DatexConnectorInput | None:
        if connector.standard is None:
            return None

        connector_type_enum = self._connector_type_map.get(connector.standard)
        max_power_w = float(connector.max_electric_power) if connector.max_electric_power else 0.0

        datex_connector = DatexConnectorInput(
            connectorType=ConnectorTypeEnumGInput(value=connector_type_enum) if connector_type_enum else UnsetValue,
            maxPowerAtSocket=max_power_w,
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

    def _map_tariff_to_energy_rate(self, tariff: Tariff) -> EnergyRateInput:
        # Extract rate idG from tariff uid (format: "{evse_uid}:{rate_idG}")
        rate_id = tariff.uid.rsplit(':', 1)[-1] if ':' in tariff.uid else tariff.uid

        rate_policy = RatePolicyEnum.ADHOC
        if tariff.type:
            rate_policy = self._tariff_type_to_rate_policy_map.get(tariff.type, RatePolicyEnum.ADHOC)

        energy_rate = EnergyRateInput(
            idG=rate_id,
            ratePolicy=RatePolicyEnumGInput(value=rate_policy),
            lastUpdated=tariff.last_updated.isoformat(),
            applicableCurrency=[tariff.currency] if tariff.currency else ['EUR'],
        )

        if tariff.elements:
            energy_prices = []
            for element in tariff.elements:
                if element.price_components:
                    for component in element.price_components:
                        price_type = self._price_component_type_to_price_type_map.get(
                            component.get('type', ''),
                            PriceTypeEnum.OTHER,
                        )
                        energy_price = EnergyPriceInput(
                            priceType=PriceTypeEnumGInput(value=price_type),
                            value=component.get('price', 0),
                        )
                        if 'tax_included' in component:
                            energy_price.taxIncluded = component['tax_included']
                        if 'vat' in component:
                            energy_price.taxRate = component['vat']
                        if 'time_based_applicability' in component:
                            tba = component['time_based_applicability']
                            time_applicability = TimeBasedApplicabilityInput()
                            if 'from_minute' in tba:
                                time_applicability.fromMinute = tba['from_minute']
                            if 'to_minute' in tba:
                                time_applicability.toMinute = tba['to_minute']
                            energy_price.timeBasedApplicability = time_applicability
                        energy_prices.append(energy_price)
            if energy_prices:
                energy_rate.energyPrice = energy_prices

        return energy_rate

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
