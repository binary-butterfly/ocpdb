# DATEX II 3.5 Static Output Mapping

This documents the output mapping from OCPDB internal models to the
[DATEX II German Energy Infrastructure Profile](https://github.com/MobilithekDE/AFIR-DATEX-II-Recharging-Profil/)
(JSON, version 3.5) static data endpoint.

**Endpoint**: `GET /api/public/datex/v3.5/json/static`

The response is a JSON object with a single `payload` key containing a `PayloadPublicationG` object. The hierarchical
structure is: `aegiEnergyInfrastructureTablePublication` -> `energyInfrastructureTable` ->
`energyInfrastructureSite` -> `energyInfrastructureStation` -> `refillPoint` / `aegiElectricChargingPoint` ->
`connector`.


## PayloadPublicationG

Top-level publication wrapper.

| Field                                    | Type                                                                          | Mapping                      | Comment      |
|------------------------------------------|-------------------------------------------------------------------------------|------------------------------|--------------|
| modelBaseVersionG                        | string                                                                        | `3`                          | Static value |
| versionG                                 | string                                                                        | `3.5`                        | Static value |
| profileNameG                             | string                                                                        | `Afir Energy Infrastructure` | Static value |
| profileVersionG                          | string                                                                        | `01-00-00`                   | Static value |
| aegiEnergyInfrastructureTablePublication | [EnergyInfrastructureTablePublication](#energyinfrastructuretablepublication) |                              |              |


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

| Field                       | Type                                                          | Mapping                  | Comment                                |
|-----------------------------|---------------------------------------------------------------|--------------------------|----------------------------------------|
| idG                         | string                                                        | location.uid             |                                        |
| versionG                    | string (datetime)                                             | location.last_updated    | ISO 8601 format                        |
| additionalInformation       | [MultilingualString](#multilingualstring)[]                   | location.name            | Only set if name is present            |
| operatingHours              | [OperatingHoursG](#operatinghoursg)                           | location.twentyfourseven | Only set if `twentyfourseven` is true  |
| locationReference           | [LocationReferenceG (site)](#locationreferenceg-site-level)   |                          | See sub-table                          |
| operator                    | [OrganisationG](#organisationg)                               | location.operator        | Only set if operator is present        |
| helpdesk                    | [OrganisationG](#organisationg-helpdesk)                      | location.help_phone      | Only set if help_phone is present      |
| dedicatedParkingSpaces      | [DedicatedParkingSpaces](#dedicatedparkingspaces)[]           | location.parking_spaces  | Only set if parking spaces are present |
| energyInfrastructureStation | [EnergyInfrastructureStation](#energyinfrastructurestation)[] | location.charging_pool   |                                        |


### LocationReferenceG (site level)

Site-level location reference uses `locAreaLocation` for coordinates and `locPointLocation` for address.

| Field                                                           | Type                  | Mapping       | Comment       |
|-----------------------------------------------------------------|-----------------------|---------------|---------------|
| locAreaLocation.coordinatesForDisplay.latitude                  | decimal               | location.lat  |               |
| locAreaLocation.coordinatesForDisplay.longitude                 | decimal               | location.lon  |               |
| locPointLocation.locLocationExtensionG.FacilityLocation.address | [Address](#address)   |               | See sub-table |


### LocationReferenceG (station level)

Station-level location reference uses `locPointLocation` for both coordinates and address. Only set when
`charging_station.lat` and `charging_station.lon` are present. Coordinates and address are taken from the parent
location.

| Field                                                            | Type                          | Mapping            | Comment                          |
|------------------------------------------------------------------|-------------------------------|--------------------|----------------------------------|
| locPointLocation.coordinatesForDisplay.latitude                  | decimal                       | location.lat       | Uses parent location coordinates |
| locPointLocation.coordinatesForDisplay.longitude                 | decimal                       | location.lon       | Uses parent location coordinates |
| locPointLocation.locLocationExtensionG.FacilityLocation.address  | [Address](#address)           |                    | See sub-table                    |
| locPointLocation.locLocationExtensionG.FacilityLocation.timeZone | string                        | location.time_zone | Only set if time_zone is present |


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

Operator mapping.

| Field                                                     | Type                                      | Mapping                | Comment                                          |
|-----------------------------------------------------------|-------------------------------------------|------------------------|--------------------------------------------------|
| afacAnOrganisation.name                                   | [MultilingualString](#multilingualstring) | business.name          |                                                  |
| afacAnOrganisation.externalIdentifier[0].identifier       | string                                    | business.emobility_uid | Only set if emobility_uid is present             |
| afacAnOrganisation.externalIdentifier[0].typeOfIdentifier | TypeOfIdentifierEnumG                     |                        | `extendedG` with `extendedValueG` = `operatorId` |


### OrganisationG (helpdesk)

Helpdesk organisation, only set when `location.help_phone` is present.

| Field                                                                                                          | Type                                      | Mapping               | Comment                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------|-----------------------|-----------------------------------------|
| afacReferenceableOrganisation.idG                                                                              | string                                    | `HELP`                | Static value                            |
| afacReferenceableOrganisation.versionG                                                                         | string                                    | location.last_updated | ISO 8601 format                         |
| afacReferenceableOrganisation.name                                                                             | [MultilingualString](#multilingualstring) | business.name         | Falls back to `Helpdesk` if no operator |
| afacReferenceableOrganisation.organisationUnit[0].contactInformation[0].afacContactInformation.telephoneNumber | string                                    | location.help_phone   |                                         |


## DedicatedParkingSpaces

Each `ParkingSpace` on the location maps to a `DedicatedParkingSpaces` entry.

| Field               | Type                                                   | Mapping                           | Comment                                                  |
|---------------------|--------------------------------------------------------|-----------------------------------|----------------------------------------------------------|
| idG                 | string                                                 | `PARKING`                         | Static value                                             |
| versionG            | string (datetime)                                      | location.last_updated             | ISO 8601 format                                          |
| numberOfSpaces      | integer                                                | parking_space.parking_space_count |                                                          |
| applicableForVehicles | [VehicleCharacteristics](#vehiclecharacteristics)[]  | parking_space.vehicle_types       | Only set if vehicle types can be mapped                  |
| amenities.roofed    | boolean                                                | parking_space.has_roof            |                                                          |
| amenities.illuminated | boolean                                              | parking_space.is_illuminated      |                                                          |
| accessibility       | AccessibilityEnumG[]                                   | parking_space.is_accessible       | `barrierFreeAccessible` if accessible, otherwise not set |


### VehicleCharacteristics

| Field                                                                            | Type                           | Mapping                      | Comment                                           |
|----------------------------------------------------------------------------------|--------------------------------|------------------------------|---------------------------------------------------|
| comVehicleCharacteristicsExtensionG.VehicleCharacteristicsExtended.euVehicleCategory | EuVehicleCategoryEnumG[]   | parking_space.vehicle_types  | See [vehicle category mapping](#vehicle-category-mapping) |
| grossWeightCharacteristic[0].grossVehicleWeight                                  | float                          | parking_space.max_weight     | Converted: kg / 1000 = tonnes, `lessThanOrEqualTo` |
| heightCharacteristic[0].vehicleHeight                                            | float                          | parking_space.max_height     | Converted: cm / 100 = metres, `lessThanOrEqualTo`  |
| lengthCharacteristic[0].vehicleLength                                            | float                          | parking_space.max_length     | Converted: cm / 100 = metres, `lessThanOrEqualTo`  |
| widthCharacteristic[0].vehicleWidth                                              | float                          | parking_space.max_width      | Converted: cm / 100 = metres, `lessThanOrEqualTo`  |


### Vehicle Category Mapping

| Internal (VehicleCategoryEnum) | DATEX II (EuVehicleCategoryEnum) |
|--------------------------------|----------------------------------|
| L1 - L7                       | l1 - l7                         |
| M, M1 - M3                    | m, m1 - m3                      |
| N, N1 - N3                    | n, n1 - n3                      |
| O, O1 - O4                    | o, o1 - o4                      |
| R1 - R4                       | r1 - r4                         |
| T1 - T4, T41 - T43            | t1 - t4, t41 - t43              |


## EnergyInfrastructureStation

A `ChargingStation` maps to an `EnergyInfrastructureStation`.

| Field                                     | Type                                                              | Mapping                                   | Comment                                                         |
|-------------------------------------------|-------------------------------------------------------------------|-------------------------------------------|-----------------------------------------------------------------|
| idG                                       | string                                                            | charging_station.uid                      |                                                                 |
| versionG                                  | string (datetime)                                                 | charging_station.last_updated             | ISO 8601 format                                                 |
| numberOfRefillPoints                      | integer                                                           | len(charging_station.evses)               |                                                                 |
| totalMaximumPower                         | float                                                             | charging_station.max_power_value          | Only set if not None                                            |
| serviceType                               | [ServiceType](#servicetype)[]                                     | charging_station.service_type             | Only set if service_type is present and mappable                |
| locationReference                         | [LocationReferenceG (station)](#locationreferenceg-station-level) |                                           | Only set if charging_station has lat/lon                        |
| authenticationAndIdentificationMethods    | AuthenticationAndIdentificationEnumG[]                            | charging_station.capabilities             | See [capability mapping](#capability-to-authentication-mapping) |
| userInterfaceLanguage                     | string[]                                                          | charging_station.user_interface_languages | Only set if present                                             |
| refillPoint                               | [RefillPointG](#refillpointg)[]                                   | charging_station.evses                    |                                                                 |


### ServiceType

| Field       | Type                | Mapping                       | Comment |
|-------------|---------------------|-------------------------------|---------|
| serviceType | ServiceTypeEnumG    | charging_station.service_type |         |

#### ServiceType Mapping

| Internal (ServiceType)  | DATEX II (ServiceTypeEnum) |
|-------------------------|----------------------------|
| PHYSICAL_ATTENDANCE     | physicalAttendance         |
| UNATTENDED              | unattended                 |


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

| Field                  | Type                                  | Mapping                             | Comment                                            |
|------------------------|---------------------------------------|-------------------------------------|----------------------------------------------------|
| idG                    | string                                | evse.uid                            |                                                    |
| versionG               | string (datetime)                     | evse.last_updated                   | ISO 8601 format                                    |
| deliveryUnit           | DeliveryUnitEnumG                     | `kWh`                               | Static value                                       |
| currentType            | CurrentTypeEnumG                      | first connector's power_type        | See [current type mapping](#current-type-mapping)  |
| numberOfConnectors     | integer                               | len(evse.connectors)                |                                                    |
| availableVoltage       | int[]                                 | connectors' max_voltage             | Collected from all connectors, only set if any     |
| availableChargingPower | int[]                                 | connectors' max_electric_power      | Collected from all connectors, only set if any     |
| electricEnergy         | [ElectricEnergy](#electricenergy)[]   | location.energy_mix, evse.tariffs   | Only set if energy mix or tariffs exist            |
| connector              | [Connector](#connector)[]             | evse.connectors                     | Connectors without `standard` are skipped          |


### Current Type Mapping

Derived from the first connector's `power_type`. Defaults to `ac` if not available.

| Internal (PowerType) | DATEX II (CurrentTypeEnum) |
|----------------------|----------------------------|
| DC                   | dc                         |
| AC_1_PHASE           | ac                         |
| AC_3_PHASE           | ac                         |


### ElectricEnergy

The `electricEnergy` combines energy mix and tariff information. Only set if at least one of `isGreenEnergy` or
`energyRate` is available.

| Field         | Type                        | Mapping                             | Comment                                    |
|---------------|-----------------------------|-------------------------------------|--------------------------------------------|
| isGreenEnergy | boolean                     | location.energy_mix.is_green_energy | Only set if energy_mix exists              |
| energyRate    | [EnergyRate](#energyrate)[] | evse.tariff_associations            | One entry per tariff association on the EVSE |


### EnergyRate

Tariffs associated with the EVSE are mapped to `EnergyRate` entries. The `idG` is extracted from the tariff UID
(format `{evse_uid}:{rate_idG}`, the part after the last `:` is used).

| Field              | Type                                    | Mapping                        | Comment                                                         |
|--------------------|-----------------------------------------|--------------------------------|-----------------------------------------------------------------|
| idG                | string                                  | tariff.uid (suffix after `:`)  | Extracted from `{evse_uid}:{idG}` format                        |
| ratePolicy         | [RatePolicyEnumG](#ratepolicyenum)      | tariff_association.audience    | See [RatePolicyEnum](#ratepolicyenum) mapping, default: `adHoc` |
| lastUpdated        | string (datetime)                       | tariff.last_updated            | ISO 8601 format                                                 |
| applicableCurrency | string[]                                | tariff.currency                | Single-element list, defaults to `EUR`                          |
| energyPrice        | [EnergyPrice](#energyprice)[]           | tariff.elements                | One entry per price component, only set if any                  |


### RatePolicyEnum

| Internal (TariffAudience) | DATEX II (RatePolicyEnum) |
|---------------------------|---------------------------|
| AD_HOC_PAYMENT            | adHoc                     |
| EMSP_CONTRACT             | contract                  |


### EnergyPrice

Each tariff element's price component maps to an `EnergyPrice`.

| Field                    | Type                                                  | Mapping                                    | Comment                                                              |
|--------------------------|-------------------------------------------------------|--------------------------------------------|----------------------------------------------------------------------|
| priceType                | [PriceTypeEnumG](#pricetypeenum)                      | price_component.type                       | See [PriceTypeEnum](#pricetypeenum) mapping                          |
| value                    | float                                                 | price_component.price                      | Defaults to 0 if not set                                             |
| taxRate                  | float                                                 | price_component.taxes[0].percentage        | Only set if tax with percentage exists                               |
| timeBasedApplicability   | [TimeBasedApplicability](#timebasedapplicability)     | tariff_element.restrictions                | Only set if min_duration or max_duration is present                  |
| overallPeriod            | [OverallPeriod](#overallperiod)                       | tariff_element.restrictions                | Only set if start_time or end_time is present                        |
| energyBasedApplicability | [EnergyBasedApplicability](#energybasedapplicability) | tariff_element.restrictions                | Only set if min_energy or max_energy is present                      |


### PriceTypeEnum

| Internal (TariffDimensionType) | DATEX II (PriceTypeEnum) |
|--------------------------------|--------------------------|
| ENERGY                         | pricePerKWh              |
| TIME                           | pricePerMinute           |
| FLAT                           | flatRate                 |
| PARKING_TIME                   | pricePerMinute           |
| (other)                        | other                    |


### TimeBasedApplicability

| Field      | Type    | Mapping                                  | Comment                                |
|------------|---------|------------------------------------------|----------------------------------------|
| fromMinute | integer | tariff_element.restrictions.min_duration  | Converted: seconds / 60 = minutes      |
| toMinute   | integer | tariff_element.restrictions.max_duration  | Converted: seconds / 60 = minutes      |


### OverallPeriod

Only set when `tariff_element.restrictions.start_time` or `end_time` is present.

| Field                                          | Type              | Mapping                              | Comment                                                  |
|------------------------------------------------|-------------------|--------------------------------------|----------------------------------------------------------|
| overallStartTime                               | string (datetime) | tariff_association.start_date_time   | Falls back to current UTC time                           |
| validPeriod[0].recurringTimePeriodOfDay[0].startTimeOfPeriod | string  | tariff_element.restrictions.start_time | Falls back to `00:00`                        |
| validPeriod[0].recurringTimePeriodOfDay[0].endTimeOfPeriod   | string  | tariff_element.restrictions.end_time   | Falls back to `23:59`                        |


### EnergyBasedApplicability

Only set when `tariff_element.restrictions.min_energy` or `max_energy` is present.

| Field   | Type    | Mapping                                 | Comment    |
|---------|---------|-----------------------------------------|------------|
| fromKWh | integer | tariff_element.restrictions.min_energy  | Cast to int |
| toKWh   | integer | tariff_element.restrictions.max_energy  | Cast to int |


### Connector

| Field            | Type                     | Mapping                      | Comment                                                   |
|------------------|--------------------------|------------------------------|-----------------------------------------------------------|
| connectorType    | ConnectorTypeEnumG       | connector.standard           | See [connector type mapping](#connector-type-mapping)     |
| maxPowerAtSocket | float                    | connector.max_electric_power | 0.0 if not available                                      |
| voltage          | float                    | connector.max_voltage        | Only set if present                                       |
| maximumCurrent   | float                    | connector.max_amperage       | Only set if present                                       |
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
