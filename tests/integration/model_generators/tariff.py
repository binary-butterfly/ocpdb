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

from tests.integration.model_generators.source import SOURCE_UID_1
from webapp.models.tariff import Tariff
from webapp.models.tariff_association import TariffAssociation

TARIFF_UID_1 = 'TARIFF-1'
TARIFF_UID_2 = 'TARIFF-2'


def get_tariff(**kwargs) -> Tariff:
    default_data = {
        'uid': TARIFF_UID_1,
        'source': SOURCE_UID_1,
        'currency': 'EUR',
        'last_updated': datetime.now(timezone.utc),
    }
    data = {**default_data, **kwargs}

    tariff = Tariff()
    for key, value in data.items():
        setattr(tariff, key, value)

    if 'elements' not in data:
        tariff.elements = []

    return tariff


def get_tariff_1(**kwargs) -> Tariff:
    return get_tariff(**kwargs)


def get_tariff_2(**kwargs) -> Tariff:
    return get_tariff(uid=TARIFF_UID_2, **kwargs)


def get_tariff_association(**kwargs) -> TariffAssociation:
    default_data = {
        'uid': 'TA-1',
        'source': SOURCE_UID_1,
        'start_date_time': datetime.now(timezone.utc),
        'last_updated': datetime.now(timezone.utc),
    }
    data = {**default_data, **kwargs}
    return TariffAssociation(**data)
