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

from webapp.extensions import celery
from webapp.services.import_services import ImageImportService, ImportServices


@celery.task()
def static_import_task(source: str):
    from webapp.dependencies import dependencies

    import_services = dependencies.get_import_services()
    import_services.importer_by_uid[source].fetch_static_data()


@celery.task()
def realtime_import_task(source: str):
    from webapp.dependencies import dependencies

    import_services: ImportServices = dependencies.get_import_services()
    import_services.importer_by_uid[source].fetch_realtime_data()


@celery.task()
def image_import_task():
    from webapp.dependencies import dependencies

    image_import_services: ImageImportService = dependencies.get_image_import_service()
    image_import_services.fetch_images()
