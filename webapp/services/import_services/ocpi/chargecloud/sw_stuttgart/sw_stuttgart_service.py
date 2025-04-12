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

from webapp.common.remote_helper import RemoteServerType
from webapp.services.import_services.base_import_service import SourceInfo
from webapp.services.import_services.ocpi.chargecloud.chargecloud_base_service import ChargecloudBaseImportService


class SWStuttgartImportService(ChargecloudBaseImportService):
    remote_server_type = RemoteServerType.SW_STUTTGART

    source_info = SourceInfo(
        uid='sw_stuttgart',
        name='Stadtwerke Stuttgart',
        public_url='https://new-poi.chargecloud.de/SW-Stuttgart',
        has_realtime_data=True,
    )
