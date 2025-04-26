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
from datetime import datetime, timezone

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.contexts import TelemetryContext
from webapp.common.logging.models import LogMessageType
from webapp.common.remote_helper import RemoteServerType
from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService, SourceInfo

from .chargeit_mapper import ChargeitMapper
from .chargeit_validators import ChargeitInput, LocationInput

logger = logging.getLogger(__name__)


class ChargeitImportService(BaseImportService):
    chargit_mapper: ChargeitMapper = ChargeitMapper()
    chargeit_validator = DataclassValidator(ChargeitInput)
    location_validator = DataclassValidator(LocationInput)

    source_info = SourceInfo(
        uid='chargeit',
        name='LichtBlick SE',
        public_url='https://www.lichtblick.de',
        has_realtime_data=True,
    )

    def fetch_static_data(self):
        self.download_and_save()

    def fetch_realtime_data(self):
        self.download_and_save()

    def download_and_save(self):
        source = self.get_source()
        static_error_count = 0
        realtime_error_count = 0
        data_updated_at = datetime.now(tz=timezone.utc)

        input_dict = self.remote_helper.get(remote_server_type=RemoteServerType.CHARGEIT, path='/ps/rest/feed')

        try:
            input_data: ChargeitInput = self.chargeit_validator.validate(input_dict)
        except ValidationError as e:
            logger.error(
                f'chargeit data {input_dict} has validation error: {e.to_dict()}',
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
                static_error_count += 1
                realtime_error_count += 1
                continue

            # don't add unpublished location to list, then it will be removed afterwards if it still is in db
            if not location_input.published:
                continue

            location_updates.append(
                self.chargit_mapper.map_location_to_location_update(
                    operator_input=input_data.operator,
                    location_input=location_input,
                ),
            )

        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_error_count=static_error_count,
            realtime_error_count=realtime_error_count,
            static_data_updated_at=data_updated_at,
            realtime_data_updated_at=data_updated_at,
            static_status=SourceStatus.ACTIVE,
            realtime_status=SourceStatus.ACTIVE,
        )
