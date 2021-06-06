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

import pytz
import json
from typing import Union
from decimal import Decimal
from datetime import datetime, date
from ..extensions import db
from .base import BaseModel


class Option(db.Model, BaseModel):
    __tablename__ = 'option'

    key = db.Column(db.String(128), index=True)
    type = db.Column(db.Enum('string', 'date', 'datetime', 'integer', 'decimal', 'dict', 'list', name='OptionType'))
    value = db.Column(db.Text)

    @classmethod
    def get(cls, key, default=None) -> Union[None, dict, list, str, int, datetime, date, Decimal]:
        option = cls.query.filter_by(key=key).first()
        if not option:
            return default
        output = cls.get_output_value(option)
        return output

    @classmethod
    def get_output_value(cls, option: 'Option') -> Union[None, dict, list, str, int, datetime, date, Decimal]:
        if not option:
            return None
        if not option.type or option.type == 'string':
            return option.value
        elif option.type == 'integer':
            return int(option.value)
        elif option.type == 'decimal':
            return Decimal(option.value)
        elif option.type == 'datetime':
            return datetime.strptime(option.value, '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.UTC)
        elif option.type == 'date':
            return datetime.strptime(option.value, '%Y-%m-%d').date()
        elif option.type in ['dict', 'list']:
            return json.loads(option.value)

    @classmethod
    def set(cls, key: str, value: Union[None, dict, list, str, int, datetime, date, Decimal], value_type: str = 'string'):
        option = cls.query.filter_by(key=key).first()
        if option:
            if value == cls.get_output_value(option) and value_type == option.type:
                return
        else:
            option = cls()
            option.key = key
        option.type = value_type
        if value_type == 'string':
            option.value = value
        elif value_type == 'decimal' or value_type == 'integer':
            option.value = str(value)
        elif option.type == 'datetime':
            option.value = value.strftime('%Y-%m-%dT%H:%M:%S')
        elif option.type == 'date':
            option.value = value.strftime('%Y-%m-%d')
        elif option.type in ['dict', 'list']:
            option.value = json.dumps(value)
        db.session.add(option)
        db.session.commit()

    @classmethod
    def delete(cls, key: str) -> None:
        option = cls.query.filter_by(key=key).first()
        if not option:
            return
        db.session.delete(option)
        db.session.commit()
