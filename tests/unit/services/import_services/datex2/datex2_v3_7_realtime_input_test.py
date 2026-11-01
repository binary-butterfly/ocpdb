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

import json
from pathlib import Path

import pytest
from validataclass.exceptions import ValidationError

from webapp.services.import_services.datex2.v3_7.base_datex2_v3_7_import_service import BaseDatex2V37ImportService

REALTIME_DATA_PATH = Path(
    Path(__file__).parents[4],
    'integration',
    'services',
    'import_services',
    'datex2',
    'data',
    'datex2_giroe_realtime_reduced.json',
)


def _load_realtime_data() -> dict:
    with REALTIME_DATA_PATH.open() as realtime_file:
        return json.load(realtime_file)


def _count_refill_point_statuses(payloads: list) -> int:
    return sum(
        len(station_status.refillPointStatus)
        for payload in payloads
        for site_status in payload.aegiEnergyInfrastructureStatusPublication.energyInfrastructureSiteStatus
        for station_status in site_status.energyInfrastructureStationStatus
    )


def test_get_realtime_payloads_from_message_container() -> None:
    payloads = BaseDatex2V37ImportService.get_realtime_payloads(_load_realtime_data())

    assert len(payloads) == 1
    assert _count_refill_point_statuses(payloads) == 8


def test_get_realtime_payloads_from_d2_payload() -> None:
    payload = _load_realtime_data()['messageContainer']['payload'][0]

    payloads = BaseDatex2V37ImportService.get_realtime_payloads({'payload': payload})

    assert len(payloads) == 1
    assert _count_refill_point_statuses(payloads) == 8


def test_get_realtime_payloads_rejects_message_container_without_wrapper() -> None:
    # Payloads and exchange information outside a messageContainer field are no valid DATEX II document
    data = _load_realtime_data()['messageContainer']

    with pytest.raises(ValidationError):
        BaseDatex2V37ImportService.get_realtime_payloads(data)


def test_get_realtime_payloads_rejects_unknown_message_container_fields() -> None:
    data = _load_realtime_data()
    data['messageContainer']['unknownField'] = True

    with pytest.raises(ValidationError):
        BaseDatex2V37ImportService.get_realtime_payloads(data)
