# Stadtwerke Stuttgart Mapping

This documents the input data model from Stadtwerke Stuttgart and the mapping to
[OCPI 2.2.1 Locations / EVSEs / Connectors](https://github.com/ocpi/ocpi/blob/release-2.2.1-bugfixes/mod_locations.asciidoc#131-location-object).

Stadtwerke Stuttgart data uses some fields from OCPI, but adds several further fields. It also supports `null` as unset
value.

## Source Location

| Field         | Type                              | Cardinality | Mapping                | Comment                                                                 |
|---------------|-----------------------------------|-------------|------------------------|-------------------------------------------------------------------------|
| id            | string                            | 1           | location.original_id   |                                                                         |
| name          | string                            | 1           | location.name          |                                                                         |
| status        | StadtwerkeStuttgartLocationStatus | 1           |                        |                                                                         |
| address       | string                            | 1           | location.address       |                                                                         |
| city          | string                            | 1           | location.city          |                                                                         |
| postal_code   | string                            | 1           | location.postal_code   |                                                                         |
| country       | string                            | 1           | location.country       | Transformation from 2 digit language code to OCPI 3 digit language code |
| directions    | string                            | 1           | location.directions    | Transformation to OCPI `DisplayText` with language DE                   |
| comment       | string                            | 1           |                        |                                                                         |
| coordinates   | StadtwerkeStuttgartCoordinates    | 1           | location.coordinates   |                                                                         |
| distance_in_m | integer as string                 | 1           |                        |                                                                         |
| operator      | StadtwerkeStuttgartBusiness       | 1           | location.operator      |                                                                         |
| opening_times | StadtwerkeStuttgartOpeningTimes   | 1           | location.opening_times |                                                                         |
| owner         | StadtwerkeStuttgartBusiness       | ?           | location.owner         | Always null in our dataset                                              |
| roaming       | boolean                           | 1           |                        |                                                                         |


#### StadtwerkeStuttgartLocationStatus

| Key       | Mapping |
|-----------|---------|
| active    |         |

In our example data, no other value then `active` is set.


### Source StadtwerkeStuttgartCoordinates

| Field     | Type        | Cardinality | Mapping                        |
|-----------|-------------|-------------|--------------------------------|
| latitude  | string      | 1           | location.coordinates.latitude  |
| longitude | string      | 1           | location.coordinates.longitude |


### Source StadtwerkeStuttgartBusiness

| Field      | Type   | Cardinality | Mapping       |
|------------|--------|-------------|---------------|
| operatorId | string | 1           |               |
| name       | string | 1           | business.name |
| hotline    | string | 1           |               |


### Source OpeningTimes

| Field           | Type    | Cardinality | Mapping                                |
|-----------------|---------|-------------|----------------------------------------|
| twentyfourseven | boolean | 1           | location.opening_times.twentyfourseven |

In our example data, no other opening time representation then `twentyfourseven: true` is set.


## Source EVSE

| Field                          | Type                           | Cardinality | Mapping                 |
|--------------------------------|--------------------------------|-------------|-------------------------|
| uid                            | string                         | 1           | location.original_uid   |
| id                             | string                         | 1           | evse.evse_id            |
| status                         | EvseStatus                     | 1           | evse.status             |
| reservable                     | boolean                        | 1           |                         |
| capabilities                   | EvseCapability                 | *           | evse.capabilities       |
| physical_reference             | string                         | 1           | evse.physical_reference |
| floor_level                    | boolean                        | 1           | evse.floor_level        |
| vehicle_type                   | StadtwerkeStuttgartVehicleType | 1           |                         |
| chargePointPosition            | ?                              | ?           |                         |
| chargePointPublicComment       | ?                              | ?           |                         |
| chargePointParkingSpaceNumbers | string                         | ?           |                         |
| chargingStationPosition        | string                         | ?           |                         |
| roaming                        | boolean                        | 1           |                         |


### StadtwerkeStuttgartVehicleType

| Key           | Mapping |
|---------------|---------|
| four_wheeled  |         |

In our example data, no other value then `four_wheeled` is set.


## Source Connector

| Field        | Type               | Cardinality | Mapping                      | Comment                                             |
|--------------|--------------------|-------------|------------------------------|-----------------------------------------------------|
| id           | string             | 1           | connector.original_id        |                                                     |
| status       | EvseStatus         | 1           |                              |                                                     |
| standard     | ConnectorStandard  | 1           | connector.standard           |                                                     |
| format       | ConnectorFormat    | 1           | connector.format             |                                                     |
| power_type   | ConnectorPowerType | 1           | connector.power_type         |                                                     |
| ampere       | integer as string  | 1           | connector.max_amperage       |                                                     |
| voltage      | integer as string  | 1           | connector.max_voltage        |                                                     |
| max_power    | integer            | 1           | connector.max_electric_power | Unit is kW and has to be transformed in Wh for OCPI |
| tariff_id    | Coordinates        | ?           |                              |                                                     |
