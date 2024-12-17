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

from webapp.common.error_handling.exceptions import AppException


class RestApiException(AppException):
    """
    Base exception class for errors that are specific to REST APIs.
    """


class RestApiRemoteException(RestApiException):
    code = 'remote_exception'
    http_status = 500


class RestApiNotImplementedException(RestApiException):
    code = 'not_implemented'
    http_status = 501


class WrongContentTypeException(RestApiException):
    code = 'wrong_content_type'
    http_status = 400


class WrongJsonTypeException(RestApiException):
    code = 'wrong_json_type'
    http_status = 400


class InputValidationException(RestApiException):
    code = 'validation_error'
    http_status = 400


class UnauthorizedException(RestApiException):
    code = 'unauthorized'
    http_status = 401


class NotFoundException(RestApiException):
    code = 'not_found'
    http_status = 404
