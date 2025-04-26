"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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


class LogMessageType(Enum):
    REQUEST_IN = 'request-in'
    REQUEST_OUT = 'request-out'
    DATABASE_CREATE = 'database-create'
    DATABASE_UPDATE = 'database-update'
    DATABASE_DELETE = 'database-delete'
    EXCEPTION = 'exception'
    DUPLICATE_HANDLING = 'duplicate-handling'
    IMPORT_SOURCE = 'import-source'
    IMPORT_LOCATION = 'import-location'
    IMPORT_EVSE = 'import-evse'
    IMPORT_IMAGE = 'import-image'
    MISC = 'misc'
    MAIN = 'main'
