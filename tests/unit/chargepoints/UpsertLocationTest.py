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

from decimal import Decimal
from dataclasses import asdict
from validataclass.helpers import UnsetValue
from tests.helper import monkey_patch
from tests.helper import BaseTestCase

from webapp.services.generic.SaveLocation import upsert_location, LocationUpdate
from webapp.models import Location


class UpsertLocationTest(BaseTestCase):

    def test_xml_to_update(self):
        location_update = LocationUpdate(
            source='unittest',
            uid='UNITTEST',
            name='TEST-LOCATION',
            address='Test-Adresse',
            postal_code='12345',
            city='Test-Stadt',
            country='DE',
            lat=Decimal('51.163361111111'),
            lon=Decimal('10.447683333333'),
            twentyfourseven=True,
            regular_hours=[],
            exceptional_openings=[],
            exceptional_closings=[],
            chargepoints=[]
        )
        location_to_update = Location()
        location = upsert_location(location_update, location_to_update, [], [], commit=False)
        for field, value in asdict(location_update).items():
            if value == []:
                continue
            if value is UnsetValue:
                assert getattr(location, field) is None
            else:
                assert getattr(location, field) == value




