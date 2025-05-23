# OCHP

This documents the mapping between [OCHP 1.4 ChargePointInfo / ](https://github.com/e-clearing-net/OCHP) and
[OCPI 2.2.1 Locations / EVSEs / Connectors](https://github.com/ocpi/ocpi/blob/release-2.2.1-bugfixes/mod_locations.asciidoc#131-location-object).

OCHP will be used by any operator at the LISY platform from Ladenetz, which uses eClearing for centralized operations
like getting charge infrastructure data.


# ChargePointInfo

The OCPI `Location` and `EVSE` at OCHP is combined at one object, `ChargePointInfo`, which is basically a
denormalized `EVSE`, where the `locationId` acts as a grouping identifier. `ChargePointInfo` contains static information
only, realtime information is transported using the `EvseStatusType`.

| Field               | Type                                            | Cardinality | Mapping                                                             | Comment |
|---------------------|-------------------------------------------------|-------------|---------------------------------------------------------------------|---------|
| evseId              | string (48)                                     | 1           | evse.uid and evse.evse_id                                           |         |
| locationId          | string (15)                                     | 1           | location.uid                                                        |         |
| timestamp           | string (datetime)                               | ?           | location.last_updated (last one will be used) and evse.last_updated |         |
| locationName        | string (100)                                    | 1           | location.name                                                       |         |
| locationNameLang    | string (3)                                      | 1           |                                                                     |         |
| images              | [EvseImageUrlType](#EvseImageUrlType)           | *           |                                                                     |         |
| relatedResource     | RelatedResourceType                             | *           |                                                                     |         |
| chargePointAddress  | [AddressType](#AddressType)                     | 1           |                                                                     |         |
| chargePointLocation | [GeoPointType](#GeoPointType)                   | 1           |                                                                     |         |
| relatedLocation     | AdditionalGeoPointType                          | ?           |                                                                     |         |
| timeZone            | string (255)                                    | ?           | location.time_zone                                                  |         |
| openingTimes        | [HoursType](#HoursType)                         | 1           |                                                                     |         |
| status              | [ChargePointStatusType](#ChargePointStatusType) | ?           | evse.status                                                         |         |
| statusSchedule      | ChargePointScheduleType                         | *           |                                                                     |         |
| telephoneNumber     | string (19)                                     | ?           |                                                                     |         |
| location            | [GeneralLocationType](#GeneralLocationType)     | 1           | location.parking_type                                               |         |
| parkingSpot         | ParkingSpotInfo                                 | *           |                                                                     |         |
| restriction         | RestrictionType                                 | *           |                                                                     |         |
| authMethods         | AuthMethodType                                  | +           |                                                                     |         |
| connectors          | [ConnectorType](#ConnectorType)                 | +           |                                                                     |         |
| chargePointType     | string (2)                                      | 1           |                                                                     |         |
| ratings             | [RatingsType](#RatingsType)                     | ?           |                                                                     |         |
| userInterfaceLang   | string (3)                                      | *           |                                                                     |         |
| maxReservation      | float                                           | ?           |                                                                     |         |


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

| Key                | Mapping            |
|--------------------|--------------------|
| on-street          | ON_STREET          |
| parking-garage     | PARKING_GARAGE     |
| underground-garage | UNDERGROUND_GARAGE |
| parking-lot        | PARKING_LOT        |
| private            | PRIVATE            |
| other              |                    |
| unknown            |                    |


## EvseImageUrlType

| Field       | Type                      | Cardinality | Mapping         | Comment                                    |
|-------------|---------------------------|-------------|-----------------|--------------------------------------------|
| uri         | string(255)               | 1           | image.url       | Will be downloaded and delivered by OCPDB. |
| thumbUri    | string(255)               | ?           | image.thumbnail | Will be downloaded and delivered by OCPDB. |
| class       | [ImageClass](#ImageClass) | 1           | image.category  |                                            |
| type        | string(4)                 | 1           | image.type      |                                            |
| width       | int(5)                    | ?           | image.width     |                                            |
| height      | int(5)                    | ?           | image.height    |                                            |


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


## HoursType

| Field           | Type             | Cardinality | Mapping                                | Comment |
|-----------------|------------------|-------------|----------------------------------------|---------|
| twentyfourseven | bool             | 1           | location.opening_times.twentyfourseven |         |
| regularHours    | RegularHoursType | 1           | location.opening_times.twentyfourseven |         |


## RegularHoursType

| Field       | Type          | Cardinality | Mapping                                           | Comment |
|-------------|---------------|-------------|---------------------------------------------------|---------|
| weekday     | integer       | 1           | location.opening_times.regular_hours.weekday      |         |
| periodBegin | string (time) | 1           | location.opening_times.regular_hours.period_begin |         |
| periodEnd   | string (time) | 1           | location.opening_times.regular_hours.period_end   |         |


## ConnectorType

| Field             | Type                  | Cardinality | Mapping            | Comment              |
|-------------------|-----------------------|-------------|--------------------|----------------------|
| connectorStandard | ConnectorStandardType | 1           | connector.standard | 1:1 mappingt to OCPI |
| connectorFormat   | ConnectorFormatType   | 1           | connector.format   | 1:1 mappingt to OCPI |
| tariffId          | TariffId              | ?           |                    |                      |


## RatingsType

This can be a source of invalid data, because at OCPI, `max_electric_power` and `voltage` is at Connector level,
while the data source provides it at EVSE level. This might lead to invalid data, if one plug has less power then the
others. Obvious errors are fixed (Type F plugs cannot have 22kW), but especially if it comes to fast charging, it's
impossible to determine the power of combined CCS + CHAdeMO plugs, so we just set the given `maximumPower` for every
plug. Same applies for voltage, too.

| Field           | Type    | Cardinality | Mapping                      | Comment                        |
|-----------------|---------|-------------|------------------------------|--------------------------------|
| maximumPower    | float   | 1           | connector.max_electric_power | Unit: kW, is transformed in W. |
| guaranteedPower | float   | ?           |                              |                                |
| nominalVoltage  | integer | ?           | connector.voltage            |                                |


# EvseStatusType

The `EvseStatusType` is the OCHP object for realtime data. The status is split up into `major` and `minor`. If `minor`
is set, the minor status is used, otherwise the major status is used.

| Field  | Type                    | Cardinality | Mapping           | Comment |
|--------|-------------------------|-------------|-------------------|---------|
| evseId | string (48)             | 1           |                   |         |
| major  | [MajorType](#MajorType) | 1           | evse.status       |         |
| minor  | [MinorType](#MinorType) | ?           | evse.status       |         |
| ttl    | string (datetime)       | ?           | evse.last_updated |         |


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
