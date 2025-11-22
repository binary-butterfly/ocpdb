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

from webapp.models import Source

SOURCE_UID_1 = 'SOURCE-1'
SOURCE_UID_2 = 'SOURCE-2'


def get_source(**kwargs) -> Source:
    default_data = {
        'uid': SOURCE_UID_1,
        'name': 'Test Source',
    }
    data = {**default_data, **kwargs}
    return Source(**data)
