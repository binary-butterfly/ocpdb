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

from __future__ import annotations

from datetime import datetime, timezone

from webapp.models.evse import Evse, EvseStatus
from webapp.models.location import Location
from webapp.shared.datex2.german_realtime.d_a_t_e_x_i_i3_d2_payload_input import DATEXII3D2PayloadInput
from webapp.shared.datex2.german_realtime.energy_infrastructure_site_status_input import (
    EnergyInfrastructureSiteStatusInput,
)
from webapp.shared.datex2.german_realtime.energy_infrastructure_station_status_input import (
    EnergyInfrastructureStationStatusInput,
)
from webapp.shared.datex2.german_realtime.energy_infrastructure_status_publication_input import (
    EnergyInfrastructureStatusPublicationInput,
)
from webapp.shared.datex2.german_realtime.facility_object_versioned_reference_g_input import (
    FacilityObjectVersionedReferenceGInput,
)
from webapp.shared.datex2.german_realtime.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.german_realtime.payload_publication_g_input import PayloadPublicationGInput
from webapp.shared.datex2.german_realtime.refill_point_status_enum import RefillPointStatusEnum
from webapp.shared.datex2.german_realtime.refill_point_status_enum_g_input import RefillPointStatusEnumGInput
from webapp.shared.datex2.german_realtime.refill_point_status_g_input import RefillPointStatusGInput
from webapp.shared.datex2.german_realtime.refill_point_status_input import RefillPointStatusInput


class DatexV36RealtimeExportMapper:
    _evse_status_to_refill_point_status_map: dict[EvseStatus, RefillPointStatusEnum] = {
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

    def map_locations_to_realtime_payload(self, locations: list[Location]) -> DATEXII3D2PayloadInput:
        now = datetime.now(tz=timezone.utc).isoformat()

        site_statuses = []
        for location in locations:
            site_status = self._map_location_to_site_status(location)
            if site_status is not None:
                site_statuses.append(site_status)

        payload = PayloadPublicationGInput(
            modelBaseVersionG='3',
            versionG='3.6',
            profileNameG='AFIR Energy Infrastructure',
            profileVersionG='01-00-00',
            aegiEnergyInfrastructureStatusPublication=EnergyInfrastructureStatusPublicationInput(
                lang='de',
                publicationTime=now,
                publicationCreator=InternationalIdentifierInput(
                    country='DE',
                    nationalIdentifier='OCPDB',
                ),
                energyInfrastructureSiteStatus=site_statuses,
            ),
        )

        return DATEXII3D2PayloadInput(payload=payload)

    def _map_location_to_site_status(self, location: Location) -> EnergyInfrastructureSiteStatusInput | None:
        station_statuses = []
        for charging_station in location.charging_pool:
            station_status = self._map_charging_station_to_station_status(charging_station)
            if station_status is not None:
                station_statuses.append(station_status)

        if not station_statuses:
            return None

        version_g = location.last_updated.isoformat()

        return EnergyInfrastructureSiteStatusInput(
            reference=FacilityObjectVersionedReferenceGInput(
                targetClass='FacilityObject',
                idG=location.uid,
                versionG=version_g,
            ),
            lastUpdated=version_g,
            energyInfrastructureStationStatus=station_statuses,
        )

    def _map_charging_station_to_station_status(self, charging_station):
        refill_point_statuses = []
        for evse in charging_station.evses:
            refill_point_status = self._map_evse_to_refill_point_status(evse)
            if refill_point_status is not None:
                refill_point_statuses.append(refill_point_status)

        if not refill_point_statuses:
            return None

        version_g = charging_station.last_updated.isoformat()

        return EnergyInfrastructureStationStatusInput(
            reference=FacilityObjectVersionedReferenceGInput(
                targetClass='FacilityObject',
                idG=charging_station.uid,
                versionG=version_g,
            ),
            refillPointStatus=refill_point_statuses,
        )

    def _map_evse_to_refill_point_status(self, evse: Evse) -> RefillPointStatusGInput | None:
        status_enum = self._evse_status_to_refill_point_status_map.get(evse.status)
        if status_enum is None:
            return None

        version_g = evse.last_updated.isoformat()
        last_updated = evse.status_last_updated.isoformat() if evse.status_last_updated else version_g

        return RefillPointStatusGInput(
            aegiRefillPointStatus=RefillPointStatusInput(
                reference=FacilityObjectVersionedReferenceGInput(
                    targetClass='FacilityObject',
                    idG=evse.uid,
                    versionG=version_g,
                ),
                lastUpdated=last_updated,
                status=RefillPointStatusEnumGInput(value=status_enum),
            ),
        )
