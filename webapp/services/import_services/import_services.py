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
import traceback

from webapp.common.contexts import TelemetryContext
from webapp.common.logging.models import LogMessageType
from webapp.repositories import (
    ConnectorRepository,
    EvseRepository,
    LocationRepository,
    OfficialRegionCodeRepository,
    SourceRepository,
    TariffRepository,
)
from webapp.repositories.business_repository import BusinessRepository
from webapp.repositories.image_repository import ImageRepository
from webapp.services.base_service import BaseService
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.bnetza import BnetzaApiImportService, BnetzaExcelImportService
from webapp.services.import_services.datex2 import (
    AmpecoDatex2ImportService,
    ChargecloudDatex2ImportService,
    EcoMovementDatex2ImportService,
    EluMobilityDatex2ImportService,
    EnBWDatex2ImportService,
    EnioDatex2ImportService,
    ErftDatex2ImportService,
    ERoundDatex2ImportService,
    GiroEDatex2ImportService,
    GridAndCoDatex2ImportService,
    LadebusinessDatex2ImportService,
    LichtblickDatex2ImportService,
    MidorionDatex2ImportService,
    MontaDatex2ImportService,
    MsuDatex2ImportService,
    PumpDatex2ImportService,
    QwelloDatex2ImportService,
    SmatricsDatex2ImportService,
    TeslaDatex2ImportService,
    VaylensDatex2ImportService,
    VolkswagenDatex2ImportService,
    WirelaneDatex2ImportService,
)
from webapp.services.import_services.giroe import GiroeImportService
from webapp.services.import_services.goldbeck_ipcm import HeilbronnNeckarbogenImportService
from webapp.services.import_services.lichtblick import LichtblickImportService
from webapp.services.import_services.ochp.albwerk import AlbwerkOchpImportService
from webapp.services.import_services.ochp.ladenetz import LadenetzOchpImportService
from webapp.services.import_services.ocpi.chargecloud_afir.ludwigsburg.ludwigsburg_service import (
    LudwigsburgImportService,
)
from webapp.services.import_services.ocpi.chargecloud_public.pforzheim import PforzheimImportService
from webapp.services.import_services.ocpi.chargecloud_public.sw_stuttgart import SWStuttgartImportService
from webapp.services.import_services.ocpi.chargecloud_public.tuebingen import TuebingenImportService
from webapp.services.import_services.ocpi.eaaze_pbw import EaazePbwImportService
from webapp.services.import_services.ocpi.stadtnavi.stadtnavi_service import StadtnaviImportService
from webapp.services.import_services.opendata_swiss import OpendataSwissImportService

logger = logging.getLogger(__name__)


class ImportServices(BaseService):
    importer_by_uid: dict[str, BaseImportService] = {}

    importer_classes: list[type[BaseImportService]] = [
        AlbwerkOchpImportService,
        AmpecoDatex2ImportService,
        BnetzaApiImportService,
        BnetzaExcelImportService,
        ChargecloudDatex2ImportService,
        EaazePbwImportService,
        EcoMovementDatex2ImportService,
        EluMobilityDatex2ImportService,
        EnBWDatex2ImportService,
        EnioDatex2ImportService,
        ErftDatex2ImportService,
        ERoundDatex2ImportService,
        GiroEDatex2ImportService,
        GiroeImportService,
        GridAndCoDatex2ImportService,
        HeilbronnNeckarbogenImportService,
        LadebusinessDatex2ImportService,
        LadenetzOchpImportService,
        LichtblickDatex2ImportService,
        LichtblickImportService,
        LudwigsburgImportService,
        MidorionDatex2ImportService,
        MontaDatex2ImportService,
        MsuDatex2ImportService,
        OpendataSwissImportService,
        PforzheimImportService,
        PumpDatex2ImportService,
        QwelloDatex2ImportService,
        SmatricsDatex2ImportService,
        StadtnaviImportService,
        SWStuttgartImportService,
        TeslaDatex2ImportService,
        TuebingenImportService,
        VaylensDatex2ImportService,
        VolkswagenDatex2ImportService,
        WirelaneDatex2ImportService,
    ]

    def __init__(
        self,
        *,
        source_repository: SourceRepository,
        location_repository: LocationRepository,
        evse_repository: EvseRepository,
        connector_repository: ConnectorRepository,
        business_repository: BusinessRepository,
        image_repository: ImageRepository,
        official_region_code_repository: OfficialRegionCodeRepository,
        tariff_repository: TariffRepository,
        **kwargs,
    ):
        super().__init__(**kwargs)

        dependencies = {
            'source_repository': source_repository,
            'location_repository': location_repository,
            'evse_repository': evse_repository,
            'connector_repository': connector_repository,
            'business_repository': business_repository,
            'image_repository': image_repository,
            'official_region_code_repository': official_region_code_repository,
            'tariff_repository': tariff_repository,
            'config_helper': self.config_helper,
            'context_helper': self.context_helper,
        }

        importer_classes_by_uid = {cls.source_info.uid: cls for cls in self.importer_classes}

        for source_uid in self.config_helper.get('SOURCES').keys():
            if source_uid not in importer_classes_by_uid:
                raise Exception(f'Unknown source UID {source_uid}')

            for required_config_key in importer_classes_by_uid[source_uid].required_config_keys:
                if required_config_key not in self.config_helper.get('SOURCES', {}).get(source_uid, {}):
                    raise Exception(f'Missing required config key {required_config_key} for source UID {source_uid}')

            self.importer_by_uid[source_uid] = importer_classes_by_uid[source_uid](**dependencies)

    def fetch_sources(self) -> None:
        """
        Fetch all sources enabled via `fetch_at_init`, which is true by default
        """
        for source_uid in self.importer_by_uid.keys():
            if source_uid not in self.config_helper.get('SOURCES'):
                continue
            if self.config_helper.get('SOURCES')[source_uid].get('fetch_at_init', True) is False:
                continue
            try:
                self.fetch_source(source_uid)
            except Exception as e:
                logger.error(
                    f'Import for {source_uid} fails due {e}: {traceback.format_exc()}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )

    def fetch_source(self, source_uid: str) -> None:
        """
        Fetches static and realtime data for a specific source uid.
        """
        if source_uid not in self.importer_by_uid:
            raise Exception('Unknown source UID')

        importer_service = self.importer_by_uid[source_uid]
        self.context_helper.set_telemetry_context(TelemetryContext.SOURCE, importer_service.source_info.uid)

        if hasattr(importer_service, 'fetch_static_data'):
            importer_service.fetch_static_data()

        if hasattr(importer_service, 'fetch_realtime_data'):
            importer_service.fetch_realtime_data()

    def fetch_static_source(self, source_uid: str) -> None:
        """
        Fetches static and realtime data for a specific source uid.
        """
        if source_uid not in self.importer_by_uid:
            raise Exception('Unknown source UID')

        importer_service = self.importer_by_uid[source_uid]
        self.context_helper.set_telemetry_context(TelemetryContext.SOURCE, importer_service.source_info.uid)

        if hasattr(importer_service, 'fetch_static_data'):
            importer_service.fetch_static_data()

    def fetch_realtime_source(self, source_uid: str) -> None:
        """
        Fetches static and realtime data for a specific source uid.
        """
        if source_uid not in self.importer_by_uid:
            raise Exception('Unknown source UID')

        importer_service = self.importer_by_uid[source_uid]
        self.context_helper.set_telemetry_context(TelemetryContext.SOURCE, importer_service.source_info.uid)

        if hasattr(importer_service, 'fetch_realtime_data'):
            importer_service.fetch_realtime_data()
