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
from webapp.common.error_handling.exceptions import RemoteException
from webapp.common.logging.models import LogMessageType
from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService, SourceInfo
from webapp.services.import_services.models import EvseUpdate, LocationUpdate

from .giroe_mapper import GiroeMapper
from .giroe_validator import ConnectorInput, ItemListInput, LocationInput

logger = logging.getLogger(__name__)


class GiroeImportService(BaseImportService):
    giroe_mapper: GiroeMapper
    item_list_validator = DataclassValidator(ItemListInput)
    location_validator = DataclassValidator(LocationInput)
    connector_validator = DataclassValidator(ConnectorInput)

    required_config_keys: list[str] = ['user', 'password']

    source_info = SourceInfo(
        uid='giroe',
        name='GLS Mobility GmbH',
        public_url='https://www.gls-mobility.de',
        has_realtime_data=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.giroe_mapper = GiroeMapper(config_helper=self.config_helper)

    def fetch_static_data(self):
        source = self.get_source()
        location_updates: list[LocationUpdate] = []
        static_success_count = 0
        static_error_count = 0
        static_data_updated_at = datetime.now(timezone.utc)

        try:
            location_list_data = self.json_request(
                path='/api/server/v1/charge-locations',
                params={
                    'technical_backend': 'tcc',
                    'public': True,
                },
                auth=(self.config.get('user'), self.config.get('password')),
            )
            location_list_input: ItemListInput = self.item_list_validator.validate(location_list_data)
        except (ValidationError, RemoteException) as e:
            logger.error(
                f'giro-e static data has error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED)
            return

        location_dicts: list[dict] = location_list_input.items

        while location_list_input.next_path:
            try:
                location_list_data = self.json_request(
                    path=location_list_input.next_path,
                    auth=(self.config.get('user'), self.config.get('password')),
                )
                location_list_input: ItemListInput = self.item_list_validator.validate(location_list_data)
                location_dicts += location_list_input.items
            except (ValidationError, RemoteException) as e:
                logger.error(
                    f'giro-e static data has error: {e.to_dict()}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                self.update_source(source, static_status=SourceStatus.FAILED)
                return

        for location_dict in location_dicts:
            try:
                location_input: LocationInput = self.location_validator.validate(location_dict)
            except ValidationError as e:
                logger.warning(
                    f'location {location_dict} has validation error: {e.to_dict()}',
                    extra={
                        'attributes': {
                            'type': LogMessageType.IMPORT_LOCATION,
                            'location_dict': location_dict.get('id'),
                        },
                    },
                )
                static_error_count += 1
                continue

            location_updates.append(self.giroe_mapper.map_location_input_to_update(location_input))
            static_success_count += 1

        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_status=SourceStatus.ACTIVE,
            static_error_count=static_error_count,
            static_data_updated_at=static_data_updated_at,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} static with {static_success_count} valid locations and '
            f'{static_error_count} failed locations.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def fetch_realtime_data(self):
        source = self.get_source()
        # Don't fetch realtime updates if there is no static data
        if source.static_status != SourceStatus.ACTIVE:
            return

        evse_updates: list[EvseUpdate] = []
        realtime_success_count = 0
        realtime_error_count = 0
        realtime_data_updated_at = datetime.now(timezone.utc)

        params = {
            'technical_backend': 'tcc',
            'public': True,
        }
        if source.realtime_data_updated_at:
            params['modified_since'] = source.realtime_data_updated_at.isoformat()
        try:
            connector_list_data = self.json_request(
                path='/api/server/v1/charge-connectors',
                params=params,
                auth=(self.config.get('user'), self.config.get('password')),
            )
            connector_list_input: ItemListInput = self.item_list_validator.validate(connector_list_data)
        except (ValidationError, RemoteException) as e:
            logger.error(
                f'giro-e realtime data has error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, realtime_status=SourceStatus.FAILED)
            return

        connector_dicts: list[dict] = connector_list_input.items

        while connector_list_input.next_path:
            try:
                connector_list_data = self.json_request(
                    path=connector_list_input.next_path,
                    auth=(self.config.get('user'), self.config.get('password')),
                )
                connector_list_input: ItemListInput = self.item_list_validator.validate(connector_list_data)
                connector_dicts += connector_list_input.items
            except (ValidationError, RemoteException) as e:
                logger.error(
                    f'giro-e realtime data has error: {e.to_dict()}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                self.update_source(source, realtime_status=SourceStatus.FAILED)
                return

        for connector_dict in connector_dicts:
            try:
                connector_input: ConnectorInput = self.connector_validator.validate(connector_dict)
            except ValidationError as e:
                logger.warning(
                    f'connector {connector_dict} has validation error: {e.to_dict()}',
                    extra={
                        'attributes': {
                            'type': LogMessageType.IMPORT_EVSE,
                            TelemetryContext.EVSE: connector_dict.get('uid'),
                        },
                    },
                )
                realtime_error_count += 1
                continue

            evse_updates.append(
                EvseUpdate(
                    uid=connector_input.uid,
                    evse_id=connector_input.uid,
                    last_updated=connector_input.modified,
                ),
            )

        self.save_evse_updates(evse_updates)

        self.update_source(
            source=source,
            realtime_status=SourceStatus.ACTIVE,
            realtime_error_count=realtime_error_count,
            realtime_data_updated_at=realtime_data_updated_at,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} realtime with {realtime_success_count} valid locations '
            f'and {realtime_error_count} failed locations.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )
