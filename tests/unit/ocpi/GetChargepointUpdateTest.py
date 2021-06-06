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

from webapp.services.ocpi.SaveChargepoint import get_chargepoint_update


class GetLocationUpdateTest(BaseTestCase):

    def test_json_to_update(self):
        data_chargepoint = {
            "evse_id": "DE*EBW*E800282*1",
            "status": "AVAILABLE",
            "phone": "072172586460",
            "capabilities": [
                "REMOTE_START_STOP_CAPABLE",
                "RFID_READER"
            ]
        }

        chargepoint = get_chargepoint_update(data_chargepoint)
        assert chargepoint is not None




