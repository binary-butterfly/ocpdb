"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2024 binary butterfly GmbH

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

from webapp.services.import_services.datex2.base_datex2_v3_5_import_service import BaseDatex2V35ImportService
from webapp.services.import_services.models import SourceInfo


class MontaDatex2ImportService(BaseDatex2V35ImportService):
    source_info = SourceInfo(
        uid='datex2_monta',
        name='Monta Datex II',
        public_url='https://mobilithek.info/offers/963836072152719360',
        source_url='https://mobilithek.info/offers/963836072152719360',
        attribution_license='CC-0',
        has_realtime_data=True,
    )
