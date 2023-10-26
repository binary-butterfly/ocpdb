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

from webapp.common.sqlalchemy import Col
from webapp.extensions import db
from .base import BaseModel


class Option(db.Model, BaseModel):
    __tablename__ = 'option'

    key: Col[str] = db.Column(db.String(128), index=True)
    type: Col[str] = db.Column(db.Enum('string', 'date', 'datetime', 'integer', 'decimal', 'dict', 'list', name='OptionType'))
    value: Col[str] = db.Column(db.Text)
