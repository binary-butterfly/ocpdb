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

from webapp.common.base_blueprint import BaseBlueprint

from .business_api import BusinessBlueprint
from .location_api import LocationBlueprint
from .ocpi_api import OcpiBlueprint
from .source_api import SourceBlueprint
from .tiles_api import TilesBlueprint


class PublicApi(BaseBlueprint):
    documentation_base = True
    blueprints: list[type[BaseBlueprint]] = [
        TilesBlueprint,
        BusinessBlueprint,
        OcpiBlueprint,
        LocationBlueprint,
        SourceBlueprint,
    ]

    def __init__(self):
        super().__init__('public', __name__, url_prefix='')
        for blueprint in self.blueprints:
            self.register_blueprint(blueprint())
