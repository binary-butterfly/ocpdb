"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2023 binary butterfly GmbH

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
from webapp.public_api.location_api.location_search_queries import LocationSearchQuery
from webapp.repositories import LocationRepository


class LocationHandler(PublicApiBaseHandler):
    location_repository: LocationRepository

    def __init__(self, *args, location_repository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository

    def get_locations(self, query: LocationSearchQuery, strict: bool = False) -> PaginatedResult[dict]:
        locations = self.location_repository.fetch_locations(query)
        return locations.map(lambda location: self._map_location_to_ocpi(location, strict=strict))

    def get_location(self, location_id: int, strict: bool = False) -> dict:
        location = self.location_repository.fetch_location_by_id(location_id, include_children=True)

        return self._map_location_to_ocpi(location, strict=strict)

    def _map_location_to_ocpi(self, location: Location, strict: bool = False):
        location_dict = self.filter_none(location.to_dict(strict=strict))

        for regular_hours in location.regular_hours:
            if 'opening_times' not in location_dict:
                location_dict['opening_times'] = {}
            if 'regular_hours' not in location_dict['opening_times']:
                location_dict['opening_times']['regular_hours'] = []
            location_dict['opening_times']['regular_hours'].append(regular_hours.to_dict())

        for business in ['operator', 'owner', 'suboperator']:
            if getattr(location, f'{business}_id'):
                location_dict[business] = self.filter_none(getattr(location, business).to_dict())

        for exceptional_opening in location.exceptional_openings:
            if 'exceptional_openings' not in location_dict['opening_times']:
                location_dict['opening_times']['exceptional_openings'] = []

            location_dict['opening_times']['exceptional_openings'].append(exceptional_opening.to_dict())

        for exceptional_closing in location.exceptional_closings:
            if 'exceptional_closings' not in location_dict['opening_times']:
                location_dict['opening_times']['exceptional_closings'] = []

            location_dict['opening_times']['exceptional_closings'].append(exceptional_closing.to_dict())

        location_dict['evses'] = []
        for evse in location.evses:
            evse_dict = evse.to_dict(strict=strict)
            evse_dict['connectors'] = []
            for connector in evse.connectors:
                evse_dict['connectors'].append(self.filter_none(connector.to_dict(strict=strict)))

            for image in evse.images:
                if 'images' not in evse_dict:
                    evse_dict['images'] = []

                evse_dict['images'].append(self.filter_none(image.to_dict(strict=strict)))

            location_dict['evses'].append(self.filter_none_and_empty_list(evse_dict))

        return location_dict
