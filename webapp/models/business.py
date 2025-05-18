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

from typing import TYPE_CHECKING, Optional

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

if TYPE_CHECKING:
    from .image import Image


class Business(BaseModel):
    __tablename__ = 'business'

    logo: Mapped[Optional['Image']] = relationship('Image', uselist=False)

    logo_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('image.id', use_alter=True), nullable=True)

    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    website: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def to_dict(self, *args, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []
        ignore += ['logo_id', 'id', 'created', 'modified']

        return super().to_dict(*args, ignore=ignore, **kwargs)
