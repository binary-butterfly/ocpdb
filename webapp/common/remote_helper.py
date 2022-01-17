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

import json
from enum import Enum
from dataclasses import dataclass
from requests import request
from typing import Optional, Union, List, TYPE_CHECKING
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError
from json.decoder import JSONDecodeError
from webapp.common.misc import DefaultJSONEncoder
from webapp.common.config import ConfigHelper
if TYPE_CHECKING:
    from webapp.common.logger import Logger


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


class ExternalException(Exception):
    http_status: Optional[int] = None

    def __init__(self, http_status: Optional[int] = None):
        self.http_status = http_status


class RemoteHelper:
    logger: 'Logger'
    config_helper: ConfigHelper

    def __init__(self, logger: 'Logger', config_helper: ConfigHelper):
        self.logger = logger
        self.config_helper = config_helper

    def request(self, method: str, remote_server: RemoteServer, path: str, data: dict = None) -> Union[dict, list]:
        url = '%s%s' % (remote_server.url, path)
        json_data = json.dumps(data, cls=DefaultJSONEncoder) if data else None
        try:
            response = request(
                method=method,
                url=url,
                auth=(remote_server.user, remote_server.password),
                **({} if json_data is None else {'data': json_data}),
                headers={
                    'content-type': 'application/json'
                }
            )
            self.logger.info('server.external', "%s %s: HTTP %s%s\n<< %s" % (
                url,
                method,
                response.status_code,
                "\n>> %s" % json_data if method in ['post', 'put', 'patch'] and json_data else '',
                response.text
            ))
            try:
                if response.status_code not in [200, 201]:
                    raise ExternalException(
                        http_status=response.status_code
                    )
                return response.json()
            except JSONDecodeError:
                raise ExternalException(http_status=response.status_code)
        except (ConnectionError, NewConnectionError):
            raise ExternalException

    def get(self, remote_server_type: RemoteServerType, path):
        return self.request('get', self.config_helper.get('REMOTE_SERVERS')[remote_server_type], path)

    def post(self, remote_server_type: RemoteServerType, path: str, data: dict):
        return self.request('put', self.config_helper.get('REMOTE_SERVERS')[remote_server_type], path, data)

    def put(self, remote_server_type: RemoteServerType, path: str, data: dict):
        return self.request('put', self.config_helper.get('REMOTE_SERVERS')[remote_server_type], path, data)

    def patch(self, remote_server_type: RemoteServerType, path: str, data: dict):
        return self.request('patch', self.config_helper.get('REMOTE_SERVERS')[remote_server_type], path, data)

    def delete(self, remote_server_type: RemoteServerType, path: str):
        return self.request('delete', self.config_helper.get('REMOTE_SERVERS')[remote_server_type], path)
