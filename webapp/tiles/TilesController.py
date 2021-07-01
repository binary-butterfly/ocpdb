# encoding: utf-8

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
from flask import Blueprint, current_app
from ..extensions import db
from ..common.response import protobuf_response


tiles_controller = Blueprint('tiles_controller', __name__)


@tiles_controller.route('/tiles/<int:z>/<int:x>/<int:y>.mvt')
def tile_data(x, y, z):
    tile = VectorTile()
    if z < 8:
        return protobuf_response(tile.serialize())

    bbox = mercantile.bounds(x, y, z)
    query = """
    SELECT location.id, location.lat, location.lon, location.name, location.address, COUNT(chargepoint.id) as chargepoint_count, 
        SUM(CASE WHEN chargepoint.status = 'AVAILABLE' THEN 1 ELSE 0 END) as chargepoint_available_count, 
        SUM(CASE WHEN chargepoint.status = 'UNKNOWN' THEN 1 ELSE 0 END) as chargepoint_unknown_count
    FROM location 
    LEFT JOIN chargepoint ON chargepoint.location_id = location.id
    WHERE MBRContains(GeomFromText('LINESTRING(%s %s, %s %s)'), location.geometry)
    GROUP BY location.id
    """ % (
        bbox[1] - (0.5 * (bbox[3] - bbox[1])),
        bbox[0] - (0.5 * (bbox[2] - bbox[0])),
        bbox[3] + (0.5 * (bbox[3] - bbox[1])),
        bbox[2] + (0.5 * (bbox[2] - bbox[0]))
    )
    chargepoints = db.session.execute(query)

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
            'cu': int(item.chargepoint_unknown_count)
        }
        feature.extend = 4096
    return protobuf_response(tile.serialize())
