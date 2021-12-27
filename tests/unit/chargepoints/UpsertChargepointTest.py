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

from dataclasses import asdict
from validataclass.helpers import UnsetValue

from tests.helper import monkey_patch
from tests.helper import BaseTestCase

from webapp.services.generic.SaveChargepoint import upsert_chargepoint, ChargepointUpdate
from webapp.enums import Capability, ParkingRestriction
from webapp.models import Chargepoint, Location


class UpsertChargepointTest(BaseTestCase):

    def test_xml_to_update(self):
        chargepoint_update = ChargepointUpdate(
            source='unittest',
            uid='UNITTEST',
            evse_id='UNITTEST',
            phone='+49 1234567890',
            parking_uid='TESTING',
            parking_floor_level='12',
            parking_spot_number='1234',
            capabilities=[Capability.RFID_READER, Capability.PUBLIC],
            parking_restrictions=[ParkingRestriction.EV_ONLY, ParkingRestriction.CUSTOMERS],
            related_resources=[],
            connectors=[]
        )
        chargepoint_to_update = Chargepoint()
        chargepoint = upsert_chargepoint(chargepoint_update, Location(), chargepoint_to_update, [], commit=False)
        for field, value in asdict(chargepoint_update).items():
            if value == []:
                continue
            if value is UnsetValue:
                assert getattr(chargepoint, field) is None
            else:
                assert getattr(chargepoint, field) == value




