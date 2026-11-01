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
from datetime import datetime, timezone

from validataclass.exceptions import ValidationError
from validataclass.validators import AnythingValidator, DataclassValidator, ListValidator

from webapp.common.error_handling.exceptions import RemoteException
from webapp.common.logging.models import LogMessageType
from webapp.common.rest.exceptions import IncompleteConfigException
from webapp.models import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.models import EvseRealtimeUpdate, LocationUpdate, SourceInfo

from .eliso_validators import ElisoEvseStatusInput, ElisoLocationInput

logger = logging.getLogger(__name__)


class ElisoImportService(BaseImportService):
    """
    eliso publishes its AFIR data at the Mobilithek in a custom JSON format instead of DATEX II. Static data is a list
    of locations, realtime data is a snapshot of all EVSE statuses, with one entry per EVSE and price.
    """

    source_info = SourceInfo(
        uid='eliso',
        name='eliso',
        public_url='https://mobilithek.info/offers/843477276990078976',
        source_url='https://mobilithek.info/offers/843477276990078976',
        attribution_contributor='eliso GmbH',
        has_realtime_data=True,
    )

    list_validator = ListValidator(AnythingValidator(allowed_types=[dict]))
    location_validator = DataclassValidator(ElisoLocationInput)
    evse_status_validator = DataclassValidator(ElisoEvseStatusInput)

    def fetch_static_data(self):
        source = self.get_source()
        static_data_updated_at = datetime.now(tz=timezone.utc)

        try:
            location_dicts = self.list_validator.validate(self.request_data('static_subscription_id'))
        except (RemoteException, ValidationError) as e:
            logger.error(
                f'{self.source_info.uid} static data has error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED)
            return

        location_updates: list[LocationUpdate] = []
        error_count = 0
        for location_dict in location_dicts:
            try:
                location_input: ElisoLocationInput = self.location_validator.validate(location_dict)
            except ValidationError as e:
                logger.warning(
                    f'{self.source_info.uid} location has error: {e.to_dict()}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                error_count += 1
                continue
            location_updates.append(location_input.to_location_update(self.source_info.uid))

        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_status=SourceStatus.ACTIVE,
            static_error_count=error_count,
            static_data_updated_at=static_data_updated_at,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} static data with {len(location_updates)} valid '
            f'locations and {error_count} failed locations.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def fetch_realtime_data(self):
        source = self.get_source()
        if source.static_status != SourceStatus.ACTIVE:
            return

        realtime_data_updated_at = datetime.now(tz=timezone.utc)

        try:
            data = self.request_data('realtime_subscription_id')
            if not isinstance(data, dict):
                raise ValidationError(reason='realtime data is no object')
            evse_status_dicts = self.list_validator.validate(data.get('evses'))
        except (RemoteException, ValidationError) as e:
            logger.error(
                f'{self.source_info.uid} realtime data has error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, realtime_status=SourceStatus.FAILED)
            return

        # There is one entry per EVSE and price, all with the same status
        evse_updates_by_uid: dict[str, EvseRealtimeUpdate] = {}
        error_count = 0
        for evse_status_dict in evse_status_dicts:
            try:
                evse_status_input: ElisoEvseStatusInput = self.evse_status_validator.validate(evse_status_dict)
            except ValidationError as e:
                logger.warning(
                    f'{self.source_info.uid} EVSE status has error: {e.to_dict()}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                error_count += 1
                continue
            evse_updates_by_uid[evse_status_input.evseId] = evse_status_input.to_evse_realtime_update()

        self.save_evse_updates(list(evse_updates_by_uid.values()))

        self.update_source(
            source=source,
            realtime_status=SourceStatus.ACTIVE,
            realtime_error_count=error_count,
            realtime_data_updated_at=realtime_data_updated_at,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} realtime data with {len(evse_updates_by_uid)} valid EVSEs '
            f'and {error_count} failed EVSEs.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def request_data(self, subscription_config_key: str) -> dict | list:
        subscription_id: int | None = self.config.get(subscription_config_key)
        if subscription_id is None:
            raise IncompleteConfigException(message=f'Missing {subscription_config_key} in config')

        return self.json_request(
            url=f'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription?subscriptionID={subscription_id}',
            cert=(
                self.config.get('mobilithek_cert_path'),
                self.config.get('mobilithek_key_path'),
            ),
        )
