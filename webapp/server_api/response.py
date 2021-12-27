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
import traceback
from typing import Union, Optional

from flask import Response
from webapp.common.misc import DefaultJSONEncoder
from webapp.common.exceptions import AppException


class ServerApiResponse(Response):  # pylint: disable=too-many-ancestors

    charset = 'utf-8'
    default_status = 200
    default_mimetype = 'application/json'

    _http_error_code_mapping = {
        400: 'bad_request',
        401: 'unauthorized',
        403: 'forbidden',
        404: 'not_found',
        405: 'method_not_allowed',
        408: 'request_timeout',
        418: 'im_a_teapot',
        500: 'internal_server_error',
        501: 'not_implemented',
        502: 'bad_gateway',
        503: 'service_unavailable',
        504: 'gateway_timeout',
    }

    @classmethod
    def success(cls, data: Union[list, dict, None], status: int = 200):
        assert status in [200, 201]
        result = json.dumps({} if data is None else data, cls=DefaultJSONEncoder)
        return cls(result, status)

    @classmethod
    def error(
            cls,
            http_status: int = 400,
            code: str = None,
            message: str = None,
            exception: Optional[Exception] = None,
            data: Optional[dict] = None):
        assert http_status in cls._http_error_code_mapping.keys()
        response = {'error': {}}
        if exception is None or not isinstance(exception, AppException):
            response['error']['code'] = cls._http_error_code_mapping[http_status] if code is None else code
            if message:
                response['error']['message'] = message
            if data is not None:
                response['error']['data'] = data
        else:
            http_status = exception.http_status
            response['error']['code'] = exception.code
            if exception.data:
                response['error']['data'] = exception.data
        if exception is not None and not isinstance(exception, AppException):
            response['_debug'] = {
                'exception': repr(exception),
                'traceback': traceback.format_exc().splitlines(),
            }

        response_json = json.dumps(response, cls=DefaultJSONEncoder)
        return cls(response_json, http_status)
