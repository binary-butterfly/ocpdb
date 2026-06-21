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

import click
from flask.cli import AppGroup

from webapp.common.error_handling import catch_exception
from webapp.dependencies import dependencies
from webapp.services.push_services.datex_push_service import ChargeLocationService

location_cli = AppGroup('location')


@location_cli.command('assign-regionalschluessel', help='Assigns official region codes to locations')
@click.option('-s', '--source-id', default=None, help='Limit to a specific source')
@click.option('--re-assign', is_flag=True, default=False, help='Re-assign existing official region codes')
def assign_regionalschluessel(source_id: str | None, re_assign: bool):
    dependencies.get_location_service().assign_official_region_codes(source_id=source_id, re_assign=re_assign)


@location_cli.command('push-mobilithek-static', help='Push the full static DATEX II snapshot to Mobilithek.')
@catch_exception
def push_mobilithek_static() -> None:
    charge_location_service: ChargeLocationService = dependencies.get_charge_location_service()
    charge_location_service.push_datex_static()


@location_cli.command(
    'push-mobilithek-realtime-full',
    help='Push the full realtime DATEX II status snapshot to Mobilithek.',
)
@catch_exception
def push_mobilithek_realtime_full() -> None:
    charge_location_service: ChargeLocationService = dependencies.get_charge_location_service()
    charge_location_service.push_datex_realtime(incremental_update=False)


@location_cli.command(
    'push-mobilithek-realtime-diff',
    help='Push an incremental realtime DATEX II status diff to Mobilithek (nothing is sent if the diff is empty).',
)
@catch_exception
def push_mobilithek_realtime_diff() -> None:
    charge_location_service: ChargeLocationService = dependencies.get_charge_location_service()
    charge_location_service.push_datex_realtime(incremental_update=True)
