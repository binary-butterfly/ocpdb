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
from datetime import datetime
from typing import List, Tuple

from validataclass.helpers import UnsetValue, OptionalUnset

from webapp.models import Evse, Location
from webapp.models.evse import EvseStatus
from .base_repository import BaseRepository, ObjectNotFoundException, InconsistentDataException


@dataclass
class EvseUpdate:
    last_updated: OptionalUnset[datetime] = UnsetValue
    status: OptionalUnset[EvseStatus] = UnsetValue


class EvseRepository(BaseRepository[Evse]):
    model_cls = Evse

    def fetch_by_id(self, evse_id: int) -> Evse:
        result = self.session.query(Evse).get(evse_id)

        if result is None:
            raise ObjectNotFoundException(message=f'evse with id {evse_id} not found')

        return result

    def fetch_by_uid(self, source: str, uid: str) -> Evse:
        items = self.session.query(Evse)\
            .filter(Evse.uid == uid)\
            .join(Location, Location.id == Evse.location_id)\
            .filter(Location.source == source)\
            .all()

        if len(items) == 0:
            raise ObjectNotFoundException(message=f'evse with uid {uid} and source {source} not found')

        if len(items) > 1:
            raise InconsistentDataException(f'more than one evse with uid {uid} and source {source}')

        return items[0]

    def fetch_evse_by_location_id(self, location_id: int) -> List[Evse]:
        return self.session.query(Evse).filter(Evse.location_id == location_id)

    def fetch_evse_uids(self) -> List[str]:
        items = self.session.query(Evse.uid).all()

        return [item.uid for item in items]

    def fetch_extended_evse_uids(self) -> List[Tuple[str, int]]:
        items = self.session.query(Evse.uid, Evse.location_id).all()

        return [(item.uid, item.location_id) for item in items]

    def save_evse(self, evse: Evse, *, commit: bool = True):
        self.session.add(evse)
        if commit:
            self.session.commit()

    def delete_evse_by_ids(self, evse_ids: List[int]):
        self.session.query(Evse)\
            .filter(Evse.id.in_(evse_ids))\
            .delete(synchronize_session=False)

    def delete_evse_by_id(self, evse_id: int):
        self.session.query(Evse)\
            .filter(id=evse_id)\
            .delete(synchronize_session=False)
