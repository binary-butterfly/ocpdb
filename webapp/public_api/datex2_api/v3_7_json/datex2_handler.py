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

from datetime import datetime, timezone

from webapp.models.evse import EvseStatus
from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.repositories import LocationRepository
from webapp.shared.datex2.models import (
    AgentOutput,
    DynamicInformationOutput,
    ExchangeContextOutput,
    ExchangeInformationOutput,
    ExchangeStatusEnum,
    ExchangeStatusEnumGOutput,
    MessageContainerOutput,
    MessageContainerWrapperOutput,
    ProtocolTypeEnum,
    ProtocolTypeEnumGOutput,
)
from webapp.shared.datex2.v3_7.realtime.d_a_t_e_x_i_i3_d2_payload_output import (
    DATEXII3D2PayloadOutput as DATEXII3D2RealtimePayloadOutput,
)
from webapp.shared.datex2.v3_7.static.d_a_t_e_x_i_i3_d2_payload_output import (
    DATEXII3D2PayloadOutput as DATEXII3D2StaticPayloadOutput,
)
from webapp.shared.datex2.v3_7_realtime_export_mapper import DatexV37JSONRealtimeExportMapper
from webapp.shared.datex2.v3_7_static_export_mapper import DatexV37JSONStaticExportMapper
from webapp.shared.location_search_queries import LocationApiSearchQuery


class Datex2V37JSONHandler(PublicApiBaseHandler):
    location_repository: LocationRepository
    datex_static_export_mapper: DatexV37JSONStaticExportMapper
    datex_realtime_export_mapper: DatexV37JSONRealtimeExportMapper

    def __init__(self, *args, location_repository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository
        self.datex_static_export_mapper = DatexV37JSONStaticExportMapper()
        self.datex_realtime_export_mapper = DatexV37JSONRealtimeExportMapper()

    def get_datex2_payload(self, search_query: LocationApiSearchQuery) -> DATEXII3D2StaticPayloadOutput:
        locations = self.location_repository.fetch_locations(
            search_query=search_query,
            include_charging_stations=True,
            include_evses=True,
            include_connectors=True,
            include_tariffs=True,
            include_operators=True,
        )

        return self.datex_static_export_mapper.map_locations_to_static_payload(list(locations))

    def get_datex2_realtime_payload(self, search_query: LocationApiSearchQuery) -> DATEXII3D2RealtimePayloadOutput:
        search_query.exclude_evse_status = [EvseStatus.STATIC]
        locations = self.location_repository.fetch_locations(
            search_query=search_query,
            include_charging_stations=True,
            include_evses=True,
        )

        return self.datex_realtime_export_mapper.map_locations_to_realtime_payload(list(locations))

    def get_datex2_mobilithek_realtime(self, search_query: LocationApiSearchQuery) -> MessageContainerWrapperOutput:
        search_query.exclude_evse_status = [EvseStatus.STATIC]
        locations = self.location_repository.fetch_locations(
            search_query=search_query,
            include_charging_stations=True,
            include_evses=True,
        )
        payload_result = self.datex_realtime_export_mapper.map_locations_to_realtime_payload(locations)

        if search_query.evse_status_last_updated_since is None:
            protocol_type = ProtocolTypeEnum.SNAPSHOT_PUSH
        else:
            protocol_type = ProtocolTypeEnum.DELTA_PUSH

        message_container = MessageContainerOutput(
            payload=[payload_result.payload],
            exchangeInformation=ExchangeInformationOutput(
                exchangeContext=ExchangeContextOutput(
                    codedExchangeProtocol=ProtocolTypeEnumGOutput(
                        value=protocol_type,
                    ),
                    exchangeSpecificationVersion='3.7',
                    supplierOrCisRequester=AgentOutput(
                        name=self.config_helper.get('MOBILITHEK_NAME'),
                    ),
                ),
                dynamicInformation=DynamicInformationOutput(
                    exchangeStatus=ExchangeStatusEnumGOutput(
                        value=ExchangeStatusEnum.ONLINE,
                    ),
                    messageGenerationTimestamp=datetime.now(tz=timezone.utc),
                ),
            ),
        )

        return MessageContainerWrapperOutput(
            message_container=message_container,
        )
