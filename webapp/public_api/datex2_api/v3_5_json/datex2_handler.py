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
from webapp.repositories import LocationRepository, TariffRepository
from webapp.shared.datex2.v3_5_json_realtime.models.d_a_t_e_x_i_i3_d2_payload_input import (
    DATEXII3D2PayloadInput as DATEXII3D2RealtimePayloadInput,
)
from webapp.shared.datex2.v3_5_json_static.models.d_a_t_e_x_i_i3_d2_payload_input import (
    DATEXII3D2PayloadInput as DATEXII3D2StaticPayloadInput,
)
from webapp.shared.datex2.v3_5_realtime_export_mapper import DatexV35JSONRealtimeExportMapper
from webapp.shared.datex2.v3_5_static_export_mapper import DatexV35JSONStaticExportMapper
from webapp.shared.location_search_queries import LocationApiSearchQuery


class Datex2V35JSONHandler(PublicApiBaseHandler):
    location_repository: LocationRepository
    tariff_repository: TariffRepository
    datex_static_export_mapper: DatexV35JSONStaticExportMapper
    datex_realtime_export_mapper: DatexV35JSONRealtimeExportMapper

    def __init__(self, *args, location_repository: LocationRepository, tariff_repository: TariffRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository
        self.tariff_repository = tariff_repository
        self.datex_static_export_mapper = DatexV35JSONStaticExportMapper()
        self.datex_realtime_export_mapper = DatexV35JSONRealtimeExportMapper()

    def get_datex2_payload(self, search_query: LocationApiSearchQuery) -> DATEXII3D2StaticPayloadInput:
        locations = self.location_repository.fetch_locations(search_query=search_query)

        return self.datex_static_export_mapper.map_locations_to_static_payload(locations)

    def get_datex2_realtime_payload(self, search_query: LocationApiSearchQuery) -> DATEXII3D2RealtimePayloadInput:
        locations = self.location_repository.fetch_locations(search_query=search_query)

        return self.datex_realtime_export_mapper.map_locations_to_realtime_payload(list(locations))
