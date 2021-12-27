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

    def update_evse(self, evse: Evse, evse_update: EvseUpdate):
        for key, value in asdict(evse_update).items():
            if value is UnsetValue:
                continue
            setattr(evse, key, value)

        self.session.add(evse)
        self.session.commit()

