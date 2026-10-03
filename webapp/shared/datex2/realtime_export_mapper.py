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

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from enum import Enum
from typing import Iterable

from webapp.models.evse import EvseStatus
from webapp.repositories.location_repository import RealtimeEvseRow

from .realtime_export_models import (
    EnergyInfrastructureSiteStatus,
    EnergyInfrastructureStationStatus,
    RealtimePayload,
    RefillPointStatusG,
)


class DatexJSONRealtimeExportMapper(ABC):
    version: str
    profile_name: str
    evse_status_to_refill_point_status_map: dict[EvseStatus, Enum]

    @staticmethod
    @abstractmethod
    def format_last_updated(value: datetime) -> datetime | str:
        """
        Formats the lastUpdated and publicationTime fields, which differ between the DATEX II versions.
        """

    def map_rows_to_realtime_payload(self, rows: Iterable[RealtimeEvseRow]) -> RealtimePayload:
        """
        Maps the rows of LocationRepository.fetch_realtime_evse_rows() to a realtime payload. As the rows are ordered by
        location and charging station, a new site or station status starts whenever the location or station id changes.
        Stations and sites without any mappable EVSE are skipped.
        """
        format_last_updated = self.format_last_updated
        status_map = self.evse_status_to_refill_point_status_map

        site_statuses: list[EnergyInfrastructureSiteStatus] = []
        station_statuses: list[EnergyInfrastructureStationStatus] = []
        refill_point_statuses: list[RefillPointStatusG] = []
        current_location_id: int | None = None
        current_charging_station_id: int | None = None

        for (
            location_id,
            location_uid,
            location_last_updated,
            charging_station_id,
            charging_station_uid,
            charging_station_last_updated,
            evse_uid,
            evse_status,
            evse_last_updated,
            evse_status_last_updated,
        ) in rows:
            refill_point_status = status_map.get(evse_status)
            if refill_point_status is None:
                continue

            if location_id != current_location_id:
                current_location_id = location_id
                current_charging_station_id = None
                station_statuses = []
                site_statuses.append({
                    'reference': {
                        'targetClass': 'FacilityObject',
                        'idG': location_uid,
                        'versionG': location_last_updated,
                    },
                    'lastUpdated': format_last_updated(location_last_updated),
                    'energyInfrastructureStationStatus': station_statuses,
                })

            if charging_station_id != current_charging_station_id:
                current_charging_station_id = charging_station_id
                refill_point_statuses = []
                station_statuses.append({
                    'reference': {
                        'targetClass': 'FacilityObject',
                        'idG': charging_station_uid,
                        'versionG': charging_station_last_updated,
                    },
                    'refillPointStatus': refill_point_statuses,
                })

            refill_point_statuses.append({
                'aegiRefillPointStatus': {
                    'reference': {
                        'targetClass': 'FacilityObject',
                        'idG': evse_uid,
                        'versionG': evse_last_updated,
                    },
                    'lastUpdated': format_last_updated(evse_status_last_updated or evse_last_updated),
                    'status': {'value': refill_point_status},
                },
            })

        return {
            'payload': {
                'versionG': self.version,
                'modelBaseVersionG': '3',
                'profileNameG': self.profile_name,
                'profileVersionG': '01-00-00',
                'aegiEnergyInfrastructureStatusPublication': {
                    'lang': 'de',
                    'publicationTime': format_last_updated(datetime.now(tz=timezone.utc)),
                    'publicationCreator': {
                        'country': 'DE',
                        'nationalIdentifier': 'OCPDB',
                    },
                    'energyInfrastructureSiteStatus': site_statuses,
                },
            },
        }
