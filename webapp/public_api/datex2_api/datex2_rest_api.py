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

from webapp.public_api.base_blueprint import BaseBlueprint

from .v3_5_json import Datex2V35JSONBlueprint
from .v3_7_json import Datex2V37JSONBlueprint


class Datex2Blueprint(BaseBlueprint):
    documented = True

    def __init__(self):
        super().__init__('datex2', __name__, url_prefix='/api/public/datex')
        self.register_blueprint(Datex2V35JSONBlueprint())
        self.register_blueprint(Datex2V37JSONBlueprint())
