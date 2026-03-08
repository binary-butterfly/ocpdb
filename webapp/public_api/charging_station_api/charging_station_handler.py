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

from validataclass_search_queries.pagination import PaginatedResult

from webapp.models.charging_station import ChargingStation
from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.public_api.charging_station_api.charging_station_search_queries import ChargingStationSearchQuery
from webapp.repositories import ChargingStationRepository


class ChargingStationHandler(PublicApiBaseHandler):
    charging_station_repository: ChargingStationRepository

    def __init__(self, *args, charging_station_repository: ChargingStationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.charging_station_repository = charging_station_repository

    def get_charging_stations(
        self,
        query: ChargingStationSearchQuery,
        strict: bool = False,
    ) -> PaginatedResult[dict]:
        charging_stations = self.charging_station_repository.fetch_charging_stations(query)
        return charging_stations.map(lambda cs: self._map_charging_station_to_ocpi(cs, strict=strict))

    def get_charging_station(self, charging_station_id: int, strict: bool = False) -> dict:
        charging_station = self.charging_station_repository.fetch_charging_station_by_id(
            charging_station_id,
            include_children=True,
        )
        return self._map_charging_station_to_ocpi(charging_station, strict=strict)

    def _map_charging_station_to_ocpi(self, charging_station: ChargingStation, strict: bool = False) -> dict:
        cs_dict: dict = {
            'uid': str(charging_station.id),
            'last_updated': charging_station.last_updated,
        }

        if not strict:
            cs_dict['original_uid'] = charging_station.uid
            if charging_station.go_live_date:
                cs_dict['go_live_date'] = charging_station.go_live_date

        if charging_station.max_power_unit and charging_station.max_power_value:
            cs_dict['max_power'] = {
                'unit': charging_station.max_power_unit,
                'value': charging_station.max_power_value,
            }

        capabilities = [c.value for c in charging_station.capabilities]
        if capabilities:
            cs_dict['capabilities'] = capabilities

        if charging_station.floor_level:
            cs_dict['floor_level'] = charging_station.floor_level

        if charging_station.lat is not None and charging_station.lon is not None:
            cs_dict['coordinates'] = {
                'latitude': charging_station.lat,
                'longitude': charging_station.lon,
            }

        if charging_station.directions:
            cs_dict['directions'] = charging_station.directions

        if charging_station.physical_reference:
            cs_dict['physical_reference'] = charging_station.physical_reference

        for image in charging_station.images:
            if 'images' not in cs_dict:
                cs_dict['images'] = []
            cs_dict['images'].append(self.filter_none(image.to_dict(strict=strict)))

        cs_dict['evses'] = []
        for evse in charging_station.evses:
            evse_dict = evse.to_dict(strict=strict)

            evse_dict['connectors'] = []
            for connector in evse.connectors:
                evse_dict['connectors'].append(self.filter_none(connector.to_dict(strict=strict)))

            for image in evse.images:
                if 'images' not in evse_dict:
                    evse_dict['images'] = []
                evse_dict['images'].append(self.filter_none(image.to_dict(strict=strict)))

            cs_dict['evses'].append(self.filter_none_and_empty_list(evse_dict))

        return self.filter_none_and_empty_list(cs_dict)
