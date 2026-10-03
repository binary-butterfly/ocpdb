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
from enum import Enum
from typing import TypedDict

# Output models of the DATEX II realtime exports. Realtime exports contain >100k EVSEs, so they are built as plain dicts,
# which are much faster to build and to serialize with orjson than the generated validataclass models. Datetimes stay
# datetime objects where the export uses ISO 8601 with microseconds and offset, as orjson renders them that way itself.


class FacilityObjectReference(TypedDict):
    targetClass: str
    idG: str
    versionG: datetime


class RefillPointStatusValue(TypedDict):
    value: Enum


class RefillPointStatus(TypedDict):
    reference: FacilityObjectReference
    lastUpdated: datetime | str
    status: RefillPointStatusValue


class RefillPointStatusG(TypedDict):
    aegiRefillPointStatus: RefillPointStatus


class EnergyInfrastructureStationStatus(TypedDict):
    reference: FacilityObjectReference
    refillPointStatus: list[RefillPointStatusG]


class EnergyInfrastructureSiteStatus(TypedDict):
    reference: FacilityObjectReference
    lastUpdated: datetime | str
    energyInfrastructureStationStatus: list[EnergyInfrastructureStationStatus]


class InternationalIdentifier(TypedDict):
    country: str
    nationalIdentifier: str


class EnergyInfrastructureStatusPublication(TypedDict):
    lang: str
    publicationTime: datetime | str
    publicationCreator: InternationalIdentifier
    energyInfrastructureSiteStatus: list[EnergyInfrastructureSiteStatus]


class PayloadPublicationG(TypedDict):
    versionG: str
    modelBaseVersionG: str
    profileNameG: str
    profileVersionG: str
    aegiEnergyInfrastructureStatusPublication: EnergyInfrastructureStatusPublication


class RealtimePayload(TypedDict):
    payload: PayloadPublicationG
