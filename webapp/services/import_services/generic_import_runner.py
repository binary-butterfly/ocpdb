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

from webapp.extensions import celery
from webapp.services.base_service import BaseService

from .generic_import_heartbeat_tasks import image_import_task, realtime_import_task, static_import_task
from .import_services import ImportServices


class GenericImportRunner(BaseService):
    import_services: ImportServices

    def __init__(self, *, import_services: ImportServices, **kwargs):
        super().__init__(**kwargs)
        self.import_services = import_services

    def start(self):
        if self.config_helper.get('DISABLE_AUTOFETCH'):
            return

        celery.add_periodic_task(
            crontab(
                minute=str(self.config_helper.get('IMAGE_PULL_MINUTE', 0)),
                hour=str(self.config_helper.get('IMAGE_PULL_HOUR', 4)),
            ),
            image_import_task,
        )

        for source_uid, importer_service in self.import_services.importer_by_uid.items():
            if source_uid not in self.config_helper.get('SOURCES'):
                continue
            if self.config_helper.get('SOURCES')[source_uid].get('auto_fetch', True) is False:
                continue

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
