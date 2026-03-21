# XML vs JSON Schema Differences for DATEX2 version 3.7

This document describes the structural differences between the DATEX II v3.7 XSD schema
(`docs/schema/v3_7/xml`) and the JSON Schema representation (`docs/schema/v3_7/json`). Both describe the same
domain model but use format-specific conventions.

## General Structural Patterns

### Definition containers

- XSD: `xs:complexType`, `xs:simpleType`, `xs:element` within `.xsd` files
- JSON: `$defs` within `.json` files

### Namespaces vs file references

- XSD: XML namespaces (`http://datex2.eu/schema/3/common`, etc.) with `xs:import` and namespace prefixes
  (`com:`, `egi:`, `fac:`, `loc:`, `locx:`, `comx:`)
- JSON: no namespaces; dependencies via relative `$ref` paths (e.g.,
  `DATEXII_3_Common.json#/$defs/String`); namespace prefixes baked into property names (`com`, `egi`,
  `fac`, `loc`)

### Attributes vs properties

XSD distinguishes XML attributes from child elements. JSON has no such distinction -- everything is an
object property. Fields that are XSD attributes become regular JSON properties, often with a `G` suffix.

| XSD attribute                   | JSON property                   | Types affected                                                                                               |
|---------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------|
| `id` (required)                 | `idG` (required)                | FacilityObject, EnergyInfrastructureTable, OperatingHoursSpecification, OrganisationSpecification, RateTable |
| `version` (required)            | `versionG` (required)           | Same as above                                                                                                |
| `lang` (required)               | `lang` (required)               | PayloadPublication                                                                                           |
| `energyMixIndex` (required)     | `energyMixIndex` (required)     | ElectricEnergyMix                                                                                            |
| `order` (required)              | `order` (required)              | AddressLine                                                                                                  |
| `sequence` (required)           | `sequence` (required)           | RateLine                                                                                                     |
| `collectionSequence` (required) | `collectionSequence` (required) | RateLineCollection                                                                                           |
| `index` (required)              | `index` (required)              | locationContainedInItinerary                                                                                 |
| `targetClass` (fixed)           | `targetClass` (default)         | Versioned reference types                                                                                    |
| `_extendedValue`                | `extendedValueG`                | All enum wrapper types                                                                                       |

---

## Inheritance and Polymorphism

This is the most fundamental difference between the two formats.

### XSD: inheritance with abstract types

XSD uses `xs:complexContent/xs:extension` for type inheritance. Abstract base types (`abstract="true"`)
define shared properties, and concrete subtypes extend them. At runtime, `xsi:type` selects the concrete
subtype.

Key inheritance chains:

```
FacilityObject (abstract)
  -> Facility (abstract)
       -> RefillPoint (abstract)
       |    -> ElectricChargingPoint
       -> EnergyInfrastructureSite
       -> EnergyInfrastructureStation

PayloadPublication (abstract)
  -> EnergyInfrastructureTablePublication

OperatingHours (abstract)
  -> OpenAllHours
  -> OperatingHoursSpecification
  -> OperatingHoursByReference
  -> UnknownOperatingHours
  -> UndefinedOperatingHours

Rates (abstract)
  -> RateTable
  -> FreeOfCharge
  -> GeneralRateInformation
  -> RatesByReference
  -> UnknownRates
  -> UnspecifiedRates

Organisation (abstract)
  -> OrganisationSpecification

ContactInformation
  -> ContactPerson

LocationReference (abstract)
  -> Location (abstract)
  |    -> NetworkLocation (abstract)
  |         -> PointLocation
  |    -> AreaLocation
  -> LocationGroup (abstract)
  |    -> LocationGroupByList
  |    -> LocationGroupByReference
  -> Itinerary (abstract)
       -> ItineraryByIndexedLocations
       -> ItineraryByReference

DataValue (abstract)
  -> TemperatureValue, WindSpeedValue, PressureValue, ...
```

### JSON: flattened types with "G" union wrappers

JSON Schema has no inheritance. Instead:

1. **Property flattening**: every concrete type redeclares ALL inherited properties inline. For example,
   `ElectricChargingPoint` in JSON includes `idG`, `versionG`, `name`, `externalIdentifier`,
   `lastUpdated`, `operatingHours`, `locationReference`, `owner`, `operator`, `rates`,
   `supplementalFacility` (from FacilityObject/Facility/RefillPoint) alongside its own properties, plus
   extension points from every level (`facFacilityObjectExtensionG`, `facFacilityExtensionG`,
   `egiRefillPointExtensionG`, `egiElectricChargingPointExtensionG`).

2. **"G" union wrapper types**: every abstract type gets a wrapper object where each property corresponds
   to a concrete subtype. The description states "Only one of the properties shall be used in an
   instance." This is a manual discriminated union (JSON Schema `oneOf` is not used).

Examples:

| XSD abstract type    | JSON "G" wrapper      | Properties (one-of)                                                                                                                           |
|----------------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `RefillPoint`        | `RefillPointG`        | `egiElectricChargingPoint`                                                                                                                    |
| `OperatingHours`     | `OperatingHoursG`     | `facOperatingHoursSpecification`, `facUnknownOperatingHours`, `facOperatingHoursByReference`, `facOpenAllHours`, `facUndefinedOperatingHours` |
| `Rates`              | `RatesG`              | `facUnknownRates`, `facGeneralRateInformation`, `facRatesByReference`, `facUnspecifiedRates`, `facRateTable`, `facFreeOfCharge`               |
| `Organisation`       | `OrganisationG`       | `facOrganisationSpecification`                                                                                                                |
| `ContactInformation` | `ContactInformationG` | `facContactInformation`, `facContactPerson`                                                                                                   |
| `LocationReference`  | `LocationReferenceG`  | `locLocationGroupByList`, `locLocationGroupByReference`, `locItineraryByIndexedLocations`, `locItineraryByReference`, `locPointLocation`      |
| `Location`           | `LocationG`           | `locPointLocation`                                                                                                                            |
| `DataValue`          | `DataValueG`          | `comTemperatureValue`, `comWindSpeedValue`, ...                                                                                               |
| `NamedArea`          | `NamedAreaG`          | `locNamedArea`, `locNutsNamedArea`, `locIsoNamedArea`                                                                                         |

### Consequences

- Abstract types (`FacilityObject`, `Facility`, `RefillPoint`, `LocationReference`, `Location`,
  `NetworkLocation`, `DataValue`, `OperatingHours`, `Rates`, `Organisation`, `SupplementalFacility`,
  `PayloadPublication`, etc.) exist only in XSD, not in JSON.
- JSON is denormalized: if a base type changes, every subtype's definition must be updated separately.
- XSD polymorphism uses `xsi:type`; JSON uses property-name-based discrimination.
- JSON `*G` wrappers add an extra nesting level that does not exist in XSD.

---

## Enum Representation

### Structure

XSD uses two types per enum:

1. A `xs:simpleType` with `xs:restriction base="xs:string"` and `xs:enumeration` values. Each value has
   `xs:annotation/xs:documentation`. The extension sentinel is `_extended`.
2. An underscore-prefixed `xs:complexType` (e.g., `_ConnectorTypeEnum`) wrapping the enum as
   `xs:simpleContent`, adding an `_extendedValue` **XML attribute**.

JSON uses two definitions per enum:

1. A `"type": "string"` with an `"enum"` array. No per-value descriptions. The extension sentinel is
   `extendedG`.
2. A `G`-suffixed wrapper object (e.g., `ConnectorTypeEnumG`) with `value` (the enum ref) and
   `extendedValueG` (string) as properties.

### Key differences

| Aspect                  | XSD                                                                            | JSON                                    |
|-------------------------|--------------------------------------------------------------------------------|-----------------------------------------|
| Extension sentinel      | `_extended`                                                                    | `extendedG`                             |
| Wrapper type naming     | `_` prefix (e.g., `_ConnectorTypeEnum`)                                        | `G` suffix (e.g., `ConnectorTypeEnumG`) |
| Extended value          | XML attribute `_extendedValue`                                                 | Property `extendedValueG`               |
| Per-value documentation | `xs:documentation` on each value                                               | None                                    |
| Typed extension values  | Some enums constrain `_extendedValue` to specific values via typed simpleTypes | Always unconstrained `"type": "string"` |

Enum values themselves are identical across both formats (same strings, same sets).

### Typed enum extension values (XSD only)

Some XSD enums restrict the `_extendedValue` attribute to specific allowed extensions via dedicated
simpleTypes (e.g., `_EmissionClassificationEuroEnumExtensionType` limits extensions to `euro0`, `euro6d`,
etc.). In JSON, the corresponding `*EnumExtensionTypeG` definitions list these as enum arrays, but the
`extendedValueG` property on the standard `*EnumG` wrappers is always plain `"type": "string"` -- the
constraint exists as a separate definition but is not referenced from the wrapper.

---

## Extension Points

### XSD

Generic extensions use `_ExtensionType`:
```xml
<xs:complexType name="_ExtensionType">
  <xs:sequence>
    <xs:any namespace="##any" processContents="lax"
            minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
</xs:complexType>
```

Typed extensions (e.g., `_LocationReferenceExtensionType`) contain a specific optional element plus
`xs:any namespace="##other"`.

Extension element names use underscore prefix: `_connectorExtension`, `_facilityObjectExtension`.

### JSON

Generic extensions use `ExtensionTypeG`:
```json
{ "type": "object", "additionalProperties": true }
```

Typed extensions (e.g., `LocationReferenceExtensionTypeG`) have specific named properties plus
`additionalProperties: true`.

Extension property names use module prefix + `G` suffix: `egiConnectorExtensionG`,
`facFacilityObjectExtensionG`.

### Flattened extension points

Because JSON flattens inheritance, each level of the hierarchy gets its own named extension property on
the concrete type. For example, `PointLocation` in JSON has four extension properties:

- `locLocationReferenceExtensionG` (from LocationReference)
- `locLocationExtensionG` (from Location)
- `locNetworkLocationExtensionG` (from NetworkLocation)
- `locPointLocationExtensionG` (own)

In XSD, these exist at the corresponding level in the extension chain.

---

## PayloadPublicationG (JSON) vs PayloadPublication (XSD)

This type has the largest structural difference.

**XSD**: `PayloadPublication` is abstract. It has child elements `publicationTime`, `publicationCreator`,
`_payloadPublicationExtension` and attributes `lang`, `modelBaseVersion` (fixed "3"), `extensionName`,
`extensionVersion`, `profileName`, `profileVersion`. Concrete publications extend it.

**JSON**: `PayloadPublicationG` is a flat choice wrapper with properties `versionG` (default "3.7"),
`modelBaseVersionG` (default "3"), `extensionNameG`, `extensionVersionG`, `profileNameG`,
`profileVersionG`, plus the concrete publication property
(`egiEnergyInfrastructureTablePublication`). The `publicationTime`, `publicationCreator`, and `lang`
properties live on the concrete publication type instead.

Additional JSON-only property: `versionG` (with default "3.7") has no XSD counterpart at the instance
data level. XSD carries the version as a schema-level attribute (`version="3.7"` on the `xs:schema`
element).

---

## Uniqueness Constraints (XSD only)

The XSD `D2Payload.xsd` defines five `xs:unique` constraints on the payload element:

- `_payloadOperatingHoursSpecificationConstraint`
- `_payloadOrganisationSpecificationConstraint`
- `_payloadFacilityObjectConstraint`
- `_payloadRateTableConstraint`
- `_payloadEnergyInfrastructureTableConstraint`

These enforce uniqueness of `id`/`version` pairs across instances. JSON Schema has no equivalent mechanism.

---

## Primitive Type Mappings

| DATEX II type        | JSON Schema                                   | XSD                                              |
|----------------------|-----------------------------------------------|--------------------------------------------------|
| `String`             | `"type": "string", "maxLength": 1024`         | `xs:restriction base="xs:string" maxLength=1024` |
| `Float`              | `"type": "number"`                            | `xs:restriction base="xs:float"`                 |
| `Decimal`            | `"type": "number"`                            | `xs:restriction base="xs:decimal"`               |
| `Integer`            | `"type": "integer"`                           | `xs:restriction base="xs:integer"`               |
| `NonNegativeInteger` | `"type": "integer", "minimum": 0.0`           | `xs:restriction base="xs:nonNegativeInteger"`    |
| `Boolean`            | `"type": "boolean"`                           | `xs:restriction base="xs:boolean"`               |
| `DateTime`           | `"type": "string", "format": "date-time"`     | `xs:restriction base="xs:dateTime"`              |
| `Time`               | `"type": "string", "pattern": "^(([01]...)$"` | `xs:restriction base="xs:time"`                  |
| `Language`           | `"type": "string", "pattern": "^[a-z]{2}$"`   | `xs:restriction base="xs:language"`              |
| `Url`                | `"type": "string"` (no format)                | `xs:restriction base="xs:anyURI"`                |

Notable differences:

- `Float` and `Decimal` both map to JSON `"type": "number"` -- no distinction in JSON.
- `Time` uses explicit regex in JSON vs built-in `xs:time` in XSD.
- `Language` is restricted to exactly 2 lowercase chars in JSON (`^[a-z]{2}$`), while XSD `xs:language`
  also allows subtags like `en-US`.
- `Url` has no format constraint in JSON; XSD uses `xs:anyURI`.

### Constraint loss in JSON

- `AmountOfMoney`: XSD has `xs:totalDigits value="8"` and `xs:fractionDigits value="2"`; JSON has no
  numeric constraints beyond referencing `Decimal`.
- `TimeZone`: XSD has `xs:pattern value="[-+][0-9][0-9]:[0-9][0-9]|Z"`; JSON has no pattern.
- `MultilingualStringValueType`: XSD has `xs:maxLength value="1024"`; JSON has no length restriction on
  the `value` property (only on the `String` type when used directly).

---

## MultilingualString

**XSD**: `values` contains a sequence of `MultilingualStringValue` elements. Each has `xs:simpleContent`
(text restricted to maxLength 1024) with a `lang` XML attribute of type `xs:language`.

**JSON**: `values` is an array of `MultiLingualStringValue` objects (note capital L). Each has `lang`
(pattern `^[a-z]{2}$`) and `value` (string) as sibling properties.

Differences:
- XSD: text value is element content; JSON: `value` is a property
- XSD: `lang` is an XML attribute; JSON: `lang` is a peer property
- XSD: allows language subtags (`en-US`); JSON: only 2-letter codes

---

## Versioned References

**XSD**: underscore-prefixed types (e.g., `_OrganisationVersionedReference`) extend `com:VersionedReference`
with a `targetClass` XML attribute (fixed to a namespace-qualified class name like
`loc:PredefinedItinerary`). `id` and `version` are inherited as XML attributes.

**JSON**: `G`-suffixed flat objects (e.g., `OrganisationVersionedReferenceG`) with `targetClass` (string
with `default` value, no namespace prefix), `idG` (required), and `versionG` (optional) as regular
properties.

---

## Cardinality

Both formats express the same cardinality constraints using format-specific mechanisms:

| Constraint         | XSD                                           | JSON                                             |
|--------------------|-----------------------------------------------|--------------------------------------------------|
| Required element   | `minOccurs="1"` (default)                     | Listed in `required` array                       |
| Required attribute | `use="required"`                              | Listed in `required` array                       |
| Optional element   | `minOccurs="0"`                               | Not in `required`; property defined              |
| Array (0..*)       | `minOccurs="0" maxOccurs="unbounded"`         | `"type": "array", "minItems": 0`                 |
| Array (1..*)       | `maxOccurs="unbounded"` (default minOccurs=1) | `"type": "array", "minItems": 1` + in `required` |
| Bounded array      | `maxOccurs="7"`                               | `"maxItems": 7`                                  |

No semantic differences in required/optional status were found between the formats.

---

## Summary of Key Differences

1. **Polymorphism**: XSD uses inheritance hierarchies with abstract types and `xsi:type` runtime
   discrimination. JSON uses flat types with "G"-suffixed union wrappers using property-name
   discrimination.

2. **Inheritance flattening**: JSON redeclares all inherited properties on each concrete type. XSD
   inherits via `xs:extension`. Each inheritance level's extension point becomes a separate named property
   in JSON.

3. **Attributes vs properties**: XSD attributes (`id`, `version`, `lang`, `order`, `energyMixIndex`,
   `_extendedValue`, etc.) become regular JSON properties, often with `G` suffix.

4. **Naming conventions**: XSD uses `_` prefix for wrapper/internal types and `_` prefix for extension
   elements. JSON uses `G` suffix for wrappers and module-prefix + `G` suffix for extension properties.

5. **Enum extensibility**: sentinel `_extended` (XSD) vs `extendedG` (JSON). XSD has per-value
   documentation and typed extension constraints; JSON does not.

6. **Uniqueness constraints**: XSD `xs:unique` has no JSON equivalent.

7. **Type precision**: JSON conflates `Float`/`Decimal` into `number`, loses `xs:anyURI` and
   `xs:language` subtag semantics, and drops some numeric/pattern constraints.

8. **Abstract types**: exist only in XSD. JSON has no abstract types -- concrete types are self-contained
   and union wrappers provide polymorphism.
