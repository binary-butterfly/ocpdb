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

from mercantile import LngLatBbox
from webapp.storage import Location
from .base_repository import BaseRepository, ObjectNotFoundException


class LocationRepository(BaseRepository):

    def fetch_by_id(self, location_id: int) -> Location:
        result = self.session.query(Location).get(location_id)
        if result is None:
            raise ObjectNotFoundException
        return result

    def fetch_locations_by_bounds(self, bbox: LngLatBbox, static: bool = False):
        query = """
        SELECT location.id, location.lat, location.lon, location.name, location.address, 
            COUNT(chargepoint.id) as chargepoint_count, 
            SUM(CASE WHEN chargepoint.status = 'AVAILABLE' THEN 1 ELSE 0 END) as chargepoint_available_count, 
            SUM(CASE WHEN chargepoint.status = 'UNKNOWN' THEN 1 ELSE 0 END) as chargepoint_unknown_count,
            SUM(CASE WHEN chargepoint.status = 'STATIC' THEN 1 ELSE 0 END) as chargepoint_static_count,
            SUM(CASE WHEN chargepoint.parking_restrictions & 64 = 64 THEN 1 ELSE 0 END) as chargepoint_bike_count
        FROM location 
        LEFT JOIN chargepoint ON chargepoint.location_id = location.id
        WHERE MBRContains(GeomFromText('LINESTRING(%s %s, %s %s)'), location.geometry)
            %s
        GROUP BY location.id
        """ % (
            bbox[1] - (0.5 * (bbox[3] - bbox[1])),
            bbox[0] - (0.5 * (bbox[2] - bbox[0])),
            bbox[3] + (0.5 * (bbox[3] - bbox[1])),
            bbox[2] + (0.5 * (bbox[2] - bbox[0])),
            '' if static is None else "AND chargepoint.status %s 'STATIC'" % ('=' if static is True else '!=')
        )
        return self.session.execute(query)
