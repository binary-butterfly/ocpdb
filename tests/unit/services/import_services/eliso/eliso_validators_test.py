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

from datetime import datetime, timezone
from decimal import Decimal

import pytest
from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import EvseStatus
from webapp.services.import_services.eliso.eliso_validators import ElisoEvseStatusInput, ElisoLocationInput


def _get_location_dict(**kwargs) -> dict:
    return {
        'city': 'Haßfurt',
        'address': 'Am Wasserwerk 2',
        'postalCode': '97437',
        'country_iso_3166_alpha_2': 'DE',
        'coordinates': {'latitude': 50.030589789349, 'longitude': 10.520250965406},
        'operator_name': 'eliso GmbH',
        'hotline_number': '+49 711 40042100',
        'opening_time': '24/7',
        'mobilithek_last_updated_dts': '2026-10-28T04:04:51.23388+00:00',
        'evses': [
            {
                'evseId': 'DE*ELI*E5207046',
                'connectors': [{'maxPower': 135, 'powerType': 'DC', 'type_of_connector': 'Combo2/CCS (DC)'}],
            },
            {
                'evseId': 'DE*ELI*E5207045',
                'connectors': [{'maxPower': 22, 'powerType': 'AC_3_PHASE', 'type_of_connector': 'Type 2 (AC)'}],
            },
        ],
        **kwargs,
    }


def test_location_to_location_update() -> None:
    location_input = DataclassValidator(ElisoLocationInput).validate(_get_location_dict())

    location_update = location_input.to_location_update('eliso')

    assert location_update.uid == 'DE*ELI*E5207045'
    assert location_update.country == 'DEU'
    assert location_update.lat == Decimal('50.0305898')
    assert location_update.twentyfourseven is True
    assert location_update.operator.name == 'eliso GmbH'
    evses = location_update.charging_pool[0].evses
    assert [evse.evse_id for evse in evses] == ['DE*ELI*E5207046', 'DE*ELI*E5207045']
    assert evses[0].connectors[0].standard == ConnectorType.IEC_62196_T2_COMBO
    assert evses[0].connectors[0].format == ConnectorFormat.CABLE
    assert evses[0].connectors[0].power_type == PowerType.DC
    assert evses[0].connectors[0].max_electric_power == 135000
    assert evses[1].connectors[0].standard == ConnectorType.IEC_62196_T2
    assert evses[1].connectors[0].format == ConnectorFormat.SOCKET


def test_location_with_unknown_connector_type() -> None:
    location_dict = _get_location_dict()
    location_dict['evses'][0]['connectors'][0]['type_of_connector'] = 'CHAdeMO'

    with pytest.raises(ValidationError):
        DataclassValidator(ElisoLocationInput).validate(location_dict)


@pytest.mark.parametrize(
    ('operational_status', 'availability_status', 'evse_status'),
    [
        ('Operational', 'Not in use', EvseStatus.AVAILABLE),
        ('Operational', 'In use', EvseStatus.CHARGING),
        ('Operational', None, EvseStatus.UNKNOWN),
        ('Non-operational', None, EvseStatus.INOPERATIVE),
    ],
)
def test_evse_status_to_evse_realtime_update(
    operational_status: str,
    availability_status: str | None,
    evse_status: EvseStatus,
) -> None:
    evse_status_dict = {
        'evseId': 'DE*ELI*E3584570',
        'adhoc_price': 0.49,
        'operational_status': operational_status,
        'mobilithek_last_updated_dts': '2026-10-28T19:53:17.994069+00:00',
    }
    if availability_status is not None:
        evse_status_dict['availability_status'] = availability_status

    evse_update = DataclassValidator(ElisoEvseStatusInput).validate(evse_status_dict).to_evse_realtime_update()

    assert evse_update.evse_id == 'DE*ELI*E3584570'
    assert evse_update.status == evse_status
    assert evse_update.status_last_updated == datetime(2026, 10, 28, 19, 53, 17, 994069, tzinfo=timezone.utc)
