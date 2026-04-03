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

from webapp.models.enums import TariffAudience, TariffType
from webapp.models.tariff_association import TariffAssociation
from webapp.public_api.base_handler import PublicApiBaseHandler

_audience_to_tariff_type: dict[TariffAudience, TariffType] = {
    TariffAudience.AD_HOC_PAYMENT: TariffType.AD_HOC_PAYMENT,
    TariffAudience.EMSP_CONTRACT: TariffType.REGULAR,
}


class TariffMapper:
    @staticmethod
    def map_tariff_association_to_ocpi_22(tariff_association: TariffAssociation) -> dict:
        tariff = tariff_association.tariff

        result: dict = {
            'id': str(tariff_association.id),
            'original_id': tariff_association.uid,
            'source': tariff_association.source,
            'currency': tariff.currency,
            'elements': tariff.elements,
            'start_date_time': tariff_association.start_date_time.isoformat(),
            'last_updated': tariff_association.last_updated.isoformat(),
        }

        if tariff_association.audience is not None:
            tariff_type = _audience_to_tariff_type.get(tariff_association.audience)
            if tariff_type is not None:
                result['type'] = tariff_type.value

        if tariff.tariff_alt_text is not None:
            result['tariff_alt_text'] = tariff.tariff_alt_text
        if tariff.tariff_alt_url is not None:
            result['tariff_alt_url'] = tariff.tariff_alt_url
        if tariff.min_price is not None:
            result['min_price'] = tariff.min_price
        if tariff.max_price is not None:
            result['max_price'] = tariff.max_price
        if tariff.energy_mix is not None:
            result['energy_mix'] = tariff.energy_mix

        return PublicApiBaseHandler.filter_none(result)
