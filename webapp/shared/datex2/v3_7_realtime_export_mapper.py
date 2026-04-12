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

from datetime import datetime, timezone

from webapp.models.evse import Evse, EvseStatus
from webapp.models.location import Location
from webapp.shared.datex2.v3_7.realtime.d_a_t_e_x_i_i3_d2_payload_output import DATEXII3D2PayloadOutput
from webapp.shared.datex2.v3_7.realtime.energy_infrastructure_site_status_output import (
    EnergyInfrastructureSiteStatusOutput,
)
from webapp.shared.datex2.v3_7.realtime.energy_infrastructure_station_status_output import (
    EnergyInfrastructureStationStatusOutput,
)
from webapp.shared.datex2.v3_7.realtime.energy_infrastructure_status_publication_output import (
    EnergyInfrastructureStatusPublicationOutput,
)
from webapp.shared.datex2.v3_7.realtime.payload_publication_g_output import PayloadPublicationGOutput
from webapp.shared.datex2.v3_7.realtime.refill_point_status_enum import RefillPointStatusEnum
from webapp.shared.datex2.v3_7.realtime.refill_point_status_enum_g_output import RefillPointStatusEnumGOutput
from webapp.shared.datex2.v3_7.realtime.refill_point_status_g_output import RefillPointStatusGOutput
from webapp.shared.datex2.v3_7.realtime.refill_point_status_output import RefillPointStatusOutput
from webapp.shared.datex2.v3_7.shared.facility_object_versioned_reference_g_output import (
    FacilityObjectVersionedReferenceGOutput,
)
from webapp.shared.datex2.v3_7.shared.international_identifier_output import InternationalIdentifierOutput


class DatexV37JSONRealtimeExportMapper:
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

    def map_locations_to_realtime_payload(self, locations: list[Location]) -> DATEXII3D2PayloadOutput:
        now = datetime.now(tz=timezone.utc)

        site_statuses = []
        for location in locations:
            site_status = self._map_location_to_site_status(location)
            if site_status is not None:
                site_statuses.append(site_status)

        payload = PayloadPublicationGOutput(
            modelBaseVersionG='3',
            versionG='3.7',
            profileNameG='Afir Energy Infrastructure',
            profileVersionG='01-00-00',
            aegiEnergyInfrastructureStatusPublication=EnergyInfrastructureStatusPublicationOutput(
                lang='de',
                publicationTime=now,
                publicationCreator=InternationalIdentifierOutput(
                    country='DE',
                    nationalIdentifier='OCPDB',
                ),
                energyInfrastructureSiteStatus=site_statuses,
            ),
        )

        return DATEXII3D2PayloadOutput(payload=payload)

    def _map_location_to_site_status(self, location: Location) -> EnergyInfrastructureSiteStatusOutput | None:
        station_statuses = []
        for charging_station in location.charging_pool:
            station_status = self._map_charging_station_to_station_status(charging_station)
            if station_status is not None:
                station_statuses.append(station_status)

        if not station_statuses:
            return None

        return EnergyInfrastructureSiteStatusOutput(
            reference=FacilityObjectVersionedReferenceGOutput(
                targetClass='FacilityObject',
                idG=location.uid,
                versionG=location.last_updated.isoformat(),
            ),
            lastUpdated=location.last_updated,
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

        return EnergyInfrastructureStationStatusOutput(
            reference=FacilityObjectVersionedReferenceGOutput(
                targetClass='FacilityObject',
                idG=charging_station.uid,
                versionG=charging_station.last_updated.isoformat(),
            ),
            refillPointStatus=refill_point_statuses,
        )

    def _map_evse_to_refill_point_status(self, evse: Evse) -> RefillPointStatusGOutput | None:
        status_enum = self._evse_status_to_refill_point_status_map.get(evse.status)
        if status_enum is None:
            return None

        last_updated = evse.status_last_updated or evse.last_updated

        return RefillPointStatusGOutput(
            aegiRefillPointStatus=RefillPointStatusOutput(
                reference=FacilityObjectVersionedReferenceGOutput(
                    targetClass='FacilityObject',
                    idG=evse.uid,
                    versionG=evse.last_updated.isoformat(),
                ),
                lastUpdated=last_updated,
                status=RefillPointStatusEnumGOutput(value=status_enum),
            ),
        )
