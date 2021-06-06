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
from ..config import Config
from .OcpiApiController import ocpi_controller
from ..services.ocpi.OcpiGetLocationRequest import ocpi_get_chargepoint_list


@ocpi_controller.cli.command("get", help='OCPI Location: downloads and stores chargepoint updates')
@click.argument('source', nargs=1, type=click.Choice(list(Config.OCPI_SOURCES.keys())))
def cli_get(source: str):
    ocpi_get_chargepoint_list(source=source)
