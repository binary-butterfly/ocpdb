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

from webapp.models import Business

BUSINESS_1_NAME = 'Electro Inc'
BUSINESS_2_NAME = 'Power Inc'


def get_business(**kwargs) -> Business:
    default_data = {
        'name': BUSINESS_1_NAME,
    }
    data = {**default_data, **kwargs}
    return Business(**data)


def get_business_1(**kwargs) -> Business:
    return get_business(**kwargs)


def get_business_2(**kwargs) -> Business:
    return get_business(name=BUSINESS_2_NAME, **kwargs)
