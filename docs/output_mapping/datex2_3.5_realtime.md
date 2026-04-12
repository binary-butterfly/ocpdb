# DATEX II 3.5 Realtime Output Mapping

This documents the output mapping from OCPDB internal models to the
[DATEX II German Energy Infrastructure Profile](https://github.com/MobilithekDE/AFIR-DATEX-II-Recharging-Profil/)
(JSON, version 3.5) realtime data endpoint.

**Endpoint**: `GET /api/public/datex/v3.5/json/realtime`

The response is a JSON object with a single `payload` key containing a `PayloadPublicationG` object. The payload
contains an `aegiEnergyInfrastructureStatusPublication` with the hierarchical structure:
`energyInfrastructureSiteStatus` -> `energyInfrastructureStationStatus` -> `refillPointStatus`.

The realtime data references static data objects by their `idG`, allowing consumers to correlate status information
with the static endpoint's structural data.


## PayloadPublicationG

Top-level publication wrapper.

| Field                                      | Type                                                                            | Mapping                      | Comment      |
|--------------------------------------------|---------------------------------------------------------------------------------|------------------------------|--------------|
| modelBaseVersionG                          | string                                                                          | `3`                          | Static value |
| versionG                                   | string                                                                          | `3.5`                        | Static value |
| profileNameG                               | string                                                                          | `AFIR Energy Infrastructure` | Static value |
| profileVersionG                            | string                                                                          | `01-00-00`                   | Static value |
| aegiEnergyInfrastructureStatusPublication  | [EnergyInfrastructureStatusPublication](#energyinfrastructurestatuspublication) |                              |              |


## EnergyInfrastructureStatusPublication

| Field                                 | Type                                                                | Mapping          | Comment         |
|---------------------------------------|---------------------------------------------------------------------|------------------|-----------------|
| lang                                  | string                                                              | `de`             | Static value    |
| publicationTime                       | string (datetime)                                                   | Current UTC time | ISO 8601 format |
| publicationCreator.country            | string                                                              | `DE`             | Static value    |
| publicationCreator.nationalIdentifier | string                                                              | `OCPDB`          | Static value    |
| energyInfrastructureSiteStatus        | [EnergyInfrastructureSiteStatus](#energyinfrastructuresitestatus)[] |                  |                 |


## EnergyInfrastructureSiteStatus

A `Location` maps to an `EnergyInfrastructureSiteStatus`. Locations where all charging stations have no mappable
EVSEs are skipped.

| Field                             | Type                                                                      | Mapping               | Comment         |
|-----------------------------------|---------------------------------------------------------------------------|-----------------------|-----------------|
| reference.targetClass             | string                                                                    | `FacilityObject`      | Static value    |
| reference.idG                     | string                                                                    | location.uid          |                 |
| reference.versionG                | string (datetime)                                                         | location.last_updated | ISO 8601 format |
| lastUpdated                       | string (datetime)                                                         | location.last_updated | ISO 8601 format |
| energyInfrastructureStationStatus | [EnergyInfrastructureStationStatus](#energyinfrastructurestationstatus)[] |                       |                 |


## EnergyInfrastructureStationStatus

A `ChargingStation` maps to an `EnergyInfrastructureStationStatus`. Stations where all EVSEs have unmappable
status are skipped.

| Field                 | Type                                        | Mapping                       | Comment         |
|-----------------------|---------------------------------------------|-------------------------------|-----------------|
| reference.targetClass | string                                      | `FacilityObject`              | Static value    |
| reference.idG         | string                                      | charging_station.uid          |                 |
| reference.versionG    | string (datetime)                           | charging_station.last_updated | ISO 8601 format |
| refillPointStatus     | [RefillPointStatusG](#refillpointstatusg)[] |                               |                 |


## RefillPointStatusG

An `Evse` maps to a `RefillPointStatusG`. EVSEs whose `status` cannot be mapped (e.g. `STATIC`) are skipped.

| Field                                       | Type                  | Mapping                  | Comment                                          |
|---------------------------------------------|-----------------------|--------------------------|--------------------------------------------------|
| aegiRefillPointStatus.reference.targetClass | string                | `FacilityObject`         | Static value                                     |
| aegiRefillPointStatus.reference.idG         | string                | evse.uid                 |                                                  |
| aegiRefillPointStatus.reference.versionG    | string (datetime)     | evse.last_updated        | ISO 8601 format                                  |
| aegiRefillPointStatus.lastUpdated           | string (datetime)     | evse.status_last_updated | Falls back to evse.last_updated if not available |
| aegiRefillPointStatus.status.value          | RefillPointStatusEnum | evse.status              | See [status mapping](#evse-status-mapping)       |


### EvseStatus Mapping

| Internal (EvseStatus) | DATEX II (RefillPointStatusEnum) |
|-----------------------|----------------------------------|
| AVAILABLE             | available                        |
| BLOCKED               | blocked                          |
| CHARGING              | charging                         |
| INOPERATIVE           | inoperative                      |
| OUTOFORDER            | outOfOrder                       |
| PLANNED               | planned                          |
| REMOVED               | removed                          |
| RESERVED              | reserved                         |
| UNKNOWN               | unknown                          |
| STATIC                | *(not mapped, EVSE skipped)*     |
