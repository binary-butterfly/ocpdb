# DATEX II 3.7 Static Output Mapping

This documents the output mapping from OCPDB internal models to the
[DATEX II German Energy Infrastructure Profile](https://github.com/MobilithekDE/AFIR-DATEX-II-Recharging-Profil/)
(JSON, version 3.7) static data endpoint.

**Endpoint**: `GET /api/public/datex/v3.7/json/static`

The response is a JSON object with a single `payload` key containing a `PayloadPublicationG` object. The hierarchical
structure is: `aegiEnergyInfrastructureTablePublication` -> `energyInfrastructureTable` ->
`energyInfrastructureSite` -> `energyInfrastructureStation` -> `refillPoint` / `aegiElectricChargingPoint` ->
`connector`.


## PayloadPublicationG

Top-level publication wrapper.

| Field                                    | Type                                                                          | Mapping                      | Comment      |
|------------------------------------------|-------------------------------------------------------------------------------|------------------------------|--------------|
| modelBaseVersionG                        | string                                                                        | `3`                          | Static value |
| versionG                                 | string                                                                        | `3.7`                        | Static value |
| profileNameG                             | string                                                                        | `Afir Energy Infrastructure` | Static value |
| profileVersionG                          | string                                                                        | `01-00-00`                   | Static value |
| aegiEnergyInfrastructureTablePublication | [EnergyInfrastructureTablePublication](#energyinfrastructuretablepublication) |                              |              |


## EnergyInfrastructureTablePublication

| Field                                 | Type                                                      | Mapping          | Comment             |
|---------------------------------------|-----------------------------------------------------------|------------------|---------------------|
| lang                                  | string                                                    | `de`             | Static value        |
| publicationTime                       | datetime                                                  | Current UTC time | datetime object     |
| publicationCreator.country            | string                                                    | `DE`             | Static value        |
| publicationCreator.nationalIdentifier | string                                                    | `OCPDB`          | Static value        |
| energyInfrastructureTable             | [EnergyInfrastructureTable](#energyinfrastructuretable)[] |                  | Single-element list |


## EnergyInfrastructureTable

| Field                    | Type                                                    | Mapping       | Comment      |
|--------------------------|---------------------------------------------------------|---------------|--------------|
| idG                      | string                                                  | `1`           | Static value |
| versionG                 | string                                                  | `1`           | Static value |
| energyInfrastructureSite | [EnergyInfrastructureSite](#energyinfrastructuresite)[] |               |              |


## EnergyInfrastructureSite

A `Location` maps to an `EnergyInfrastructureSite`. Locations without `lat`/`lon` are skipped.

| Field                       | Type                                                          | Mapping                  | Comment                               |
|-----------------------------|---------------------------------------------------------------|--------------------------|---------------------------------------|
| idG                         | string                                                        | location.uid             |                                       |
| versionG                    | string (datetime)                                             | location.last_updated    | ISO 8601 format                       |
| name                        | [MultilingualString](#multilingualstring)                     | location.name            | Only set if name is present           |
| operatingHours              | [OperatingHoursG](#operatinghoursg)                           | location.twentyfourseven | Only set if `twentyfourseven` is true |
| locationReference           | [LocationReferenceG](#locationreferenceg)                     |                          | See sub-table                         |
| operator                    | [OrganisationG](#organisationg)                               | location.operator        | Only set if operator is present       |
| energyInfrastructureStation | [EnergyInfrastructureStation](#energyinfrastructurestation)[] | location.charging_pool   |                                       |

Note: Unlike v3.5, the site name is set via the `name` field (not `additionalInformation`). Helpdesk and parking
spaces are not mapped in v3.7.


### LocationReferenceG

A single location reference structure is used for both site and station level. Coordinates are provided via
`pointByCoordinates.pointCoordinates` and address via `locLocationExtensionG.AfirFacilityLocation`.

| Field                                                                        | Type                | Mapping       | Comment   |
|------------------------------------------------------------------------------|---------------------|---------------|-----------|
| locPointLocation.pointByCoordinates.pointCoordinates.latitude                | decimal             | location.lat  |           |
| locPointLocation.pointByCoordinates.pointCoordinates.longitude               | decimal             | location.lon  |           |
| locPointLocation.locLocationExtensionG.AfirFacilityLocation.address          | [Address](#address) |               | See below |


### Address

| Field       | Type                                      | Mapping              | Comment                                                 |
|-------------|-------------------------------------------|----------------------|---------------------------------------------------------|
| postcode    | string                                    | location.postal_code | Only set if postal_code is present                      |
| city        | [MultilingualString](#multilingualstring) | location.city        | Only set if city is present                             |
| countryCode | string (2)                                | location.country     | Converted from 3-digit ISO to 2-digit ISO via pycountry |
| addressLine | [AddressLine](#addressline)[]             | location.address     | Split into street and house number, see sub-table       |


### AddressLine

The address string is split by regex into street and optional house number.

| Field | Type                                      | Mapping          | Comment                                              |
|-------|-------------------------------------------|------------------|------------------------------------------------------|
| order | integer                                   |                  | 1 for street, 2 for house number                     |
| type  | AddressLineTypeEnumG                      |                  | `street` or `houseNumber`                            |
| text  | [MultilingualString](#multilingualstring) | location.address | Split from address: street part or house number part |


### OperatingHoursG

| Field            | Type         | Mapping                  | Comment                           |
|------------------|--------------|--------------------------|-----------------------------------|
| afacOpenAllHours | OpenAllHours | location.twentyfourseven | Empty object, presence means 24/7 |


### OrganisationG

Operator mapping. Uses `afacReferenceableOrganisation` with an `idG` derived from the operator.

| Field                                          | Type                                      | Mapping                    | Comment                                     |
|------------------------------------------------|-------------------------------------------|----------------------------|---------------------------------------------|
| afacReferenceableOrganisation.idG              | string                                    | business.emobility_uid     | Falls back to `OP-{business.id}` if not set |
| afacReferenceableOrganisation.versionG         | string                                    | `1`                        | Static value                                |
| afacReferenceableOrganisation.name             | [MultilingualString](#multilingualstring) | business.name              |                                             |
| afacReferenceableOrganisation.organisationUnit | OrganisationUnit[]                        |                            | Single empty element                        |

Note: Unlike v3.5, the operator does not include `externalIdentifier`. The `emobility_uid` is used as the `idG`
instead.


## EnergyInfrastructureStation

A `ChargingStation` maps to an `EnergyInfrastructureStation`. This is simpler than v3.5: no `numberOfRefillPoints`,
`totalMaximumPower`, `serviceType`, or `userInterfaceLanguage`.

| Field                                     | Type                                                  | Mapping                       | Comment                                                         |
|-------------------------------------------|-------------------------------------------------------|-------------------------------|-----------------------------------------------------------------|
| idG                                       | string                                                | charging_station.uid          |                                                                 |
| versionG                                  | string (datetime)                                     | charging_station.last_updated | ISO 8601 format                                                 |
| locationReference                         | [LocationReferenceG](#locationreferenceg)              |                               | Only set if charging_station has lat/lon, uses parent location  |
| authenticationAndIdentificationMethods    | AuthenticationAndIdentificationEnumG[]                | charging_station.capabilities | See [capability mapping](#capability-to-authentication-mapping) |
| refillPoint                               | [RefillPointG](#refillpointg)[]                       | charging_station.evses        |                                                                 |


### Capability to Authentication Mapping

| Internal (Capability)       | DATEX II (AuthenticationAndIdentificationEnum) |
|-----------------------------|------------------------------------------------|
| CREDIT_CARD_PAYABLE         | creditCard                                     |
| DEBIT_CARD_PAYABLE          | debitCard                                      |
| RFID_READER                 | rfid                                           |
| CONTACTLESS_CARD_SUPPORT    | nfc                                            |
| REMOTE_START_STOP_CAPABLE   | overTheAir                                     |
| IEC15118                    | plc                                            |
| CASH                        | cashPayment                                    |
| PED_TERMINAL                | pinPad                                         |
| CHIP_CARD_SUPPORT           | calypso                                        |


## RefillPointG

An `Evse` maps to a `RefillPointG` wrapping an `ElectricChargingPoint`.

| Field                     | Type                                            | Mapping | Comment |
|---------------------------|-------------------------------------------------|---------|---------|
| aegiElectricChargingPoint | [ElectricChargingPoint](#electricchargingpoint) |         |         |


### ElectricChargingPoint

| Field                  | Type                                          | Mapping                             | Comment                                                    |
|------------------------|-----------------------------------------------|-------------------------------------|------------------------------------------------------------|
| idG                    | string                                        | evse.uid                            |                                                            |
| versionG               | string (datetime)                             | evse.last_updated                   | ISO 8601 format                                            |
| deliveryUnit           | DeliveryUnitEnumG                             | `kWh`                               | Static value                                               |
| currentType            | CurrentTypeEnumG                              | first connector's power_type        | See [current type mapping](#current-type-mapping)          |
| availableVoltage       | float[]                                       | connectors' max_voltage             | Collected from all connectors, only set if any             |
| availableChargingPower | float[]                                       | connectors' max_electric_power      | Collected from all connectors, only set if any             |
| energyProduct          | [EnergyProductG](#energyproductg)[]           | location.energy_mix.is_green_energy | Only set if energy_mix with `is_green_energy` exists       |
| connector              | [Connector](#connector)[]                     | evse.connectors                     | Connectors with unmappable `standard` are skipped          |

Note: Unlike v3.5, tariffs are not mapped in v3.7. Energy mix uses `energyProduct` instead of `electricEnergy`.


### Current Type Mapping

Derived from the first connector's `power_type`. Defaults to `ac` if not available.

| Internal (PowerType) | DATEX II (CurrentTypeEnum) |
|----------------------|----------------------------|
| DC                   | dc                         |
| AC_1_PHASE           | ac                         |
| AC_3_PHASE           | ac                         |


### EnergyProductG

| Field               | Type                                        | Mapping                             | Comment |
|---------------------|---------------------------------------------|-------------------------------------|---------|
| aegiElectricEnergy  | [ElectricEnergy](#electricenergy)           |                                     |         |


### ElectricEnergy

| Field         | Type    | Mapping                             | Comment |
|---------------|---------|-------------------------------------|---------|
| isGreenEnergy | boolean | location.energy_mix.is_green_energy |         |


### Connector

Connectors with an unmapped `standard` are skipped entirely (not included in output).

| Field            | Type                     | Mapping                      | Comment                                                   |
|------------------|--------------------------|------------------------------|-----------------------------------------------------------|
| connectorType    | ConnectorTypeEnumG       | connector.standard           | See [connector type mapping](#connector-type-mapping)     |
| maxPowerAtSocket | float                    | connector.max_electric_power | 0.0 if not available                                      |
| voltage          | float                    | connector.max_voltage        | Only set if present                                       |
| maximumCurrent   | float                    | connector.max_amperage       | Only set if present                                       |
| connectorFormat  | ConnectorFormatTypeEnumG | connector.format             | See [connector format mapping](#connector-format-mapping) |


### Connector Type Mapping

Note: v3.7 uses different enum values for domestic types (e.g. `domesticAType` instead of `domesticA`).

| Internal (ConnectorType)   | DATEX II (ConnectorTypeEnum) |
|----------------------------|------------------------------|
| CHADEMO                    | chademo                      |
| DOMESTIC_A                 | domesticAType                |
| DOMESTIC_B                 | domesticBType                |
| DOMESTIC_C                 | domesticCType                |
| DOMESTIC_D                 | domesticDType                |
| DOMESTIC_E                 | domesticEType                |
| DOMESTIC_F                 | domesticFType                |
| DOMESTIC_G                 | domesticGType                |
| DOMESTIC_H                 | domesticHType                |
| DOMESTIC_I                 | domesticIType                |
| DOMESTIC_J                 | domesticJType                |
| DOMESTIC_K                 | domesticKType                |
| DOMESTIC_L                 | domesticLType                |
| IEC_60309_2_single_16      | iec60309x2Single16           |
| IEC_60309_2_three_16       | iec60309x2Three16            |
| IEC_60309_2_three_32       | iec60309x2Three32            |
| IEC_60309_2_three_64       | iec60309x2Three64            |
| IEC_62196_T1               | iec62196T1                   |
| IEC_62196_T1_COMBO         | iec62196T1Combo              |
| IEC_62196_T2               | iec62196T2                   |
| IEC_62196_T2_COMBO         | iec62196T2Combo              |
| IEC_62196_T3A              | iec62196T3A                  |
| IEC_62196_T3C              | iec62196T3C                  |
| PANTOGRAPH_BOTTOM_UP       | pantographBottomUp           |
| PANTOGRAPH_TOP_DOWN        | pantographTopDown            |
| TESLA_R                    | teslaR                       |
| TESLA_S                    | teslaS                       |


### Connector Format Mapping

| Internal (ConnectorFormat) | DATEX II (ConnectorFormatTypeEnum) |
|----------------------------|------------------------------------|
| SOCKET                     | socket                             |
| CABLE                      | cableMode3                         |


## MultilingualString

All multilingual strings default to language `de`.

| Field           | Type   | Mapping | Comment          |
|-----------------|--------|---------|------------------|
| values[0].lang  | string | `de`    | Static value     |
| values[0].value | string |         | The text content |
