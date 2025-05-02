"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from validataclass.helpers import UnsetValueType

from webapp.services.import_services.models import BusinessUpdate, SourceInfo
from webapp.services.import_services.ochp.base_ochp_service import BaseOchpImportService


class AlbwerkOchpImportService(BaseOchpImportService):
    source_info = SourceInfo(
        uid='ochp_albwerk',
        name='Albwerk',
        public_url='https://albwerk.de',
        source_url='https://echs.e-clearing.net',
        has_realtime_data=True,
    )

    def get_operator(self) -> BusinessUpdate | UnsetValueType:
        return BusinessUpdate(
            name='Albwerk',
        )
