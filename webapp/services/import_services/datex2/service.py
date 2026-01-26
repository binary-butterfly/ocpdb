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
from datetime import datetime, timezone

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.logging.models import LogMessageType
from webapp.models import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.datex2.german_mapper import GermanStaticDatexMapper
from webapp.services.import_services.datex2.german_static.d_a_t_e_x_i_i3_d2_payload_input import DATEXII3D2PayloadInput
from webapp.services.import_services.datex2.german_static.energy_infrastructure_site_input import (
    EnergyInfrastructureSiteInput,
)
from webapp.services.import_services.models import LocationUpdate, SourceInfo

logger = logging.getLogger(__name__)


class EnBWDatex2ImportService(BaseImportService):
    german_static_datex_validator = DataclassValidator(DATEXII3D2PayloadInput)
    energy_infrastructure_site_validator = DataclassValidator(EnergyInfrastructureSiteInput)
    german_static_datex_mapper = GermanStaticDatexMapper()

    source_info = SourceInfo(
        uid='datex2_enbw',
        name='EnBW Datex II',
        public_url='https://mobilithek.info/offers/907574882292453376',
        source_url='https://mobilithek.info/offers/907574882292453376',
        attribution_contributor='EnBW AG',
        attribution_license='CC BY 4.0',
        has_realtime_data=True,
    )

    def fetch_static_data(self):
        source = self.get_source()
        error_count = 0
        success_count = 0
        location_updates: list[LocationUpdate] = []
        static_data_updated_at = datetime.now(timezone.utc)
        data = self.request_data(self.config.get('static_subscription_id'))

        # with open('/app/tests/integration/services/import_services/datex2/data/datex2_enbw_reduced.json', 'r', encoding='utf-8') as f:
        #    data = json.loads(f.read())

        try:
            datex_input = self.german_static_datex_validator.validate(data)
        except ValidationError as e:
            logger.error(
                f'missing payload or aegiEnergyInfrastructureTablePublication in datex2_enbw static data {data}: {e.to_dict()}',
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
                f'missing payload or aegiEnergyInfrastructureTablePublication in datex2_enbw static data {data}',
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
                    f'opendata swiss EVSEDataRecord {energy_infrastructure_site_dict} has error: {e.to_dict()}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                error_count += 1
                continue

            location_update = self.german_static_datex_mapper.map_energy_infrastructure_site_to_location(
                self.source_info.uid, energy_infrastructure_site_input
            )
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
