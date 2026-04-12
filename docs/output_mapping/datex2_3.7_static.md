# DATEX II 3.7 Static Output Mapping

This documents the output mapping from OCPDB internal models to the
[DATEX II German Energy Infrastructure Profile](https://github.com/MobilithekDE/AFIR-DATEX-II-Recharging-Profil/)
(JSON, version 3.7) static data endpoint.

**Endpoint**: `GET /api/public/datex/v3.7/json/static`

The response is a JSON object with a single `payload` key containing a `PayloadPublicationG` object. The hierarchical
structure is: `egiEnergyInfrastructureTablePublication` -> `energyInfrastructureTable` ->
`energyInfrastructureSite` -> `energyInfrastructureStation` -> `refillPoint` / `egiElectricChargingPoint` ->
`connector`.


## PayloadPublicationG

Top-level publication wrapper.

| Field                                   | Type                                                                          | Mapping                      | Comment      |
|-----------------------------------------|-------------------------------------------------------------------------------|------------------------------|--------------|
| modelBaseVersionG                       | string                                                                        | `3`                          | Static value |
| versionG                                | string                                                                        | `3.7`                        | Static value |
| profileNameG                            | string                                                                        | `Afir Energy Infrastructure` | Static value |
| profileVersionG                         | string                                                                        | `01-00-00`                   | Static value |
| egiEnergyInfrastructureTablePublication | [EnergyInfrastructureTablePublication](#energyinfrastructuretablepublication) |                              |              |


## EnergyInfrastructureTablePublication

| Field                                 | Type                                                      | Mapping          | Comment             |
|---------------------------------------|-----------------------------------------------------------|------------------|---------------------|
| lang                                  | string                                                    | `de`             | Static value        |
| publicationTime                       | string (datetime)                                         | Current UTC time | ISO 8601 format     |
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

Note: Unlike v3.5, the site name is set via the `name` field (not `additionalInformation`). Helpdesk is not mapped in
v3.7.


### LocationReferenceG

A single location reference structure is used for both site and station level. Coordinates are provided via
`pointByCoordinates.pointCoordinates` and address via `locLocationReferenceExtensionG.FacilityLocation`.

| Field                                                                              | Type                | Mapping       | Comment   |
|------------------------------------------------------------------------------------|---------------------|---------------|-----------|
| locPointLocation.pointByCoordinates.pointCoordinates.latitude                      | decimal             | location.lat  |           |
| locPointLocation.pointByCoordinates.pointCoordinates.longitude                     | decimal             | location.lon  |           |
| locPointLocation.locLocationReferenceExtensionG.FacilityLocation.address           | [Address](#address) |               | See below |


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
| facOpenAllHours  | OpenAllHours | location.twentyfourseven | Empty object, presence means 24/7 |


### OrganisationG

Operator mapping. Uses `facOrganisationSpecification` (different from v3.5's `afacAnOrganisation`).

| Field                                              | Type                                      | Mapping                    | Comment                                     |
|----------------------------------------------------|-------------------------------------------|----------------------------|---------------------------------------------|
| facOrganisationSpecification.idG                   | string                                    | business.emobility_uid     | Falls back to `OP-{business.id}` if not set |
| facOrganisationSpecification.versionG              | string                                    | `1`                        | Static value                                |
| facOrganisationSpecification.name                  | [MultilingualString](#multilingualstring) | business.name              |                                             |
| facOrganisationSpecification.organisationUnit       | OrganisationUnit[]                        |                            | Single empty element                        |

Note: Unlike v3.5, the operator does not include `externalIdentifier`. The `emobility_uid` is used as the `idG` instead.


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
| egiElectricChargingPoint  | [ElectricChargingPoint](#electricchargingpoint) |         |         |


### ElectricChargingPoint

Simpler than v3.5: no `deliveryUnit`, `currentType`, or `numberOfConnectors`.

| Field                  | Type                                          | Mapping                             | Comment                                            |
|------------------------|-----------------------------------------------|-------------------------------------|----------------------------------------------------|
| idG                    | string                                        | evse.uid                            |                                                    |
| versionG               | string (datetime)                             | evse.last_updated                   | ISO 8601 format                                    |
| availableVoltage       | int[]                                         | connectors' max_voltage             | Collected from all connectors, only set if any     |
| availableChargingPower | int[]                                         | connectors' max_electric_power      | Collected from all connectors, only set if any     |
| electricEnergyMix      | [ElectricEnergyMix](#electricenergymix)[]     | location.energy_mix.is_green_energy | Only set if energy_mix with is_green_energy exists |
| connector              | [Connector](#connector)[]                     | evse.connectors                     | Connectors without mappable `standard` are skipped |

Note: Unlike v3.5, tariffs are not mapped in v3.7.


### ElectricEnergyMix

Energy mix uses a separate `ElectricEnergyMix` type (not `ElectricEnergy` as in v3.5), referenced via
`electricEnergyMix` (not `electricEnergy`).

| Field          | Type    | Mapping                             | Comment      |
|----------------|---------|-------------------------------------|--------------|
| energyMixIndex | integer | `0`                                 | Static value |
| isGreenEnergy  | boolean | location.energy_mix.is_green_energy |              |


### Connector

Connectors with an unmapped `standard` are skipped entirely (not included in output).

| Field            | Type                     | Mapping                      | Comment                                                   |
|------------------|--------------------------|------------------------------|-----------------------------------------------------------|
| connectorType    | ConnectorTypeEnumG       | connector.standard           | See [connector type mapping](#connector-type-mapping)     |
| maxPowerAtSocket | float                    | connector.max_electric_power | 0.0 if not available                                      |
| voltage          | int                      | connector.max_voltage        | Only set if present                                       |
| maximumCurrent   | int                      | connector.max_amperage       | Only set if present                                       |
| connectorFormat  | ConnectorFormatTypeEnumG | connector.format             | See [connector format mapping](#connector-format-mapping) |


### Connector Type Mapping

| Internal (ConnectorType)   | DATEX II (ConnectorTypeEnum) |
|----------------------------|------------------------------|
| CHADEMO                    | chademo                      |
| DOMESTIC_A                 | domesticA                    |
| DOMESTIC_B                 | domesticB                    |
| DOMESTIC_C                 | domesticC                    |
| DOMESTIC_D                 | domesticD                    |
| DOMESTIC_E                 | domesticE                    |
| DOMESTIC_F                 | domesticF                    |
| DOMESTIC_G                 | domesticG                    |
| DOMESTIC_H                 | domesticH                    |
| DOMESTIC_I                 | domesticI                    |
| DOMESTIC_J                 | domesticJ                    |
| DOMESTIC_K                 | domesticK                    |
| DOMESTIC_L                 | domesticL                    |
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
