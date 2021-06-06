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

import os
import json
from lxml import etree

from tests.helper import monkey_patch
from tests.integration.helper.BaseIntegrationTestCase import BaseIntegrationTestCase

from flask import current_app
from webapp.services.ocpi.SaveLocation import save_locations


class SaveChargepointTest(BaseIntegrationTestCase):
    run_reset_database = True

    def test_json_to_update(self):
        with open(os.path.join(current_app.config['TESTS_DIR'], 'files', 'ocpi.json')) as ochp_file:
            ocpi_data = json.loads(ochp_file.read())
        save_locations(ocpi_data['data'])
