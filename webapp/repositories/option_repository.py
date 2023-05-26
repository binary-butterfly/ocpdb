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


import json
from decimal import Decimal
from datetime import datetime
from typing import Any, Optional

import pytz

from .base_repository import BaseRepository
from webapp.models import Option


class OptionRepository(BaseRepository[Option]):
    model_cls = Option

    model_cls = Option

    def get(self, key, default: Optional[Any] = None) -> Any:
        option = self.session.query(Option).filter_by(key=key).first()
        if not option:
            return default
        output = self.get_output_value(option)
        return output

    def get_output_value(self, option: Option) -> Any:
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

    def set(self, key: str, value: Any, value_type='string'):
        option = self.session.query(Option).filter_by(key=key).first()
        if option:
            if value == self.get_output_value(option) and value_type == option.type:
                return
        else:
            option = Option()
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
        self.session.add(option)
        self.session.commit()

    def delete(self, key: str):
        option = self.session.query(Option).filter_by(key=key).first()
        if not option:
            return
        self.session.delete(option)
        self.session.commit()

