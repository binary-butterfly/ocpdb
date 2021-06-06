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

from lxml import etree

from tests.helper import monkey_patch
from tests.helper import BaseTestCase
from tests.files.ChargepointData import test_dataset

from webapp.services.ocpi.SaveConnector import get_connector_update


class GetConnectorUpdateTest(BaseTestCase):

    def test_json_to_update(self):
        data_connector = {
          "uid": "1",
          "standard": "IEC_62196_T2",
          "format": "SOCKET",
          "power_type": "AC_3_PHASE",
          "max_voltage": 400,
          "max_amperage": 32,
          "max_electric_power": 22000
        }
        connector = get_connector_update(data_connector)
        assert connector is not None




