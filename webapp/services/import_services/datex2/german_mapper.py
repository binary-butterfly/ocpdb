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

from pycountry import countries
from validataclass.helpers import UnsetValue, UnsetValueType

from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType, ac_1_phase_connector_types
from webapp.services.import_services.datex2.german_static.address_line_type_enum import AddressLineTypeEnum
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
from webapp.services.import_services.datex2.german_static.multilingual_string_input import MultilingualStringInput
from webapp.services.import_services.datex2.german_static.organisation_g_input import OrganisationGInput
from webapp.services.import_services.datex2.german_static.point_location_input import PointLocationInput
from webapp.services.import_services.datex2.german_static.refill_point_g_input import RefillPointGInput
from webapp.services.import_services.models import (
    BusinessUpdate,
    ConnectorUpdate,
    EvseUpdate,
    LocationUpdate,
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
        )

        self._apply_point_location(energy_infrastructure_site.locationReference.locPointLocation, location)
        self._apply_operator(energy_infrastructure_site.operator, location)
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

        point_location.postal_code = point_location.locLocationExtensionG.FacilityLocation.address.postcode
        point_location.city = self.get_multilanguage_string(
            point_location.locLocationExtensionG.FacilityLocation.address.city,
        )
        if point_location.locLocationExtensionG.FacilityLocation.address.countryCode:
            location.country = countries.get(
                alpha_2=point_location.locLocationExtensionG.FacilityLocation.address.countryCode,
            ).alpha_3

        point_location.time_zone = point_location.locLocationExtensionG.FacilityLocation.timeZone or 'Europe/Berlin'

    def _apply_operator(self, organization: OrganisationGInput | UnsetValueType, location: LocationUpdate):
        if organization is UnsetValue:
            return
        if organization.afacAnOrganisation is UnsetValue:
            return
        location.operator = BusinessUpdate(
            name=self.get_multilanguage_string(organization.afacAnOrganisation.name),
        )

    def _apply_energy_infrastructure_stations(
        self, energy_infrastructure_station: EnergyInfrastructureStationInput, location: LocationUpdate
    ):
        # TODO: station model
        if energy_infrastructure_station.refillPoint is UnsetValue:
            return

        location.evses = []
        for refill_point in energy_infrastructure_station.refillPoint:
            self._apply_refill_point(refill_point, location)

    def _apply_refill_point(self, refill_point: RefillPointGInput, location: LocationUpdate):
        if refill_point.aegiElectricChargingPoint is UnsetValue:
            return

        evse = EvseUpdate(
            uid=refill_point.aegiElectricChargingPoint.idG,
            evse_id=refill_point.aegiElectricChargingPoint.idG,
            last_updated=refill_point.aegiElectricChargingPoint.lastUpdated,
        )
        location.evses.append(evse)

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

        connector = ConnectorUpdate(
            uid=str(i),
            standard=standard,
            format=ConnectorFormat.CABLE if power_type == PowerType.DC else ConnectorFormat.SOCKET,
            power_type=power_type,
            max_electric_power=int(connector_input.maxPowerAtSocket * 1000),
            last_updated=charging_point.lastUpdated,
        )
        evse.connectors.append(connector)

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

    @staticmethod
    def get_multilanguage_string(values: MultilingualStringInput | UnsetValueType) -> str | UnsetValueType:
        if values is UnsetValue:
            return UnsetValue

        item = next(iter(values.values), UnsetValue)

        if item is UnsetValue:
            return UnsetValue

        return item.value
