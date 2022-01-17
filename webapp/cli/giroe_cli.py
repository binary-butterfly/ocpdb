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
from typing import Optional
from datetime import datetime
from flask.cli import AppGroup
from webapp.services.giroe.giroe_service import GiroeService
from webapp.services.base_service import get_full_service_dependencies
from .helper import catch_exception


giroe_cli = AppGroup('giroe')


@giroe_cli.command("download-and-save", help='Giro-e: downloads and saves chargepoint updates')
@click.option(
    '-cf', '--created-since', 'created_since',
    type=click.DateTime(formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
    help='created since'
)
@click.option(
    '-ct', '--created-until', 'created_until',
    type=click.DateTime(formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
    help='created until'
)
@click.option(
    '-cf', '--modified-since', 'modified_since',
    type=click.DateTime(formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
    help='modified since'
)
@click.option(
    '-ct', '--modified-until', 'modified_until',
    type=click.DateTime(formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]),
    help='modified until'
)
@catch_exception
def cli_download_and_save(
        created_since: Optional[datetime] = None,
        created_until: Optional[datetime] = None,
        modified_since: Optional[datetime] = None,
        modified_until: Optional[datetime] = None):
    GiroeService(
        **get_full_service_dependencies(),
    ).download_and_save(created_since, created_until, modified_since, modified_until)
