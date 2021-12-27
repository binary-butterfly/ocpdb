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

from flask import Config, current_app
from typing import Optional
from sqlalchemy.orm import Session
from webapp.extensions import db
from webapp.common.exceptions import AppException


class UnsetValue:
    def __call__(self):
        return self

    def __repr__(self):
        return 'UnsetValue'

    def __str__(self):
        return '<UnsetValue>'

    def __bool__(self):
        return False


# Create sentinel object and redefine __new__ so that the object cannot be cloned
unset_value = UnsetValue()
UnsetValue.__new__ = lambda cls: unset_value


class InconsistentDataException(Exception):
    pass


class ObjectNotFoundException(AppException):
    """
    The requested object was not found or is out of scope.
    This exception may be extended (e.g. UserNotFoundException) for specific object types if needed.
    """
    code = 'not_found'
    message = 'object not found'
    http_status = 404


class BaseRepository:

    session: Session

    def __init__(self, session: Optional[Session] = None) -> None:
        self.session = db.session if session is None else session

    def exists(self, obj, field, value):
        return self.session(obj).filter(**{field: value}).count() > 0
