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

from datetime import datetime, timezone

from webapp.models import Connector
from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType

CONNECTOR_1_UID = 'CONNECTOR-1'
CONNECTOR_2_UID = 'CONNECTOR-2'


def get_connector(**kwargs) -> Connector:
    default_data = {
        'uid': CONNECTOR_1_UID,
        'standard': ConnectorType.IEC_62196_T2,
        'format': ConnectorFormat.SOCKET,
        'power_type': PowerType.AC_3_PHASE,
        'max_voltage': 400,
        'max_amperage': 32,
        'max_electric_power': 22000,
        'last_updated': datetime.now(tz=timezone.utc),
    }
    data = {**default_data, **kwargs}
    return Connector(**data)


def get_ac_connector(**kwargs) -> Connector:
    return get_connector(**kwargs)


def get_dc_connector(**kwargs) -> Connector:
    return get_connector(
        power_type=PowerType.DC,
        standard=ConnectorType.IEC_62196_T2_COMBO,
        format=ConnectorFormat.CABLE,
        max_voltage=400,
        max_amperage=350,
        max_electric_power=150000,
        **kwargs,
    )
