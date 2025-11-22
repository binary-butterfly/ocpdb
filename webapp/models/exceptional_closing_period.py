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
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy_utc import UtcDateTime

from .base import BaseModel
from .connector import mapped_column

if TYPE_CHECKING:
    from .location import Location


class ExceptionalClosingPeriod(BaseModel):
    __tablename__ = 'exceptional_closing_period'

    location: Mapped['Location'] = relationship('Location', back_populates='exceptional_closings')
    location_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey('location.id', use_alter=True), nullable=False, index=True
    )
    period_begin: Mapped[datetime] = mapped_column(UtcDateTime(), nullable=False)
    period_end: Mapped[datetime] = mapped_column(UtcDateTime(), nullable=False)

    def to_dict(self, *args, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []
        ignore += ['id', 'created', 'modified']

        result = super().to_dict(*args, ignore, **kwargs)

        return result
