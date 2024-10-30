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
from mapbox_vector_tile import encode

from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.public_api.tiles_api.tiles_validators import TileFilterInput
from webapp.repositories import LocationRepository

RENDER_CHARGEPOINTS_MIN_ZOOM = 8

class TilesHandler(PublicApiBaseHandler):
    location_repository: LocationRepository

    def __init__(self, *args, location_respository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_respository

    def generate_tile(self, x: int, y: int, z: int, tile_filter_input: TileFilterInput) -> bytes:
        # don't render any chargepoints if zoomed out too far
        if z < RENDER_CHARGEPOINTS_MIN_ZOOM:
            return encode(layers=[])

        # fetch chargepoints in the tile's bounding box
        bbox = mercantile.bounds((x, y, z))
        chargepoints = self.location_repository.fetch_locations_summary_by_bounds(
            bbox,
            filter_duplicates=tile_filter_input.filter_duplicates,
            static=tile_filter_input.static,
        )

        # create layer dict
        layer = {
            'name': 'chargepoints',
            'features': [],
        }

        # add features for chargepoints
        for item in chargepoints:
            point_x = int(4096 * (float(item.lon) - bbox[0]) / (bbox[2] - bbox[0]))
            point_y = int(4096 * (bbox[3] - float(item.lat)) / (bbox[3] - bbox[1]))
            feature = {
                'geometry': f'POINT({point_x} {point_y})',
                'properties': {
                    'id': item.id,
                    'name': item.name or item.address,
                    'c': item.chargepoint_count,
                    'ca': int(item.chargepoint_available_count),
                    'cu': int(item.chargepoint_unknown_count),
                    'cb': int(item.chargepoint_bike_count),
                    'cs': int(item.chargepoint_static_count),
                },
            }
            layer['features'].append(feature)

        return encode(layers=[layer])
