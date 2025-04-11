# Heilbronn Neckarbogen Mapping

This documents the input data model from Heilbronn Neckarbogen and the mapping to
[OCPI 2.2.1 Locations / EVSEs / Connectors](https://github.com/ocpi/ocpi/blob/release-2.2.1-bugfixes/mod_locations.asciidoc#131-location-object). It is an extension to the `_general.md`, for global mapping
decisions, please have a look at the general document.

We use `postalAddress.id` to group chargepoints to locations. Any chargepoint outlet in this data source includes a
denormalized OCPI location in its parent, the chargepoint itself, and a flattened OCPI connector; therefore, there is
always just one OCPI connector per OCPI EVSE.

Global / generated values:

* `location.time_zone` is always `Europe/Berlin`

## ChargePoint


| Field                  | Type                                          | Cardinality | Mapping           | Comment |
|------------------------|-----------------------------------------------|-------------|-------------------|---------|
| attributes             | [ChargepointAttribute](#ChargepointAttribute) | *           |                   |         |
| id                     | integer                                       | 1           | evse.uid          |         |
| lastUpdatedAt          | string (date-time)                            | 1           | evse.last_updated |         |
| modelName              | string                                        | 1           |                   |         |
| name                   | string                                        | ?           | evse.directions   |         |
| nativeStatus           | OCPI EVSE Status                              | 1           |                   |         |
| outlets                | [Outlet](#Outlet)                             | *           |                   |         |
| position               | [Position](#Position)                         | 1           |                   |         |
| postalAddress          | [PostalAddress](#PostalAddress)               | 1           |                   |         |
| roamingChargingStation | boolean                                       | 1           |                   |         |
| tenant                 | [Tenant](#Tenant)                             | 1           | location.operator |         |
|


## ChargepointAttribute

Some OCPP related attributes, none of them have an OCPI representation.

| Field         | Type               | Cardinality | Mapping | Comment |
|---------------|--------------------|-------------|---------|---------|
| key           | string             | 1           |         |         |
| value         | string             | 1           |         |         |


## Position

| Field     | Type     | Cardinality | Mapping                        | Comment |
|-----------|----------|-------------|--------------------------------|---------|
| latitude  | numeric  | 1           | location.coordinates.latitude  |         |
| longitude | numeric  | 1           | location.coordinates.longitude |         |


## PostalAddress

| Field   | Type    | Cardinality | Mapping              | Comment                                                                                     |
|---------|---------|-------------|----------------------|---------------------------------------------------------------------------------------------|
| city    | string  | 1           | location.city        |                                                                                             |
| country | string  | 1           | location.country     | Source data is ISO 3166-1 alpha-2 code and will be transformed into ISO 3166-1 alpha-3 code |
| id      | integer | 1           | location.id          |                                                                                             |
| name    | string  | 1           | location.name        |                                                                                             |
| street1 | string  | 1           | location.address     | Combined with street2                                                                       |
| street2 | string  | 1           | location.address     | Combined with street1                                                                       |
| type    | string  | 1           |                      |                                                                                             |
| zip     | string  | 1           | location.postal_code |                                                                                             |


## Tenant

The tenant is input for an OCPI business, which is used as `location.operator`.

| Field | Type    | Cardinality | Mapping       | Comment |
|-------|---------|-------------|---------------|---------|
| id    | integer | 1           |               |         |
| name  | string  | 1           | business.name |         |


## Outlet

The outlet represents an EVSE.

| Field        | Type                                | Cardinality | Mapping      | Comment |
|--------------|-------------------------------------|-------------|--------------|---------|
| attributes   | [OutletAttribute](#OutletAttribute) | *           |              |         |
| connectorId  | integer                             | 1           |              |         |
| evseId       | string                              | 1           | evse.evse_id |         |
| image        | [Image](#Image)                     | 1           |              |         |
| modelName    | evse.evse_id                        | 1           |              |         |
| nativeStatus | OCPI EVSE Status                    | 1           | evse.status  |         |


## Image

As images just contain SVGs with generic plugs, they don't contain usable information.

| Field       | Type    | Cardinality | Mapping | Comment |
|-------------|---------|-------------|---------|---------|
| contentType | integer | 1           |         |         |
| fileName    | string  | 1           |         |         |
| id          | integer | 1           |         |         |
| size        | integer | 1           |         |         |


## OutletAttribute

These attributes contain the connector information.

| Field         | Type               | Cardinality | Mapping | Comment |
|---------------|--------------------|-------------|---------|---------|
| key           | string             | 1           |         |         |
| value         | string             | 1           |         |         |

Following keys are used:

| Key                | Mapping                      | Comment                                          |
|--------------------|------------------------------|--------------------------------------------------|
| FORMAT             | connector.format             |                                                  |
| MAX_ELECTRIC_POWER | connector.max_electric_power |                                                  |
| MAX_VOLTAGE        | connector.max_voltage        |                                                  |
| MAX_AMPERAGE       | connector.max_amperage       |                                                  |
| POWER_TYPE         | connector.standard           | Always `AC3`, which is mapped to `IEC_62196_T2`. |
