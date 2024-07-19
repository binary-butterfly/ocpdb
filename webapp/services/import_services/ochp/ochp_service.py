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

from typing import Dict, List

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService, SourceInfo

from .ochp_api_client import OchpApiClient
from .ochp_mapper import OchpMapper
from .ochp_validators import ChargePointInput, ChargePointStatusInput


class OchpImportService(BaseImportService):
    ochp_api_client: OchpApiClient
    charge_point_validator = DataclassValidator(ChargePointInput)
    charge_point_status_validator = DataclassValidator(ChargePointStatusInput)

    ochp_mapper = OchpMapper()

    source_info = SourceInfo(
        uid='ochp',
        name='Ladenetz',
        public_url='https://ladenetz.de',
        has_realtime_data=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ochp_api_client = OchpApiClient(
            remote_helper=self.remote_helper,
            config_helper=self.config_helper,
        )

    def base_load_and_save(self):
        source = self.get_source()
        static_error_count = 0

        chargepoints_by_location: Dict[str, List[ChargePointInput]] = {}
        try:
            ochp_chargepoint_dicts = self.ochp_api_client.download_base_data()
        except ValidationError as e:
            self.logger.info('import-ochp', f'ochp static data has validation error: {e.to_dict()}')
            self.update_source(source, static_status=SourceStatus.FAILED)
            return
        for ochp_chargepoint_dict in ochp_chargepoint_dicts:
            try:
                ochp_chargepoint: ChargePointInput = self.charge_point_validator.validate(ochp_chargepoint_dict)
            except ValidationError as e:
                self.logger.info(
                    'import-ochp',
                    f'evse status {ochp_chargepoint_dict} has validation error: {e.to_dict()}',
                )
                static_error_count += 1
                continue
            if ochp_chargepoint.locationId not in chargepoints_by_location.keys():
                chargepoints_by_location[ochp_chargepoint.locationId] = []
            chargepoints_by_location[ochp_chargepoint.locationId].append(ochp_chargepoint)

        location_updates = []
        for ochp_chargepoints in chargepoints_by_location.values():
            location_updates.append(self.ochp_mapper.map_chargepoint_to_location_update(ochp_chargepoints))

        self.save_location_updates(location_updates)

        self.update_source(source=source, static_error_count=static_error_count)

    def live_load_and_save(self, full_sync: bool = False):
        source = self.get_source()
        if source.static_status == SourceStatus.FAILED:
            return
        realtime_error_count = 0

        try:
            evse_status_dicts = self.ochp_api_client.download_live_data(
                last_update=None if full_sync is True else source.realtime_data_updated_at,
            )
        except ValidationError as e:
            self.logger.info('import-ochp', f'ochp realtime data has validation error: {e.to_dict()}')
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
                    'import-ochp',
                    f'evse status {evse_status_dict} has validation error: {e.to_dict()}',
                )
                realtime_error_count += 1
                continue
            evse_update = self.ochp_mapper.map_evse_status_to_update(evse_status_input)
            evse_updates.append(evse_update)

        self.save_evse_updates(evse_updates)

        self.update_source(source=source, realtime_error_count=realtime_error_count)
