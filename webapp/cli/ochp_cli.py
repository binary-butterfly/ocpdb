# encoding: utf-8

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
from webapp.services.ochp.OchpChargepointRequest import ochp_get_chargepoint_list, ochp_get_chargepoint_list_update, \
    ochp_get_status
from .helper import catch_exception


ochp_cli = AppGroup('ochp')


@ochp_cli.command("get", help='OCHP GetChargePointList: downloads and stores chargepoints')
@catch_exception
def cli_get():
    ochp_get_chargepoint_list()


@ochp_cli.command("get-update", help='OCHP GetChargePointListUpdates: downloads and stores chargepoint updates')
@click.option('--full', default=False, is_flag=True)
@catch_exception
def cli_get(full: bool = False):
    ochp_get_chargepoint_list_update(full=full)


@ochp_cli.command("status", help='OCHP GetStatus: downloads and stores chargepoint live status')
@click.option('--full', default=False, is_flag=True)
@catch_exception
def cli_get(full: bool = False):
    ochp_get_status(full=full)
