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

from enum import Enum
from sqlalchemy_utc import UtcDateTime
from .base import BaseModel
from webapp.extensions import db


class ExceptionalPeriodType(Enum):
    opening = 'opening'
    closing = 'closing'


class ExceptionalPeriod(db.Model, BaseModel):
    __tablename__ = "exceptional_period"

    location_id = db.Column(db.BigInteger, db.ForeignKey('location.id'))
    type = db.Column(db.Enum(ExceptionalPeriodType, name='ExceptionalPeriodType'))
    period_begin = db.Column(UtcDateTime(timezone=True))
    period_end = db.Column(UtcDateTime(timezone=True))
