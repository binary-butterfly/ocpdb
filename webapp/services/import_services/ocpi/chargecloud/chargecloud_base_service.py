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
from abc import ABC, abstractmethod

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.contexts import TelemetryContext
from webapp.common.logging.models import LogMessageType
from webapp.common.remote_helper import RemoteException, RemoteServerType
from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.ocpi.ocpi_mapper import OcpiMapper
from webapp.services.import_services.ocpi.ocpi_validators import OcpiInput

from .chargecloud_validators import ChargecloudLocationInput

logger = logging.getLogger(__name__)


class ChargecloudBaseImportService(BaseImportService, ABC):
    ocpi_validator = DataclassValidator(OcpiInput)
    location_validator = DataclassValidator(ChargecloudLocationInput)
    ocpi_mapper = OcpiMapper()

    @property
    @abstractmethod
    def remote_server_type(self) -> RemoteServerType: ...

    def fetch_static_data(self):
        self.download_and_save()

    def fetch_realtime_data(self):
        self.download_and_save()

    def download_and_save(self):
        source = self.get_source()
        try:
            input_dict = self.remote_helper.get(
                remote_server_type=self.remote_server_type,
            )
        except RemoteException as e:
            logger.error(
                f'request failed: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return
        static_error_count: int = 0
        realtime_error_count: int = 0

        try:
            input_data: OcpiInput = self.ocpi_validator.validate(input_dict)
        except ValidationError as e:
            logger.error(
                f'data {input_dict} has validation error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        location_updates = []
        for location_dict in input_data.data:
            try:
                location_input: ChargecloudLocationInput = self.location_validator.validate(location_dict)
            except ValidationError as e:
                logger.warning(
                    f'location {location_dict} has validation error: {e.to_dict()}',
                    extra={
                        'attributes': {
                            'type': LogMessageType.IMPORT_LOCATION,
                            TelemetryContext.LOCATION: location_dict.get('id'),
                        },
                    },
                )
                static_error_count += 1
                realtime_error_count += 1
                continue
            location_updates.append(self.ocpi_mapper.map_location(location_input, self.source_info.uid))

        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_error_count=static_error_count,
            realtime_error_count=realtime_error_count,
        )
