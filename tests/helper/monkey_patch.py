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

# TODO: this can be done better by https://docs.pytest.org/en/latest/how-to/monkeypatch.html?highlight=mock#simple-example-monkeypatching-functions or https://changhsinlee.com/pytest-mock/

from datetime import datetime, date
from webapp.common import helpers
from tests.helper import mock_data


def get_today():
    return mock_data.get('today') or date.today()


helpers.get_today = get_today


def get_now():
    return mock_data.get('now') or datetime.utcnow()


helpers.get_now = get_now


helpers.is_offline = lambda: True
