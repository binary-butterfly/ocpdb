# OCHP

This documents the mapping between [OCHP 1.4 ChargePointInfo / ](https://github.com/e-clearing-net/OCHP) and
[OCPI 2.2.1 Locations / EVSEs / Connectors](https://github.com/ocpi/ocpi/blob/release-2.2.1-bugfixes/mod_locations.asciidoc#131-location-object).

OCHP will be used by any operator at the LISY platform from Ladenetz, which uses eClearing for centralized operations
like getting charge infrastructure data.

# ChargePointInfo

The OCPI `Location` and `EVSE` at OCHP is combined at one object, `ChargePointInfo`, which is basically a
denormalized `EVSE`, where the `locationId` acts as a grouping identifier. `ChargePointInfo` contains static information
only, realtime information is transported using the `EvseStatusType`.

| Field               | Type                    | Cardinality | Mapping                                     | Comment |
|---------------------|-------------------------|-------------|---------------------------------------------|---------|
| evseId              | EvseId                  | 1           | evse.uid and evse.evse_id                   |         |
| locationId          | string (15)             | 1           | location.id                                 |         |
| timestamp           | DateTimeType            | ?           | location.last_updated and evse.last_updated |         |
| locationName        | string (100)            | 1           | location.name                               |         |
| locationNameLang    | string (3)              | 1           |                                             |         |
| images              | EvseImageUrlType        | *           | .                                           |         |
| relatedResource     | RelatedResourceType     | *           |                                             |         |
| chargePointAddress  | AddressType             | 1           |                                             |         |
| chargePointLocation | GeoPointType            | 1           |                                             |         |
| relatedLocation     | AdditionalGeoPointType  | ?           |                                             |         |
| timeZone            | string (255)            | ?           | location.time_zone                          |         |
| openingTimes        | HoursType               | 1           |                                             |         |
| status              | ChargePointStatusType   | ?           | evse.status                                 |         |
| statusSchedule      | ChargePointScheduleType | *           |                                             |         |
| telephoneNumber     | string(19)              | ?           |                                             |         |
| location            | GeneralLocationType     | 1           | location.parking_type                       |         |
| parkingSpot         | ParkingSpotInfo         | *           |                                             |         |
| restriction         | RestrictionType         | *           |                                             |         |
| authMethods         | AuthMethodType          | +           |                                             |         |
| connectors          | ConnectorType           | +           |                                             |         |
| chargePointType     | string(2)               | 1           |                                             |         |
| ratings             | RatingsType             | ?           |                                             |         |
| userInterfaceLang   | string(3)               | *           |                                             |         |
| maxReservation      | float                   | ?           |                                             |         |


### ChargePointStatusType

The `ChargePointStatusType` is *not* a realtime status, so it will be ignored as soon as we get `EvseStatusType`.

| Key         | Mapping     |
|-------------|-------------|
| Unknown     | UNKNOWN     |
| Operative   | AVAILABLE   |
| Inoperative | INOPERATIVE |
| Planned     | PLANNED     |
| Closed      | REMOVED     |


### GeneralLocationType

OCHP `GeneralLocationType` maps to OCPI `ParkingType`.

| Key         | Mapping     |
|-------------|-------------|
| evonly      | EV_ONLY     |
| plugged     | PLUGGED     |
| disabled    | DISABLED    |
| customers   | CUSTOMERS   |
| motorcycles | MOTORCYCLES |
| carsharing  | CARSHARING  |


## EvseImageUrlType

| Field       | Type          | Cardinality | Mapping         | Comment                                    |
|-------------|---------------|-------------|-----------------|--------------------------------------------|
| uri         | string(255)   | 1           | image.url       | Will be downloaded and delivered by OCPDB. |
| thumbUri    | string(255)   | ?           | image.thumbnail | Will be downloaded and delivered by OCPDB. |
| class       | ImageClass    | 1           | image.category  |                                            |
| type        | string(4)     | 1           | image.type      |                                            |
| width       | int(5)        | ?           | image.width     |                                            |
| height      | int(5)        | ?           | image.height    |                                            |


### ImageClass

OCHP `ImageClass` maps to OCPI `ImageCategory`

| Key           | Mapping  |
|---------------|----------|
| networkLogo   | NETWORK  |
| operatorLogo  | OPERATOR |
| ownerLogo     | OWNER    |
| stationPhoto  | CHARGER  |
| locationPhoto | LOCATION |
| entrancePhoto | ENTRANCE |
| otherPhoto    | OTHER    |
| otherLogo     | OTHER    |
| otherGraphic  | OTHER    |


## AddressType

| Field               | Type       | Cardinality | Mapping              | Comment                                                                            |
|---------------------|------------|-------------|----------------------|------------------------------------------------------------------------------------|
| houseNumber         | string(6)  | ?           | location.address     | Will be combined with AddressType.address. A `houseNumber` of '0' will be ignored. |
| address             | string(45) | 1           | location.address     |                                                                                    |
| city                | string(45) | 1           | location.city        |                                                                                    |
| zipCode             | string(10) | 1           | location.postal_code |                                                                                    |
| country             | string(3)  | 1           | location.country     |                                                                                    |


## GeoPointType

| Field   | Type       | Cardinality | Mapping                        | Comment |
|---------|------------|-------------|--------------------------------|---------|
| lat     | string(10) | 1           | location.coordinates.latitude  |         |
| lon     | string(11) | 1           | location.coordinates.longitude |         |


## ConnectorType

| Field             | Type                  | Cardinality | Mapping            | Comment              |
|-------------------|-----------------------|-------------|--------------------|----------------------|
| connectorStandard | ConnectorStandardType | 1           | connector.standard | 1:1 mappingt to OCPI |
| connectorFormat   | ConnectorFormatType   | 1           | connector.format   | 1:1 mappingt to OCPI |
| tariffId          | TariffId              | ?           |                    |                      |


# EvseStatusType

The `EvseStatusType` is the OCHP object for realtime data. The status is split up into `major` and `minor`. If `minor`
is set, the minor status is used, otherwise the major status is used.

| Field  | Type         | Cardinality | Mapping           | Comment |
|--------|--------------|-------------|-------------------|---------|
| evseId | EvseId       | 1           |                   |         |
| major  | MajorType    | 1           | evse.status       |         |
| minor  | MinorType    | ?           | evse.status       |         |
| ttl    | DateTimeType | ?           | evse.last_updated |         |


### MajorType

| Key           | Mapping     |
|---------------|-------------|
| available     | AVAILABLE   |
| not-available | INOPERATIVE |
| unknown       | UNKNOWN     |


### MinorType

| Key         | Mapping    |
|-------------|------------|
| available   | AVAILABLE  |
| reserved    | RESERVED   |
| charging    | BLOCKED    |
| blocked     | CHARGING   |
| outoforder  | OUTOFORDER |
