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

import logging
from abc import ABC
from datetime import datetime, timezone

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.contexts import TelemetryContext
from webapp.common.error_handling.exceptions import RemoteException
from webapp.common.logging.models import LogMessageType
from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService, SourceInfo

from .lichtblick_mapper import LichtblickMapper
from .lichtblick_validators import LichtblickInput, LocationInput

logger = logging.getLogger(__name__)


class LichtblickImportService(BaseImportService, ABC):
    chargit_mapper: LichtblickMapper = LichtblickMapper()
    lichtblick_validator = DataclassValidator(LichtblickInput)
    location_validator = DataclassValidator(LocationInput)

    required_config_keys: list[str] = ['user', 'password']

    source_info = SourceInfo(
        uid='lichtblick',
        name='Lichtblick',
        public_url='https://www.lichtblick.de',
        source_url='https://portal.lichtblick-emobility.de',
        has_realtime_data=True,
    )

    def fetch_static_data(self):
        self.download_and_save()

    def fetch_realtime_data(self):
        self.download_and_save()

    def download_and_save(self):
        source = self.get_source()
        success_count = 0
        error_count = 0
        data_updated_at = datetime.now(tz=timezone.utc)
        try:
            input_dict = self.json_request()
        except RemoteException as e:
            logger.error(
                f'lichtblick request failed: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(
                source=source,
                static_status=SourceStatus.FAILED,
                realtime_status=SourceStatus.FAILED,
            )
            return

        try:
            input_data: LichtblickInput = self.lichtblick_validator.validate(input_dict)
        except ValidationError as e:
            logger.error(
                f'lichtblick data {input_dict} has validation error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(
                source=source,
                static_status=SourceStatus.FAILED,
                realtime_status=SourceStatus.FAILED,
            )
            return

        location_updates = []
        for location_dict in input_data.operator.operatorPlaces:
            try:
                location_input: LocationInput = self.location_validator.validate(location_dict)
            except ValidationError as e:
                logger.warning(
                    f'location {location_dict} has validation error: {e.to_dict()}',
                    extra={
                        'attributes': {
                            'type': LogMessageType.IMPORT_LOCATION,
                            TelemetryContext.LOCATION: location_dict.get('shortcode'),
                        },
                    },
                )
                error_count += 1
                continue

            # don't add unpublished location to list, then it will be removed afterwards if it still is in db
            if not location_input.published:
                continue

            location_update = self.chargit_mapper.map_location_to_location_update(
                operator_input=input_data.operator,
                location_input=location_input,
            )
            location_updates.append(location_update)
            success_count += 1

        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_error_count=error_count,
            realtime_error_count=error_count,
            static_data_updated_at=data_updated_at,
            realtime_data_updated_at=data_updated_at,
            static_status=SourceStatus.ACTIVE,
            realtime_status=SourceStatus.ACTIVE,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} static and realtime with {success_count} valid '
            f'locations and {error_count} failed locations. .',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )
