# Schema Differences: v3.5 vs v3.7

This document describes the differences between the DATEX II v3.7 generic schema (`docs/schema/v3_7/json`) and the
German v3.5 schema (`docs/schema/v3_5/json`).

## General

### File naming

| v3.7                                  | v3.5                                      |
|---------------------------------------|-------------------------------------------|
| `DATEXII_3_EnergyInfrastructure.json` | `DATEXII_3_AfirEnergyInfrastructure.json` |
| `DATEXII_3_Facilities.json`           | `DATEXII_3_AfirFacilities.json`           |
| `DATEXII_3_CommonExtension.json`      | `DATEXII_3_CommonExtension.json`          |
| `DATEXII_3_Common.json`               | `DATEXII_3_Common.json`                   |
| `DATEXII_3_D2Payload.json`            | `DATEXII_3_D2Payload.json`                |
| `DATEXII_3_LocationExtension.json`    | `DATEXII_3_LocationExtension.json`        |
| `DATEXII_3_LocationReferencing.json`  | `DATEXII_3_LocationReferencing.json`      |

### JSON Schema definition keyword

Both use `$schema: https://json-schema.org/draft/2020-12/schema`, but the container key differs:

- v3.7: `$defs` (2020-12 standard)
- v3.5: `definitions` (older draft-07 convention)

All `$ref` paths differ accordingly (`#/$defs/Foo` vs `#/definitions/Foo`).

### Property prefix conventions

| v3.7  | v3.5           | Context                                               |
|-------|----------------|-------------------------------------------------------|
| `egi` | `aegi`         | EnergyInfrastructure extension/polymorphic properties |
| `fac` | `afac`         | Facilities extension/polymorphic properties           |

Examples: `egiConnectorExtensionG` vs `aegiConnectorExtensionG`, `facOpenAllHours` vs `afacOpenAllHours`,
`egiElectricChargingPoint` vs `aegiElectricChargingPoint`, `facOrganisationSpecification` vs
`afacAnOrganisation`.

### Extension type pattern

v3.7 uses typed extension points (`LocationReferenceExtensionTypeG`, `NamedAreaExtensionTypeG`,
`DayWeekMonthExtensionTypeG`, `PeriodExtensionTypeG`) that restrict extensions to specific structures.
v3.5 uses the generic `ExtensionTypeG` (open-ended `additionalProperties: true`) on those same fields,
or places a `LocationExtensionTypeG` on a different extension property (`locLocationExtensionG`).

---

## D2Payload

Structurally identical apart from `$defs` vs `definitions`.

---

## Common (PayloadPublicationG)

### PayloadPublicationG

| Property                  | v3.7                                      | v3.5                                       |
|---------------------------|-------------------------------------------|--------------------------------------------|
| `versionG` default        | `"3.7"`                                   | `"3.5"`                                    |
| `profileNameG` default    | none                                      | `"AFIR Energy InfrastructureG"`            |
| `profileVersionG` default | none                                      | `"01-00-00G"`                              |
| Publication property name | `egiEnergyInfrastructureTablePublication` | `aegiEnergyInfrastructureTablePublication` |
| Publication `$ref` target | `DATEXII_3_EnergyInfrastructure.json`     | `DATEXII_3_AfirEnergyInfrastructure.json`  |

### Definitions only in v3.7 Common (45)

Measurement/data value types: `ConcentrationKilogramsPerCubicMetre`, `ConcentrationMicrogramsPerCubicMetre`,
`CubicMetres`, `Hectopascal`, `Integer`, `IntensityKilogramsPerSquareMetre`, `IntensityMillimetresPerHour`,
`MetresPerSecond`, `TemperatureCelsius`, `VehiclesPerHour`, `ApplicationRateValue`, `DirectionBearingValue`,
`DirectionCompassValue`, `FloatingPointMetreDistanceValue`, `FrictionValue`, `IntegerMetreDistanceValue`,
`KilogramsConcentrationValue`, `MicrogramsConcentrationValue`, `PercentageValue`,
`PrecipitationIntensityValue`, `PressureValue`, `TemperatureBelowOrAboveRoadSurface`, `TemperatureValue`,
`VehicleFlowValue`, `WindSpeedValue`.

Enum types: `DangerousGoodsRegulationsEnum`/`G`, `DirectionCompassEnum`/`G`, `ValidityStatusEnum`/`G`.

Typed enum extensions: `FuelTypeEnumExtensionTypeG`, `LoadTypeEnumExtensionTypeG`,
`VehicleEquipmentEnumExtensionTypeG`, `VehicleTypeEnumExtensionTypeG`, `VehicleUsageEnumExtensionTypeG`,
`WeightTypeEnumExtensionTypeG`.

Complex types: `AxleSpacing`, `AxleWeight`, `DataValueG`, `HazardousMaterials`, `HazardousMaterialsG`,
`Validity`.

Extension types: `DayWeekMonthExtensionTypeG`, `PeriodExtensionTypeG`.

### Definitions only in v3.5 Common (10)

`Base64Binary`, `ConfidentialityValueEnum`/`G`, `HeaderInformation`, `InformationStatusEnum`/`G`,
`LongString`, `UrlLink`, `UrlLinkTypeEnum`/`G`.

### Property differences in shared definitions

**Time**: v3.7 uses regex `pattern`; v3.5 uses `"format": "time"`.

**Enum extension wrappers** (`FuelTypeEnumG`, `LoadTypeEnumG`, `VehicleEquipmentEnumG`, `VehicleTypeEnumG`,
`VehicleUsageEnumG`, `WeightTypeEnumG`): v3.7 restricts `extendedValueG` to typed `*ExtensionTypeG` refs;
v3.5 allows any string.

**CalendarWeekWithinMonth, DayWeekMonth, InstanceOfDayWithinMonth**: `comDayWeekMonthExtensionG` refs
`DayWeekMonthExtensionTypeG` in v3.7 vs generic `ExtensionTypeG` in v3.5.

**Period**: `comPeriodExtensionG` refs `PeriodExtensionTypeG` in v3.7 vs generic `ExtensionTypeG` in
v3.5.

---

## EnergyInfrastructure / AfirEnergyInfrastructure

### Definitions only in v3.7 (6)

`ElectricEnergyMix`, `ElectricEnergySourceRatio`, `ElectricEnergySourceTypeEnum`/`G`,
`EnergyPricingPolicy`, `PricingPolicyEnum`/`G`.

### Definitions only in v3.5 (26)

`ChargingPointUsageTypeEnum`/`G`, `CurrentTypeEnum`/`G`, `DedicatedParkingSpaces`,
`DeliveryUnitEnum`/`G`, `ElectricChargingEquipment`, `ElectricEnergy`, `EnergyBasedApplicability`,
`EnergyInfrastructureSiteTypeEnum`/`G`, `EnergyPrice`, `EnergyRate`, `EnergyRateReferenceG`,
`GramsPerKilowattHour`, `PriceTypeEnum`/`G`, `RatePolicyEnum`/`G`, `ServiceType`,
`ServiceTypeEnum`/`G`, `SmartRechargingServicesEnum`/`G`, `TimeBasedApplicability`,
`VehicleToGridCommunicationTypeEnum`/`G`.

### EnergyInfrastructureTablePublication

v3.5 adds `headerInformation` (HeaderInformation).

### EnergyInfrastructureTable

v3.5 adds `tableName` (String).

### EnergyInfrastructureSite

Properties only in v3.5: `alias`, `description`, `accessibility`, `additionalInformation`,
`typeOfSite`, `exclusiveUsers`, `preferredUsers`, `externalIdentifier` (array of ExternalIdentifier objects),
`informationWebsite`, `photoUrl`, `photo`, `helpdesk`, `applicableForVehicles`, `dimension`, `amenities`,
`dedicatedParkingSpaces`, `serviceType`, `exit`, `energyDistributor`, `mobilityServiceProvider`,
`roamingPlatfom`.

v3.7 has `rates` (RatesG) and `externalIdentifier` as a simple String; v3.5 handles rates through
EnergyRate at station/point level and uses typed ExternalIdentifier objects.

v3.7 uses `name` directly; v3.5 uses `additionalInformation` for display name and has a separate
`name` field.

### EnergyInfrastructureStation

Properties only in v3.5: `alias`, `description`, `accessibility`, `additionalInformation`,
`totalMaximumPower` (required), `numberOfRefillPoints` (required), `refillPointByReference`,
`userInterfaceLanguage`, `externalIdentifier`, `informationWebsite`, `photoUrl`, `photo`, `helpdesk`,
`applicableForVehicles`, `dimension`, `amenities`, `dedicatedParkingSpaces`, `energyDistributor`,
`mobilityServiceProvider`, `roamingPlatform`, `serviceType` (required), `electricEnergy`.

v3.7 has `energyProvider` (OrganisationG) and `rates` (RatesG) instead.

Required fields differ:

- v3.7: `idG`, `versionG`
- v3.5: `idG`, `versionG`, `totalMaximumPower`, `numberOfRefillPoints`, `serviceType`

### ElectricChargingPoint

Properties only in v3.5: `alias`, `description`, `accessibility`, `additionalInformation`,
`deliveryUnit` (required), `modelType`, `reservation`, `currentType` (required), `usageType`,
`vehicleToGridCommunicationType`, `numberOfConnectors`, `chargingMode` (moved here from Connector),
`smartRechargingServices`, `otherSmartRechargingServices`, `externalIdentifier`, `informationWebsite`,
`photoUrl`, `photo`, `helpdesk`, `applicableForVehicles`, `dimension`, `amenities`,
`supplementalFacility`, `dedicatedParkingSpaces`, `electricEnergy`.

v3.7 has `electricEnergyMix`; v3.5 replaces this with `electricEnergy` (different structure).

Required fields differ:

- v3.7: `idG`, `versionG`
- v3.5: `idG`, `versionG`, `deliveryUnit`, `currentType`

### Connector

Properties only in v3.5: `otherConnector`, `countryOfDomesticSocket`, `externalIdentifier`.

v3.7 has `chargingMode` on Connector; v3.5 moves it to ElectricChargingPoint.

### RefillPointG

Polymorphic property name: `egiElectricChargingPoint` (v3.7) vs `aegiElectricChargingPoint`
(v3.5).

### ConnectorTypeEnum

v3.5 adds `mcs` (Megawatt Charging System).

### AuthenticationAndIdentificationEnum

Identical in both schemas.

---

## Facilities / AfirFacilities

### Definitions only in v3.7 (38+)

Rate/pricing system: `AmountInCurrency`, `BrandsAcceptedCodeList`, `BrandsAcceptedText`, `FreeOfCharge`,
`GeneralRateInformation`, `RatesG`, `RateTable`, `RateTableVersionedReferenceG`, `RateLineCollection`,
`RateLineCollectionG`, `RateLine`, `RateLineTax`, `RateLineTypeEnum`/`G`, `RateTypeEnum`/`G`,
`RateUsageConditionsTypeEnum`/`G`, `RateMatrixVersionedReferenceG`, `RatesByReference`,
`RateAvailabilityTypeEnum`/`G`, `RateDiscount`, `RateEligibility`, `RelativeTimeRates`, `Surcharge`,
`SurchargeTypeEnum`/`G`, `UnknownRates`, `UnspecifiedRates`, `RefundTypeEnum`/`G`.

Organisation: `OrganisationSpecification`, `OrganisationVersionedReferenceG`.

Other: `Credential`, `CredentialAssigned`, `CredentialG`, `CredentialTypeEnum`/`G`, `Duration`,
`Eligibility`, `EnergySourceEnum`/`G`, `PaymentMethod`, `PaymentTimingEnum`/`G`, `Qualification`,
`RightSpecification`, `RightTypeEnum`/`G`, `UserQualification`.

### Definitions only in v3.5 (32+)

Organisation: `AnOrganisation`, `AnOrganisationG`, `ReferenceableOrganisation`,
`ReferenceableOrganisationVersionedReferenceG`, `OrganisationByReference`,
`OrganisationTableVersionedReferenceG`, `OrganisationTypeEnum`/`G`, `UndefinedOrganisation`,
`UnknownOrganisation`.

Facility extensions: `AccessibilityEnum`/`G`, `Amenities`, `AvailabilityEnum`/`G`, `Dimension`,
`EquipmentTypeEnum`/`G`, `Image`, `ImageFormatEnum`/`G`, `Payment`, `PaymentModeEnum`/`G`,
`ReservationTypeEnum`/`G`, `ServiceFacilityTypeEnum`/`G`, `SquareMetres`, `SupplementalEquipment`,
`SupplementalServiceFacility`.

Other: `ExternalIdentifier`, `TypeOfIdentifierEnum`, `TypeOfIdentifierEnumExtensionTypeG`,
`TypeOfIdentifierEnumG`.

### OrganisationG (major restructuring)

v3.7 has one option: `facOrganisationSpecification` -> `OrganisationSpecification` (requires `name` and
`organisationUnit` with minItems 1).

v3.5 has five options: `afacAnOrganisation` -> `AnOrganisation`, `afacReferenceableOrganisation` ->
`ReferenceableOrganisation`, `afacUndefinedOrganisation`, `afacUnknownOrganisation`,
`afacOrganisationByReference`. `AnOrganisation` requires only `name` and has richer properties
(linkToLogo, linkToWebform, available24hours, responsibility, publishingAgreement, type,
vatIdentificationNumber, etc.). `ReferenceableOrganisation` adds `idG`/`versionG`.

### SupplementalFacilityG

v3.7: empty object (no properties).

v3.5: three options (`afacSupplementalServiceFacility`, `afacSupplementalEquipment`,
`aegiElectricChargingEquipment`).

### FacilityObjectG

v3.7: 3 options (`egiElectricChargingPoint`, `egiEnergyInfrastructureStation`,
`egiEnergyInfrastructureSite`).

v3.5: 7 options (adds `aegiDedicatedParkingSpaces`, `afacSupplementalServiceFacility`,
`afacSupplementalEquipment`, `aegiElectricChargingEquipment`).

### OperatingHoursG

Property names: `facOpenAllHours` vs `afacOpenAllHours`, `facOperatingHoursSpecification` vs
`afacOperatingHoursSpecification`, etc.

### ContactInformationG

Property names: `facContactInformation` vs `afacContactInformation`, `facContactPerson` vs
`afacContactPerson`.

### MeansOfPaymentEnum

v3.5 adds: `nfc`, `emv`, `qrCode`, `website`.

### UserTypeEnum

v3.7 has `pregnantWomen`; v3.5 replaces it with `pregnantPerson` and adds
`personsWithDisabilities`.

---

## Rates/Pricing (major architectural difference)

v3.7 uses a generic rate table system from the Facilities layer: `RatesG` -> `RateTable` ->
`RateLineCollection` -> `RateLine`. `EnergyPricingPolicy` with `PricingPolicyEnum` (pricePerChargingTime,
pricePerDeliveryUnit, contract, flatRate). Rates attach to ElectricChargingPoint,
EnergyInfrastructureStation, and EnergyInfrastructureSite.

v3.5 replaces this with energy-specific pricing: `EnergyRate` (idG, ratePolicy,
applicableCurrency, rateName, etc.) with `EnergyPrice` and `PriceTypeEnum` (pricePerMinute, pricePerKWh,
basePrice, flatRate, free, other). Time-based (`TimeBasedApplicability`: fromMinute/toMinute) and
energy-based (`EnergyBasedApplicability`: fromKWh/toKWh) ranges. `Payment` object with `paymentMode`,
`paymentMeans`, `brandsAccepted`. Rates attach via `electricEnergy` arrays on ElectricChargingPoint and
EnergyInfrastructureStation.

---

## Energy mix (conceptual replacement)

v3.7 `ElectricEnergyMix`: `energyMixIndex` (required), `isGreenEnergy`, `electricEnergySourceRatio`
(array with per-source-type ratios: biogas, coal, gas, nuclear, solar, water, wind, generalGreen,
generalFossil, other), `energyProvider`, `rates`.

v3.5 `ElectricEnergy`: `energyProductName`, `isGreenEnergy`, `carbonDioxideImpact`,
`nuclearWasteImpact`, `energyRateByReference`, `energyProductInformation`, `renewableEnergyEvidence`,
`mobilityServiceProvider`, `energyRate`. No per-source-type ratio breakdown; adds environmental impact
metrics and product information URLs instead.

---

## LocationReferencing

### Definitions only in v3.7 (26)

Navigation/routing: `AlertCArea`, `AlertCLocation`, `AlertCLocationCode`, `AreaDestination`, `DestinationG`,
`ItineraryByIndexedLocations`, `ItineraryByReference`, `ItineraryG`, `PointDestination`, `PointLocationG`,
`PredefinedItineraryVersionedReferenceG`, `locationContainedInItineraryG`.

TPEG: `TpegAreaDescriptor`, `TpegAreaLocationG`, `TpegDescriptorG`, `TpegGeometricArea`, `TpegHeight`,
`TpegLoc01AreaLocationSubtypeEnum`/`G`, `TpegLoc03AreaDescriptorSubtypeEnum`/`G`,
`TpegLoc04HeightTypeEnum`/`G`, `TpegNamedOnlyArea`.

Extension types: `LocationReferenceExtensionTypeG`, `NamedAreaExtensionTypeG`.

### Definitions only in v3.5 (22)

Position accuracy: `AltitudeAccuracyEnum`/`G`, `AltitudeConfidence`, `PositionAccuracy`,
`PositionConfidenceCodedErrorEnum`/`G`, `PositionConfidenceEllipse`.

OpenLR extensions: `OpenlrBasePointLocationG`, `OpenlrOffsets`, `OpenlrOrientationEnum`/`G`,
`OpenlrPoiWithAccessPoint`, `OpenlrPointAlongLine`, `OpenlrSideOfRoadEnum`/`G`.

Other: `AreaPlacesEnum`/`G`, `GmlPosList`, `LocationByReference`,
`PredefinedLocationVersionedReferenceG`, `SupplementaryPositionalDescription`,
`LocationExtensionTypeG`.

### LocationReferenceG

v3.7 adds `locItineraryByIndexedLocations`, `locItineraryByReference`.
v3.5 adds `locAreaLocation`, `locLocationByReference`.

### LocationG

v3.5 adds `locAreaLocation`, `locLocationByReference`. v3.7 only has `locPointLocation`.

### PointLocation

v3.5 adds: `coordinatesForDisplay`, `externalReferencing`, `openlrPointLocationReference`,
`supplementaryPositionalDescription`.

Extension point swap: v3.7 puts `LocationReferenceExtensionTypeG` on `locLocationReferenceExtensionG` and
generic `ExtensionTypeG` on `locLocationExtensionG`; v3.5 does the reverse (generic on
`locLocationReferenceExtensionG`, `LocationExtensionTypeG` on `locLocationExtensionG`).

### AreaLocation

v3.5 adds: `areasAtWhichApplicable`, `coordinatesForDisplay`, `externalReferencing`,
`gmlMultiPolygon`, `namedArea`, `openlrAreaLocationReference`. Same extension point swap as PointLocation.

### PointCoordinates

v3.5 adds: `horizontalPositionAccuracy`, `positionConfidenceEllipse`.

### HeightCoordinate

v3.5 adds: `altitudeConfidence`, `verticalPositionAccuracy`.

---

## CommonExtension

### Definitions only in v3.7 (18)

`ADRClass`, `AgeCharacteristic`, `ApplicableDaysWithinMonthEnum`/`G`, `DangerousGoodsExtended`,
`DayWeekMonthExtended`, `EnginePowerCharacteristics`, `EuSpecialPurposeVehicleEnum`/`G`, `FuzzyPeriod`,
`FuzzyTimeEnum`/`G`, `GrossTrailerWeightCharacteristics`, `PeriodExtended`, `PowerUnitOfMeasureEnum`/`G`,
`RegulatedCharacteristics`, `TrailerCharacteristics`.

### Definitions only in v3.5

None.

### VehicleCharacteristicsExtended

v3.7 has `ageCharacteristic`, `trailerCharacteristics`, `regulatedCharacteristics`.
v3.5 has only `euVehicleCategory` (required).

### EuVehicleCategoryEnum

Only in v3.7: `r`.
Only in v3.5: `l`, `n1ClassI`, `n1ClassII`, `n1ClassIII`, `n1ClassIIIAndN2`, `other`.

---

## LocationExtension

### AddressLineTypeEnum

v3.7: `street`, `houseNumber`, `extendedG`.

v3.5 adds: `apartment`, `building`, `poBox`, `unit`, `region`, `town`, `districtTerritory`,
`floor`, `generalTextLine`.

### FacilityLocation

v3.5 adds `nutsArea` property (array of NutsArea with nutsCodeType and nutsCode).

### NamedAreaExtended (v3.7) vs NutsArea (v3.5)

v3.7 has `NamedAreaExtended` with a generic `namedAreaCode`. v3.5 replaces this with `NutsArea`
(typed NUTS/LAU code with `nutsCodeType` and `nutsCode`).
