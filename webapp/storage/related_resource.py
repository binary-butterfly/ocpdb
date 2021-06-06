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
from enum import Enum
from .base import BaseModel
from ..extensions import db


class RelatedResourceType(Enum):
    OPERATOR_MAP = 1 << 0
    OPERATOR_PAYMENT = 1 << 1
    STATION_INFO = 1 << 2
    SURROUNDING_INFO = 1 << 3
    OWNER_HOMEPAGE = 1 << 4
    FEEDBACK_FORM = 1 << 5
    OPENING_TIMES = 1 << 5


class RelatedResource(db.Model, BaseModel):
    __tablename__ = "related_resource"

    chargepoint_id = db.Column(db.BigInteger, db.ForeignKey('chargepoint.id'))
    url = db.Column(db.String(255))
    _types = db.Column('types', db.Integer)

    def _get_types(self) -> List[RelatedResourceType]:
        if not self._types:
            return []
        return sorted(
            [item for item in list(RelatedResourceType) if item.value & self._types],
            key=lambda item: item.value
        )

    def _set_types(self, types: List[RelatedResourceType]) -> None:
        self._types = 0
        for type in types:
            self._types = self._types | type.value

    types = db.synonym('_types', descriptor=property(_get_types, _set_types))
