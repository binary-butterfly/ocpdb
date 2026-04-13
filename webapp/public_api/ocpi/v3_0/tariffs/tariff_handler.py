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

from validataclass_search_queries.pagination import PaginatedResult

from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.repositories.tariff_repository import TariffRepository
from webapp.shared.ocpi.tariffs.tariff_search_queries import TariffSearchQuery

from .tariff_mapper import TariffMapper


class TariffHandler(PublicApiBaseHandler):
    tariff_repository: TariffRepository

    def __init__(self, *args, tariff_repository: TariffRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.tariff_repository = tariff_repository

    def get_tariffs(self, query: TariffSearchQuery) -> PaginatedResult[dict]:
        tariffs = self.tariff_repository.fetch_tariffs(query)
        return tariffs.map(TariffMapper.map_tariff_to_ocpi)

    def get_tariff(self, tariff_id: int) -> dict:
        tariff = self.tariff_repository.fetch_tariff_by_id(tariff_id)
        return TariffMapper.map_tariff_to_ocpi(tariff)
