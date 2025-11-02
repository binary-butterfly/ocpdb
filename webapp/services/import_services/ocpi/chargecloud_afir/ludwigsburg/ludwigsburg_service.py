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

from webapp.services.import_services.base_import_service import SourceInfo
from webapp.services.import_services.ocpi.chargecloud_afir.base_service import ChargecloudAfirBaseImportService


class LudwigsburgImportService(ChargecloudAfirBaseImportService):
    source_info = SourceInfo(
        uid='chargecloud_ludwigsburg',
        name='Stadtwerke Ludwigsburg',
        public_url='https://www.swlb.de/emobilitaet/ladeinfrastruktur',
        source_url='https://afir.data.chargecloud.app/v1/2e60790a-4a07-446c-b4fc-30ce433a2735/locations',
        has_realtime_data=True,
    )
