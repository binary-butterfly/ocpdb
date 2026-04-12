"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from datetime import datetime

import click
from flask.cli import AppGroup

from webapp.dependencies import dependencies

location_cli = AppGroup('location')


@location_cli.command('assign-regionalschluessel', help='Assigns official region codes to locations')
@click.option('-s', '--source-id', default=None, help='Limit to a specific source')
@click.option('--re-assign', is_flag=True, default=False, help='Re-assign existing official region codes')
def assign_regionalschluessel(source_id: str | None, re_assign: bool):
    dependencies.get_location_service().assign_official_region_codes(source_id=source_id, re_assign=re_assign)


@location_cli.command('push-datex-static', help='pushes datex2 static data')
def push_datex_static() -> None:
    charge_location_service = dependencies.get_charge_location_service()
    charge_location_service.push_datex_static()


@location_cli.command('push-datex-realtime', help='pushes datex2 realtime data')
@click.option('-s', '--since', 'updated_since', type=click.DateTime())
@click.option('--incremental-update', 'incremental_update', default=False, is_flag=True)
def push_datex_realtime(updated_since: datetime | None = None, incremental_update: bool | None = None) -> None:
    if incremental_update is not None and updated_since is not None:
        raise click.BadParameter('Cannot specify incremental update and updated since')

    charge_location_service = dependencies.get_charge_location_service()
    charge_location_service.push_datex_realtime(
        updated_since=updated_since,
        incremental_update=incremental_update or False,
    )
