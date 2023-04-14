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

from datetime import datetime, timedelta
from typing import Optional

import click
from flask.cli import AppGroup

from webapp.common.error_handling import catch_exception
from webapp.dependencies import dependencies


giroe_cli = AppGroup('giroe')


@giroe_cli.command("import", help='Giro-e: downloads and saves chargepoint updates')
@click.option(
    '-p', '--preset', 'preset',
    type=click.Choice(['daily', 'weekly']),
    help='preset for daily (last 36 hours) or weekly (last 10 days) sync',
)
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
        preset: Optional[str] = None,
        created_since: Optional[datetime] = None,
        created_until: Optional[datetime] = None,
        modified_since: Optional[datetime] = None,
        modified_until: Optional[datetime] = None,
):
    if preset and (created_since or created_until or modified_since or modified_until):
        raise Exception('cannot use preset together with created / modified parameters')

    if preset == 'daily':
        modified_since = datetime.utcnow() - timedelta(hours=36)
    elif preset == 'weekly':
        modified_since = datetime.utcnow() - timedelta(days=10)

    dependencies.get_import_services().giroe_import_service.download_and_save(
        created_since=created_since,
        created_until=created_until,
        modified_since=modified_since,
        modified_until=modified_until,
    )
