# Bundesnetzagentur Data

The Bundesnetzagentur provides an API with most public charging stations in Germany.

For the mapping, please keep the rules defined  in `basics.md` in mind.

Static values:

* `location.country` will allways be `DEU`
* `location.time_zone` will always be `Europe/Berlin`

The response will have `documentDate`, a string formatted by `dd.MM.yyyy`, and `documentTime`, a string formatted by `HH:mm Uhr`, on root level. Both values will be combined and be used as `last_updated` value for `location`, `evse` and `connector`.

As there is no unique identifier for `evse.uid`, `evse.uid` will be set as `{location.id}-{i}`, with i as the array position in `evses` array.

As there is no unique identifier for `connector.id`, `connector.id` will be set as `{location.id}-{i}-{j}`, with i as the array position in `evses` array, and j the array position in `connectors` array.


## ChargingStation

| Field                       | Type                                            | Cardinality | Mapping                                | Comment                                                 |
|-----------------------------|-------------------------------------------------|-------------|----------------------------------------|---------------------------------------------------------|
| id                          | integer                                         | 1           | location.id                            |                                                         |
| operator                    | [Operator](#Operator)                           | 1           |                                        |                                                         |
| status                      | [ChargingStationStatus](#ChargingStationStatus) | 1           |                                        |                                                         |
| type                        | [ChargingStationType](#ChargingStationType)     | 1           |                                        |                                                         |
| location_description        | string                                          | ?           |                                        |                                                         |
| street                      | string                                          | ?           | location.address                       | Combined with `house_no`                                |
| house_no                    | string                                          | ?           | location.address                       | Combined with `street`, will be ignored when set to `0` |
| address_addition            | string                                          | ?           |                                        |                                                         |
| city                        | string                                          | 1           | location.city                          |                                                         |
| postal_code                 | string                                          | 1           | location.postal_code                   |                                                         |
| district_independent_city   | string                                          | 1           |                                        |                                                         |
| state                       | string                                          | 1           |                                        |                                                         |
| coordinates                 | [Coordinates](#Coordinates)                     | 1           |                                        |                                                         |
| payment_systems             | [PaymentSystem](#PaymentSystem)                 | 1           | evse.capabilities                      |                                                         |
| access_restriction          | [AccessRestriction](#AccessRestriction)         | ?           |                                        |                                                         |
| go_live_date                | string (dd.MM.yyyy)                             | 1           |                                        |                                                         |
| opening_hours_specification | [OpeningHours](#OpeningHours)                   | 1           | location.opening_hours.twentyfourseven |                                                         |
| opening_days                | [OpeningDay](#OpeningDay)                       | *           | location.opening_hours.regular_hours   |                                                         |
| max_electric_power_station  | numeric                                         | 1           |                                        | unit: kW                                                |
| evses                       | [Evse](#Evse)                                   | *           |                                        |                                                         |


### ChargingStationType

| Key                    | Mapping |
|------------------------|---------|
| Normalladeeinrichtung  |         |
| Schnellladeeinrichtung |         |


### PaymentSystem

| Key                        | Mapping                                       |
|----------------------------|-----------------------------------------------|
| Kostenlos                  |                                               |
| Bargeld                    |                                               |
| Kostenlos                  |                                               |
| Kreditkarte (Lesegerät)    | CREDIT_CARD_PAYABLE, CHIP_CARD_SUPPORT        |
| Kreditkarte (NFC)          | CREDIT_CARD_PAYABLE, CONTACTLESS_CARD_SUPPORT |
| Kreditkarte (Webseite/App) | REMOTE_START_STOP_CAPABLE                     |
| Debitkarte (Lesegerät)     | DEBIT_CARD_PAYABLE, CHIP_CARD_SUPPORT         |
| Debitkarte (NFC)           | DEBIT_CARD_PAYABLE, CONTACTLESS_CARD_SUPPORT  |
| Debitkarte (Webseite/App)  | REMOTE_START_STOP_CAPABLE                     |
| Onlinezahlungsverfahren    | REMOTE_START_STOP_CAPABLE                     |
| RFID-Karte                 | RFID_READER                                   |
| Kostenlos (Registrierung)  |                                               |
| Plug & Charge              |                                               |
| Sonstige                   |                                               |


### AccessRestriction

| Key                     | Mapping |
|-------------------------|---------|
| Keine Beschränkung      |         |
| Nur für Kunden/Besucher |         |


### OpeningHours

| Key           | Mapping                                                        |
|---------------|----------------------------------------------------------------|
| 247           | `location.opening_times.twentyfourseven` will be set to `true` |
| Eingeschränkt |                                                                |
| Keine Angabe  |                                                                |



## Operator

| Field       | Type    | Cardinality | Mapping                | Comment |
|-------------|---------|-------------|------------------------|---------|
| companyName | string  | 1           | location.operator.name |         |
| displayName | string  | ?           |                        |         |


## ChargingStationStatus

| Field       | Type                                    | Cardinality | Mapping | Comment |
|-------------|-----------------------------------------|-------------|---------|---------|
| operational | [OperationalStatus](#OperationalStatus) | 1           |         |         |


### OperationalStatus

| Key        | Mapping     |
|------------|-------------|
| In Betrieb | STATIC      |
| In Wartung | INOPERATIVE |


## Coordinates

| Field     | Type  | Cardinality | Mapping                        | Comment |
|-----------|-------|-------------|--------------------------------|---------|
| latitude  | float | 1           | location.coordinates.latitude  |         |
| longitude | float | 1           | location.coordinates.longitude |         |


## OpeningDay

| Field     | Type                | Cardinality | Mapping                                           | Comment |
|-----------|---------------------|-------------|---------------------------------------------------|---------|
| weekday   | [Weekday](#Weekday) | ?           | location.opening_hours.regular_hours.weekday      |         |
| open_from | string (HH:mm)      | 1           | location.opening_hours.regular_hours.period_begin |         |
| open_to   | string (HH:mm)      | 1           | location.opening_hours.regular_hours.period_end   |         |


### Weekday

| Key        | Mapping |
|------------|---------|
| Montag     | 1       |
| Dienstag   | 2       |
| Mittwoch   | 3       |
| Donnerstag | 4       |`
| Freitag    | 5       |
| Samstag    | 6       |
| Sonntag    | 7       |


## Evse

| Field                | Type                    | Cardinality | Mapping      | Comment |
|----------------------|-------------------------|-------------|--------------|---------|
| evse_id              | string                  | ?           | evse.evse_id |         |
| public_key_available | bool                    | 1           |              |         |
| public_key           | string                  | 1           |              |         |
| connectors           | [Connector](#Connector) | *           |              |         |


## Connector

| Field                        | Type                            | Cardinality | Mapping                                                    | Comment |
|------------------------------|---------------------------------|-------------|------------------------------------------------------------|---------|
| connector_type               | [ConnectorType](#ConnectorType) | ?           | connector.standard, connector.format, connector.power_type |         |
| max_electric_power_connector | numeric                         | 1           | connector.max_electric_power                               |         |

If `connector_type` is `AC Schuko`, `max_electric_power` is capped to 3700 kW, as there are a lot of wrong datasets in the data source with 22000 kW.



### ConnectorType

| Key                                   | Mapping `ConnectorType` | Mapping `ConnectorFormat` | Comment                                                                                                                        |
|---------------------------------------|-------------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| AC Typ 2 Steckdose                    | IEC_62196_T2            | SOCKET                    |                                                                                                                                |
| AC Typ 2 Fahrzeugkupplung             | IEC_62196_T2            | CABLE                     |                                                                                                                                |
| DC Fahrzeugkupplung Typ Combo 2 (CCS) | IEC_62196_T2_COMBO      | SOCKET                    |                                                                                                                                |
| AC Schuko                             | DOMESTIC_F              | SOCKET                    |                                                                                                                                |
| DC CHAdeMO                            | CHADEMO                 | CABLE                     |                                                                                                                                |
| AC Typ 1 Steckdose                    | IEC_62196_T1            | SOCKET                    |                                                                                                                                |
| DC Tesla Fahrzeugkupplung (Typ 2)     | TESLA_S                 | CABLE                     | Could be `TESLA_R`, too, but `TESLA_S` is more common.                                                                         |
| AC CEE 3-polig                        | IEC_60309_2_single_16   | SOCKET                    |                                                                                                                                |
| AC CEE 5-polig                        | IEC_60309_2_three_32    | SOCKET                    | Could be `IEC_60309_2_three_16`, `IEC_60309_2_three_32` and `IEC_60309_2_three_64`, but `IEC_60309_2_three_32` is most common. |
| Kabellos/Induktiv                     |                         |                           |                                                                                                                                |
