"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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

from dataclasses import dataclass

from sqlalchemy.orm import selectinload
from validataclass_search_queries.pagination import PaginatedResult
from validataclass_search_queries.search_queries import BaseSearchQuery

from webapp.common.sqlalchemy import Query
from webapp.models import Evse, Location
from webapp.models.evse import EvseStatus

from .base_repository import BaseRepository
from .exceptions import InconsistentDataException, ObjectNotFoundException


@dataclass
class EvseStatusSummary:
    evse: str
    location: str
    status: EvseStatus
    source: str


class EvseRepository(BaseRepository[Evse]):
    model_cls = Evse

    def fetch_by_id(self, evse_id: int) -> Evse:
        result = self.session.query(Evse).get(evse_id)

        if result is None:
            raise ObjectNotFoundException(message=f'evse with id {evse_id} not found')

        return result

    def fetch_evse_by_id(self, evse_id: int, *, include_children: bool = False) -> Evse:
        query = self.session.query(Evse)

        if include_children:
            query = query.options(
                selectinload(Evse.connectors),
                selectinload(Evse.images),
            )

        result = query.filter(Evse.id == evse_id).first()

        if result is None:
            raise ObjectNotFoundException(message=f'evse with id {evse_id} not found')

        return result

    def fetch_evses(self, search_query: BaseSearchQuery | None = None) -> PaginatedResult[Evse]:
        options = [
            selectinload(Evse.connectors),
            selectinload(Evse.images),
        ]

        query = self.session.query(Evse).options(*options)
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
            query = query.join(Location, Location.id == Evse.location_id).filter(Location.source == source_uid)

        if source_uids := getattr(search_query, 'source_uids', None):
            query = query.join(Location, Location.id == Evse.location_id).filter(Location.source.in_(source_uids))

        if exclude_source_uid := getattr(search_query, 'exclude_source_uid', None):
            query = query.join(Location, Location.id == Evse.location_id).filter(Location.source != exclude_source_uid)

        if exclude_source_uids := getattr(search_query, 'exclude_source_uids', None):
            query = query.join(Location, Location.id == Evse.location_id).filter(
                Location.source.notin_(exclude_source_uids)
            )

        return query

    def fetch_by_uid(self, source: str, uid: str) -> Evse:
        items = (
            self.session
            .query(Evse)
            .filter(Evse.uid == uid)
            .join(Location, Location.id == Evse.location_id)
            .filter(Location.source == source)
            .all()
        )

        if len(items) == 0:
            raise ObjectNotFoundException(message=f'evse with uid {uid} and source {source} not found')

        if len(items) > 1:
            raise InconsistentDataException(f'more than one evse with uid {uid} and source {source}')

        return items[0]

    def fetch_evses_by_source_and_uids(self, source_uid: str, uids: list[str]) -> list[Evse]:
        query = (
            self.session
            .query(Evse)
            .filter(Evse.uid.in_(uids))
            .join(Evse.location)
            .filter(Location.source == source_uid)
        )

        return query.all()

    def fetch_evse_by_location_id(self, location_id: int) -> list[Evse]:
        return self.session.query(Evse).filter(Evse.location_id == location_id).all()

    def fetch_evse_uids(self) -> list[str]:
        items = self.session.query(Evse.uid).all()

        return [item.uid for item in items]

    def fetch_extended_evse_uids(self) -> list[tuple[str, int]]:
        items = self.session.query(Evse.uid, Evse.location_id).all()

        return [(item.uid, item.location_id) for item in items]

    def save_evse(self, evse: Evse, *, commit: bool = True):
        self._save_resources(evse, commit=commit)

    def fetch_evse_status_summary(self) -> list[EvseStatusSummary]:
        items = (
            self.session
            .query(Evse.uid.label('evse'), Evse.status, Location.uid.label('location'), Location.source)
            .filter(Evse.status != EvseStatus.STATIC)
            .join(Evse.location)
            .all()
        )
        result: list[EvseStatusSummary] = []
        for item in items:
            result.append(EvseStatusSummary(**dict(item)))

        return result
