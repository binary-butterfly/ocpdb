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

import logging

from webapp.models import Location
from webapp.repositories import LocationRepository, ObjectNotFoundException, OfficialRegionCodeRepository
from webapp.services.base_service import BaseService

logger = logging.getLogger(__name__)


class LocationService(BaseService):
    location_repository: LocationRepository
    official_region_code_repository: OfficialRegionCodeRepository

    def __init__(
        self,
        *args,
        location_repository: LocationRepository,
        official_region_code_repository: OfficialRegionCodeRepository,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository
        self.official_region_code_repository = official_region_code_repository

    def assign_official_region_codes(self, source_id: str | None = None, re_assign: bool = False):
        available_databases = self.official_region_code_repository.available_databases_by_country()
        if not available_databases:
            logger.warning('No official region code databases available')
            return

        if source_id:
            locations = self.location_repository.fetch_locations_by_source(source_id, include_children=False)
        else:
            locations = self.location_repository.session.query(Location).all()

        for location in locations:
            if not re_assign and location.official_region_code is not None:
                continue

            if not location.lat or not location.lon or not location.country:
                continue

            if location.country not in available_databases:
                continue

            try:
                location.official_region_code = (
                    self.official_region_code_repository.fetch_official_region_code_by_coordinates(
                        country=location.country,
                        lat=location.lat,
                        lon=location.lon,
                    )
                )
            except ObjectNotFoundException:
                logger.warning(
                    'Cannot find official regional code for location %s %s / %s',
                    location.country,
                    location.lat,
                    location.lon,
                )

            self.location_repository.save_location(location)
