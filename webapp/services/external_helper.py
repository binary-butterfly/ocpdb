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
from typing import Union, Optional
from requests import request
from flask import current_app
from validataclass.validators import StringValidator
from validataclass.helpers import validataclass
from webapp.common.misc import DefaultJSONEncoder
from webapp.extensions import logger
from webapp.common.remote_helper import RemoteServerType, RemoteServer
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError
from json.decoder import JSONDecodeError


@validataclass
class ExternalExceptionErrorData:
    code: str = StringValidator()
    message: str = StringValidator()


class ExternalException(Exception):
    http_status: Optional[int] = None

    def __init__(self, http_status: Optional[int] = None, error: ExternalExceptionErrorData = None):
        self.http_status = http_status
        self.error = error


class ExternalHelper:

    def request(
            self,
            method: str,
            remote_server: RemoteServer,
            url: Optional[str] = None,
            path: Optional[str] = None,
            data: dict = None) -> Union[dict, list]:
        if not url:
            url = remote_server.url if path is None else '%s%s' % (remote_server.url, path)
        try:
            response = request(
                method=method,
                url=url,
                auth=(remote_server.user, remote_server.password),
                **({} if data is None else {'data': json.dumps(data, cls=DefaultJSONEncoder)}),
                headers={
                    'content-type': 'application/json'
                }
            )
            logger.info('server.external', "%s %s: HTTP %s%s\n<< %s" % (
                url,
                method,
                response.status_code,
                "\n>> %s" % '' if data is None else data,
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
            logger.error('server.external', 'cannot %s data to %s: %s' % (method, url, data))
            raise ExternalException

    def get(
            self,
            remote_server_type: RemoteServerType,
            url: Optional[str] = None,
            path: Optional[str] = None) -> Union[dict, list]:
        return self.request(
            'get',
            remote_server=current_app.config['REMOTE_SERVERS'][remote_server_type],
            url=url,
            path=path
        )

    def post(
            self,
            remote_server_type: RemoteServerType,
            url: Optional[str] = None,
            path: Optional[str] = None,
            data: Optional[dict] = None) -> Union[dict, list]:
        return self.request(
            'post',
            remote_server=current_app.config['REMOTE_SERVERS'][remote_server_type],
            url=url,
            path=path,
            data=data
        )

    def put(
            self,
            remote_server_type: RemoteServerType,
            url: Optional[str] = None,
            path: Optional[str] = None,
            data: Optional[dict] = None) -> Union[dict, list]:
        return self.request(
            'put',
            remote_server=current_app.config['REMOTE_SERVERS'][remote_server_type],
            url=url,
            path=path,
            data=data
        )

    def patch(
            self,
            remote_server_type: RemoteServerType,
            url: Optional[str] = None,
            path: Optional[str] = None,
            data: Optional[dict] = None) -> Union[dict, list]:
        return self.request(
            'patch',
            remote_server=current_app.config['REMOTE_SERVERS'][remote_server_type],
            url=url,
            path=path,
            data=data
        )

    def delete(
            self,
            remote_server_type: RemoteServerType,
            url: Optional[str] = None,
            path: Optional[str] = None) -> Union[dict, list]:
        return self.request(
            'delete',
            remote_server=current_app.config['REMOTE_SERVERS'][remote_server_type],
            url=url,
            path=path
        )
