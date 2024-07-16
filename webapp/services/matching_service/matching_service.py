"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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
from math import cos, exp, pi

from geopy.distance import geodesic
from mercantile import LngLatBbox
from ngram import NGram

from webapp.models import Location
from webapp.repositories import LocationRepository
from webapp.services.base_service import BaseService


class MatchingService(BaseService):
    location_repository: LocationRepository
    earth_radius = 6378.137

    def __init__(self, *args, location_repository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository

    def _add_lat(self, lat: Decimal, meter: int) -> float:
        meter_factor = (1 / ((2 * pi / 360) * self.earth_radius)) / 1000
        return float(lat) + (meter * meter_factor)

    def _add_lon(self, lat: Decimal, lon: Decimal, meter: int) -> float:
        meter_factor = (1 / ((2 * pi / 360) * self.earth_radius)) / 1000
        return float(lon) + (meter * meter_factor) / cos(float(lat) * (pi / 180))

    def match(self):
        static_locations = self.location_repository.fetch_locations_by_source('bnetza')
        for static_location in static_locations:
            self.match_location(static_location)

    def match_location(self, static_location: Location):
        locations = self.location_repository.fetch_locations_by_bounds(
            LngLatBbox(
                self._add_lon(static_location.lat, static_location.lon, -250),
                self._add_lat(static_location.lat, -250),
                self._add_lon(static_location.lat, static_location.lon, 250),
                self._add_lat(static_location.lat, 250),
            ),
        )
        if not len(locations):
            self._unset_location_relation(static_location)
            return

        locations_by_factors = {self._match_location_pair(static_location, location): location for location in locations}

        # sort factors
        sorted_factors = sorted(locations_by_factors.keys(), reverse=True)
        if not len(sorted_factors):
            self._unset_location_relation(static_location)
            return

        if sorted_factors[0] < self.config_helper.get('MATCHING_FACTOR_THRESHOLD'):
            self._unset_location_relation(static_location)
            return

        matched_location = locations_by_factors[sorted_factors[0]]
        if static_location.dynamic_location_id == matched_location.id:
            return

        static_location.dynamic_location_id = matched_location.id
        self.location_repository.save_location(static_location)

    def _unset_location_relation(self, location: Location):
        if location.dynamic_location_id is None:
            return

        location.dynamic_location_id = None
        self.location_repository.save_location(location)

    @staticmethod
    def _match_location_pair(static_location: Location, dynamic_location: Location) -> float:
        # distance factor
        distance = geodesic(
            (float(static_location.lat), float(static_location.lon)),
            (float(dynamic_location.lat), float(dynamic_location.lon)),
        ).meters
        distance_factor = exp(-1 * (distance / 100) ** 2)

        # street ngram factor
        street_factor = NGram.compare(static_location.address.lower(), dynamic_location.address.lower())

        # operator ngram factor (if dynamic operator is existing)
        operator_factor = 1
        if dynamic_location.operator_id:
            operator_factor = NGram.compare(static_location.operator.name.lower(), dynamic_location.operator.name.lower())

        # evse count factor
        evse_count_factor = 1 - 0.4 * (
                abs(len(static_location.evses) - len(dynamic_location.evses))
                / (abs(len(static_location.evses) - len(dynamic_location.evses)) + 1)
        )

        # weighting modifications
        street_factor = street_factor ** 0.5
        distance_factor = distance_factor ** 0.5

        return distance_factor * street_factor * operator_factor * evse_count_factor
