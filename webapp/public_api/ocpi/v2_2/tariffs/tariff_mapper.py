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

from webapp.models.tariff import Tariff
from webapp.public_api.base_handler import PublicApiBaseHandler


class TariffMapper:
    @staticmethod
    def map_tariff_to_ocpi(tariff: Tariff) -> dict:
        result = tariff.to_dict()

        return PublicApiBaseHandler.filter_none(result)
