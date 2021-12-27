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

from tests.helper import monkey_patch
from tests.helper import BaseTestCase

from webapp.services.generic.SaveConnector import upsert_connector, ConnectorUpdate
from webapp.enums import ConnectorType, ConnectorFormat
from webapp.models import Connector, Chargepoint


class UpsertConnectorTest(BaseTestCase):

    def test_xml_to_update(self):
        connector_update = ConnectorUpdate(
            source='unittest',
            uid='1',
            standard=ConnectorType.IEC_62196_T2,
            format=ConnectorFormat.SOCKET,
            max_electric_power=22000
        )
        connector_to_update = Connector()
        chargepoint = upsert_connector(connector_update, Chargepoint(), connector_to_update, False)
        for field, value in asdict(connector_update).items():
            if field in ['max_voltage']:
                continue
            assert getattr(chargepoint, field) == value
        assert chargepoint.max_voltage == 400
        assert chargepoint.max_amperage == 32
