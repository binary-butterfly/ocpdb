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

from flask import Flask

from .bnetza_cli import bnetza_cli
from .chargeit_cli import chargeit_cli
from .giroe_cli import giroe_cli
from .match_cli import match_cli
from .ochp_cli import ochp_cli
from .source_cli import source_cli
from .stadtnavi_cli import stadtnavi_cli
from .sw_stuttgart_cli import sw_stuttgart_cli


def register_cli_to_app(app: Flask):
    app.cli.add_command(bnetza_cli)
    app.cli.add_command(chargeit_cli)
    app.cli.add_command(giroe_cli)
    app.cli.add_command(match_cli)
    app.cli.add_command(ochp_cli)
    app.cli.add_command(stadtnavi_cli)
    app.cli.add_command(sw_stuttgart_cli)
    app.cli.add_command(source_cli)
