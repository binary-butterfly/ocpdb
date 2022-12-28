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

from typing import Optional

from sqlalchemy.orm import Session

from webapp.common.error_handling.exceptions import AppException
from webapp.extensions import db


class InconsistentDataException(AppException):
    code = 'inconsistent_data'


class ObjectNotFoundException(AppException):
    """
    The requested object was not found or is out of scope.
    This exception may be extended (e.g. UserNotFoundException) for specific object types if needed.
    """
    code = 'not_found'
    http_status = 404


class BaseRepository:

    session: Session

    def __init__(self, session: Optional[Session] = None) -> None:
        self.session = db.session if session is None else session

    def exists(self, obj, field, value):
        return self.session.query(obj).filter(**{field: value}).count() > 0
