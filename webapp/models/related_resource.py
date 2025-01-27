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

from enum import Enum
from typing import TYPE_CHECKING, List

from sqlalchemy.ext.hybrid import hybrid_property

from webapp.common.sqlalchemy import Mapped
from webapp.extensions import db

from .base import BaseModel

if TYPE_CHECKING:
    from .evse import Evse


class RelatedResourceType(Enum):
    OPERATOR_MAP = 'OPERATOR_MAP'
    OPERATOR_PAYMENT = 'OPERATOR_PAYMENT'
    STATION_INFO = 'STATION_INFO'
    SURROUNDING_INFO = 'SURROUNDING_INFO'
    OWNER_HOMEPAGE = 'OWNER_HOMEPAGE'
    FEEDBACK_FORM = 'FEEDBACK_FORM'
    OPENING_TIMES = 'OPENING_TIMES'


class RelatedResource(db.Model, BaseModel):
    __tablename__ = 'related_resource'

    evse: Mapped['Evse'] = db.relationship('Evse', back_populates='related_resources')
    evse_id: Mapped[int] = db.Column(db.BigInteger, db.ForeignKey('evse.id', use_alter=True), nullable=False)

    url: Mapped[str | None] = db.Column(db.String(255), nullable=True)
    _types: Mapped[int | None] = db.Column('types', db.Integer, nullable=True)

    @hybrid_property
    def types(self) -> List[RelatedResourceType]:
        if not self._types:
            return []
        return sorted(
            [item for item in list(RelatedResourceType) if item.value & self._types], key=lambda item: item.value
        )

    @types.setter
    def types(self, types: List[RelatedResourceType]) -> None:
        self._types = 0
        for _type in types:
            self._types = self._types | _type.value

    def to_dict(self, *args, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []
        ignore += ['id', 'created', 'modified', 'evse_id']

        result = super().to_dict(*args, ignore, **kwargs)

        return result
