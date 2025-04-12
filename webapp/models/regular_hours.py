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

from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

if TYPE_CHECKING:
    from .location import Location


class RegularHours(BaseModel):
    __tablename__ = 'regular_hours'

    location: Mapped['Location'] = relationship('Location', back_populates='regular_hours')
    location_id = mapped_column(BigInteger, ForeignKey('location.id', use_alter=True), nullable=False)

    weekday: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    period_begin: Mapped[int] = mapped_column(Integer, nullable=False)
    period_end: Mapped[int] = mapped_column(Integer, nullable=False)

    def to_dict(self, *args, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []
        ignore += ['location_id', 'id', 'created', 'modified']

        result = super().to_dict(*args, ignore=ignore, **kwargs)

        result['period_begin'] = '%02d:%02d' % (self.period_begin // 3600, self.period_begin % 60 // 60)
        result['period_end'] = '%02d:%02d' % (self.period_end // 3600, self.period_end % 60 // 60)

        return result
