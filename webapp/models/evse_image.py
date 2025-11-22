"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from webapp.extensions import db


class EvseImageAssociation(db.Model):
    __tablename__ = 'evse_image'

    evse_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('evse.id'),
        primary_key=True,
        nullable=False,
        index=True,
    )
    image_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('image.id'),
        primary_key=True,
        nullable=False,
        index=True,
    )
