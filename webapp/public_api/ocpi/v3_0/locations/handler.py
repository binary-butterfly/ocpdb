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

from webapp.models import Location
from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.repositories import LocationRepository
from webapp.shared.location_search_queries import LocationApiSearchQuery


class Ocpi30LocationHandler(PublicApiBaseHandler):
    location_repository: LocationRepository

    def __init__(self, *args, location_repository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository

    def get_locations(self, search_query: LocationApiSearchQuery, strict: bool = False) -> PaginatedResult[dict]:
        locations = self.location_repository.fetch_locations(search_query=search_query)
        return locations.map(lambda location: self._map_location_to_ocpi_30(location, strict=strict))

    def get_location(self, location_id: int, strict: bool = False) -> dict:
        location = self.location_repository.fetch_location_by_id(location_id, include_children=True)
        return self._map_location_to_ocpi_30(location, strict=strict)

    def _map_location_to_ocpi_30(self, location: Location, strict: bool = False) -> dict:
        location_dict = self.filter_none(location.to_dict(strict=strict))

        for business in ['operator', 'owner', 'suboperator']:
            if getattr(location, f'{business}_id'):
                location_dict[business] = self.filter_none(getattr(location, business).to_dict())

        # At non-strict, it's already in dict
        if location.max_power_unit is not None or location.max_power_value is not None and strict:
            location_dict['max_power'] = self.filter_none({
                'unit': location.max_power_unit,
                'value': location.max_power_value,
            })

        location_dict['charging_pool'] = []
        for charging_station in location.charging_pool:
            cs_dict = charging_station.to_dict(strict=strict)

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

            location_dict['charging_pool'].append(self.filter_none_and_empty_list(cs_dict))

        return location_dict
