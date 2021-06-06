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

from typing import TypeVar, Optional, List
from sqlalchemy.types import UserDefinedType
from sqlalchemy.sql.sqltypes import DateTime, Numeric, Enum, String, Boolean, Integer, Text, Date, SmallInteger
from ..extensions import db
from ..common.helpers import get_current_time

CurrentObject = TypeVar('CurrentObject', bound='Parent')


class BaseModel:
    __table_args__ = {
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_unicode_ci'
    }
    version = '1.0'

    id = db.Column(db.BigInteger, primary_key=True)
    created = db.Column(db.DateTime(timezone=True), nullable=False, default=get_current_time)
    modified = db.Column(db.DateTime(timezone=True), nullable=False, default=get_current_time, onupdate=get_current_time)

    def to_dict(self, fields: Optional[List[str]] = None, ignore: Optional[List[str]] = None) -> dict:
        result = {}
        for field in self.metadata.tables[self.__tablename__].c.keys():
            if fields is not None and field not in fields:
                continue
            if ignore is not None and field in ignore:
                continue
            result[field] = getattr(self, field)
        return result

    def from_dict(self, data: dict, include_id: bool = True) -> CurrentObject:
        for field in self.metadata.tables[self.__tablename__].c.keys():
            if field == 'id' and not include_id:
                continue
            if field not in data:
                continue
            setattr(self, field, data[field])
        return self

    @classmethod
    def json_schema(cls) -> dict:
        result = {}
        for field in cls.metadata.tables[cls.__tablename__].c.keys():
            field_type = cls.metadata.tables.get(cls.__tablename__).c[field].type
            if type(field_type) is Boolean:
                result[field] = {
                    'type': 'boolean'
                }
            elif type(field_type) is Integer:
                result[field] = {
                    'type': 'integer'
                }
            elif type(field_type) is SmallInteger:
                result[field] = {
                    'type': 'integer'
                }
            elif type(field_type) in [String, Text]:
                result[field] = {
                    'type': 'string'
                }
                if field_type.length:
                    result[field]['maxLength'] = field_type.length
            elif type(field_type) is Enum:
                result[field] = {
                    'type': 'string',
                    'enum': field_type.enums
                }
            elif type(field_type) is Numeric:
                result[field] = {
                    'type': 'string',
                    'pattern': "^[+-]?\d+(\.\d+)?$"
                }
            elif type(field_type) is Date:
                result[field] = {
                    'type': 'string',
                    'format': 'date'
                }
            elif type(field_type) is DateTime:
                result[field] = {
                    'type': 'string',
                    'format': 'date-time'
                }
            if field in result:
                result[field]['description'] = cls.metadata.tables.get(cls.__tablename__).c[field].info.get('description', '')
        return {
            '$schema': 'http://json-schema.org/draft-07/schema#',
            'title': cls.__name__,
            'type': 'object',
            'properties': result
        }


class Point(UserDefinedType):
    def get_col_spec(self):
        return 'POINT'
