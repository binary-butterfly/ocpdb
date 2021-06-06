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

from tests.helper import monkey_patch

from datetime import date
from webapp.common import helpers
from webapp.common.helpers import get_today
from tests.helper import BaseTestCase, mock_data


class HelpersTest(BaseTestCase):

    def test_get_current_date(self):
        expected_date = date.today()
        assert helpers.get_today() == expected_date

    def test_mocking(self):
        mock_data['today'] = date(2020, 1, 1)
        assert helpers.get_today() == date(2020, 1, 1)
        assert get_today() == date(2020, 1, 1)
