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

from webapp.models import Business
from .base_repository import BaseRepository, ObjectNotFoundException


class BusinessRepository(BaseRepository[Business]):
    model_cls = Business

    def fetch_by_id(self, business_id: int) -> Business:
        result = self.session.query(Business).filter(Business.id == business_id).one_or_none()

        if result is None:
            raise ObjectNotFoundException(f'business with id {business_id} not found')

        return result

    def fetch_businesses(self) -> List[Business]:
        return self.session.query(Business).all()

    def fetch_business_by_name(self, name: str) -> Business:

        result = self.session.query(Business).filter(Business.name.__contains__(name)).first()

        if result is None:
            raise ObjectNotFoundException(f'business with name {name} not found')

        return result
