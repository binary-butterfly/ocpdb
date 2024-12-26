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
from webapp.services.import_services import ImportServices

source_cli = AppGroup('source', help='Generic interface for fetching all data sources')


@source_cli.command('fetch-all', help='Fetches static and realtime data from all auto-fetched sources.')
@catch_exception
def fetch_all_sources() -> None:
    import_service: ImportServices = dependencies.get_import_services()
    import_service.fetch_sources()


@source_cli.command('fetch', help='Fetches static and realtime data for specified source.')
@click.argument('source_uid')
@catch_exception
def fetch_source(source_uid: str) -> None:
    import_service: ImportServices = dependencies.get_import_services()
    import_service.fetch_source(source_uid)
