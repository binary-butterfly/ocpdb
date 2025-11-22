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
from decimal import Decimal

from tests.integration.model_generators.business import get_business_1, get_business_2
from tests.integration.model_generators.evse import (
    get_full_evse_1,
    get_full_evse_2,
    get_full_evse_3,
    get_full_evse_4,
    get_full_evse_5,
    get_full_evse_6,
)
from tests.integration.model_generators.source import SOURCE_UID_1, SOURCE_UID_2
from webapp.models import Location

LOCATION_UID_1 = 'LOCATION-1'
LOCATION_UID_2 = 'LOCATION-2'
LOCATION_UID_3 = 'LOCATION-3'


def get_location(**kwargs) -> Location:
    default_data = {
        'uid': LOCATION_UID_1,
        'source': SOURCE_UID_1,
        'name': 'Test Location',
        'address': 'Test Street 123',
        'postal_code': '12345',
        'city': 'Test City',
        'country': 'DEU',
        'lat': Decimal('52.52003'),
        'lon': Decimal('13.40489'),
        'time_zone': 'Europe/Berlin',
        'last_updated': datetime.now(tz=timezone.utc),
        'twentyfourseven': True,
    }

    data = {**default_data, **kwargs}
    return Location(**data)


def get_location_1(**kwargs) -> Location:
    return get_location(**kwargs)


def get_location_2(**kwargs) -> Location:
    return get_location(uid=LOCATION_UID_2, **kwargs)


def get_location_3(**kwargs) -> Location:
    return get_location(uid=LOCATION_UID_3, **kwargs)


def get_full_location_1(**kwargs) -> Location:
    return get_location_1(
        evses=[
            get_full_evse_1(),
            get_full_evse_2(),
        ],
        operator=get_business_1(),
        **kwargs,
    )


def get_full_location_2(**kwargs) -> Location:
    return get_location_2(
        evses=[
            get_full_evse_3(),
            get_full_evse_4(),
        ],
        operator=get_business_1(),
        **kwargs,
    )


def get_full_location_3(**kwargs) -> Location:
    return get_location_1(
        evses=[
            get_full_evse_5(),
            get_full_evse_6(),
        ],
        operator=get_business_2(),
        source=SOURCE_UID_2,
        **kwargs,
    )
