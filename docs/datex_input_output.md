# DATEX II Input vs Output Differences

This document describes the transformations that occur when DATEX II data is ingested into OCPDB and then
exported again via the API. The input file is the raw DATEX II payload from EnBW; the output file is what the
OCPDB API returns in DATEX II format.

Both files share the same DATEX II AEGI (AFIR Energy Infrastructure) envelope structure, but there are
significant differences at every level of the hierarchy.

## Publication level

| Field                                   | Input                                   | Output                            |
|-----------------------------------------|-----------------------------------------|-----------------------------------|
| `versionG`                              | `3.5` or `3.6`                          | `3.5`                             |
| `publicationCreator.nationalIdentifier` | `DE-NAP-EnBWAG` (original source)       | `OCPDB` (replaced by system)      |
| `publicationTime`                       | Original timestamp from source          | Regenerated at export time        |
| `energyInfrastructureTable[].idG`       | Original ID (e.g. `907574882292453376`) | Replaced with sequential ID (`1`) |
| `energyInfrastructureTable[].versionG`  | Original version (e.g. `2`)             | Replaced with `1`                 |


## Site level (`energyInfrastructureSite`)

### Preserved fields

- `idG` — kept as-is
- `operatingHours` — kept as-is
- `locationReference.locAreaLocation.coordinatesForDisplay` — latitude/longitude preserved
- `locationReference.locPointLocation.locLocationExtensionG.FacilityLocation.address` — full address preserved (postcode, city, countryCode, addressLines)
- `operator.afacAnOrganisation.name` — preserved
- `helpdesk` — structure preserved (phone number, organisation units)
- `energyInfrastructureStation` — all stations preserved


### Dropped fields

| Field                     | Notes                                                                                                                 |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `additionalInformation`   | Site description text (e.g. "EDEKA Wangen, Siemensstraße 10") is not stored/exported                                  |
| `accessibility`           | Empty arrays in input, not present in output                                                                          |
| `dedicatedParkingSpaces`  | Entire parking space data dropped (vehicle types, EU categories, number of spaces, amenities like illuminated/roofed) |


### Modified fields

| Field                                             | Input                                              | Output                                             |
|---------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| `versionG`                                        | Original source timestamp                          | Replaced with OCPDB internal timestamp             |
| `operator.afacAnOrganisation.externalIdentifier`  | Two identifiers: `operatorId` + `operatorIdBNetzA` | Only `operatorId` kept; `operatorIdBNetzA` dropped |
| `helpdesk.afacReferenceableOrganisation.name`     | Original casing (e.g. `EnBW`)                      | Uppercased by system (e.g. `ENBW`)                 |
| `helpdesk.afacReferenceableOrganisation.versionG` | Original source timestamp                          | Replaced with OCPDB internal timestamp             |


## Station level (`energyInfrastructureStation`)

### Preserved fields

- `idG` — kept as-is
- `totalMaximumPower` — preserved
- `numberOfRefillPoints` — preserved
- `userInterfaceLanguage` — preserved
- `serviceType` — preserved


### Dropped fields

| Field                                            | Notes                                                                                                               |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `accessibility`                                  | Empty arrays in input, not present in output                                                                        |
| `externalIdentifier`                             | BNetzA external identifiers (e.g. `operatorIdBNetzA` with values like `1121151`) are dropped                        |
| `supplementalFacility`                           | Empty arrays in input, not present in output                                                                        |
| `operatingHours`                                 | Not output at station level (only at site level)                                                                    |
| `operator`                                       | Not output at station level (only at site level)                                                                    |
| `locationReference`                              | Only present when station has its own coordinates; otherwise dropped entirely (see coordinate handling note below)  |
| `locationReference...FacilityLocation.nutsArea`  | NUTS region codes (e.g. `DE1`, `DE4`, `DED`) are dropped even when locationReference is present                     |
| `locationReference...FacilityLocation.address`   | Station-level address and timezone are not output even when locationReference is present                            |


### Modified fields

| Field                                    | Input                                                 | Output                                                   |
|------------------------------------------|-------------------------------------------------------|----------------------------------------------------------|
| `versionG`                               | Original source timestamp                             | Replaced with OCPDB internal timestamp                   |
| `authenticationAndIdentificationMethods` | Specific RFID types: `mifareClassic`, `mifareDesfire` | Consolidated to generic `rfid`; order may change         |


### Coordinate handling

Station-level `locationReference` is only output when the station has its own coordinates (`lat`/`lon`). When
present, it contains only `coordinatesForDisplay` — the station-level address, timezone, and NUTS area from the
input are not included.

In the input, stations typically repeat the site-level coordinates. In the current output, station-level
coordinates are omitted entirely if the station does not have its own coordinates in the database. This means
station-level location information from the input (including address, timezone, and NUTS codes) is lost.


## Refill point level (`aegiElectricChargingPoint`)

### Preserved fields

- `idG` — kept as-is
- `deliveryUnit` — preserved
- `currentType` — preserved (`dc`, `ac`)
- `numberOfConnectors` — preserved
- `availableVoltage` — preserved
- `availableChargingPower` — preserved
- `electricEnergy[].isGreenEnergy` — preserved
- `electricEnergy[].energyRate` — preserved (see tariff data below)


### Modified fields

| Field      | Input                     | Output                                 |
|------------|---------------------------|----------------------------------------|
| `versionG` | Original source timestamp | Replaced with OCPDB internal timestamp |


### Tariff / energy rate data

Energy rate data from `electricEnergy[].energyRate` is now imported and exported. The following fields are
preserved through the import/export cycle:

| Field                                        | Notes                                                                            |
|----------------------------------------------|----------------------------------------------------------------------------------|
| `energyRate[].idG`                           | Preserved (extracted from tariff uid)                                            |
| `energyRate[].ratePolicy`                    | Mapped: `adHoc` ↔ `AD_HOC_PAYMENT`, `contract` ↔ `REGULAR`                      |
| `energyRate[].lastUpdated`                   | Preserved as tariff `last_updated`                                               |
| `energyRate[].applicableCurrency`            | Preserved as tariff `currency`                                                   |
| `energyRate[].energyPrice[].priceType`       | Mapped: `pricePerKWh` ↔ `ENERGY`, `pricePerMinute` ↔ `TIME`, `flatRate` ↔ `FLAT`|
| `energyRate[].energyPrice[].value`           | Preserved as price component `price`                                             |
| `energyRate[].energyPrice[].taxIncluded`     | Preserved as price component `tax_included`                                      |
| `energyRate[].energyPrice[].taxRate`         | Preserved as price component `vat`                                               |
| `energyRate[].energyPrice[].timeBasedApplicability` | Preserved (fromMinute, toMinute)                                          |

### Dropped fields (energy rate)

| Field                                        | Notes                                                                            |
|----------------------------------------------|----------------------------------------------------------------------------------|
| `energyRate[].payment.paymentMeans`          | Payment means not round-tripped (dropped on export)                              |
| `energyRate[].rateName`                      | Not stored                                                                       |
| `energyRate[].additionalInformation`         | Not stored                                                                       |
| `energyRate[].overallPeriod`                 | Not stored                                                                       |
| `energyRate[].combinationWithParkingFee`     | Not stored                                                                       |
| `energyRate[].maximumDeliveryFee`            | Not stored                                                                       |
| `energyRate[].minimumDeliveryFee`            | Not stored                                                                       |
| `energyRate[].discount`                      | Not stored                                                                       |


### Internal storage model

Tariff data is stored using OCPI 3.0-aligned tables:

- **`tariff`** — One tariff per EVSE per rate (uid = `{evse_uid}:{rate_idG}`). Stores currency, type, timestamps.
- **`tariff_element`** — Price components stored as JSON (list of `{type, price, vat, tax_included, time_based_applicability}`).
- **`tariff_association`** — Links each tariff to an EVSE and connector via foreign key relationships (`evse_id`, `connector_id`).


## Connector level

### Preserved fields

- `connectorType` — preserved (e.g. `iec62196T2COMBO`, `iec62196T2`)
- `maxPowerAtSocket` — preserved


### Added fields (not in input)

| Field             | Value                                          | Notes                                                                                                        |
|-------------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `connectorFormat` | `cableMode3` (DC) / `socket` (AC)              | Derived by the system based on connector type                                                                |
| `voltage`         | From `availableVoltage` of parent refill point | Copied down from refill point level                                                                          |
| `maximumCurrent`  | Calculated                                     | For DC: equals `availableChargingPower`; for AC: calculated as `power / voltage` (e.g. 22000 / 0.23 = 95652) |


## Summary of data loss

The main categories of information lost during the import/export cycle:

1. **Parking information** — Dedicated parking spaces, vehicle type restrictions, EU vehicle categories, amenities (illuminated, roofed)
2. **Site descriptions** — `additionalInformation` text labels
3. **BNetzA identifiers** — `operatorIdBNetzA` external identifiers at both operator and station level
4. **NUTS region codes** — Regional classification codes
5. **Station-level location details** — Station-level address, timezone, and NUTS area are dropped; coordinates are only output when the station has its own lat/lon in the database
6. **Station-level operating hours** — Not output at station level (only at site level)
7. **Station-level operator** — Not output at station level (only at site level)
8. **Source identity** — Original publication creator and table IDs replaced by OCPDB values
9. **Authentication method granularity** — Specific RFID types (`mifareClassic`, `mifareDesfire`) consolidated to generic `rfid`
10. **Energy rate metadata** — `payment.paymentMeans`, `rateName`, `additionalInformation`, `overallPeriod`, `discount`, delivery fee bounds


## Summary of data enrichment

Fields added by the system that are not present in the input:

1. **`connectorFormat`** — Derived from connector type (cable vs socket)
2. **`voltage`** on connector — Propagated from refill point `availableVoltage`
3. **`maximumCurrent`** on connector — Calculated from power and voltage
