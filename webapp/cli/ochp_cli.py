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


ochp_cli = AppGroup('ochp')


@ochp_cli.command('import', help='OCHP GetChargePointList: downloads and stores chargepoints')
@catch_exception
def cli_get():
    dependencies.get_import_services().ochp_import_service.base_load_and_save()


"""
@ochp_cli.command("get-update", help='OCHP GetChargePointListUpdates: downloads and stores chargepoint updates')
@click.option('--full', default=False, is_flag=True)
@catch_exception
def cli_get(full: bool = False):
    dependencies.get_ochp_import_service().import_base_data()
"""


@ochp_cli.command('status', help='OCHP GetStatus: downloads and stores chargepoint live status')
@click.option('--full', 'full_sync', default=False, is_flag=True)
@catch_exception
def cli_get(full_sync: bool = False):
    dependencies.get_import_services().ochp_import_service.live_load_and_save(full_sync)
