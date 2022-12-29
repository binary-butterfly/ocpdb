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
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from json.decoder import JSONDecodeError
from typing import Optional, Union, Tuple

from requests import request
from requests.exceptions import ConnectionError, Timeout
from urllib3.exceptions import NewConnectionError

from webapp.common.config import ConfigHelper
from webapp.common.logger import Logger
from webapp.common.json import DefaultJSONEncoder


class RemoteServerType(Enum):
    CHARGEIT = 'CHARGEIT'
    GIROE = 'GIROE'
    STADTNAVI = 'STADTNAVI'
    LADENETZ = 'LADENETZ'


@dataclass
class RemoteServer:
    url: str
    user: Optional[str] = None
    password: Optional[str] = None
    cert: Optional[str] = None


class RemoteHelperMethodMixin(ABC):

    @abstractmethod
    def request(self, **kwargs):
        pass

    def get(self, **kwargs):
        return self.request(method='get', **kwargs)

    def post(self, **kwargs):
        return self.request(method='post', **kwargs)

    def put(self, **kwargs):
        return self.request(method='put', **kwargs)

    def patch(self, **kwargs):
        return self.request(method='patch', **kwargs)

    def delete(self, **kwargs):
        return self.request(method='delete', **kwargs)


class RemoteException(Exception):
    http_status: Optional[int] = None

    def __init__(self, http_status: Optional[int] = None):
        self.http_status = http_status


class RemoteHelper(RemoteHelperMethodMixin):
    config_helper: ConfigHelper
    logger: Logger

    def __init__(self, config_helper: ConfigHelper, logger: Logger):
        self.config_helper = config_helper
        self.logger = logger

    def request(
            self,
            method: str,
            remote_server_type: Optional[RemoteServerType] = None,
            url: Optional[str] = None,
            path: Optional[str] = None,
            auth: Optional[Tuple[str, str]] = None,
            params: Optional[dict] = None,
            data: Optional[dict] = None,
            headers: Optional[dict] = None,
            ignore_404: Optional[bool] = False,
            raw: Optional[bool] = False,
    ) -> Union[dict, list, bytes, None]:
        if remote_server_type:
            remote_server = self.config_helper.get('REMOTE_SERVERS')[remote_server_type]
            if auth is None:
                auth = (remote_server.user, remote_server.password)
            if url is None:
                url = remote_server.url
        if path is not None:
            url = url + path
        try:
            response = request(
                method=method,
                url=url,
                params=params,
                auth=auth,
                data=(data if raw else json.dumps(data, cls=DefaultJSONEncoder)) if data else None,
                headers={'content-type': 'application/json', **({} if headers is None else headers)},
            )

            self.logger.info('server-remote', "%s %s: HTTP %s%s\n<< %s" % (
                url,
                method,
                response.status_code,
                '' if data is None else ("\n>> %s" % data),
                response.text,
            ))
            try:
                if response.status_code == 404 and ignore_404:
                    return
                if response.status_code not in [200, 201]:
                    raise RemoteException(http_status=response.status_code)
                if response.status_code == 204:
                    return
                if raw:
                    return response.content
                return response.json()
            except JSONDecodeError:
                raise RemoteException(http_status=response.status_code)

        except (ConnectionError, NewConnectionError, Timeout):
            self.logger.error('server-remote', 'cannot %s data to %s: %s' % (method, url, data))
            raise RemoteException
