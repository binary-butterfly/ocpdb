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

from .businesses import OcpiBusinessBlueprint
from .charging_stations import OcpiChargingStationBlueprint
from .connectors import OcpiConnectorBlueprint
from .evses import OcpiEvseBlueprint
from .locations import OcpiLegacyLocationBlueprint, OcpiLocationBlueprint


class Ocpi22Blueprint(BaseBlueprint):
    blueprints: list[type[BaseBlueprint]] = [
        OcpiBusinessBlueprint,
        OcpiChargingStationBlueprint,
        OcpiConnectorBlueprint,
        OcpiEvseBlueprint,
        OcpiLocationBlueprint,
        OcpiLegacyLocationBlueprint,
    ]

    def __init__(self):
        super().__init__('ocpi_22', __name__, url_prefix='/api/ocpi/2.2')
        for blueprint in self.blueprints:
            self.register_blueprint(blueprint())
