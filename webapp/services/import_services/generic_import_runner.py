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
from webapp.services.push_services.datex_push_service import ChargeLocationService

from .generic_import_heartbeat_tasks import image_import_task, realtime_import_task, static_import_task
from .import_services import ImportServices


class GenericBeatRunner(BaseService):
    import_services: ImportServices
    charge_location_service: ChargeLocationService

    def __init__(self, *, import_services: ImportServices, charge_location_service: ChargeLocationService, **kwargs):
        super().__init__(**kwargs)
        self.import_services = import_services
        self.charge_location_service = charge_location_service

    def start(self):
        self._schedule_imports()
        self._schedule_push()

    def _schedule_imports(self):
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

    def _schedule_push(self):
        if not self.config_helper.get('MOBILITHEK_ENABLED', False):
            return

        celery.add_periodic_task(
            crontab(
                minute=str(self.config_helper.get('DATEX_STATIC_PUSH_MINUTE', 0)),
                hour=str(self.config_helper.get('DATEX_STATIC_PUSH_HOUR', 3)),
            ),
            push_datex_static_task,
        )

        celery.add_periodic_task(
            self.config_helper.get('DATEX_REALTIME_PUSH_FREQUENCY', 60),
            push_datex_realtime_task,
        )


@celery.task()
def push_datex_static_task():
    from webapp.dependencies import dependencies

    dependencies.get_charge_location_service().push_datex_static()


@celery.task()
def push_datex_realtime_task():
    from webapp.dependencies import dependencies

    dependencies.get_charge_location_service().push_datex_realtime(incremental_update=True)
