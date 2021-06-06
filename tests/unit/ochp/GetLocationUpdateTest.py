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

from webapp.services.ochp.SaveLocation import get_location_update
from webapp.services.ochp.Helper import get_nsmap


class GetLocationUpdateTest(BaseTestCase):

    def test_xml_to_update(self):
        nsmap = get_nsmap()
        data_xml = etree.fromstring(test_dataset)
        data_chargepoints = list(data_xml.xpath('//soap:Envelope/soap:Body/ns:GetChargePointListResponse/ns:chargePointInfoArray', namespaces=nsmap))
        data_chargepoint = data_chargepoints[0]
        location = get_location_update(data_chargepoint)
        assert location is not None
        assert location.uid == 'DE1ESS0013'




