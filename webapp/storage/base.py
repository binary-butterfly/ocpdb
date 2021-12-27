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

from sqlalchemy_utc import UtcDateTime
from typing import TypeVar, Optional, List
from sqlalchemy.types import UserDefinedType
from webapp.extensions import db
from webapp.common.helpers import get_now_localized

CurrentObject = TypeVar('CurrentObject', bound='Parent')


class BaseModel:
    __table_args__ = {
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_unicode_ci'
    }
    version = '1.0'

    id = db.Column(db.BigInteger, primary_key=True)
    created = db.Column(UtcDateTime(timezone=True), nullable=False, default=get_now_localized)
    modified = db.Column(UtcDateTime(timezone=True), nullable=False, default=get_now_localized, onupdate=get_now_localized)

    def to_dict(self, fields: Optional[List[str]] = None, ignore: Optional[List[str]] = None) -> dict:
        result = {}
        for field in self.metadata.tables[self.__tablename__].c.keys():
            if fields is not None and field not in fields:
                continue
            if ignore is not None and field in ignore:
                continue
            result[field] = getattr(self, field)
        return result


class Point(UserDefinedType):
    def get_col_spec(self):
        return 'POINT'
