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

from datetime import datetime, time, timezone, timedelta
from typing import Dict, List

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.services.import_services.base_import_service import BaseImportService
from .ochp_api_client import OchpApiClient
from .ochp_mapper import OchpMapper
from .ochp_validators import ChargePointInput, ChargePointStatusInput


class OchpImportService(BaseImportService):
    ochp_api_client: OchpApiClient
    charge_point_validator: ChargePointInput = DataclassValidator(ChargePointInput)
    charge_point_status_validator: ChargePointStatusInput = DataclassValidator(ChargePointStatusInput)

    ochp_mapper = OchpMapper()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ochp_api_client = OchpApiClient(
            remote_helper=self.remote_helper,
            config_helper=self.config_helper,
        )

    def base_load_and_save(self):
        chargepoints_by_location: Dict[str, List[ChargePointInput]] = {}
        for item in self.ochp_api_client.download_base_data():
            try:
                ochp_chargepoint = self.charge_point_validator.validate(item)
            except ValidationError as e:
                # TODO: error handling
                continue
            if ochp_chargepoint.locationId not in chargepoints_by_location.keys():
                chargepoints_by_location[ochp_chargepoint.locationId] = []
            chargepoints_by_location[ochp_chargepoint.locationId].append(ochp_chargepoint)

        location_updates = []
        for location_uid, ochp_chargepoints in chargepoints_by_location.items():
            location_updates.append(self.ochp_mapper.map_chargepoint_to_location_update(ochp_chargepoints))

        self.save_location_updates(location_updates, 'ochp')

    def live_load_and_save(self, full_sync: bool = False):
        last_downloaded = self.option_repository.get('ochp_status_last_downloaded') if not full_sync else None
        if last_downloaded:
            last_downloaded = last_downloaded - timedelta(minutes=5)

        evse_status_dicts = self.ochp_api_client.download_live_data(last_downloaded)
        evse_updates = []

        for evse_status_dict in evse_status_dicts:
            try:
                evse_status_input = self.charge_point_status_validator.validate(evse_status_dict)
            except ValidationError:
                # TODO: error handling
                continue
            evse_update = self.ochp_mapper.map_evse_status_to_update(evse_status_input)
            evse_updates.append(evse_update)

        self.save_evse_updates('ochp', evse_updates)
        self.option_repository.set('ochp_status_last_downloaded', datetime.now(tz=timezone.utc), 'datetime')

