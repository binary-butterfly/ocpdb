"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from datetime import datetime

from webapp.models.evse import EvseStatus
from webapp.shared.datex2.v3_7.shared.refill_point_status_enum import RefillPointStatusEnum

from .realtime_export_mapper import DatexJSONRealtimeExportMapper


class DatexV37JSONRealtimeExportMapper(DatexJSONRealtimeExportMapper):
    version = '3.7'
    profile_name = 'Afir Energy Infrastructure'
    evse_status_to_refill_point_status_map = {
        EvseStatus.AVAILABLE: RefillPointStatusEnum.AVAILABLE,
        EvseStatus.BLOCKED: RefillPointStatusEnum.BLOCKED,
        EvseStatus.CHARGING: RefillPointStatusEnum.CHARGING,
        EvseStatus.INOPERATIVE: RefillPointStatusEnum.INOPERATIVE,
        EvseStatus.OUTOFORDER: RefillPointStatusEnum.OUTOFORDER,
        EvseStatus.PLANNED: RefillPointStatusEnum.PLANNED,
        EvseStatus.REMOVED: RefillPointStatusEnum.REMOVED,
        EvseStatus.RESERVED: RefillPointStatusEnum.RESERVED,
        EvseStatus.UNKNOWN: RefillPointStatusEnum.UNKNOWN,
    }

    @staticmethod
    def format_last_updated(value: datetime) -> datetime | str:
        # UTC without microseconds, like all datetimes rendered by the DefaultJSONEncoder. Same result as
        # strftime('%Y-%m-%dT%H:%M:%SZ'), but twice as fast, which matters for >100k EVSEs.
        return value.isoformat(timespec='seconds')[:19] + 'Z'
