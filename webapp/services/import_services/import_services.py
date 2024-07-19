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
from webapp.repositories import ConnectorRepository, EvseRepository, LocationRepository, OptionRepository, SourceRepository
from webapp.repositories.business_repository import BusinessRepository
from webapp.repositories.image_repository import ImageRepository
from webapp.services.base_service import BaseService
from webapp.services.import_services.bnetza import BnetzaImportService
from webapp.services.import_services.chargeit import ChargeitImportService
from webapp.services.import_services.giroe import GiroeImportService
from webapp.services.import_services.ochp.ochp_service import OchpImportService
from webapp.services.import_services.ocpi.stadtnavi.stadtnavi_service import StadtnaviImportService


class ImportServices(BaseService):
    bnetza_import_service: BnetzaImportService
    ochp_import_service: OchpImportService
    chargeit_import_service: ChargeitImportService
    giroe_import_service: GiroeImportService
    stadtnavi_import_service: StadtnaviImportService

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
        self.ochp_import_service = OchpImportService(**kwargs, **default_dependencies)
        self.stadtnavi_import_service = StadtnaviImportService(**kwargs, **default_dependencies)
