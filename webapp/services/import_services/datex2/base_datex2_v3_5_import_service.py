"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2024 binary butterfly GmbH

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
from datetime import datetime, timezone

from validataclass.exceptions import ValidationError
from validataclass.helpers import UnsetValue
from validataclass.validators import DataclassValidator

from webapp.common.logging.models import LogMessageType
from webapp.models import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.datex2.german_mapper import GermanStaticDatexMapper
from webapp.services.import_services.models import LocationUpdate
from webapp.shared.datex2.v3_5_json_realtime.d_a_t_e_x_i_i3_d2_payload_input import (
    DATEXII3D2PayloadInput as DATEXII3D2RealtimePayloadInput,
)
from webapp.shared.datex2.v3_5_json_realtime.energy_infrastructure_station_status_input import (
    EnergyInfrastructureStationStatusInput,
)
from webapp.shared.datex2.v3_5_json_static.d_a_t_e_x_i_i3_d2_payload_input import (
    DATEXII3D2PayloadInput as DATEXII3D2StaticPayloadInput,
)
from webapp.shared.datex2.v3_5_json_static.energy_infrastructure_site_input import EnergyInfrastructureSiteInput

logger = logging.getLogger(__name__)


class BaseDatex2V35ImportService(BaseImportService, ABC):
    v3_5_json_static_datex_validator = DataclassValidator(DATEXII3D2StaticPayloadInput)
    v3_5_json_realtime_datex_validator = DataclassValidator(DATEXII3D2RealtimePayloadInput)
    energy_infrastructure_site_validator = DataclassValidator(EnergyInfrastructureSiteInput)
    energy_infrastructure_station_status_validator = DataclassValidator(EnergyInfrastructureStationStatusInput)
    v3_5_json_static_datex_mapper = GermanStaticDatexMapper()

    def fetch_static_data(self):
        source = self.get_source()
        error_count = 0
        success_count = 0
        location_updates: list[LocationUpdate] = []
        static_data_updated_at = datetime.now(timezone.utc)
        data = self.request_data(self.config.get('static_subscription_id'))

        try:
            datex_input = self.v3_5_json_static_datex_validator.validate(data)
        except ValidationError as e:
            logger.error(
                f'missing payload or aegiEnergyInfrastructureTablePublication in {self.source_info.uid} static data {data}: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        if (
            not datex_input.payload
            or not datex_input.payload.aegiEnergyInfrastructureTablePublication
            or len(datex_input.payload.aegiEnergyInfrastructureTablePublication.energyInfrastructureTable) != 1
        ):
            logger.error(
                f'missing payload or aegiEnergyInfrastructureTablePublication in {self.source_info.uid} static data {data}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        publication_input = datex_input.payload.aegiEnergyInfrastructureTablePublication.energyInfrastructureTable[0]

        for energy_infrastructure_site_dict in publication_input.energyInfrastructureSite:
            try:
                energy_infrastructure_site_input = self.energy_infrastructure_site_validator.validate(
                    energy_infrastructure_site_dict
                )
            except ValidationError as e:
                logger.warning(
                    f'DATEX2 EnergyInfrastructureSite {energy_infrastructure_site_dict} has error: {e.to_dict()}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                error_count += 1
                continue

            location_update = self.v3_5_json_static_datex_mapper.map_energy_infrastructure_site_to_location(
                self.source_info.uid, energy_infrastructure_site_input
            )
            if location_update is None:
                continue
            location_updates.append(location_update)
            success_count += 1

        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_status=SourceStatus.ACTIVE,
            static_error_count=error_count,
            static_data_updated_at=static_data_updated_at,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} static data with {success_count} valid '
            f'locations and {error_count} failed locations.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def fetch_realtime_data(self):
        source = self.get_source()
        if source.static_status != SourceStatus.ACTIVE:
            return

        realtime_error_count = 0
        realtime_success_count = 0
        realtime_data_updated_at = datetime.now(timezone.utc)
        data = self.request_data(self.config.get('realtime_subscription_id'))

        try:
            realtime_data = {'payload': data['messageContainer']['payload'][0]}
        except (KeyError, IndexError, TypeError):
            logger.error(
                f'missing messageContainer or payload in {self.source_info.uid} realtime data',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, realtime_status=SourceStatus.FAILED)
            return

        try:
            datex_input = self.v3_5_json_realtime_datex_validator.validate(realtime_data)
        except ValidationError as e:
            logger.error(
                f'invalid {self.source_info.uid} realtime data: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, realtime_status=SourceStatus.FAILED)
            return

        if (
            datex_input.payload is UnsetValue
            or datex_input.payload.aegiEnergyInfrastructureStatusPublication is UnsetValue
            or datex_input.payload.aegiEnergyInfrastructureStatusPublication.energyInfrastructureSiteStatus
            is UnsetValue
        ):
            logger.error(
                f'missing payload or aegiEnergyInfrastructureStatusPublication in {self.source_info.uid} realtime data',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, realtime_status=SourceStatus.FAILED)
            return

        evse_updates = []
        for site_status in datex_input.payload.aegiEnergyInfrastructureStatusPublication.energyInfrastructureSiteStatus:
            if site_status.energyInfrastructureStationStatus is UnsetValue:
                continue
            for station_status_dict in site_status.energyInfrastructureStationStatus:
                try:
                    station_status = self.energy_infrastructure_station_status_validator.validate(station_status_dict)
                except ValidationError as e:
                    logger.warning(
                        f'DATEX2 EnergyInfrastructureStationStatus {station_status_dict} has error: {e.to_dict()}',
                        extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                    )
                    realtime_error_count += 1
                    continue
                if station_status.refillPointStatus is UnsetValue:
                    continue
                for refill_point_status_g in station_status.refillPointStatus:
                    evse_update = self.v3_5_json_static_datex_mapper.map_energy_infrastructure_station_status(
                        refill_point_status_g,
                    )
                    if evse_update is None:
                        realtime_error_count += 1
                        continue
                    evse_updates.append(evse_update)
                    realtime_success_count += 1

        self.save_evse_updates(evse_updates)

        self.update_source(
            source=source,
            realtime_status=SourceStatus.ACTIVE,
            realtime_error_count=realtime_error_count,
            realtime_data_updated_at=realtime_data_updated_at,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} realtime with {realtime_success_count} valid EVSEs '
            f'and {realtime_error_count} failed EVSEs.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def request_data(self, subscription_id: int) -> dict:
        url = f'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID={subscription_id}'
        return self.json_request(
            url=url,
            cert=(
                self.config.get('mobilithek_cert_path'),
                self.config.get('mobilithek_key_path'),
            ),
            fix_encoding=True,
        )
