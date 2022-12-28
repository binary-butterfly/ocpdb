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

from sqlalchemy_utc import UtcDateTime

from webapp.common.sqlalchemy import Col, Rel
from webapp.extensions import db
from .base import BaseModel

if TYPE_CHECKING:
    from .location import Location


class ExceptionalClosingPeriod(db.Model, BaseModel):
    __tablename__ = "exceptional_closing_period"

    location: Rel['Location'] = db.relationship('Location', back_populates='exceptional_closings')
    location_id: Col[int] = db.Column(db.BigInteger, db.ForeignKey('location.id', use_alter=True), nullable=False)
    period_begin: Col[datetime] = db.Column(UtcDateTime(), nullable=False)
    period_end: Col[datetime] = db.Column(UtcDateTime(), nullable=False)
