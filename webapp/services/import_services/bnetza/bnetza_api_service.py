"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from celery.schedules import crontab
from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.bnetza.bnetza_api_validators import BnetzaChargingStation, BnetzaResponseInput
from webapp.services.import_services.models import LocationUpdate, SourceInfo


class BnetzaApiImportService(BaseImportService):
    schedule = crontab(day_of_week='1')

    response_validator = DataclassValidator(BnetzaResponseInput)
    charging_station_validator = DataclassValidator(BnetzaChargingStation)

    source_info = SourceInfo(
        uid='bnetza_api',
        name='Bundesnetzagentur',
        public_url='https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet'
        '/Ladesaeulenkarte/start.html',
        attribution_license='CC BY 4.0',
        attribution_url='https://creativecommons.org/licenses/by/4.0/deed.de',
        has_realtime_data=False,
    )

    def fetch_static_data(self):
        last_updated = datetime.now(tz=timezone.utc)

        response_data = self.remote_helper.get(
            url='https://ladesaeulenregister.bnetza.de/els/service/public/v1/chargepoints',
            headers={'Accept': 'application/json'},
        )

        response_input: BnetzaResponseInput = self.response_validator.validate(response_data)

        location_updates: list[LocationUpdate] = []
        for charging_station_dict in response_input.chargingStations:
            try:
                charging_station = self.charging_station_validator.validate(charging_station_dict)
            except ValidationError as e:
                self.logger.info(
                    'import-bnetza-api',
                    f'bnetza data {charging_station_dict} has validation error: {e.to_dict()}',
                )
                continue

            location_updates.append(charging_station.to_location_update(last_updated=last_updated))

        self.save_location_updates(location_updates)
