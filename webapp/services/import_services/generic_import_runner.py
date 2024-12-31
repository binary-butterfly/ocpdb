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

from celery.schedules import crontab

from webapp.common.config import ConfigHelper
from webapp.common.logger import Logger
from webapp.extensions import celery

from .generic_import_heartbeat_tasks import realtime_import_task, static_import_task
from .import_services import ImportServices


class GenericImportRunner:
    logger: Logger
    config_helper: ConfigHelper
    import_services: ImportServices

    def __init__(
        self,
        logger: Logger,
        config_helper: ConfigHelper,
        import_services: ImportServices,
    ):
        self.logger = logger
        self.config_helper = config_helper
        self.import_services = import_services

    def start(self):
        for importer_service in self.import_services.importer_by_uid.values():
            if importer_service.source_info.uid not in self.config_helper.get('AUTO_FETCH_SOURCES', []):
                continue

            if hasattr(importer_service, 'fetch_static_data'):
                if importer_service.schedule is None:
                    schedule = crontab(
                        minute=str(self.config_helper.get('STATIC_PULL_MINUTE', 0)),
                        hour=str(self.config_helper.get('STATIC_PULL_HOUR', 1)),
                    )
                else:
                    schedule = importer_service.schedule

                celery.add_periodic_task(
                    schedule,
                    static_import_task,
                    kwargs={'source': importer_service.source_info.uid},
                )

            if hasattr(importer_service, 'fetch_realtime_data'):
                celery.add_periodic_task(
                    self.config_helper.get('REALTIME_PULL_FREQUENCY', 60),
                    realtime_import_task,
                    kwargs={'source': importer_service.source_info.uid},
                )
