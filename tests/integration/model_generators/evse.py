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

from tests.integration.model_generators.connector import get_ac_connector, get_dc_connector
from webapp.models import Evse
from webapp.models.evse import EvseStatus

EVSE_UID_1 = 'EVSE-1'
EVSE_UID_2 = 'EVSE-2'
EVSE_UID_3 = 'EVSE-3'
EVSE_UID_4 = 'EVSE-4'
EVSE_UID_5 = 'EVSE-5'
EVSE_UID_6 = 'EVSE-6'


def get_evse(**kwargs) -> Evse:
    default_data = {
        'uid': EVSE_UID_1,
        'evse_id': EVSE_UID_1,
        'status': EvseStatus.AVAILABLE,
        'last_updated': datetime.now(timezone.utc),
    }
    data = {**default_data, **kwargs}
    return Evse(**data)


def get_evse_1(**kwargs) -> Evse:
    return get_evse(**kwargs)


def get_evse_2(**kwargs) -> Evse:
    return get_evse(uid=EVSE_UID_2, **kwargs)


def get_evse_3(**kwargs) -> Evse:
    return get_evse(uid=EVSE_UID_3, **kwargs)


def get_evse_4(**kwargs) -> Evse:
    return get_evse(uid=EVSE_UID_4, **kwargs)


def get_evse_5(**kwargs) -> Evse:
    return get_evse(uid=EVSE_UID_5, **kwargs)


def get_evse_6(**kwargs) -> Evse:
    return get_evse(uid=EVSE_UID_6, **kwargs)


def get_full_evse_1(**kwargs) -> Evse:
    return get_evse_1(
        connectors=[get_ac_connector()],
        **kwargs,
    )


def get_full_evse_2(**kwargs) -> Evse:
    return get_evse_2(
        connectors=[get_ac_connector()],
        **kwargs,
    )


def get_full_evse_3(**kwargs) -> Evse:
    return get_evse_3(
        connectors=[get_dc_connector()],
        **kwargs,
    )


def get_full_evse_4(**kwargs) -> Evse:
    return get_evse_4(
        connectors=[get_dc_connector()],
        **kwargs,
    )


def get_full_evse_5(**kwargs) -> Evse:
    return get_evse_5(
        connectors=[get_ac_connector()],
        **kwargs,
    )


def get_full_evse_6(**kwargs) -> Evse:
    return get_evse_6(
        connectors=[get_ac_connector()],
        **kwargs,
    )
