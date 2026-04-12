"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from flask_openapi.decorator import Schema as Component
from flask_openapi.schema import (
    ArrayField,
    BooleanField,
    IntegerField,
    JsonSchema,
    NumericField,
    Reference,
    StringField,
)

# --- Primitive / enum wrapper schemas ---

multilingual_string_value_schema = JsonSchema(
    title='Datex2V37MultiLingualStringValue',
    description='A single language value within a multilingual string.',
    properties={
        'lang': StringField(maxLength=2, description='ISO 639-1 two-letter language code.'),
        'value': StringField(description='The text value.'),
    },
)

multilingual_string_value_example = {'lang': 'de', 'value': 'Example text'}

multilingual_string_value_component = Component(
    'Datex2V37MultiLingualStringValue', multilingual_string_value_schema, multilingual_string_value_example
)


multilingual_string_schema = JsonSchema(
    title='Datex2V37MultilingualString',
    description='A multilingual string containing values in one or more languages.',
    properties={
        'values': ArrayField(
            items=Reference(obj='Datex2V37MultiLingualStringValue'),
            minItems=1,
            description='List of language-specific string values.',
        ),
    },
)

multilingual_string_example = {'values': [{'lang': 'de', 'value': 'Beispieltext'}]}

multilingual_string_component = Component(
    'Datex2V37MultilingualString', multilingual_string_schema, multilingual_string_example
)


connector_type_enum_g_schema = JsonSchema(
    title='Datex2V37ConnectorTypeEnumG',
    description='Connector type specification.',
    properties={
        'value': StringField(
            description='Connector type. Common values: chademo, iec62196T1, iec62196T1COMBO, iec62196T2, '
            'iec62196T2COMBO, iec62196T3A, iec62196T3C, teslaR, teslaS, pantographBottomUp, pantographTopDown.'
        ),
        'extendedValueG': StringField(required=False, description='Extended value for custom connector types.'),
    },
)

connector_type_enum_g_example = {'value': 'iec62196T2'}

connector_type_enum_g_component = Component(
    'Datex2V37ConnectorTypeEnumG', connector_type_enum_g_schema, connector_type_enum_g_example
)


connector_format_type_enum_g_schema = JsonSchema(
    title='Datex2V37ConnectorFormatTypeEnumG',
    description='Cable type used during the charging process.',
    properties={
        'value': StringField(description='Format type: socket, cableMode2, cableMode3, otherCable.'),
        'extendedValueG': StringField(required=False, description='Extended value for custom format types.'),
    },
)

connector_format_type_enum_g_example = {'value': 'socket'}

connector_format_type_enum_g_component = Component(
    'Datex2V37ConnectorFormatTypeEnumG', connector_format_type_enum_g_schema, connector_format_type_enum_g_example
)


authentication_and_identification_enum_g_schema = JsonSchema(
    title='Datex2V37AuthenticationAndIdentificationEnumG',
    description='Authentication and/or identification method.',
    properties={
        'value': StringField(
            description='Auth method. Values: creditCard, debitCard, rfid, nfc, overTheAir, plc, cashPayment, '
            'pinpad, calypso, apps, prepaidCard, website, phoneDialog, phoneSMS, unlimitedAccess.'
        ),
        'extendedValueG': StringField(required=False, description='Extended value.'),
    },
)

authentication_and_identification_enum_g_example = {'value': 'rfid'}

authentication_and_identification_enum_g_component = Component(
    'Datex2V37AuthenticationAndIdentificationEnumG',
    authentication_and_identification_enum_g_schema,
    authentication_and_identification_enum_g_example,
)


address_line_type_enum_g_schema = JsonSchema(
    title='Datex2V37AddressLineTypeEnumG',
    description='Type of address line element.',
    properties={
        'value': StringField(
            description='Address line type: street, houseNumber, apartment, building, poBox, unit, region, '
            'town, districtTerritory, floor, generalTextLine.'
        ),
        'extendedValueG': StringField(required=False, description='Extended value.'),
    },
)

address_line_type_enum_g_example = {'value': 'street'}

address_line_type_enum_g_component = Component(
    'Datex2V37AddressLineTypeEnumG', address_line_type_enum_g_schema, address_line_type_enum_g_example
)


# --- Connector and charging point schemas ---

datex2_connector_schema = JsonSchema(
    title='Datex2V37Connector',
    description='Parameters and description of a charging interface available at a charging point.',
    properties={
        'connectorType': Reference(
            obj='Datex2V37ConnectorTypeEnumG',
            description='Specification of the connector / charging interface type.',
        ),
        'maxPowerAtSocket': NumericField(description='Maximum power at the socket in kW.'),
        'voltage': NumericField(required=False, description='Voltage at the connector in volts.'),
        'maximumCurrent': NumericField(required=False, description='Maximum current in ampere.'),
        'connectorFormat': Reference(
            obj='Datex2V37ConnectorFormatTypeEnumG',
            required=False,
            description='Information on the cable type used.',
        ),
    },
)

datex2_connector_example = {
    'connectorType': {'value': 'iec62196T2'},
    'maxPowerAtSocket': 22.0,
    'voltage': 400.0,
    'maximumCurrent': 32.0,
    'connectorFormat': {'value': 'socket'},
}

datex2_connector_component = Component('Datex2V37Connector', datex2_connector_schema, datex2_connector_example)


electric_energy_mix_schema = JsonSchema(
    title='Datex2V37ElectricEnergyMix',
    description='Information about the electric energy mix.',
    properties={
        'energyMixIndex': IntegerField(minimum=0, description='Index of the energy mix entry.'),
        'isGreenEnergy': BooleanField(required=False, description='Whether the energy is from renewable sources.'),
    },
)

electric_energy_mix_example = {'energyMixIndex': 0, 'isGreenEnergy': True}

electric_energy_mix_component = Component(
    'Datex2V37ElectricEnergyMix', electric_energy_mix_schema, electric_energy_mix_example
)


electric_charging_point_schema = JsonSchema(
    title='Datex2V37ElectricChargingPoint',
    description='Technical infrastructure that facilitates electric charging of one vehicle at a time.',
    properties={
        'idG': StringField(description='Unique identifier of the charging point.'),
        'versionG': StringField(description='Version timestamp (ISO 8601).'),
        'availableVoltage': ArrayField(
            items=NumericField(),
            required=False,
            description='Available voltage levels in volts.',
        ),
        'availableChargingPower': ArrayField(
            items=NumericField(),
            required=False,
            description='Available charging power levels in kW.',
        ),
        'electricEnergyMix': ArrayField(
            items=Reference(obj='Datex2V37ElectricEnergyMix'),
            required=False,
            description='Information about the electric energy mix.',
        ),
        'connector': ArrayField(
            items=Reference(obj='Datex2V37Connector'),
            description='List of available connectors.',
        ),
    },
)

electric_charging_point_example = {
    'idG': 'EVSE-1',
    'versionG': '2026-01-01T00:00:00+00:00',
    'availableVoltage': [400.0],
    'availableChargingPower': [22.0],
    'connector': [datex2_connector_example],
}

electric_charging_point_component = Component(
    'Datex2V37ElectricChargingPoint', electric_charging_point_schema, electric_charging_point_example
)


refill_point_g_schema = JsonSchema(
    title='Datex2V37RefillPointG',
    description='A refill point providing an electric charging point.',
    properties={
        'aegiElectricChargingPoint': Reference(
            obj='Datex2V37ElectricChargingPoint',
            description='The electric charging point at this refill point.',
        ),
    },
)

refill_point_g_example = {'aegiElectricChargingPoint': electric_charging_point_example}

refill_point_g_component = Component('Datex2V37RefillPointG', refill_point_g_schema, refill_point_g_example)


# --- Station schema ---

energy_infrastructure_station_schema = JsonSchema(
    title='Datex2V37EnergyInfrastructureStation',
    description='A station within a site where vehicles can be supplied with energy.',
    properties={
        'idG': StringField(description='Unique identifier of the station.'),
        'versionG': StringField(description='Version timestamp (ISO 8601).'),
        'authenticationAndIdentificationMethods': ArrayField(
            items=Reference(obj='Datex2V37AuthenticationAndIdentificationEnumG'),
            required=False,
            description='Available authentication and identification methods.',
        ),
        'locationReference': Reference(
            obj='Datex2V37LocationReferenceG',
            required=False,
            description='Location reference for the station.',
        ),
        'refillPoint': ArrayField(
            items=Reference(obj='Datex2V37RefillPointG'),
            description='List of refill points at this station.',
        ),
    },
)

energy_infrastructure_station_example = {
    'idG': 'CS-1',
    'versionG': '2026-01-01T00:00:00+00:00',
    'refillPoint': [refill_point_g_example],
}

energy_infrastructure_station_component = Component(
    'Datex2V37EnergyInfrastructureStation', energy_infrastructure_station_schema, energy_infrastructure_station_example
)


# --- Location reference schemas ---

point_coordinates_schema = JsonSchema(
    title='Datex2V37PointCoordinates',
    description='A pair of coordinates (WGS 84).',
    properties={
        'latitude': NumericField(description='Latitude in decimal degrees.'),
        'longitude': NumericField(description='Longitude in decimal degrees.'),
    },
)

point_coordinates_example = {'latitude': 52.52003, 'longitude': 13.40489}

point_coordinates_component = Component(
    'Datex2V37PointCoordinates', point_coordinates_schema, point_coordinates_example
)


point_by_coordinates_schema = JsonSchema(
    title='Datex2V37PointByCoordinates',
    description='A point defined by its coordinates.',
    properties={
        'pointCoordinates': Reference(obj='Datex2V37PointCoordinates', description='The coordinates of the point.'),
    },
)

point_by_coordinates_example = {'pointCoordinates': point_coordinates_example}

point_by_coordinates_component = Component(
    'Datex2V37PointByCoordinates', point_by_coordinates_schema, point_by_coordinates_example
)


address_line_schema = JsonSchema(
    title='Datex2V37AddressLine',
    description='One line of a postal address.',
    properties={
        'order': IntegerField(minimum=0, description='Sequence order for display.'),
        'type': Reference(obj='Datex2V37AddressLineTypeEnumG', description='Type of address line element.'),
        'text': Reference(obj='Datex2V37MultilingualString', description='Text content of the address line.'),
    },
)

address_line_example = {
    'order': 1,
    'type': {'value': 'street'},
    'text': {'values': [{'lang': 'de', 'value': 'Musterstraße'}]},
}

address_line_component = Component('Datex2V37AddressLine', address_line_schema, address_line_example)


address_schema = JsonSchema(
    title='Datex2V37Address',
    description='A street-oriented addressing structure.',
    properties={
        'postcode': StringField(required=False, description='Postal code.'),
        'city': Reference(obj='Datex2V37MultilingualString', required=False, description='City name.'),
        'countryCode': StringField(maxLength=2, required=False, description='ISO 3166-1 alpha-2 country code.'),
        'addressLine': ArrayField(
            items=Reference(obj='Datex2V37AddressLine'),
            required=False,
            description='Address lines (street, house number, etc.).',
        ),
    },
)

address_example = {
    'postcode': '12345',
    'city': {'values': [{'lang': 'de', 'value': 'Berlin'}]},
    'countryCode': 'DE',
    'addressLine': [
        {'order': 1, 'type': {'value': 'street'}, 'text': {'values': [{'lang': 'de', 'value': 'Musterstraße'}]}},
        {'order': 2, 'type': {'value': 'houseNumber'}, 'text': {'values': [{'lang': 'de', 'value': '1'}]}},
    ],
}

address_component = Component('Datex2V37Address', address_schema, address_example)


facility_location_schema = JsonSchema(
    title='Datex2V37FacilityLocation',
    description='A location with time zone and address information.',
    properties={
        'timeZone': StringField(required=False, description='IANA time zone identifier.'),
        'address': Reference(obj='Datex2V37Address', required=False, description='Address of the facility.'),
    },
)

facility_location_example = {'address': address_example}

facility_location_component = Component(
    'Datex2V37FacilityLocation', facility_location_schema, facility_location_example
)


location_reference_extension_type_g_schema = JsonSchema(
    title='Datex2V37LocationReferenceExtensionTypeG',
    description='Extension for location referencing with facility location details.',
    properties={
        'FacilityLocation': Reference(
            obj='Datex2V37FacilityLocation',
            required=False,
            description='Facility location with address.',
        ),
    },
)

location_reference_extension_type_g_example = {'FacilityLocation': facility_location_example}

location_reference_extension_type_g_component = Component(
    'Datex2V37LocationReferenceExtensionTypeG',
    location_reference_extension_type_g_schema,
    location_reference_extension_type_g_example,
)


point_location_schema = JsonSchema(
    title='Datex2V37PointLocation',
    description='A point location with coordinates and facility location extension.',
    properties={
        'pointByCoordinates': Reference(
            obj='Datex2V37PointByCoordinates',
            required=False,
            description='Point defined by coordinates.',
        ),
        'locLocationReferenceExtensionG': Reference(
            obj='Datex2V37LocationReferenceExtensionTypeG',
            required=False,
            description='Extension with facility location details.',
        ),
    },
)

point_location_example = {
    'pointByCoordinates': point_by_coordinates_example,
    'locLocationReferenceExtensionG': location_reference_extension_type_g_example,
}

point_location_component = Component('Datex2V37PointLocation', point_location_schema, point_location_example)


location_reference_g_schema = JsonSchema(
    title='Datex2V37LocationReferenceG',
    description='A location reference with point location information.',
    properties={
        'locPointLocation': Reference(
            obj='Datex2V37PointLocation',
            required=False,
            description='Point location with coordinates and facility details.',
        ),
    },
)

location_reference_g_example = {'locPointLocation': point_location_example}

location_reference_g_component = Component(
    'Datex2V37LocationReferenceG', location_reference_g_schema, location_reference_g_example
)


# --- Organisation schemas ---

organisation_unit_schema = JsonSchema(
    title='Datex2V37OrganisationUnit',
    description='A unit within an organisation.',
    properties={},
)

organisation_unit_example = {}

organisation_unit_component = Component(
    'Datex2V37OrganisationUnit', organisation_unit_schema, organisation_unit_example
)


organisation_specification_schema = JsonSchema(
    title='Datex2V37OrganisationSpecification',
    description='A referenceable organisation specification with ID, version, name, and units.',
    properties={
        'idG': StringField(description='Unique identifier.'),
        'versionG': StringField(description='Version identifier.'),
        'name': Reference(obj='Datex2V37MultilingualString', description='Name of the organisation.'),
        'organisationUnit': ArrayField(
            items=Reference(obj='Datex2V37OrganisationUnit'),
            required=False,
            description='Organisation units.',
        ),
    },
)

organisation_specification_example = {
    'idG': 'DE*ABC',
    'versionG': '1',
    'name': {'values': [{'lang': 'de', 'value': 'Electro Inc'}]},
    'organisationUnit': [{}],
}

organisation_specification_component = Component(
    'Datex2V37OrganisationSpecification', organisation_specification_schema, organisation_specification_example
)


organisation_g_schema = JsonSchema(
    title='Datex2V37OrganisationG',
    description='An organisation reference. Exactly one of the properties should be used.',
    properties={
        'afacReferenceableOrganisation': Reference(
            obj='Datex2V37OrganisationSpecification',
            required=False,
            description='A referenceable organisation specification with ID and version.',
        ),
    },
)

organisation_g_example = {'afacReferenceableOrganisation': organisation_specification_example}

organisation_g_component = Component('Datex2V37OrganisationG', organisation_g_schema, organisation_g_example)


# --- Operating hours ---

open_all_hours_schema = JsonSchema(
    title='Datex2V37OpenAllHours',
    description='Indicates that the facility is open 24/7. Empty object.',
    properties={},
)

open_all_hours_example = {}

open_all_hours_component = Component('Datex2V37OpenAllHours', open_all_hours_schema, open_all_hours_example)


operating_hours_g_schema = JsonSchema(
    title='Datex2V37OperatingHoursG',
    description='Operating hours specification. Exactly one of the properties should be used.',
    properties={
        'afacOpenAllHours': Reference(
            obj='Datex2V37OpenAllHours',
            required=False,
            description='Indicates 24/7 operation.',
        ),
    },
)

operating_hours_g_example = {'afacOpenAllHours': {}}

operating_hours_g_component = Component('Datex2V37OperatingHoursG', operating_hours_g_schema, operating_hours_g_example)


# --- Site / Table / Publication / Payload ---

energy_infrastructure_site_schema = JsonSchema(
    title='Datex2V37EnergyInfrastructureSite',
    description='A site where vehicles can be supplied with energy, including all stations and associated services.',
    properties={
        'idG': StringField(description='Unique identifier of the site.'),
        'versionG': StringField(description='Version timestamp (ISO 8601).'),
        'name': Reference(
            obj='Datex2V37MultilingualString',
            required=False,
            description='Name of the site.',
        ),
        'operatingHours': Reference(
            obj='Datex2V37OperatingHoursG',
            required=False,
            description='Operating hours of the site.',
        ),
        'locationReference': Reference(
            obj='Datex2V37LocationReferenceG',
            required=False,
            description='Geographic and address location of the site.',
        ),
        'operator': Reference(
            obj='Datex2V37OrganisationG',
            required=False,
            description='The operator of this site.',
        ),
        'energyInfrastructureStation': ArrayField(
            items=Reference(obj='Datex2V37EnergyInfrastructureStation'),
            required=False,
            description='Charging stations at this site.',
        ),
    },
)

energy_infrastructure_site_example = {
    'idG': 'LOCATION-1',
    'versionG': '2026-01-01T00:00:00+00:00',
    'name': {'values': [{'lang': 'de', 'value': 'Test Location'}]},
    'operatingHours': operating_hours_g_example,
    'locationReference': location_reference_g_example,
    'operator': organisation_g_example,
    'energyInfrastructureStation': [energy_infrastructure_station_example],
}

energy_infrastructure_site_component = Component(
    'Datex2V37EnergyInfrastructureSite', energy_infrastructure_site_schema, energy_infrastructure_site_example
)


energy_infrastructure_table_schema = JsonSchema(
    title='Datex2V37EnergyInfrastructureTable',
    description='A table of sites where vehicles can be supplied with energy.',
    properties={
        'idG': StringField(description='Table identifier.'),
        'versionG': StringField(description='Table version.'),
        'energyInfrastructureSite': ArrayField(
            items=Reference(obj='Datex2V37EnergyInfrastructureSite'),
            description='List of energy infrastructure sites.',
        ),
    },
)

energy_infrastructure_table_example = {
    'idG': '1',
    'versionG': '1',
    'energyInfrastructureSite': [energy_infrastructure_site_example],
}

energy_infrastructure_table_component = Component(
    'Datex2V37EnergyInfrastructureTable', energy_infrastructure_table_schema, energy_infrastructure_table_example
)


international_identifier_schema = JsonSchema(
    title='Datex2V37InternationalIdentifier',
    description='An international identifier with country and national identifier.',
    properties={
        'country': StringField(maxLength=2, description='ISO 3166-1 alpha-2 country code.'),
        'nationalIdentifier': StringField(description='National identifier of the data publisher.'),
    },
)

international_identifier_example = {'country': 'DE', 'nationalIdentifier': 'OCPDB'}

international_identifier_component = Component(
    'Datex2V37InternationalIdentifier', international_identifier_schema, international_identifier_example
)


energy_infrastructure_table_publication_schema = JsonSchema(
    title='Datex2V37EnergyInfrastructureTablePublication',
    description='A publication of static information on electric vehicle charging infrastructure.',
    properties={
        'lang': StringField(maxLength=2, description='Publication language (ISO 639-1).'),
        'publicationTime': StringField(description='Publication timestamp (ISO 8601).'),
        'publicationCreator': Reference(
            obj='Datex2V37InternationalIdentifier',
            description='Creator of the publication.',
        ),
        'energyInfrastructureTable': ArrayField(
            items=Reference(obj='Datex2V37EnergyInfrastructureTable'),
            description='List of infrastructure tables.',
        ),
    },
)

energy_infrastructure_table_publication_example = {
    'lang': 'de',
    'publicationTime': '2026-01-01T00:00:00+00:00',
    'publicationCreator': international_identifier_example,
    'energyInfrastructureTable': [energy_infrastructure_table_example],
}

energy_infrastructure_table_publication_component = Component(
    'Datex2V37EnergyInfrastructureTablePublication',
    energy_infrastructure_table_publication_schema,
    energy_infrastructure_table_publication_example,
)


payload_publication_g_schema = JsonSchema(
    title='Datex2V37PayloadPublicationG',
    description='DATEX II payload publication with version information and table publication.',
    properties={
        'modelBaseVersionG': StringField(description='Base model version.'),
        'versionG': StringField(required=False, description='Schema version.'),
        'profileNameG': StringField(required=False, description='Profile name.'),
        'profileVersionG': StringField(required=False, description='Profile version.'),
        'aegiEnergyInfrastructureTablePublication': Reference(
            obj='Datex2V37EnergyInfrastructureTablePublication',
            required=False,
            description='Energy infrastructure table publication.',
        ),
    },
)

payload_publication_g_example = {
    'modelBaseVersionG': '3',
    'versionG': '3.7',
    'profileNameG': 'Afir Energy Infrastructure',
    'profileVersionG': '01-00-00',
    'aegiEnergyInfrastructureTablePublication': energy_infrastructure_table_publication_example,
}

payload_publication_g_component = Component(
    'Datex2V37PayloadPublicationG', payload_publication_g_schema, payload_publication_g_example
)


datex2_v37_static_payload_schema = JsonSchema(
    title='Datex2V37StaticPayload',
    description='DATEX II v3.7 static payload for energy infrastructure.',
    properties={
        'payload': Reference(
            obj='Datex2V37PayloadPublicationG', required=False, description='The payload publication.'
        ),
    },
)

datex2_v37_static_payload_example = {'payload': payload_publication_g_example}

datex2_v37_static_payload_component = Component(
    'Datex2V37StaticPayload', datex2_v37_static_payload_schema, datex2_v37_static_payload_example
)


# --- Component list for use with @document ---

all_datex2_v37_static_components = [
    address_component,
    address_line_component,
    address_line_type_enum_g_component,
    authentication_and_identification_enum_g_component,
    connector_format_type_enum_g_component,
    connector_type_enum_g_component,
    datex2_connector_component,
    datex2_v37_static_payload_component,
    electric_charging_point_component,
    electric_energy_mix_component,
    energy_infrastructure_site_component,
    energy_infrastructure_station_component,
    energy_infrastructure_table_component,
    energy_infrastructure_table_publication_component,
    facility_location_component,
    international_identifier_component,
    location_reference_extension_type_g_component,
    location_reference_g_component,
    multilingual_string_component,
    multilingual_string_value_component,
    open_all_hours_component,
    operating_hours_g_component,
    organisation_g_component,
    organisation_specification_component,
    organisation_unit_component,
    payload_publication_g_component,
    point_by_coordinates_component,
    point_coordinates_component,
    point_location_component,
    refill_point_g_component,
]
