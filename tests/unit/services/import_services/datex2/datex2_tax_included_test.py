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

import pytest
from validataclass.validators import DataclassValidator

from webapp.services.import_services.datex2.v3_5.datex2_v3_5_json_static_mapper import Datex2V35JSONStaticMapper
from webapp.shared.datex2.v3_5_json_static.models.energy_rate_input import EnergyRateInput


def _map_energy_prices(*energy_prices: dict) -> list:
    energy_rate = DataclassValidator(EnergyRateInput).validate({
        'idG': 'rate-1',
        'ratePolicy': {'value': 'adHoc'},
        'lastUpdated': datetime(2026, 10, 1, tzinfo=timezone.utc).isoformat(),
        'applicableCurrency': ['EUR'],
        'energyPrice': list(energy_prices),
    })
    tariff_update = Datex2V35JSONStaticMapper()._map_energy_rate(energy_rate, 'tariff-1', 'datex2_test')

    return [element.price_components[0] for element in tariff_update.elements]


@pytest.mark.parametrize(
    ('tax_included_input', 'tax_included_output'),
    [
        ({'taxIncluded': True}, True),
        ({'taxIncluded': False}, False),
        ({}, None),
    ],
)
@pytest.mark.parametrize('tax_rate_input', [{'taxRate': 19.0}, {}])
def test_map_energy_price_keeps_tax_included(
    tax_included_input: dict,
    tax_included_output: bool | None,
    tax_rate_input: dict,
) -> None:
    price_components = _map_energy_prices({
        'priceType': {'value': 'pricePerKWh'},
        'value': 0.66386555,
        **tax_included_input,
        **tax_rate_input,
    })

    assert len(price_components) == 1
    # The price is never converted between tax bases, the flag just states which basis it has
    assert float(price_components[0].price) == 0.66386555
    assert price_components[0].tax_included is tax_included_output
    assert (price_components[0].taxes is not None) == bool(tax_rate_input)


def test_map_energy_price_keeps_mixed_tax_included() -> None:
    price_components = _map_energy_prices(
        {'priceType': {'value': 'pricePerKWh'}, 'value': 0.79, 'taxIncluded': True, 'taxRate': 19.0},
        {'priceType': {'value': 'pricePerMinute'}, 'value': 0.1, 'taxIncluded': False, 'taxRate': 19.0},
        {'priceType': {'value': 'flatRate'}, 'value': 1.0},
    )

    assert [price_component.tax_included for price_component in price_components] == [True, False, None]
