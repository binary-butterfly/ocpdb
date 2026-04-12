# DATEX II 3.5 German Energy Infrastructure

This documents the mapping between the
[DATEX II German Energy Infrastructure Profile](https://github.com/MobilithekDE/AFIR-DATEX-II-Recharging-Profil/)
(JSON, version 3.5) and OCPI 3.0-preview Locations / ChargingStations / EVSEs / Connectors / Tariffs.

It is an extension to the `_general.md`.

DATEX II provides static and realtime data for charging infrastructure in Germany.

Static data is delivered as a JSON payload containing an `aegiEnergyInfrastructureTablePublication` with a hierarchical
structure: `energyInfrastructureSite` -> `energyInfrastructureStation` -> `refillPoint` / `aegiElectricChargingPoint`
-> `connector`.

Realtime data is delivered as an `aegiEnergyInfrastructureStatusPublication` containing `energyInfrastructureSiteStatus`
-> `energyInfrastructureStationStatus` -> `refillPointStatus` entries that reference the static data by ID.

## Global / Static Values

| Field              | Mapping       | Comment                                                |
|--------------------|---------------|--------------------------------------------------------|
| location.country   | DEU           | Data source is Germany-only                            |
| location.time_zone | Europe/Berlin | Default, can be overridden by station-level `timeZone` |


# energyInfrastructureSite

An `energyInfrastructureSite` maps to a `Location`.

| Field                          | Type                                                                  | Cardinality | Mapping                  | Comment                                                                        |
|--------------------------------|-----------------------------------------------------------------------|-------------|--------------------------|--------------------------------------------------------------------------------|
| idG                            | string                                                                | 1           | location.uid             |                                                                                |
| versionG                       | string                                                                | 1           |                          | Not mapped                                                                     |
| name                           | [MultilingualString](#MultilingualString)                             | ?           | location.name            |                                                                                |
| alias                          | [MultilingualString](#MultilingualString)                             | *           |                          | Not mapped                                                                     |
| lastUpdated                    | string (datetime)                                                     | ?           | location.last_updated    |                                                                                |
| description                    | [MultilingualString](#MultilingualString)                             | ?           |                          | Not mapped                                                                     |
| additionalInformation          | [MultilingualString](#MultilingualString)                             | *           |                          | Not mapped, contains human-readable site description                           |
| accessibility                  | [AccessibilityEnum](#AccessibilityEnum)                               | *           |                          | Not mapped at site level                                                       |
| typeOfSite                     | [EnergyInfrastructureSiteTypeEnum](#EnergyInfrastructureSiteTypeEnum) | ?           |                          | Not mapped                                                                     |
| brand                          | [MultilingualString](#MultilingualString)                             | ?           |                          | Not mapped                                                                     |
| exclusiveUsers                 | UserTypeEnum                                                          | *           |                          | Not mapped                                                                     |
| preferredUsers                 | UserTypeEnum                                                          | *           |                          | Not mapped                                                                     |
| externalIdentifier             | [ExternalIdentifier](#ExternalIdentifier)                             | *           |                          | Not mapped                                                                     |
| informationWebsite             | UrlLink                                                               | *           |                          | Not mapped                                                                     |
| photoUrl                       | UrlLink                                                               | *           |                          | Not mapped                                                                     |
| photo                          | Image                                                                 | *           |                          | Not mapped                                                                     |
| operatingHours                 | [OperatingHoursG](#OperatingHoursG)                                   | ?           | location.twentyfourseven | Only `afacOpenAllHours` is evaluated                                           |
| locationReference              | [LocationReferenceG](#LocationReferenceG)                             | ?           |                          | Provides lat/lon and address, see sub-table                                    |
| owner                          | [OrganisationG](#OrganisationG)                                       | ?           |                          | Not mapped                                                                     |
| operator                       | [OrganisationG](#OrganisationG)                                       | ?           | location.operator        | See [OrganisationG](#OrganisationG)                                            |
| helpdesk                       | [OrganisationG](#OrganisationG)                                       | ?           | location.help_phone      | Telephone extracted from helpdesk organisation                                 |
| applicableForVehicles          | VehicleCharacteristics                                                | *           |                          | Not mapped                                                                     |
| dimension                      | Dimension                                                             | ?           |                          | Not mapped                                                                     |
| amenities                      | [Amenities](#Amenities)                                               | ?           | location.parking_spaces  | Fallback for parking space `has_roof` / `is_illuminated`                       |
| supplementalFacility           | SupplementalFacilityG                                                 | *           |                          | Not mapped                                                                     |
| dedicatedParkingSpaces         | [DedicatedParkingSpaces](#DedicatedParkingSpaces)                     | *           | location.parking_spaces  | See [DedicatedParkingSpaces](#DedicatedParkingSpaces)                          |
| serviceType                    | ServiceType                                                           | *           |                          | Not mapped at site level                                                       |
| entrance                       | LocationG                                                             | *           |                          | Not mapped                                                                     |
| exit                           | LocationG                                                             | *           |                          | Not mapped                                                                     |
| energyInfrastructureStation    | [EnergyInfrastructureStation](#energyInfrastructureStation)           | *           | location.charging_pool   |                                                                                |
| energyDistributor              | OrganisationG                                                         | ?           |                          | Not mapped                                                                     |
| mobilityServiceProvider        | OrganisationG                                                         | *           |                          | Not mapped                                                                     |
| roamingPlatfom                 | OrganisationG                                                         | *           |                          | Not mapped                                                                     |


## LocationReferenceG

The `LocationReferenceG` provides two main location structures: `locAreaLocation` for coordinates and `locPointLocation`
for address details.

| Field                                                                       | Type                                      | Cardinality | Mapping              | Comment                                                      |
|-----------------------------------------------------------------------------|-------------------------------------------|-------------|----------------------|--------------------------------------------------------------|
| locAreaLocation.coordinatesForDisplay.latitude                              | float                                     | 1           | location.lat         |                                                              |
| locAreaLocation.coordinatesForDisplay.longitude                             | float                                     | 1           | location.lon         |                                                              |
| locPointLocation.locLocationExtensionG.FacilityLocation.address.postcode    | string                                    | ?           | location.postal_code |                                                              |
| locPointLocation.locLocationExtensionG.FacilityLocation.address.city        | [MultilingualString](#MultilingualString) | ?           | location.city        |                                                              |
| locPointLocation.locLocationExtensionG.FacilityLocation.address.countryCode | string (2)                                | ?           | location.country     | Transformation from 2 digit country code to 3 digit ISO code |
| locPointLocation.locLocationExtensionG.FacilityLocation.address.addressLine | [AddressLine](#AddressLine)               | *           | location.address     | Street and house number are concatenated                     |
| locPointLocation.locLocationExtensionG.FacilityLocation.timeZone            | string                                    | ?           | location.time_zone   | Overrides default `Europe/Berlin`                            |


### AddressLine

| Field | Type                                        | Cardinality | Mapping          | Comment                                                                   |
|-------|---------------------------------------------|-------------|------------------|---------------------------------------------------------------------------|
| order | integer                                     | 1           |                  | Defines the order of address lines                                        |
| type  | [AddressLineTypeEnum](#AddressLineTypeEnum) | 1           |                  | Determines how to use this line                                           |
| text  | [MultilingualString](#MultilingualString)   | 1           | location.address | Only `street` and `houseNumber` types are used, concatenated with a space |


### AddressLineTypeEnum

Only `street` and `houseNumber` are used for the mapping.

| Key               | Usage           |
|-------------------|-----------------|
| street            | Part of address |
| houseNumber       | Part of address |
| apartment         | Not mapped      |
| building          | Not mapped      |
| poBox             | Not mapped      |
| unit              | Not mapped      |
| region            | Not mapped      |
| town              | Not mapped      |
| districtTerritory | Not mapped      |
| floor             | Not mapped      |
| generalTextLine   | Not mapped      |


## OperatingHoursG

| Field                           | Type                        | Cardinality | Mapping                      | Comment                                     |
|---------------------------------|-----------------------------|-------------|------------------------------|---------------------------------------------|
| afacOpenAllHours                | OpenAllHours                | ?           | location.twentyfourseven     | If set, `twentyfourseven` is `true`         |
| afacOperatingHoursSpecification | OperatingHoursSpecification | ?           |                              | Not mapped yet                              |
| afacOperatingHoursByReference   | OperatingHoursByReference   | ?           |                              | Not mapped                                  |
| afacUnknownOperatingHours       | UnknownOperatingHours       | ?           |                              | Not mapped                                  |
| afacUndefinedOperatingHours     | UndefinedOperatingHours     | ?           |                              | Not mapped                                  |


## OrganisationG

`OrganisationG` is used for `operator`, `owner`, and `helpdesk`.

| Field                                 | Type                                      | Cardinality | Mapping                | Comment                                                 |
|---------------------------------------|-------------------------------------------|-------------|------------------------|---------------------------------------------------------|
| afacAnOrganisation.name               | [MultilingualString](#MultilingualString) | ?           | operator.name          | Only used for the `operator` role                       |
| afacAnOrganisation.externalIdentifier | [ExternalIdentifier](#ExternalIdentifier) | *           | operator.emobility_uid | `operatorId` extracted via `extendedValueG`, see below  |

### Helpdesk Organisation

When used as `helpdesk`, the telephone number is extracted:

| Field                                                                                                        | Type   | Cardinality | Mapping             | Comment |
|--------------------------------------------------------------------------------------------------------------|--------|-------------|---------------------|---------|
| afacReferenceableOrganisation.organisationUnit[].contactInformation[].afacContactInformation.telephoneNumber | string | ?           | location.help_phone |         |


## ExternalIdentifier

| Field                           | Type   | Cardinality | Mapping                | Comment                                                                          |
|---------------------------------|--------|-------------|------------------------|----------------------------------------------------------------------------------|
| identifier                      | string | 1           | operator.emobility_uid | Only when `typeOfIdentifier.extendedValueG` is `operatorId` and used as operator |
| typeOfIdentifier.value          | enum   | 1           |                        | Always `extendedG`                                                               |
| typeOfIdentifier.extendedValueG | enum   | ?           |                        | e.g. `operatorId`, `operatorIdBNetzA`                                            |


# energyInfrastructureStation

An `energyInfrastructureStation` maps to a `ChargingStation`. Multiple stations can exist per site.

| Field                                  | Type                                                                        | Cardinality | Mapping                                   | Comment                                                                                       |
|----------------------------------------|-----------------------------------------------------------------------------|-------------|-------------------------------------------|-----------------------------------------------------------------------------------------------|
| idG                                    | string                                                                      | 1           | charging_station.uid                      |                                                                                               |
| versionG                               | string                                                                      | 1           |                                           | Not mapped                                                                                    |
| name                                   | [MultilingualString](#MultilingualString)                                   | ?           | charging_station.name                     |                                                                                               |
| alias                                  | [MultilingualString](#MultilingualString)                                   | *           |                                           | Not mapped                                                                                    |
| lastUpdated                            | string (datetime)                                                           | ?           | charging_station.last_updated             | Falls back to location.last_updated                                                           |
| description                            | [MultilingualString](#MultilingualString)                                   | ?           |                                           | Not mapped                                                                                    |
| additionalInformation                  | [MultilingualString](#MultilingualString)                                   | *           |                                           | Not mapped                                                                                    |
| accessibility                          | [AccessibilityEnum](#AccessibilityEnum)                                     | *           |                                           | Not mapped at station level                                                                   |
| totalMaximumPower                      | float                                                                       | 1           | charging_station.max_power.value          | Unit set to W                                                                                 |
| authenticationAndIdentificationMethods | [AuthenticationAndIdentificationEnum](#AuthenticationAndIdentificationEnum) | *           | charging_station.capabilities             | See [AuthenticationAndIdentificationEnum](#AuthenticationAndIdentificationEnum) mapping table |
| numberOfRefillPoints                   | integer                                                                     | 1           |                                           | Not mapped                                                                                    |
| userInterfaceLanguage                  | string (2)                                                                  | *           | charging_station.user_interface_languages | Stored as list                                                                                |
| externalIdentifier                     | [ExternalIdentifier](#ExternalIdentifier)                                   | *           |                                           | Not mapped, contains BNetzA identifiers                                                       |
| informationWebsite                     | UrlLink                                                                     | *           |                                           | Not mapped                                                                                    |
| photoUrl                               | UrlLink                                                                     | *           |                                           | Not mapped                                                                                    |
| photo                                  | Image                                                                       | *           |                                           | Not mapped                                                                                    |
| operatingHours                         | [OperatingHoursG](#OperatingHoursG)                                         | ?           |                                           | Not mapped at station level                                                                   |
| locationReference                      | [LocationReferenceG](#LocationReferenceG)                                   | ?           |                                           | Not mapped at station level (taken from site)                                                 |
| owner                                  | [OrganisationG](#OrganisationG)                                             | ?           |                                           | Not mapped                                                                                    |
| operator                               | [OrganisationG](#OrganisationG)                                             | ?           |                                           | Not mapped at station level (taken from site)                                                 |
| helpdesk                               | [OrganisationG](#OrganisationG)                                             | ?           |                                           | Not mapped at station level                                                                   |
| applicableForVehicles                  | VehicleCharacteristics                                                      | *           |                                           | Not mapped                                                                                    |
| dimension                              | Dimension                                                                   | ?           |                                           | Not mapped                                                                                    |
| amenities                              | [Amenities](#Amenities)                                                     | ?           | charging_station.parking_spaces           | Fallback for parking space `has_roof` / `is_illuminated`                                      |
| supplementalFacility                   | SupplementalFacilityG                                                       | *           |                                           | Not mapped                                                                                    |
| dedicatedParkingSpaces                 | [DedicatedParkingSpaces](#DedicatedParkingSpaces)                           | *           | charging_station.parking_spaces           | See [DedicatedParkingSpaces](#DedicatedParkingSpaces)                                         |
| serviceType                            | [ServiceType](#ServiceTypeEnum)                                             | *           | charging_station.service_type             | See [ServiceTypeEnum](#ServiceTypeEnum) mapping table, first match used                       |
| energyDistributor                      | [OrganisationG](#OrganisationG)                                             | ?           |                                           | Not mapped                                                                                    |
| mobilityServiceProvider                | [OrganisationG](#OrganisationG)                                             | *           |                                           | Not mapped                                                                                    |
| roamingPlatform                        | [OrganisationG](#OrganisationG)                                             | *           |                                           | Not mapped                                                                                    |
| electricEnergy                         | [ElectricEnergy](#ElectricEnergy)                                           | *           |                                           | Not mapped at station level (taken from charging point)                                       |
| refillPoint                            | [RefillPointG](#refillPoint--aegiElectricChargingPoint)                     | *           | charge_station.evses                      | Contains the charging points, see below                                                       |


# refillPoint / aegiElectricChargingPoint

A `refillPoint` wraps an `aegiElectricChargingPoint`, which maps to an `EVSE`. Each charging point represents one
physical charging outlet that can serve one vehicle at a time.

| Field                          | Type                                      | Cardinality | Mapping                      | Comment                                                                                   |
|--------------------------------|-------------------------------------------|-------------|------------------------------|-------------------------------------------------------------------------------------------|
| idG                            | string                                    | 1           | evse.uid                     | Also mapped to evse.evse_id                                                               |
| versionG                       | string                                    | 1           |                              | Not mapped                                                                                |
| name                           | [MultilingualString](#MultilingualString) | ?           |                              | Not mapped                                                                                |
| alias                          | [MultilingualString](#MultilingualString) | *           |                              | Not mapped                                                                                |
| lastUpdated                    | string (datetime)                         | ?           | evse.last_updated            | Falls back to charging_station.last_updated                                               |
| description                    | [MultilingualString](#MultilingualString) | ?           |                              | Not mapped                                                                                |
| additionalInformation          | [MultilingualString](#MultilingualString) | *           |                              | Not mapped                                                                                |
| accessibility                  | [AccessibilityEnum](#AccessibilityEnum)   | *           |                              | Not mapped                                                                                |
| deliveryUnit                   | [DeliveryUnitEnum](#DeliveryUnitEnum)     | 1           |                              | Not used by the mapper                                                                    |
| modelType                      | [MultilingualString](#MultilingualString) | ?           |                              | Not mapped                                                                                |
| reservation                    | ReservationTypeEnum                       | ?           |                              | Not mapped                                                                                |
| currentType                    | [CurrentTypeEnum](#CurrentTypeEnum)       | 1           | connector.power_type         | See [CurrentTypeEnum](#CurrentTypeEnum)                                                   |
| usageType                      | ChargingPointUsageTypeEnum                | *           |                              | Not mapped                                                                                |
| vehicleToGridCommunicationType | VehicleToGridCommunicationTypeEnum        | *           |                              | Not mapped                                                                                |
| numberOfConnectors             | integer                                   | ?           |                              | Not mapped                                                                                |
| availableVoltage               | float                                     | *           | connector.max_voltage        | Fallback when connector-level `voltage` is absent, first value used                       |
| availableChargingPower         | float                                     | *           | connector.max_electric_power | Fallback when connector-level `maxPowerAtSocket` is 0, first value used, cast to int      |
| chargingMode                   | ChargingModeEnum                          | ?           |                              | Not mapped                                                                                |
| smartRechargingServices        | SmartRechargingServicesEnum               | *           |                              | Not mapped                                                                                |
| externalIdentifier             | [ExternalIdentifier](#ExternalIdentifier) | *           |                              | Not mapped                                                                                |
| informationWebsite             | UrlLink                                   | *           |                              | Not mapped                                                                                |
| photoUrl                       | UrlLink                                   | *           |                              | Not mapped                                                                                |
| photo                          | Image                                     | *           |                              | Not mapped                                                                                |
| operatingHours                 | [OperatingHoursG](#OperatingHoursG)       | ?           |                              | Not mapped at charging point level                                                        |
| locationReference              | [LocationReferenceG](#LocationReferenceG) | ?           |                              | Not mapped at charging point level                                                        |
| owner                          | [OrganisationG](#OrganisationG)           | ?           |                              | Not mapped                                                                                |
| operator                       | [OrganisationG](#OrganisationG)           | ?           |                              | Not mapped                                                                                |
| helpdesk                       | [OrganisationG](#OrganisationG)           | ?           |                              | Not mapped                                                                                |
| applicableForVehicles          | VehicleCharacteristics                    | *           |                              | Not mapped                                                                                |
| dimension                      | Dimension                                 | ?           |                              | Not mapped                                                                                |
| amenities                      | Amenities                                 | ?           |                              | Not mapped                                                                                |
| supplementalFacility           | SupplementalFacilityG                     | *           |                              | Not mapped                                                                                |
| dedicatedParkingSpaces         | DedicatedParkingSpaces                    | *           |                              | Not mapped                                                                                |
| connector                      | [Connector](#connector)                   | *           | evse.connectors              |                                                                                           |
| electricEnergy                 | [ElectricEnergy](#ElectricEnergy)         | *           |                              | Contains energy mix and tariff info, see below                                            |


## CurrentTypeEnum

The `currentType` at the `aegiElectricChargingPoint` level is used to derive the `connector.power_type`.

| Key       | Mapping                  | Comment                                        |
|-----------|--------------------------|------------------------------------------------|
| dc        | DC                       |                                                |
| ac        | AC_1_PHASE or AC_3_PHASE | Depends on connector standard, see logic below |
| extendedG | AC_3_PHASE               |                                                |

**Power type derivation logic**: If the current type is `ac`, connectors with 1-phase standards (e.g. domestic sockets,
`IEC_60309_2_single_16`) are mapped to `AC_1_PHASE`, all others to `AC_3_PHASE`.


## DeliveryUnitEnum

The `deliveryUnit` at the `aegiElectricChargingPoint` level indicates the metering unit. It is not used by the mapper.

| Key       | Comment                                  |
|-----------|------------------------------------------|
| kWh       | Energy delivered in kilowatt-hours       |
| extendedG | Extended value                           |


# connector

A `connector` maps to a `Connector`. Multiple connectors can exist per charging point.

| Field                   | Type                                      | Cardinality | Mapping                      | Comment                                                                 |
|-------------------------|-------------------------------------------|-------------|------------------------------|-------------------------------------------------------------------------|
| connectorType           | [ConnectorTypeEnum](#ConnectorTypeEnum)   | 1           | connector.standard           | See mapping table below                                                 |
| otherConnector          | string                                    | ?           |                              | Not mapped                                                              |
| countryOfDomesticSocket | string (2)                                | *           |                              | Not mapped                                                              |
| connectorFormat         | ConnectorFormatTypeEnum                   | ?           |                              | Not mapped, derived from power type instead                             |
| maxPowerAtSocket        | float                                     | 1           | connector.max_electric_power | Cast to int                                                             |
| voltage                 | float                                     | ?           | connector.max_voltage        | Cast to int                                                             |
| maximumCurrent          | float                                     | ?           | connector.max_amperage       | Cast to int                                                             |
| externalIdentifier      | [ExternalIdentifier](#ExternalIdentifier) | *           |                              | Not mapped                                                              |
| (derived)               |                                           |             | connector.uid                | Set to connector index (0, 1, 2, ...)                                   |
| (derived)               |                                           |             | connector.format             | `CABLE` for DC, `SOCKET` for AC                                         |
| (derived)               |                                           |             | connector.power_type         | Derived from [CurrentTypeEnum](#CurrentTypeEnum) and connector standard |
| (derived)               |                                           |             | connector.max_amperage       | If absent, derived as `max_electric_power / max_voltage`                |
| (derived)               |                                           |             | connector.last_updated       | Falls back to evse.last_updated                                         |


## ConnectorTypeEnum

DATEX II `connectorType` maps to OCPI `ConnectorType`.

| Key                    | Mapping                    |
|------------------------|----------------------------|
| cee3                   | IEC_60309_2_single_16      |
| cee5                   | IEC_60309_2_three_32       |
| chademo                | CHADEMO                    |
| domesticA              | DOMESTIC_A                 |
| domesticB              | DOMESTIC_B                 |
| domesticC              | DOMESTIC_C                 |
| domesticD              | DOMESTIC_D                 |
| domesticE              | DOMESTIC_E                 |
| domesticF              | DOMESTIC_F                 |
| domesticG              | DOMESTIC_G                 |
| domesticH              | DOMESTIC_H                 |
| domesticI              | DOMESTIC_I                 |
| domesticJ              | DOMESTIC_J                 |
| domesticK              | DOMESTIC_K                 |
| domesticL              | DOMESTIC_L                 |
| iec60309x2three16      | IEC_60309_2_three_16       |
| iec60309x2three32      | IEC_60309_2_three_32       |
| iec60309x2three64      | IEC_60309_2_three_64       |
| iec60309x2single16     | IEC_60309_2_single_16      |
| iec62196T1             | IEC_62196_T1               |
| iec62196T1COMBO        | IEC_62196_T1_COMBO         |
| iec62196T2             | IEC_62196_T2               |
| iec62196T2COMBO        | IEC_62196_T2_COMBO         |
| pantographBottomUp     | PANTOGRAPH_BOTTOM_UP       |
| pantographTopDown      | PANTOGRAPH_TOP_DOWN        |
| teslaConnectorEurope   | TESLA_S                    |
| teslaConnectorAmerica  | TESLA_S                    |
| teslaR                 | TESLA_R                    |
| teslaS                 | TESLA_S                    |
| yazaki                 |                            |
| domestic               |                            |
| domesticM              |                            |
| domesticN              |                            |
| domesticO              |                            |
| iec62196T3A            |                            |
| iec62196T3C            |                            |
| mcs                    |                            |
| other                  |                            |
| extendedG              |                            |


# ElectricEnergy

The `electricEnergy` provides energy product, energy mix, and pricing information. It is available at station and
charging point level. Energy mix is mapped at the charging point level to the location. Tariff information is mapped at
the charging point level to the EVSE.

| Field                     | Type                                      | Cardinality | Mapping                    | Comment                                          |
|---------------------------|-------------------------------------------|-------------|----------------------------|--------------------------------------------------|
| energyProductName         | [MultilingualString](#MultilingualString) | ?           |                            | Not mapped                                       |
| isGreenEnergy             | boolean                                   | ?           | energy_mix.is_green_energy | Mapped to location.energy_mix                    |
| carbonDioxideImpact       | float                                     | ?           |                            | Not mapped                                       |
| nuclearWasteImpact        | float                                     | ?           |                            | Not mapped                                       |
| energyProductInformation  | string                                    | ?           |                            | Not mapped                                       |
| renewableEnergyEvidence   | string                                    | ?           |                            | Not mapped                                       |
| mobilityServiceProvider   | OrganisationG                             | *           |                            | Not mapped                                       |
| energyRate                | [EnergyRate](#EnergyRate)                 | *           | evse.tariff_association    | Mapped to tariffs, see [EnergyRate](#EnergyRate) |


## EnergyRate

An `EnergyRate` maps to a `TariffUpdate` and a `TariffAssociationUpdate` on the EVSE level. The tariff UID is composed
as `{evse.uid}:{energyRate.idG}`.

| Field                     | Type                                      | Cardinality | Mapping                                                                                  | Comment                                                             |
|---------------------------|-------------------------------------------|-------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| idG                       | string                                    | 1           | tariff.uid (partial)                                                                     | Combined with evse.uid to form `{evse.uid}:{idG}`                  |
| ratePolicy                | [RatePolicyEnum](#RatePolicyEnum)         | 1           | tariff.type, tariff_association.audience                                                 | See [RatePolicyEnum](#RatePolicyEnum) mapping tables                |
| lastUpdated               | string (datetime)                         | 1           | tariff.last_updated, tariff_association.last_updated, tariff_association.start_date_time  |                                                                     |
| applicableCurrency        | string (3)                                | *           | tariff.currency                                                                          | First entry used, e.g. `EUR`                                        |
| rateName                  | [MultilingualString](#MultilingualString) | ?           |                                                                                          | Not mapped                                                          |
| combinationWithParkingFee | boolean                                   | ?           |                                                                                          | Not mapped                                                          |
| maximumDeliveryFee        | float                                     | ?           |                                                                                          | Not mapped                                                          |
| minimumDeliveryFee        | float                                     | ?           |                                                                                          | Not mapped                                                          |
| discount                  | float                                     | ?           |                                                                                          | Not mapped                                                          |
| additionalInformation     | [MultilingualString](#MultilingualString) | ?           |                                                                                          | Not mapped                                                          |
| payment                   | [Payment](#Payment)                       | ?           |                                                                                          | Not mapped                                                          |
| energyPrice               | [EnergyPrice](#EnergyPrice)               | *           | tariff.elements                                                                          | Each price maps to a TariffElement, see [EnergyPrice](#EnergyPrice) |
| overallPeriod             | OverallPeriod                             | ?           |                                                                                          | Not mapped                                                          |


## RatePolicyEnum

DATEX II `ratePolicy` maps to both `TariffType` and `TariffAudience`.

**TariffType mapping:**

| Key       | Mapping          |
|-----------|------------------|
| adHoc     | AD_HOC_PAYMENT   |
| contract  | REGULAR          |
| extendedG |                  |

**TariffAudience mapping:**

| Key       | Mapping          |
|-----------|------------------|
| adHoc     | AD_HOC_PAYMENT   |
| contract  | EMSP_CONTRACT    |
| extendedG |                  |


## EnergyPrice

An `EnergyPrice` maps to a `TariffElementUpdate` containing a `PriceComponentUpdate`.

| Field                    | Type                                                  | Cardinality | Mapping                             | Comment                                              |
|--------------------------|-------------------------------------------------------|-------------|-------------------------------------|------------------------------------------------------|
| priceType                | [PriceTypeEnum](#PriceTypeEnum)                       | 1           | tariff_element.price_component.type | See [PriceTypeEnum](#PriceTypeEnum) mapping table    |
| value                    | float                                                 | 1           | tariff_element.price_component.price | Stored as Decimal                                   |
| priceCap                 | float                                                 | ?           |                                     | Not mapped                                           |
| taxIncluded              | boolean                                               | ?           |                                     | Not mapped                                           |
| taxRate                  | float                                                 | ?           | tariff_element.price_component.taxes | Stored as TaxPercentage with name `VAT`             |
| additionalInformation    | [MultilingualString](#MultilingualString)             | ?           |                                     | Not mapped                                           |
| overallPeriod            | OverallPeriod                                         | ?           |                                     | Not mapped                                           |
| timeBasedApplicability   | [TimeBasedApplicability](#TimeBasedApplicability)     | ?           | tariff_element.restrictions         | See [TimeBasedApplicability](#TimeBasedApplicability) |
| energyBasedApplicability | EnergyBasedApplicability                              | ?           |                                     | Not mapped                                           |


## PriceTypeEnum

DATEX II `priceType` maps to `TariffDimensionType`.

| Key            | Mapping |
|----------------|---------|
| pricePerKWh    | ENERGY  |
| pricePerMinute | TIME    |
| basePrice      | FLAT    |
| flatRate       | FLAT    |
| free           |         |
| other          |         |
| extendedG      |         |


## TimeBasedApplicability

The `timeBasedApplicability` maps to `RestrictionsUpdate` on the tariff element. Values are in minutes and converted to
seconds.

| Field      | Type    | Cardinality | Mapping                              | Comment                                    |
|------------|---------|-------------|--------------------------------------|--------------------------------------------|
| fromMinute | integer | ?           | tariff_element.restrictions.min_duration | Converted: minutes * 60 = seconds     |
| toMinute   | integer | ?           | tariff_element.restrictions.max_duration | Converted: minutes * 60 = seconds     |


## Payment

| Field        | Type            | Cardinality | Mapping | Comment                                      |
|--------------|-----------------|-------------|---------|----------------------------------------------|
| paymentMeans | MeansOfPayment  | *           |         | Not mapped, e.g. `nfc`, `website`            |
| paymentMode  | PaymentModeEnum | *           |         | Not mapped                                   |


# DedicatedParkingSpaces

`DedicatedParkingSpaces` maps to `ParkingSpaceUpdate` at both the site level (-> `location.parking_spaces`) and the
station level (-> `charging_station.parking_spaces`). Parking spaces with identical properties (vehicle types,
dimensions, amenities, accessibility) are deduplicated by summing their counts.

| Field                | Type                                                            | Cardinality | Mapping                           | Comment                                                                       |
|----------------------|-----------------------------------------------------------------|-------------|-----------------------------------|-------------------------------------------------------------------------------|
| numberOfSpaces       | integer                                                         | 1           | parking_space.parking_space_count |                                                                               |
| applicableForVehicles| [VehicleCharacteristics](#VehicleCharacteristics)               | *           | parking_space.vehicle_types       | EU vehicle categories mapped, see [EuVehicleCategoryEnum](#EuVehicleCategoryEnum) |
| accessibility        | [AccessibilityEnum](#AccessibilityEnum)                         | *           | parking_space.is_accessible       | `true` if any accessible value present, see below                             |
| amenities            | [Amenities](#Amenities)                                         | ?           | parking_space.has_roof, parking_space.is_illuminated | Per-space amenities, falls back to site/station amenities   |


## VehicleCharacteristics

Vehicle characteristics provide vehicle type categories and dimension constraints for dedicated parking spaces.

| Field                                                        | Type                                                      | Cardinality | Mapping                       | Comment                                              |
|--------------------------------------------------------------|-----------------------------------------------------------|-------------|-------------------------------|------------------------------------------------------|
| comVehicleCharacteristicsExtensionG.VehicleCharacteristicsExtended.euVehicleCategory | [EuVehicleCategoryEnum](#EuVehicleCategoryEnum) | * | parking_space.vehicle_types | See mapping table below                     |
| grossWeightCharacteristic[].grossVehicleWeight               | float                                                     | ?           | parking_space.max_weight      | Converted: tonnes * 1000 = kg                        |
| heightCharacteristic[].vehicleHeight                         | float                                                     | ?           | parking_space.max_height      | Converted: metres * 100 = cm                         |
| lengthCharacteristic[].vehicleLength                         | float                                                     | ?           | parking_space.max_length      | Converted: metres * 100 = cm                         |
| widthCharacteristic[].vehicleWidth                           | float                                                     | ?           | parking_space.max_width       | Converted: metres * 100 = cm                         |


## EuVehicleCategoryEnum

DATEX II EU vehicle categories map to `VehicleCategoryEnum`. N1 sub-classes all map to `N1`.

| Key              | Mapping |
|------------------|---------|
| l1               | L1      |
| l2               | L2      |
| l3               | L3      |
| l4               | L4      |
| l5               | L5      |
| l6               | L6      |
| l7               | L7      |
| m                | M       |
| m1               | M1      |
| m2               | M2      |
| m3               | M3      |
| n                | N       |
| n1               | N1      |
| n1ClassI         | N1      |
| n1ClassII        | N1      |
| n1ClassIII       | N1      |
| n1ClassIIIAndN2  | N1      |
| n2               | N2      |
| n3               | N3      |
| o                | O       |
| o1               | O1      |
| o2               | O2      |
| o3               | O3      |
| o4               | O4      |
| r1               | R1      |
| r2               | R2      |
| r3               | R3      |
| r4               | R4      |
| t1               | T1      |
| t2               | T2      |
| t3               | T3      |
| t4               | T4      |
| t41              | T41     |
| t42              | T42     |
| t43              | T43     |


## Amenities

`Amenities` provides facility information for parking spaces. Used at site, station, and per-parking-space level.
Per-parking-space amenities take precedence; site/station amenities are used as fallback.

| Field       | Type    | Cardinality | Mapping                       | Comment |
|-------------|---------|-------------|-------------------------------|---------|
| roofed      | boolean | ?           | parking_space.has_roof        |         |
| illuminated | boolean | ?           | parking_space.is_illuminated  |         |


## AccessibilityEnum

Used within `DedicatedParkingSpaces` to determine if parking spaces are accessible.

| Key                      | Sets `is_accessible` |
|--------------------------|----------------------|
| barrierFreeAccessible    | true                 |
| disabilityAccessible     | true                 |
| wheelchairAccessible     | true                 |
| none                     |                      |
| extendedG                |                      |


# MultilingualString

A `MultilingualString` contains language-tagged values. The first value is used.

| Field          | Type       | Cardinality | Comment                                  |
|----------------|------------|-------------|------------------------------------------|
| values[].lang  | string (2) | 1           | 2-character language code, e.g. `de`     |
| values[].value | string     | 1           | The actual text value                    |


# AuthenticationAndIdentificationEnum

DATEX II `authenticationAndIdentificationMethods` maps to OCPI `Capability`. Multiple methods can map to the same
capability; duplicates are deduplicated.

| Key             | Mapping                    | Comment                    |
|-----------------|----------------------------|----------------------------|
| creditCard      | CREDIT_CARD_PAYABLE        |                            |
| debitCard       | DEBIT_CARD_PAYABLE         |                            |
| mifareClassic   | RFID_READER                |                            |
| mifareDesfire   | RFID_READER                |                            |
| rfid            | RFID_READER                |                            |
| activeRFIDChip  | RFID_READER                |                            |
| nfc             | CONTACTLESS_CARD_SUPPORT   |                            |
| overTheAir      | REMOTE_START_STOP_CAPABLE  |                            |
| apps            | REMOTE_START_STOP_CAPABLE  |                            |
| plc             | IEC15118                   |                            |
| cashPayment     | CASH                       |                            |
| pinpad          | PED_TERMINAL               |                            |
| calypso         | CHIP_CARD_SUPPORT          |                            |
| phoneSMS        |                            | Not mapped                 |
| phoneDialog     |                            | Not mapped                 |
| prepaidCard     |                            | Not mapped                 |
| website         |                            | Not mapped                 |
| unlimitedAccess |                            | Not mapped                 |
| noAccess        |                            | Not mapped                 |
| extendedG       |                            | Not mapped                 |


# ServiceTypeEnum

DATEX II `serviceType` maps to `ServiceType`. The first matching entry from the list is used.

| Key                | Mapping              |
|--------------------|----------------------|
| physicalAttendance | PHYSICAL_ATTENDANCE  |
| unattended         | UNATTENDED           |
| extendedG          |                      |


# EnergyInfrastructureSiteTypeEnum

Not mapped. Available values:

| Key              |
|------------------|
| inBuilding       |
| openSpace        |
| onStreet         |
| onCompanySite    |


---

# Realtime Data

## refillPointStatus

A `refillPointStatus` (within `energyInfrastructureStationStatus`) maps to an `EvseRealtimeUpdate`. The mapper tries
`aegiRefillPointStatus` first, falling back to `aegiElectricChargingPointStatus`. Both share the same structure for the
fields used in the mapping.

| Field                           | Type                                              | Cardinality | Mapping     | Comment                                       |
|---------------------------------|---------------------------------------------------|-------------|-------------|-----------------------------------------------|
| aegiRefillPointStatus           | [RefillPointStatus](#RefillPointStatus)           | ?           |             | Primary source, see below                     |
| aegiElectricChargingPointStatus | [ElectricChargingPointStatus](#RefillPointStatus) | ?           |             | Fallback if `aegiRefillPointStatus` is absent |


## RefillPointStatus

Both `RefillPointStatusInput` and `ElectricChargingPointStatusInput` share these mapped fields.

| Field                    | Type                                                     | Cardinality | Mapping                | Comment                              |
|--------------------------|----------------------------------------------------------|-------------|------------------------|--------------------------------------|
| reference.idG            | string                                                   | 1           | evse.uid, evse.evse_id | References the static EVSE by its ID |
| status                   | [RefillPointStatusEnum](#RefillPointStatusEnum-realtime) | 1           | evse.status            | See mapping table below              |
| lastUpdated              | string (datetime)                                        | ?           | evse.last_updated      |                                      |
| openingStatus            | OpeningStatusEnum                                        | ?           |                        | Not mapped                           |
| operationStatus          | OperationStatusEnum                                      | ?           |                        | Not mapped                           |
| statusDescription        | [MultilingualString](#MultilingualString)                | ?           |                        | Not mapped                           |
| fault                    | Fault                                                    | ?           |                        | Not mapped                           |
| newOperatingHours        | OperatingHoursG                                          | ?           |                        | Not mapped                           |
| energyRateUpdate         | EnergyRateUpdate                                         | *           |                        | Not mapped                           |
| waitingTime              | DurationValue                                            | ?           |                        | Not mapped                           |
| plannedRefillPointStatus | PlannedRefillPointStatus                                 | *           |                        | Not mapped                           |

`ElectricChargingPointStatusInput` additionally has these unmapped fields:

| Field                        | Type    | Cardinality | Mapping | Comment    |
|------------------------------|---------|-------------|---------|------------|
| remainingChargingTime        | float   | ?           |         | Not mapped |
| currentVoltage               | float   | ?           |         | Not mapped |
| currentChargingPower         | float   | ?           |         | Not mapped |
| nextAvailableChargingSlots   | string  | *           |         | Not mapped |


## RefillPointStatusEnum (realtime)

DATEX II `refillPointStatus.status` maps to OCPI `EvseStatus`.

| Key          | Mapping      | Comment                           |
|--------------|--------------|-----------------------------------|
| available    | AVAILABLE    |                                   |
| blocked      | BLOCKED      |                                   |
| charging     | CHARGING     |                                   |
| faulted      | OUTOFORDER   | Treated as out of order           |
| inoperative  | INOPERATIVE  |                                   |
| occupied     | CHARGING     | Treated as charging               |
| outOfOrder   | OUTOFORDER   |                                   |
| outOfStock   | OUTOFORDER   | Treated as out of order           |
| planned      | PLANNED      |                                   |
| removed      | REMOVED      |                                   |
| reserved     | RESERVED     |                                   |
| unavailable  | INOPERATIVE  | Treated as inoperative            |
| unknown      | UNKNOWN      |                                   |
| extendedG    |              | Not mapped (returns `None`)       |
