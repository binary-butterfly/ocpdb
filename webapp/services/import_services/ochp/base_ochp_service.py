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

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Dict, List

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.remote_helper import RemoteException, RemoteServer, RemoteServerType
from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService

from .ochp_api_client import OchpApiClient
from .ochp_mapper import OchpMapper
from .ochp_validators import ChargePointInput, ChargePointStatusInput


class BaseOchpImportService(BaseImportService, ABC):
    ochp_api_client: OchpApiClient
    remote_server: RemoteServer

    charge_point_validator = DataclassValidator(ChargePointInput)
    charge_point_status_validator = DataclassValidator(ChargePointStatusInput)

    ochp_mapper: OchpMapper

    @property
    @abstractmethod
    def remote_server_type(self) -> RemoteServerType:
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ochp_mapper = OchpMapper()
        if self.remote_server_type not in self.config_helper.get('REMOTE_SERVERS'):
            return
        self.remote_server = self.config_helper.get('REMOTE_SERVERS')[self.remote_server_type]
        self.ochp_api_client = OchpApiClient(
            remote_helper=self.remote_helper,
            remote_server=self.remote_server,
        )

    def fetch_static_data(self):
        source = self.get_source()
        static_error_count = 0

        chargepoints_by_location: Dict[str, List[ChargePointInput]] = {}
        try:
            ochp_chargepoint_dicts = self.ochp_api_client.download_base_data()
        except (ValidationError, RemoteException) as e:
            self.logger.info('import-ochp', f'ochp static data has error: {e.to_dict()}')
            self.update_source(source, static_status=SourceStatus.FAILED)
            return
        for ochp_chargepoint_dict in ochp_chargepoint_dicts:
            try:
                ochp_chargepoint: ChargePointInput = self.charge_point_validator.validate(ochp_chargepoint_dict)
            except ValidationError as e:
                self.logger.info(
                    f'import-{self.source_info.uid}',
                    f'evse status {ochp_chargepoint_dict} has validation error: {e.to_dict()}',
                )
                static_error_count += 1
                continue

            if ochp_chargepoint.locationId not in chargepoints_by_location.keys():
                chargepoints_by_location[ochp_chargepoint.locationId] = []
            chargepoints_by_location[ochp_chargepoint.locationId].append(ochp_chargepoint)

        location_updates = []
        for ochp_chargepoints in chargepoints_by_location.values():
            location_updates.append(
                self.ochp_mapper.map_chargepoint_to_location_update(
                    source_uid=self.source_info.uid,
                    charge_point_inputs=ochp_chargepoints,
                ),
            )

        self.save_location_updates(location_updates)

        self.update_source(source=source, static_error_count=static_error_count)

        # Do a full realtime sync for an initial set of status data
        self.fetch_realtime_data(full_sync=True)

    def fetch_realtime_data(self, full_sync: bool = False):
        source = self.get_source()
        if source.static_status == SourceStatus.FAILED:
            return
        realtime_error_count = 0
        realtime_data_updated_at = datetime.now(timezone.utc)

        try:
            evse_status_dicts = self.ochp_api_client.download_live_data(
                last_update=None if full_sync is True else source.realtime_data_updated_at,
            )
        except (ValidationError, RemoteException) as e:
            self.logger.info(
                f'import-{self.source_info.uid}',
                f'ochp realtime data has error: {e.to_dict()}',
            )
            self.update_source(source, realtime_status=SourceStatus.FAILED)
            return

        evse_updates = []

        for evse_status_dict in evse_status_dicts:
            try:
                evse_status_input: ChargePointStatusInput = self.charge_point_status_validator.validate(
                    evse_status_dict,
                )
            except ValidationError as e:
                self.logger.info(
                    f'import-{self.source_info.uid}',
                    f'evse status {evse_status_dict} has validation error: {e.to_dict()}',
                )
                realtime_error_count += 1
                continue

            evse_update = self.ochp_mapper.map_evse_status_to_update(evse_status_input)

            evse_updates.append(evse_update)

        self.save_evse_updates(evse_updates)

        self.update_source(
            source=source,
            realtime_error_count=realtime_error_count,
            realtime_data_updated_at=realtime_data_updated_at,
        )
