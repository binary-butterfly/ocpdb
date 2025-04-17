# OpenData Swiss mapping


## EVSEData

| Field          | Type           | Cardinality | Mapping                | Comment |
|----------------|----------------|-------------|------------------------|---------|
| EVSEDataRecord | EVSEDataRecord | *           |                        |         |
| OperatorID     | string         | 1           |                        |         |
| OperatorName   | string         | 1           | location.operator.name |         |


## EVSEDataRecord

| Field                            | Type                                            | Cardinality | Mapping               | Comment                                               |
|----------------------------------|-------------------------------------------------|-------------|-----------------------|-------------------------------------------------------|
| Accessibility                    | [Accessibility](#Accessibility)                 | 1           |                       |                                                       |
| AccessibilityLocation            | [AccessibilityLocation](#AccessibilityLocation) | ?           | location.parking_type |                                                       |
| AdditionalInfo                   | ?                                               | ?           |                       | Always null                                           |
| Address                          | [Address](#Address)                             | 1           |                       |                                                       |
| AuthenticationModes              | [AuthenticationMode](#AuthenticationMode)       | *           | evse.capabilities     |                                                       |
| CalibrationLawDataAvailability   | string                                          | 1           |                       | Always 'Not Available'                                |
| ChargingFacilities               | ChargingFacility                                | *           |                       |                                                       |
| ChargingPoolID                   | ?                                               | ?           |                       | Always null                                           |
| ChargingStationId                | string                                          | 1           | evse.uid              |                                                       |
| ChargingStationLocationReference | ?                                               | ?           |                       | Always null                                           |
| ChargingStationNames             | [ChargingStationName](#ChargingStationName)     | *           | location.directions   |                                                       |
| ClearinghouseID                  | ?                                               | ?           |                       | Always null                                           |
| deltaType                        | string                                          | ?           |                       |                                                       |
| DynamicInfoAvailable             | [DynamicInfoAvailable](#DynamicInfoAvailable)   | 1           |                       |                                                       |
| DynamicPowerLevel                | boolean                                         | ?           |                       |                                                       |
| EnergySource                     | ?                                               | ?           |                       | Always null                                           |
| EnvironmentalImpact              | ?                                               | ?           |                       | Always null                                           |
| EvseID                           | string                                          | 1           | evse.evse_id          |                                                       |
| GeoChargingPointEntrance         | object                                          | 1           |                       | Either {} or {"Google": "None None"}, both not useful |
| GeoCoordinates                   | [GeoCoordinates](#GeoCoordinates)               | 1           |                       |                                                       |
| HardwareManufacturer             | string                                          | ?           |                       |                                                       |
| HotlinePhoneNumber               | string                                          | 1           |                       |                                                       |
| HubOperatorID                    | string                                          | ?           |                       |                                                       |
| IsHubjectCompatible              | string or boolean                               | 1           | 1                     | String is `false`                                     |
| IsOpen24Hours                    | string or boolean                               | 1           |                       | String is `true`                                      |
| lastUpdate                       | string (date-time)                              | ?           |                       |                                                       |
| LocationImage                    | ?                                               | ?           |                       | Always null                                           |
| MaxCapacity                      | integer                                         | ?           |                       |                                                       |
| OpeningTimes                     | [OpeningTime](#OpeningTime)                     | *           |                       |                                                       |
| PaymentOptions                   | [PaymentOption](#PaymentOption)                 | *           |                       |                                                       |
| Plugs                            | [Plug](#Plug)                                   | *           |                       |                                                       |
| RenewableEnergy                  | boolean                                         | 1           |                       |                                                       |
| SuboperatorName                  | ?                                               | ?           |                       | Always null                                           |
| ValueAddedServices               | [ValueAddedService](#ValueAddedService)         | *           |                       |                                                       |


### Accessibility

|                            |                |
|----------------------------|----------------|
| Free publicly accessible   |                |
| Unspecified                |                |
| Test Station               |                |
| Restricted access          |                |
| Paying publicly accessible |                |


### AccessibilityLocation

|                          |                    |
|--------------------------|--------------------|
| ParkingGarage            | PARKING_GARAGE     |
| OnStreet                 | ON_STREET          |
| ParkingLot               | PARKING_LOT        |
| UndergroundParkingGarage | UNDERGROUND_GARAGE |


### AuthenticationMode

|                  |                           |
|------------------|---------------------------|
| NFC RFID DESFire | RFID_READER               |
| REMOTE           | REMOTE_START_STOP_CAPABLE |
| NFC RFID Classic | RFID_READER               |
| Direct Payment   |                           |
| PnC              |                           |


### DynamicInfoAvailable

|       |                |
|-------|----------------|
| auto  |                |
| true  |                |
| false |                |


### PaymentOption

|            |                |
|------------|----------------|
| No Payment |                |
| Contract   |                |
| Direct     |                |


### Plug

| value                             | standard           | format |
|-----------------------------------|--------------------|--------|
| Type J Swiss Standard             | DOMESTIC_J         | SOCKET |
| Type 2 Outlet                     | IEC_62196_T2       | SOCKET |
| Tesla Connector                   | TESLA_S            | SOCKET |
| Type 1 Connector (Cable Attached) | IEC_62196_T1       | CABLE  |
| Type F Schuko                     | DOMESTIC_F         | SOCKET |
| CCS Combo 1 Plug (Cable Attached) | IEC_62196_T1       | CABLE  |
| Type 2 Connector (Cable Attached) | IEC_62196_T2       | CABLE  |
| CHAdeMO                           | CHADEMO            | CABLE  |
| Type G British Standard           | DOMESTIC_G         | SOCKET |
| CCS Combo 2 Plug (Cable Attached) | IEC_62196_T2_COMBO | CABLE  |


### ValueAddedService

|                      |                |
|----------------------|----------------|
| MaximumPowerCharging |                |
| None                 |                |
| DynamicPricing       |                |


## Address

| Field           | Type    | Cardinality | Mapping                 | Comment                                           |
|-----------------|---------|-------------|-------------------------|---------------------------------------------------|
| City            | string  | 1           | location.city           |                                                   |
| Country         | string  | 1           | location.country        |                                                   |
| Floor           | string  | ?           |                         | evse.floor_level                                  |
| HouseNum        | string  | 1           | location.address        | Added to Street. Might be '0', then it's ignored. |
| ParkingFacility | boolean | ?           |                         |                                                   |
| ParkingSpot     | string  | ?           | evse.physical_reference |                                                   |
| PostalCode      | string  | 1           | location.postal_code    |                                                   |
| Region          | string  | ?           |                         |                                                   |
| Street          | string  | 1           | location.address        |                                                   |
| TimeZone        | string  | ?           | location.time_zone      | defaults to Europe/Zurich                         |


## ChargingFacility

| Field     | Type                    | Cardinality | Mapping                      | Comment                           |
|-----------|-------------------------|-------------|------------------------------|-----------------------------------|
| power     | numeric                 | 1           | connector.max_electric_power | In kW, has to be transformed in W |
| powertype | [PowerType](#PowerType) | ?           | connector.power_type         |                                   |
| Amperage  | integer                 | ?           | connector.max_amperage       |                                   |
| Voltage   | integer                 | ?           | connector.max_voltage        |                                   |


### PowerType

|            |            |
|------------|------------|
| DC         | DC         |
| AC_1_PHASE | AC_1_PHASE |
| AC_3_PHASE | AC_3_PHASE |


## OpeningTime


| Field  | Type                | Cardinality | Mapping               | Comment |
|--------|---------------------|-------------|-----------------------|---------|
| on     | [Weekday](#Weekday) | 1           | regular_hours.weekday |         |
| Period | [Period](#Period)   | *           |                       |         |

### Weekday

|           |   |
|-----------|---|
| Monday    | 1 |
| Tuesday   | 2 |
| Wednesday | 3 |
| Thursday  | 4 |
| Friday    | 5 |
| Saturday  | 6 |
| Sunday    | 7 |


## Period

| Field | Type             | Cardinality | Mapping                    | Comment |
|-------|------------------|-------------|----------------------------|---------|
| begin | string (time)    | 1           | regular_hours.period_begin |         |
| end   | string (time)    | 1           | regular_hours.period_end   |         |


## EVSEStatuses

| Field            | Type             | Cardinality | Mapping | Comment |
|------------------|------------------|-------------|---------|---------|
| EVSEStatusRecord | EVSEStatusRecord | *           |         |         |
| OperatorID       | string           | 1           |         |         |
| OperatorName     | string           | 1           |         |         |


| Field      | Type                      | Cardinality | Mapping      | Comment |
|------------|---------------------------|-------------|--------------|---------|
| EvseID     | string                    | 1           | evse.evse_id |         |
| EVSEStatus | [EVSEStatus](#EVSEStatus) | 1           | evse.status  |         |


### EVSEStatus


|              |            |
|--------------|------------|
| Available    | AVAILABLE  |
| OutOfService | OUTOFORDER |
| Occupied     | CHARGING   |
| Unknown      | UNKNOWN    |
