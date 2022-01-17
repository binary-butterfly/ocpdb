# encoding: utf-8

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

from typing import List
from datetime import datetime
from dataclasses import dataclass, asdict
from validataclass.helpers import UnsetValue, OptionalUnset
from webapp.models import Chargepoint as Evse
from .base_repository import BaseRepository, ObjectNotFoundException
from webapp.enums import ChargepointStatus as EvseStatus


@dataclass
class EvseUpdate:
    last_modified: OptionalUnset[datetime] = UnsetValue
    status: OptionalUnset[EvseStatus] = UnsetValue


class EvseRepository(BaseRepository):

    def fetch_by_id(self, chargepoint_id: int) -> Evse:
        result = self.session.query(Evse).get(chargepoint_id)
        if result is None:
            raise ObjectNotFoundException
        return result

    def fetch_by_uid(self, source: str, chargepoint_uid: str) -> Evse:
        result = self.session.query(Evse)\
            .filter(Evse.uid == chargepoint_uid)\
            .filter(Evse.source == source)\
            .first()
        if result is None:
            raise ObjectNotFoundException
        return result

    def fetch_evse_by_location_id(self, location_id: int) -> List[Evse]:
        return self.session.query(Evse).filter(Evse.location_id == location_id)

    def update_evse(self, evse: Evse, evse_update: EvseUpdate):
        for key, value in asdict(evse_update).items():
            if value is UnsetValue:
                continue
            setattr(evse, key, value)

        self.session.add(evse)
        self.session.commit()

    def delete_evse_by_ids(self, evse_ids: List[int]):
        self.session.query(Evse)\
            .filter(Evse.id.in_(evse_ids))\
            .delete(synchronize_session=False)

    def delete_evse_by_id(self, evse_id: int):
        self.session.query(Evse)\
            .filter(id=evse_id)\
            .delete(synchronize_session=False)
