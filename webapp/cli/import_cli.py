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

import click
from flask.cli import AppGroup

from webapp.common.error_handling import catch_exception
from webapp.dependencies import dependencies
from webapp.services.import_services import ImageImportService, ImportServices

import_cli = AppGroup('import')


@import_cli.command('all', help='Fetches static and realtime data from all auto-fetched sources.')
@catch_exception
def import_all_sources() -> None:
    import_service: ImportServices = dependencies.get_import_services()
    import_service.fetch_sources()


@import_cli.command('static', help='Fetch static data')
@click.argument('source_uid')
@catch_exception
def cli_get_static(source_uid: str) -> None:
    import_services: ImportServices = dependencies.get_import_services()
    if source_uid not in import_services.importer_by_uid:
        raise ValueError(
            f'Source UID {source_uid} not in registered importers: {", ".join(import_services.importer_by_uid.keys())}',
        )
    import_services.importer_by_uid[source_uid].fetch_static_data()


@import_cli.command('realtime', help='Fetch realtime data')
@click.argument('source_uid')
@catch_exception
def cli_get_realtime(source_uid: str) -> None:
    import_services: ImportServices = dependencies.get_import_services()
    if source_uid not in import_services.importer_by_uid:
        raise ValueError(
            f'Source UID {source_uid} not in registered importers: {", ".join(import_services.importer_by_uid.keys())}',
        )
    import_services.importer_by_uid[source_uid].fetch_realtime_data()


@import_cli.command('images', help='Fetch images')
@catch_exception
def cli_get_images() -> None:
    image_import_services: ImageImportService = dependencies.get_image_import_service()
    image_import_services.fetch_images()
