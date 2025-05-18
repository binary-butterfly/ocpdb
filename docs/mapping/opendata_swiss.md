# OpenData Swiss mapping

As the data source does not provide a dedicated location entity, OCPDB will use `OperatorName` plus
`GeoCoordinates.Google` field for grouping to locations. If there are different information for the location, we will
use the information of the first `EVSEDataRecord`.


## EVSEData

| Field          | Type           | Cardinality | Mapping                | Comment |
|----------------|----------------|-------------|------------------------|---------|
| EVSEDataRecord | EVSEDataRecord | *           |                        |         |
| OperatorID     | string         | 1           |                        |         |
| OperatorName   | string         | 1           | location.operator.name |         |


## EVSEDataRecord

| Field                            | Type                                            | Cardinality | Mapping                                  | Comment                                                                                           |
|----------------------------------|-------------------------------------------------|-------------|------------------------------------------|---------------------------------------------------------------------------------------------------|
| Accessibility                    | [Accessibility](#Accessibility)                 | 1           |                                          |                                                                                                   |
| AccessibilityLocation            | [AccessibilityLocation](#AccessibilityLocation) | ?           | location.parking_type                    |                                                                                                   |
| AdditionalInfo                   | ?                                               | ?           |                                          | Always null                                                                                       |
| Address                          | [Address](#Address)                             | 1           |                                          |                                                                                                   |
| AuthenticationModes              | [AuthenticationMode](#AuthenticationMode)       | *           | evse.capabilities                        |                                                                                                   |
| CalibrationLawDataAvailability   | string                                          | 1           |                                          | Always 'Not Available'                                                                            |
| ChargingFacilities               | [ChargingFacility](#ChargingFacility)           | *           |                                          |                                                                                                   |
| ChargingPoolID                   | ?                                               | ?           |                                          | Always null                                                                                       |
| ChargingStationId                | string                                          | 1           | location.id                              |                                                                                                   |
| ChargingStationLocationReference | ?                                               | ?           |                                          | Always null                                                                                       |
| ChargingStationNames             | [ChargingStationName](#ChargingStationName)     | *           | location.name                            | Sometimes dict, sometimes list of dicts. Use the entry with lang = de, if not set the first entry |
| ClearinghouseID                  | ?                                               | ?           |                                          | Always null                                                                                       |
| deltaType                        | string                                          | ?           |                                          |                                                                                                   |
| DynamicInfoAvailable             | [DynamicInfoAvailable](#DynamicInfoAvailable)   | 1           |                                          |                                                                                                   |
| DynamicPowerLevel                | boolean                                         | ?           |                                          |                                                                                                   |
| EnergySource                     | ?                                               | ?           |                                          | Always null                                                                                       |
| EnvironmentalImpact              | ?                                               | ?           |                                          | Always null                                                                                       |
| EvseID                           | string                                          | 1           | evse.evse_id                             |                                                                                                   |
| GeoChargingPointEntrance         | object                                          | 1           |                                          | Either {} or {"Google": "None None"}, both not useful                                             |
| GeoCoordinates                   | [GeoCoordinates](#GeoCoordinates)               | 1           | location.coordinates                     |                                                                                                   |
| HardwareManufacturer             | string                                          | ?           |                                          |                                                                                                   |
| HotlinePhoneNumber               | string                                          | 1           |                                          |                                                                                                   |
| HubOperatorID                    | string                                          | ?           |                                          |                                                                                                   |
| IsHubjectCompatible              | string or boolean                               | 1           |                                          | String is `false`                                                                                 |
| IsOpen24Hours                    | string or boolean                               | 1           |                                          | String is `true`                                                                                  |
| lastUpdate                       | string (date-time)                              | ?           | location.last_updated, evse.last_updated |                                                                                                   |
| LocationImage                    | ?                                               | ?           |                                          | Always null                                                                                       |
| MaxCapacity                      | integer                                         | ?           |                                          |                                                                                                   |
| OpeningTimes                     | [OpeningTime](#OpeningTime)                     | *           |                                          |                                                                                                   |
| PaymentOptions                   | [PaymentOption](#PaymentOption)                 | *           |                                          |                                                                                                   |
| Plugs                            | [Plug](#Plug)                                   | *           | connector.standard, connector.format     |                                                                                                   |
| RenewableEnergy                  | boolean                                         | 1           |                                          |                                                                                                   |
| SuboperatorName                  | ?                                               | ?           |                                          | Always null                                                                                       |
| ValueAddedServices               | [ValueAddedService](#ValueAddedService)         | *           |                                          |                                                                                                   |


### Accessibility

| Key                        | Mapping | Comment            |
|----------------------------|---------|--------------------|
| Free publicly accessible   |         |                    |
| Unspecified                |         |                    |
| Test Station               |         | Should be filtered |
| Restricted access          |         |                    |
| Paying publicly accessible |         |                    |


### AccessibilityLocation

| Key                      | Mapping            |
|--------------------------|--------------------|
| ParkingGarage            | PARKING_GARAGE     |
| OnStreet                 | ON_STREET          |
| ParkingLot               | PARKING_LOT        |
| UndergroundParkingGarage | UNDERGROUND_GARAGE |


### AuthenticationMode

| Key              | Mapping                   |
|------------------|---------------------------|
| NFC RFID DESFire | RFID_READER               |
| REMOTE           | REMOTE_START_STOP_CAPABLE |
| NFC RFID Classic | RFID_READER               |
| Direct Payment   |                           |
| PnC              |                           |


### DynamicInfoAvailable

As OCPI does not have a field like `has_realtime_data`, we cannot use this enumeration.

| Key   | Mapping |
|-------|---------|
| auto  |         |
| true  |         |
| false |         |


### PaymentOption

| Key        | Mapping |
|------------|---------|
| No Payment |         |
| Contract   |         |
| Direct     |         |


### Plug

| value                             | standard           | format |
|-----------------------------------|--------------------|--------|
| Type J Swiss Standard             | DOMESTIC_J         | SOCKET |
| Type 2 Outlet                     | IEC_62196_T2       | SOCKET |
| Tesla Connector                   | TESLA_S            | SOCKET |
| Type 1 Connector (Cable Attached) | IEC_62196_T1       | CABLE  |
| Type F Schuko                     | DOMESTIC_F         | SOCKET |
| CCS Combo 1 Plug (Cable Attached) | IEC_62196_T1_COMBO | CABLE  |
| Type 2 Connector (Cable Attached) | IEC_62196_T2       | CABLE  |
| CHAdeMO                           | CHADEMO            | CABLE  |
| Type G British Standard           | DOMESTIC_G         | SOCKET |
| CCS Combo 2 Plug (Cable Attached) | IEC_62196_T2_COMBO | CABLE  |


### ValueAddedService

| Key                  | Mapping |
|----------------------|---------|
| MaximumPowerCharging |         |
| None                 |         |
| DynamicPricing       |         |


## Address

| Field           | Type    | Cardinality | Mapping              | Comment                                                                             |
|-----------------|---------|-------------|----------------------|-------------------------------------------------------------------------------------|
| City            | string  | 1           | location.city        |                                                                                     |
| Country         | string  | 1           | location.country     | Just charge stations with `Country` in CHE, DEU, AUT and LIE get imported           |
| Floor           | string  | ?           | evse.floor_level     |                                                                                     |
| HouseNum        | string  | ?           | location.address     | Added to Street. Might be '0', then it's ignored.                                   |
| ParkingFacility | boolean | ?           |                      |                                                                                     |
| ParkingSpot     | ?       | ?           |                      |                                                                                     |
| PostalCode      | string  | ?           | location.postal_code | Might be '0', then it's ignored.                                                    |
| Region          | string  | ?           |                      |                                                                                     |
| Street          | string  | 1           | location.address     | Often includes house number                                                         |
| TimeZone        | string  | ?           | location.time_zone   | If not set, use corresponding timezone of the `Country`, eg `Europe/Zurich` for CHF |


## ChargingStationName

| Field  | Type   | Cardinality | Mapping           | Comment |
|--------|--------|-------------|-------------------|---------|
| lang   | string | 1           |                   |         |
| value  | string | 1           | display_text.text |         |


## GeoCoordinates

| Field  | Type   | Cardinality | Mapping              | Comment                                                    |
|--------|--------|-------------|----------------------|------------------------------------------------------------|
| Google | string | 1           | location.coordinates | Format: "{lat} {lon}": two floats with a space in between. |


## ChargingFacility

| Field     | Type                    | Cardinality | Mapping                      | Comment                           |
|-----------|-------------------------|-------------|------------------------------|-----------------------------------|
| power     | numeric                 | ?           | connector.max_electric_power | In kW, has to be transformed in W |
| powertype | [PowerType](#PowerType) | ?           | connector.power_type         |                                   |
| Amperage  | numeric                 | ?           | connector.max_amperage       |                                   |
| Voltage   | numeric                 | ?           | connector.max_voltage        |                                   |


### PowerType

| Key        | Mapping    |
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

| Key       | Mapping       |
|-----------|---------------|
| Monday    | 1             |
| Tuesday   | 2             |
| Wednesday | 3             |
| Thursday  | 4             |
| Friday    | 5             |
| Saturday  | 6             |
| Sunday    | 7             |
| Workdays  | 1, 2, 3, 4, 5 |


## Period

| Field | Type             | Cardinality | Mapping                    | Comment |
|-------|------------------|-------------|----------------------------|---------|
| begin | string (time)    | 1           | regular_hours.period_begin |         |
| end   | string (time)    | 1           | regular_hours.period_end   |         |


## EVSEStatuses

| Field            | Type                                  | Cardinality | Mapping | Comment |
|------------------|---------------------------------------|-------------|---------|---------|
| EVSEStatusRecord | [EVSEStatusRecord](#EVSEStatusRecord) | *           |         |         |
| OperatorID       | string                                | 1           |         |         |
| OperatorName     | string                                | 1           |         |         |


## EVSEStatusRecord


| Field      | Type                      | Cardinality | Mapping      | Comment |
|------------|---------------------------|-------------|--------------|---------|
| EvseID     | string                    | 1           | evse.evse_id |         |
| EVSEStatus | [EVSEStatus](#EVSEStatus) | 1           | evse.status  |         |


### EVSEStatus


| Key          | Mapping    |
|--------------|------------|
| Available    | AVAILABLE  |
| OutOfService | OUTOFORDER |
| Occupied     | CHARGING   |
| Unknown      | UNKNOWN    |
