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

from webapp.models.enums import TaxIncluded
from webapp.models.tariff import Tariff, TariffElement, TariffPriceComponent, TariffTax
from webapp.public_api.ocpi.v3_0.tariffs.tariff_mapper import TariffMapper


def _build_tariff(*tax_included_values: bool | None) -> Tariff:
    tariff = Tariff(
        id=1,
        uid='tariff-1',
        source='datex2_test',
        currency='EUR',
        last_updated=datetime(2026, 10, 1, tzinfo=timezone.utc),
    )
    tariff.elements = [
        TariffElement(
            price_components=[
                TariffPriceComponent(
                    type='ENERGY',
                    price=0.66386555,
                    taxes=[TariffTax(name='VAT', percentage=19)],
                    tax_included=tax_included,
                ),
            ],
        )
        for tax_included in tax_included_values
    ]
    return tariff


@pytest.mark.parametrize(
    ('tax_included_values', 'expected_tax_included'),
    [
        ((True,), TaxIncluded.YES),
        ((True, True), TaxIncluded.YES),
        ((False,), TaxIncluded.NO),
        ((False, False), TaxIncluded.NO),
        # Unknown flags must not become a confirmed tax basis
        ((None,), None),
        ((False, None), None),
        ((True, None), None),
        # Mixed flags must not be collapsed into a misleading tariff-wide value
        ((True, False), None),
        ((), None),
    ],
)
def test_get_tax_included(
    tax_included_values: tuple[bool | None, ...],
    expected_tax_included: TaxIncluded | None,
) -> None:
    assert TariffMapper.get_tax_included(_build_tariff(*tax_included_values)) is expected_tax_included


def test_map_tariff_to_ocpi_keeps_price_component_tax_included() -> None:
    result = TariffMapper.map_tariff_to_ocpi(_build_tariff(True, False, None))

    assert 'tax_included' not in result
    assert [element['price_components'][0].get('tax_included') for element in result['elements']] == [
        True,
        False,
        None,
    ]
    # Prices are never converted between tax bases
    assert all(element['price_components'][0]['price'] == 0.66386555 for element in result['elements'])


def test_map_tariff_to_ocpi_sets_tariff_tax_included() -> None:
    result = TariffMapper.map_tariff_to_ocpi(_build_tariff(False, False))

    assert result['tax_included'] == 'NO'
