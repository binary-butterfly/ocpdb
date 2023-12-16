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

from pathlib import Path

import click
from flask.cli import AppGroup

from webapp.common.error_handling import catch_exception
from webapp.dependencies import dependencies

bnetza_cli = AppGroup('bnetza')


@bnetza_cli.command("import-file", help='Bundesnetzagentur: loads and saves chargepoints from XLXS file')
@click.argument('import_file_path', type=click.Path(dir_okay=False, path_type=Path))
@catch_exception
def cli_load_and_save_file(import_file_path: Path):
    dependencies.get_import_services().bnetza_import_service.load_and_save_from_file(import_file_path)


@bnetza_cli.command("import-web", help='Bundesnetzagentur: loads and saves chargepoints from web')
@catch_exception
def cli_load_and_save_web():
    dependencies.get_import_services().bnetza_import_service.load_and_save_from_web()
