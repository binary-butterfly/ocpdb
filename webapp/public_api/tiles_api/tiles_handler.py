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

import mercantile
from vector_tile_base import VectorTile

from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.repositories import LocationRepository


class TilesHandler(PublicApiBaseHandler):
    location_repository: LocationRepository

    def __init__(self, *args, location_respository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_respository

    def generate_tile(self, x: int, y: int, z: int, static: bool) -> bytes:
        tile = VectorTile()
        if z < 8:
            tile.serialize()

        bbox = mercantile.bounds(x, y, z)
        chargepoints = self.location_repository.fetch_locations_summary_by_bounds(bbox, static=static)

        layer = tile.add_layer('chargepoints', 1)
        for item in chargepoints:
            feature = layer.add_point_feature()
            feature.add_points([
                int(4096 * (float(item.lon) - bbox[0]) / (bbox[2] - bbox[0])),
                int(4096 * (bbox[3] - float(item.lat)) / (bbox[3] - bbox[1]))
            ])
            feature.id = item.id
            feature.attributes = {
                'id': item.id,
                'name': item.name or item.address,
                'c': item.chargepoint_count,
                'ca': int(item.chargepoint_available_count),
                'cu': int(item.chargepoint_unknown_count),
                'cb': int(item.chargepoint_bike_count),
                'cs': int(item.chargepoint_static_count)
            }
            feature.extend = 4096
        return tile.serialize()

