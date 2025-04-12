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

from webapp.common.remote_helper import RemoteHelper
from webapp.repositories import (
    ConnectorRepository,
    EvseRepository,
    LocationRepository,
    OptionRepository,
    SourceRepository,
)
from webapp.repositories.business_repository import BusinessRepository
from webapp.repositories.image_repository import ImageRepository
from webapp.services.base_service import BaseService
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.bnetza import BnetzaImportService
from webapp.services.import_services.chargeit import ChargeitImportService
from webapp.services.import_services.giroe import GiroeImportService
from webapp.services.import_services.ochp.albwerk import AlbwerkOchpImportService
from webapp.services.import_services.ochp.ladenetz import LadenetzOchpImportService
from webapp.services.import_services.ocpi.stadtnavi.stadtnavi_service import StadtnaviImportService
from webapp.services.import_services.ocpi.sw_stuttgart.sw_stuttgart_service import SWStuttgartImportService


class ImportServices(BaseService):
    bnetza_import_service: BnetzaImportService
    albwerk_ochp_import_service: AlbwerkOchpImportService
    ladenetz_ochp_import_service: LadenetzOchpImportService

    chargeit_import_service: ChargeitImportService
    giroe_import_service: GiroeImportService
    stadtnavi_import_service: StadtnaviImportService
    sw_stuttgart_import_service: SWStuttgartImportService

    importer_by_uid: dict[str, BaseImportService]

    def __init__(
        self,
        *,
        source_repository: SourceRepository,
        location_repository: LocationRepository,
        evse_repository: EvseRepository,
        connector_repository: ConnectorRepository,
        business_repository: BusinessRepository,
        image_repository: ImageRepository,
        option_repository: OptionRepository,
        remote_helper: RemoteHelper,
        **kwargs,
    ):
        super().__init__(**kwargs)

        default_dependencies = {
            'source_repository': source_repository,
            'location_repository': location_repository,
            'evse_repository': evse_repository,
            'connector_repository': connector_repository,
            'business_repository': business_repository,
            'image_repository': image_repository,
            'option_repository': option_repository,
            'remote_helper': remote_helper,
        }

        self.bnetza_import_service = BnetzaImportService(**kwargs, **default_dependencies)
        self.chargeit_import_service = ChargeitImportService(**kwargs, **default_dependencies)
        self.giroe_import_service = GiroeImportService(**kwargs, **default_dependencies)
        self.albwerk_ochp_import_service = AlbwerkOchpImportService(**kwargs, **default_dependencies)
        self.ladenetz_ochp_import_service = LadenetzOchpImportService(**kwargs, **default_dependencies)
        self.stadtnavi_import_service = StadtnaviImportService(**kwargs, **default_dependencies)
        self.sw_stuttgart_import_service = SWStuttgartImportService(**kwargs, **default_dependencies)

        self.importer_by_uid = {
            self.bnetza_import_service.source_info.uid: self.bnetza_import_service,
            self.chargeit_import_service.source_info.uid: self.chargeit_import_service,
            self.giroe_import_service.source_info.uid: self.giroe_import_service,
            self.albwerk_ochp_import_service.source_info.uid: self.albwerk_ochp_import_service,
            self.ladenetz_ochp_import_service.source_info.uid: self.ladenetz_ochp_import_service,
            self.stadtnavi_import_service.source_info.uid: self.stadtnavi_import_service,
            self.sw_stuttgart_import_service.source_info.uid: self.sw_stuttgart_import_service,
        }

    def fetch_sources(self) -> None:
        """
        Fetch all sources enabled via AUTO_FETCH_SOURCES by fetching static and realtime data
        """
        for source_uid in self.importer_by_uid.keys():
            if source_uid not in self.config_helper.get('AUTO_FETCH_SOURCES', []):
                continue

            self.fetch_source(source_uid)

    def fetch_source(self, source_uid: str) -> None:
        """
        Fetches static and realtime data for a specific source uid.
        """
        if 'source_uid' not in self.importer_by_uid:
            raise Exception('Unknown source UID')

        importer_service = self.importer_by_uid[source_uid]

        if hasattr(importer_service, 'fetch_static_data'):
            importer_service.fetch_static_data()

        if hasattr(importer_service, 'fetch_realtime_data'):
            importer_service.fetch_realtime_data()
