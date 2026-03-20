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
from webapp.shared.datex2.german_realtime.d_a_t_e_x_i_i3_d2_payload_input import (
    DATEXII3D2PayloadInput as DATEXII3D2RealtimePayloadInput,
)
from webapp.shared.datex2.german_static.d_a_t_e_x_i_i3_d2_payload_input import (
    DATEXII3D2PayloadInput as DATEXII3D2StaticPayloadInput,
)

from .datex2_realtime_mapper import DatexRealtimeExportMapper
from .datex2_static_mapper import DatexStaticExportMapper


class Datex2Handler(PublicApiBaseHandler):
    location_repository: LocationRepository
    datex_static_export_mapper: DatexStaticExportMapper
    datex_realtime_export_mapper: DatexRealtimeExportMapper

    def __init__(self, *args, location_repository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository
        self.datex_static_export_mapper = DatexStaticExportMapper()
        self.datex_realtime_export_mapper = DatexRealtimeExportMapper()

    def get_datex2_payload(self) -> DATEXII3D2StaticPayloadInput:
        locations = self.location_repository.fetch_all_locations_with_children()

        return self.datex_static_export_mapper.map_locations_to_static_payload(locations)

    def get_datex2_realtime_payload(self) -> DATEXII3D2RealtimePayloadInput:
        locations = self.location_repository.fetch_all_locations_with_children()

        return self.datex_realtime_export_mapper.map_locations_to_realtime_payload(locations)
