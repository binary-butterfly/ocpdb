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

from datetime import datetime, timezone
from validataclass.helpers import validataclass, OptionalUnset, DefaultUnset
from validataclass.validators import DateTimeValidator, EnumValidator, DateTimeFormat
from webapp.enums import ChargepointStatus


@validataclass
class ConnectorPatchInput:
    modified: datetime = DateTimeValidator(
        DateTimeFormat.LOCAL_OR_UTC,
        local_timezone=timezone.utc,
        target_timezone=timezone.utc
    )
    status: OptionalUnset[ChargepointStatus] = EnumValidator(ChargepointStatus), DefaultUnset()
