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

from flask.cli import AppGroup

from webapp.common.error_handling import catch_exception
from webapp.dependencies import dependencies
from webapp.services.push_services.datex_push_service import ChargeLocationService

push_cli = AppGroup('push')


@push_cli.command('datex-static', help='Push the full static DATEX II snapshot to Mobilithek.')
@catch_exception
def cli_push_datex_static() -> None:
    charge_location_service: ChargeLocationService = dependencies.get_charge_location_service()
    charge_location_service.push_datex_static()


@push_cli.command('datex-realtime-full', help='Push the full realtime DATEX II status snapshot to Mobilithek.')
@catch_exception
def cli_push_datex_realtime_full() -> None:
    charge_location_service: ChargeLocationService = dependencies.get_charge_location_service()
    charge_location_service.push_datex_realtime(incremental_update=False)


@push_cli.command(
    'datex-realtime-diff',
    help='Push an incremental realtime DATEX II status diff to Mobilithek (nothing is sent if the diff is empty).',
)
@catch_exception
def cli_push_datex_realtime_diff() -> None:
    charge_location_service: ChargeLocationService = dependencies.get_charge_location_service()
    charge_location_service.push_datex_realtime(incremental_update=True)
