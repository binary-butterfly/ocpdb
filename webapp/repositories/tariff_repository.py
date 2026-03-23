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

from sqlalchemy.orm import selectinload
from validataclass_search_queries.pagination import PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.common.sqlalchemy import Query
from webapp.models.tariff import Tariff
from webapp.models.tariff_association import TariffAssociation

from .base_repository import BaseRepository
from .exceptions import ObjectNotFoundException


class TariffRepository(BaseRepository[Tariff]):
    model_cls = Tariff

    def fetch_tariff_by_id(self, tariff_id: int) -> Tariff:
        tariff = (
            self.session.query(Tariff).options(selectinload(Tariff.elements)).filter(Tariff.id == tariff_id).first()
        )
        if tariff is None:
            raise ObjectNotFoundException(f'tariff with id {tariff_id} not found')
        return tariff

    def fetch_tariffs(self, search_query: BaseSearchQuery | None = None) -> PaginatedResult[Tariff]:
        query = self.session.query(Tariff)

        return self._search_and_paginate(query, search_query)

    def _filter_by_search_query(self, query: Query, search_query: BaseSearchQuery | None) -> Query:
        if search_query is None:
            return query

        for _param_name, bound_filter in search_query.get_search_filters():
            if _param_name in [
                'source_uid',
                'source_uids',
                'exclude_source_uid',
                'exclude_source_uids',
            ]:
                continue

            query = self._apply_bound_search_filter(query, bound_filter)

        if source_uid := getattr(search_query, 'source_uid', None):
            query = query.filter(Tariff.source == source_uid)

        if source_uids := getattr(search_query, 'source_uids', None):
            query = query.filter(Tariff.source.in_(source_uids))

        if exclude_source_uid := getattr(search_query, 'exclude_source_uid', None):
            query = query.filter(Tariff.source != exclude_source_uid)

        if exclude_source_uids := getattr(search_query, 'exclude_source_uids', None):
            query = query.filter(Tariff.source.notin_(exclude_source_uids))

        return query

    def fetch_tariffs_by_source(self, source: str) -> list[Tariff]:
        associations_load = selectinload(Tariff.tariff_associations)
        return (
            self.session
            .query(Tariff)
            .options(
                associations_load.selectinload(TariffAssociation.evses),
                associations_load.selectinload(TariffAssociation.connectors),
            )
            .filter(Tariff.source == source)
            .all()
        )

    def fetch_tariff_ids_by_source(self, source: str) -> list[int]:
        items = self.session.query(Tariff.id).filter(Tariff.source == source).all()
        return [item.id for item in items]

    def fetch_tariff_by_uid(self, source: str, uid: str) -> Tariff:
        tariff = (
            self.session
            .query(Tariff)
            .options(
                selectinload(Tariff.elements),
                selectinload(Tariff.tariff_associations),
            )
            .filter(Tariff.source == source, Tariff.uid == uid)
            .first()
        )
        return self._or_raise(tariff, f'tariff with uid {uid} and source {source} not found')

    def save_tariff(self, tariff: Tariff, *, commit: bool = True):
        self._save_resources(tariff, commit=commit)

    def delete_tariff(self, tariff: Tariff, *, commit: bool = True):
        self.session.delete(tariff)
        if commit:
            self.session.commit()
