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

from typing import TYPE_CHECKING, List, Optional

from webapp.common.sqlalchemy import Mapped
from webapp.extensions import db

from .base import BaseModel

if TYPE_CHECKING:
    from .location import Location


class RegularHours(db.Model, BaseModel):
    __tablename__ = 'regular_hours'

    location: Mapped['Location'] = db.relationship('Location', back_populates='regular_hours')
    location_id = db.Column(db.BigInteger, db.ForeignKey('location.id', use_alter=True), nullable=False)

    weekday: Mapped[int] = db.Column(db.SmallInteger, nullable=False)
    period_begin: Mapped[int] = db.Column(db.Integer, nullable=False)
    period_end: Mapped[int] = db.Column(db.Integer, nullable=False)

    def to_dict(
        self,
        fields: Optional[List[str]] = None,
        ignore: Optional[List[str]] = None,
        transform_ocpi: bool = False,
    ) -> dict:
        result = super().to_dict(fields, ignore)
        if transform_ocpi:
            result['period_begin'] = '%02d:%02d' % (self.period_begin // 3600, self.period_begin % 60 // 60)
            result['period_end'] = '%02d:%02d' % (self.period_end // 3600, self.period_end % 60 // 60)
        return result
