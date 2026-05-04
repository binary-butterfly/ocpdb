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
from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime, parsedate_to_datetime

from validataclass.exceptions import ValidationError
from validataclass.helpers import UnsetValue
from validataclass.validators import DataclassValidator

from webapp.common.error_handling.exceptions import RemoteException
from webapp.common.logging.models import LogMessageType
from webapp.common.rest.exceptions import IncompleteConfigException
from webapp.models import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.exceptions import ImportException
from webapp.services.import_services.models import EvseRealtimeUpdate, LocationUpdate
from webapp.shared.datex2.v3_7.realtime.d_a_t_e_x_i_i3_d2_payload_input import (
    DATEXII3D2PayloadInput as DATEXII3D2RealtimePayloadInput,
)
from webapp.shared.datex2.v3_7.static.d_a_t_e_x_i_i3_d2_payload_input import (
    DATEXII3D2PayloadInput as DATEXII3D2StaticPayloadInput,
)

from .datex2_v3_7_json_static_mapper import Datex2V37JSONStaticMapper

logger = logging.getLogger(__name__)


@dataclass(kw_only=True)
class RealtimeResult:
    realtime_error_count: int = 0
    realtime_success_count: int = 0
    evse_updates_by_evse: dict[str, EvseRealtimeUpdate] = field(default_factory=dict)


class BaseDatex2V37ImportService(BaseImportService, ABC):
    v3_7_json_static_datex_validator = DataclassValidator(DATEXII3D2StaticPayloadInput)
    v3_7_json_realtime_datex_validator = DataclassValidator(DATEXII3D2RealtimePayloadInput)
    v3_7_json_static_datex_mapper = Datex2V37JSONStaticMapper()

    def fetch_static_data(self):
        subscription_id: int | None = self.config.get('static_subscription_id')
        if subscription_id is None:
            raise IncompleteConfigException(message='Missing static_subscription_id in config')

        data, last_modified = self.request_data(subscription_id)
        # Hack to support invalid MessageContainer
        if 'messageContainer' in data:
            data = {'payload': data['messageContainer']['payload'][0]}

        source = self.get_source()
        error_count = 0
        success_count = 0
        location_updates: list[LocationUpdate] = []

        try:
            datex_input: DATEXII3D2StaticPayloadInput = self.v3_7_json_static_datex_validator.validate(data)
        except ValidationError as e:
            logger.error(
                f'missing payload or aegiEnergyInfrastructureTablePublication in {self.source_info.uid} static data {data}: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        if (
            datex_input.payload is UnsetValue
            or datex_input.payload.aegiEnergyInfrastructureTablePublication is UnsetValue
            or len(datex_input.payload.aegiEnergyInfrastructureTablePublication.energyInfrastructureTable) != 1
        ):
            logger.error(
                f'missing payload or aegiEnergyInfrastructureTablePublication in {self.source_info.uid} static data {data}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        publication_input = datex_input.payload.aegiEnergyInfrastructureTablePublication.energyInfrastructureTable[0]

        for energy_infrastructure_site_input in publication_input.energyInfrastructureSite:
            location_update = self.v3_7_json_static_datex_mapper.map_energy_infrastructure_site_to_location(
                self.source_info.uid,
                energy_infrastructure_site_input,
            )
            if location_update is None:
                error_count += 1
                continue
            location_updates.append(location_update)
            success_count += 1

        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_status=SourceStatus.ACTIVE,
            static_error_count=error_count,
            static_data_updated_at=last_modified,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} static data with {success_count} valid '
            f'locations and {error_count} failed locations.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def fetch_realtime_data(self):
        source = self.get_source()
        last_modified = datetime.now(tz=timezone.utc)

        if source.static_status != SourceStatus.ACTIVE:
            return

        if self.config.get('use_realtime_push'):
            return

        subscription_id: int | None = self.config.get('realtime_subscription_id')
        if subscription_id is None:
            raise IncompleteConfigException(message='Missing static_subscription_id in config')

        source = self.get_source()
        result = RealtimeResult()

        counter = 0
        if source.realtime_data_updated_at:
            if_modified_since = source.realtime_data_updated_at.replace(tzinfo=timezone.utc)
        else:
            if_modified_since = datetime.now(tz=timezone.utc) - timedelta(hours=1)

        while counter < 25000:
            try:
                data, last_modified = self.request_data(subscription_id, if_modified_since)
            except RemoteException as e:
                logger.error(
                    f'Datex2 realtime request failed: {e.to_dict()}. Text: {e.data}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                self.update_source(source, realtime_status=SourceStatus.FAILED)
                return

            if not last_modified:
                logger.error(
                    f'Missing Last-Modified header in {self.source_info.uid} realtime data.',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                self.update_source(source, realtime_status=SourceStatus.FAILED)
                return

            try:
                self.add_realtime_data(data, result)
            except ImportException as e:
                logger.error(
                    e.message,
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                self.update_source(source, realtime_status=SourceStatus.FAILED)
                return

            logger.info(
                f'Got realtime data from {last_modified}',
                extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
            )

            if if_modified_since == last_modified:
                break

            counter += 1
            if_modified_since = last_modified

        self.save_evse_updates(list(result.evse_updates_by_evse.values()))

        self.update_source(
            source=source,
            realtime_status=SourceStatus.ACTIVE,
            realtime_error_count=result.realtime_error_count,
            realtime_data_updated_at=last_modified,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} realtime with {result.realtime_success_count} valid '
            f'EVSEs and {result.realtime_error_count} failed EVSEs.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def add_realtime_data(self, data: dict, result: RealtimeResult) -> DATEXII3D2RealtimePayloadInput:
        try:
            datex_input: DATEXII3D2RealtimePayloadInput = self.v3_7_json_realtime_datex_validator.validate(data)
        except ValidationError as e:
            raise ImportException(
                message=f'missing payload in {self.source_info.uid} realtime data',
            ) from e

        if datex_input.payload is UnsetValue:
            raise ImportException(
                message=f'missing payload in {self.source_info.uid} realtime data',
            )

        payload = datex_input.payload
        if (
            payload.aegiEnergyInfrastructureStatusPublication is UnsetValue
            or payload.aegiEnergyInfrastructureStatusPublication.energyInfrastructureSiteStatus is UnsetValue
        ):
            raise ImportException(
                message=f'missing aegiEnergyInfrastructureStatusPublication in {self.source_info.uid} realtime data',
            )

        for site_status in payload.aegiEnergyInfrastructureStatusPublication.energyInfrastructureSiteStatus:
            if site_status.energyInfrastructureStationStatus is UnsetValue:
                continue
            for station_status in site_status.energyInfrastructureStationStatus:
                if station_status.refillPointStatus is UnsetValue:
                    continue
                for refill_point_status_g in station_status.refillPointStatus:
                    evse_update = self.v3_7_json_static_datex_mapper.map_energy_infrastructure_station_status(
                        refill_point_status_g,
                    )
                    if evse_update is None:
                        result.realtime_error_count += 1
                        continue
                    result.evse_updates_by_evse[evse_update.evse_id] = evse_update
                    result.realtime_success_count += 1

        return datex_input

    def request_data(
        self,
        subscription_id: int,
        if_modified_since: datetime | None = None,
    ) -> tuple[dict, datetime | None]:
        url = f'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID={subscription_id}'
        headers: dict[str, str] = {}

        if if_modified_since:
            headers['If-Modified-Since'] = format_datetime(if_modified_since, usegmt=True)

        response = self.request(
            url=url,
            headers=headers,
            cert=(
                self.config.get('mobilithek_cert_path'),
                self.config.get('mobilithek_key_path'),
            ),
        )
        last_modified_string = response.headers.get('Last-Modified')

        if last_modified_string is None:
            return response.json(), None

        return response.json(), parsedate_to_datetime(last_modified_string)
