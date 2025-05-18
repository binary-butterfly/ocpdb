"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from webapp.dependencies import dependencies
from webapp.repositories import LocationRepository, ObjectNotFoundException, SourceRepository

source_cli = AppGroup('source')


@source_cli.command('list', help='List all source uids')
def source_list():
    source_repository: SourceRepository = dependencies.get_source_repository()
    sources = source_repository.fetch_sources()
    for source in sources:
        click.echo(source.uid)


@source_cli.command('delete', help='Deletes all data from data source')
@click.argument('source_uid')
def source_delete(source_uid: str):
    # First: delete locations
    location_repository: LocationRepository = dependencies.get_location_repository()
    locations = location_repository.fetch_locations_by_source(source_uid)

    for location in locations:
        location_repository.delete_location(location)

    # Then: delete source
    source_repository: SourceRepository = dependencies.get_source_repository()
    try:
        source = source_repository.fetch_source_by_uid(source_uid)
        source_repository.delete_source(source)
    except ObjectNotFoundException:
        pass
