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

import requests
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError
from json.decoder import JSONDecodeError

from flask import current_app
from ...models import Option
from ...extensions import logger
from ...common.helpers import get_now
from .SaveLocation import save_locations


def ocpi_get_chargepoint_list(source: str):
    start = get_now()
    try:
        ocpi_request = requests.get(current_app.config['OCPI_SOURCES'][source]['url'])
        ocpi_data = ocpi_request.json()
        assert 'data' in ocpi_data
        assert type(ocpi_data['data']) is list
    except (ConnectionError, NewConnectionError, JSONDecodeError, AssertionError):
        logger.info('ocpi.%s.get-chargepoint-list' % source, 'error getting ocpi data from source %s')
        return
    between = get_now()
    logger.info('ocpi.%s.get-chargepoint-list' % source, 'got data in %s s' % (between - start).total_seconds())
    save_locations(ocpi_data['data'])
    logger.info('ocpi.%s.get-chargepoint-list' % source, 'stored data in %s s' % (get_now() - between).total_seconds())
    Option.set('ocpi.%s.get-chargepoint-list-last-update' % source, start, 'datetime')
