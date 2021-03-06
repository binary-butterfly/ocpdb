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

from flask.cli import AppGroup
from webapp.services.chargeit.chargeit_service import ChargeitService
from webapp.services.base_service import get_full_service_dependencies
from .helper import catch_exception


chargeit_cli = AppGroup('chargeit')


@chargeit_cli.command("download-and-save", help='ChargeIT: downloads and saves chargepoint updates')
@catch_exception
def cli_download_and_save():
    ChargeitService(
        **get_full_service_dependencies(),
    ).download_and_save()
