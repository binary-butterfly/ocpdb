# DATEX II Input vs Output Differences

This document describes the transformations that occur when DATEX II data is ingested into OCPDB and then
exported again via the API. The input file is the raw DATEX II payload from EnBW; the output file is what the
OCPDB API returns in DATEX II format.

Both files share the same DATEX II AEGI (AFIR Energy Infrastructure) envelope structure, but there are
significant differences at every level of the hierarchy.

## Publication level

| Field                                   | Input                                   | Output                            |
|-----------------------------------------|-----------------------------------------|-----------------------------------|
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


### Modified fields

| Field      | Input                     | Output                                 |
|------------|---------------------------|----------------------------------------|
| `versionG` | Original source timestamp | Replaced with OCPDB internal timestamp |


### Dropped fields

| Field                         | Notes                                                                                                                                                                                                                       |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `electricEnergy[].energyRate` | Entire pricing information dropped: `ratePolicy`, `lastUpdated`, `applicableCurrency`, `payment.paymentMeans`, `energyPrice` (pricePerKWh, pricePerMinute values, tax info, time-based applicability). Will be added later. |


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

1. **Pricing data** — All energy rates, prices per kWh/minute, tax information, payment means, and time-based applicability rules
2. **Parking information** — Dedicated parking spaces, vehicle type restrictions, EU vehicle categories, amenities (illuminated, roofed)
3. **Site descriptions** — `additionalInformation` text labels
4. **BNetzA identifiers** — `operatorIdBNetzA` external identifiers at both operator and station level
5. **NUTS region codes** — Regional classification codes
6. **Station-level location details** — Station-level address, timezone, and NUTS area are dropped; coordinates are only output when the station has its own lat/lon in the database
7. **Station-level operating hours** — Not output at station level (only at site level)
8. **Station-level operator** — Not output at station level (only at site level)
9. **Source identity** — Original publication creator and table IDs replaced by OCPDB values
10. **Authentication method granularity** — Specific RFID types (`mifareClassic`, `mifareDesfire`) consolidated to generic `rfid`


## Summary of data enrichment

Fields added by the system that are not present in the input:

1. **`connectorFormat`** — Derived from connector type (cable vs socket)
2. **`voltage`** on connector — Propagated from refill point `availableVoltage`
3. **`maximumCurrent`** on connector — Calculated from power and voltage
