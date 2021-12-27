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

from enum import Enum
from typing import Optional
from dataclasses import dataclass


class RemoteServerType(Enum):
    CHARGEIT = 'CHARGEIT'
    GIROE = 'GIROE'
    STADTNAVI = 'STADTNAVI'


@dataclass
class RemoteServer:
    url: str
    user: Optional[str] = None
    password: Optional[str] = None
    cert: Optional[str] = None


def check_and_extend_config(app):
    app.config['REMOTE_SERVERS'] = {
        RemoteServerType[key]: RemoteServer(**server) for key, server in app.config['REMOTE_SERVERS'].items()
    }

    # Ensure that important config values are set
    config_check = [key for key in app.config['ENFORCE_CONFIG_VALUES'] if key not in app.config]
    if len(config_check) > 0:
        raise Exception('missing config values: %s' % ', '.join(config_check))
