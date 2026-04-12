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

import json
from datetime import datetime, timezone

import requests

from webapp.common.dataclass import filter_none_recursive, filter_unset_value, recursive_to_dict
from webapp.common.json import DefaultJSONEncoder
from webapp.common.redis import RedisHelper, RedisKeyNotFoundException
from webapp.repositories import LocationRepository
from webapp.services.base_service import BaseService
from webapp.shared.datex2.models import (
    AgentOutput,
    DynamicInformationOutput,
    ExchangeContextOutput,
    ExchangeInformationOutput,
    ExchangeStatusEnum,
    ExchangeStatusEnumGOutput,
    MessageContainerOutput,
    ProtocolTypeEnum,
    ProtocolTypeEnumGOutput,
)
from webapp.shared.datex2.v3_5_realtime_export_mapper import DatexV35JSONRealtimeExportMapper
from webapp.shared.datex2.v3_5_static_export_mapper import DatexV35JSONStaticExportMapper
from webapp.shared.datex2.v3_7_realtime_export_mapper import DatexV37JSONRealtimeExportMapper
from webapp.shared.datex2.v3_7_static_export_mapper import DatexV37JSONStaticExportMapper
from webapp.shared.location_search_queries import LocationSearchQuery


class ChargeLocationService(BaseService):
    location_repository: LocationRepository
    redis_helper: RedisHelper

    def __init__(
        self,
        *,
        location_repository: LocationRepository,
        redis_helper: RedisHelper,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.location_repository = location_repository
        self.redis_helper = redis_helper

    def push_datex_static(self) -> None:
        locations = self.location_repository.fetch_all_locations_with_children()

        version = self.config_helper.get('MOBILITHEK_VERSION', '3.5')
        if version == '3.7':
            mapper = DatexV37JSONStaticExportMapper()
            payload_result = mapper.map_locations_to_static_payload(locations)
        else:
            mapper = DatexV35JSONStaticExportMapper()
            payload_result = mapper.map_locations_to_static_payload(locations)

        data = self._build_message_container(
            payload=payload_result.payload,
            protocol_type=ProtocolTypeEnum.SNAPSHOT_PUSH,
        )
        self.push_to_mobilithek(
            data=data,
            subscription_id=self.config_helper.get('MOBILITHEK_STATIC_PUBLICATION_ID'),
        )

    def push_datex_realtime(self, updated_since: datetime | None = None, incremental_update: bool = False) -> None:
        datex_realtime_push = datetime.now(tz=timezone.utc)

        if incremental_update:
            try:
                updated_since = datetime.fromisoformat(self.redis_helper.get('last_datex_realtime_push'))
            except RedisKeyNotFoundException:
                ...

        search_query = LocationSearchQuery(
            evse_status_last_updated_since=updated_since,
        )

        locations = list(self.location_repository.fetch_locations(search_query=search_query))

        version = self.config_helper.get('MOBILITHEK_VERSION', '3.5')
        if version == '3.7':
            mapper = DatexV37JSONRealtimeExportMapper()
        else:
            mapper = DatexV35JSONRealtimeExportMapper()
        payload_result = mapper.map_locations_to_realtime_payload(locations)

        data = self._build_message_container(
            payload=payload_result.payload,
            protocol_type=ProtocolTypeEnum.DELTA_PUSH if updated_since else ProtocolTypeEnum.SNAPSHOT_PUSH,
        )
        self.push_to_mobilithek(
            data=data,
            subscription_id=self.config_helper.get('MOBILITHEK_REALTIME_PUBLICATION_ID'),
        )
        self.redis_helper.set('last_datex_realtime_push', datex_realtime_push.isoformat())

    def push_to_mobilithek(self, data: MessageContainerOutput, subscription_id: int) -> None:
        key_dir: str = self.config_helper.get('KEY_DIR')
        url = f'https://mobilithek.info:8443/mobilithek/api/v1.0/publication/{subscription_id}'
        response = requests.post(
            url=url,
            headers={'Content-Type': 'application/json'},
            cert=(
                f'{key_dir}/{self.config_helper.get("MOBILITHEK_CERTIFICATE_FILENAME")}',
                f'{key_dir}/{self.config_helper.get("MOBILITHEK_KEY_FILENAME")}',
            ),
            data=json.dumps(filter_none_recursive(filter_unset_value(recursive_to_dict(data))), cls=DefaultJSONEncoder),
            timeout=60,
        )
        response.raise_for_status()

    def _build_message_container(
        self,
        payload,
        protocol_type: ProtocolTypeEnum,
    ) -> MessageContainerOutput:
        version = self.config_helper.get('MOBILITHEK_VERSION', '3.5')
        return MessageContainerOutput(
            payload=payload,
            exchangeInformation=ExchangeInformationOutput(
                exchangeContext=ExchangeContextOutput(
                    codedExchangeProtocol=ProtocolTypeEnumGOutput(
                        value=protocol_type,
                    ),
                    exchangeSpecificationVersion=version,
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
