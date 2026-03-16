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

from webapp.dependencies import dependencies

location_cli = AppGroup('location')


@location_cli.command('assign-regionalschluessel', help='Assigns official region codes to locations')
@click.option('-s', '--source-id', default=None, help='Limit to a specific source')
@click.option('--re-assign', is_flag=True, default=False, help='Re-assign existing official region codes')
def assign_regionalschluessel(source_id: str | None, re_assign: bool):
    dependencies.get_location_service().assign_official_region_codes(source_id=source_id, re_assign=re_assign)
