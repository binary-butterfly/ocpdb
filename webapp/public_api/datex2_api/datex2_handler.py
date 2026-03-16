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

from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.repositories import LocationRepository
from webapp.shared.datex2.datex_serializer import datex_to_dict

from .datex2_mapper import DatexExportMapper
from .datex2_realtime_mapper import DatexRealtimeExportMapper


class Datex2Handler(PublicApiBaseHandler):
    location_repository: LocationRepository
    datex_export_mapper: DatexExportMapper
    datex_realtime_export_mapper: DatexRealtimeExportMapper

    def __init__(self, *args, location_repository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository
        self.datex_export_mapper = DatexExportMapper()
        self.datex_realtime_export_mapper = DatexRealtimeExportMapper()

    def get_datex2_payload(self) -> dict:
        locations = self.location_repository.fetch_all_locations_with_children()
        payload = self.datex_export_mapper.map_locations_to_payload(locations)
        return {'payload': datex_to_dict(payload)}

    def get_datex2_realtime_payload(self) -> dict:
        locations = self.location_repository.fetch_all_locations_with_children()
        message_container = self.datex_realtime_export_mapper.map_locations_to_realtime_payload(locations)
        return {'messageContainer': datex_to_dict(message_container)}
