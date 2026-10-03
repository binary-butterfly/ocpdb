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

from webapp.models.enums import TaxIncluded
from webapp.models.tariff import Tariff
from webapp.public_api.base_handler import PublicApiBaseHandler


class TariffMapper:
    @staticmethod
    def map_tariff_to_ocpi(tariff: Tariff) -> dict:
        result = tariff.to_dict()
        result['original_id'] = result.pop('uid', None)

        tax_included = TariffMapper.get_tax_included(tariff)
        if tax_included is not None:
            result['tax_included'] = tax_included.value

        return PublicApiBaseHandler.filter_none(result)

    @staticmethod
    def get_tax_included(tariff: Tariff) -> TaxIncluded | None:
        """
        Derives the OCPI 3.0 tariff-level tax_included from the price component flags. It is only set if every price
        component explicitly states the same value: unknown or mixed flags would make a tariff-wide value misleading,
        so in that case it is omitted and consumers have to look at the price components. N/A is never derived,
        because a missing tax rate does not prove that no tax applies.
        """
        tax_included_values = {
            price_component.tax_included
            for element in tariff.elements
            for price_component in element.price_components or []
        }
        if tax_included_values == {True}:
            return TaxIncluded.YES
        if tax_included_values == {False}:
            return TaxIncluded.NO
        return None
