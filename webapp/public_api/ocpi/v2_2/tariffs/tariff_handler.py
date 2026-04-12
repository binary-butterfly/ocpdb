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
from webapp.public_api.ocpi.v3_0.tariff_associations.tariff_association_search_queries import (
    TariffAssociationSearchQuery,
)
from webapp.repositories.tariff_association_repository import TariffAssociationRepository

from .tariff_mapper import TariffMapper


class TariffHandler(PublicApiBaseHandler):
    tariff_association_repository: TariffAssociationRepository

    def __init__(self, *args, tariff_association_repository: TariffAssociationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.tariff_association_repository = tariff_association_repository

    def get_tariffs(self, query: TariffAssociationSearchQuery) -> PaginatedResult[dict]:
        tariff_associations = self.tariff_association_repository.fetch_tariff_associations(query)
        return tariff_associations.map(TariffMapper.map_tariff_association_to_ocpi_22)

    def get_tariff(self, tariff_id: int) -> dict:
        tariff_association = self.tariff_association_repository.fetch_tariff_association_by_id(tariff_id)
        return TariffMapper.map_tariff_association_to_ocpi_22(tariff_association)
