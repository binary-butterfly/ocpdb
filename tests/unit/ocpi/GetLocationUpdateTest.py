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

from webapp.services.ocpi.SaveLocation import get_location_update


class GetLocationUpdateTest(BaseTestCase):

    def test_json_to_update(self):
        data_location = {
            "uid": "DE*EBW*E800282",
            "name": "Parkplatz Benzstraße Herrenberg",
            "address": "Benzstraße 10",
            "postal_code": "71083",
            "city": "Herrenberg",
            "country": "DE",
            "last_updated": "2021-04-28T15:51:49",
            "coordinates": {
                "lat": "48.599106",
                "lon": "8.870451"
            },
            "opening_times": {
                "twentyfourseven": True
            },
        }

        location = get_location_update(data_location)
        assert location is not None




