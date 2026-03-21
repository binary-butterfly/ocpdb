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
    title='Datex2MultiLingualStringValue',
    description='A single language value within a multilingual string.',
    properties={
        'lang': StringField(maxLength=2, description='ISO 639-1 two-letter language code.'),
        'value': StringField(description='The text value.'),
    },
)

multilingual_string_value_example = {'lang': 'de', 'value': 'Example text'}

multilingual_string_value_component = Component(
    'Datex2MultiLingualStringValue', multilingual_string_value_schema, multilingual_string_value_example
)


multilingual_string_schema = JsonSchema(
    title='Datex2MultilingualString',
    description='A multilingual string containing values in one or more languages.',
    properties={
        'values': ArrayField(
            items=Reference(obj='Datex2MultiLingualStringValue'),
            minItems=1,
            description='List of language-specific string values.',
        ),
    },
)

multilingual_string_example = {'values': [{'lang': 'de', 'value': 'Beispieltext'}]}

multilingual_string_component = Component(
    'Datex2MultilingualString', multilingual_string_schema, multilingual_string_example
)


connector_type_enum_g_schema = JsonSchema(
    title='Datex2ConnectorTypeEnumG',
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
    'Datex2ConnectorTypeEnumG', connector_type_enum_g_schema, connector_type_enum_g_example
)


connector_format_type_enum_g_schema = JsonSchema(
    title='Datex2ConnectorFormatTypeEnumG',
    description='Cable type used during the charging process.',
    properties={
        'value': StringField(description='Format type: socket, cableMode2, cableMode3, otherCable.'),
        'extendedValueG': StringField(required=False, description='Extended value for custom format types.'),
    },
)

connector_format_type_enum_g_example = {'value': 'socket'}

connector_format_type_enum_g_component = Component(
    'Datex2ConnectorFormatTypeEnumG', connector_format_type_enum_g_schema, connector_format_type_enum_g_example
)


delivery_unit_enum_g_schema = JsonSchema(
    title='Datex2DeliveryUnitEnumG',
    description='Measurement unit for energy delivery.',
    properties={
        'value': StringField(description='Delivery unit, e.g. kWh.'),
        'extendedValueG': StringField(required=False, description='Extended value.'),
    },
)

delivery_unit_enum_g_example = {'value': 'kWh'}

delivery_unit_enum_g_component = Component(
    'Datex2DeliveryUnitEnumG', delivery_unit_enum_g_schema, delivery_unit_enum_g_example
)


current_type_enum_g_schema = JsonSchema(
    title='Datex2CurrentTypeEnumG',
    description='The type of current (AC/DC).',
    properties={
        'value': StringField(description='Current type: ac or dc.'),
        'extendedValueG': StringField(required=False, description='Extended value.'),
    },
)

current_type_enum_g_example = {'value': 'ac'}

current_type_enum_g_component = Component(
    'Datex2CurrentTypeEnumG', current_type_enum_g_schema, current_type_enum_g_example
)


authentication_and_identification_enum_g_schema = JsonSchema(
    title='Datex2AuthenticationAndIdentificationEnumG',
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
    'Datex2AuthenticationAndIdentificationEnumG',
    authentication_and_identification_enum_g_schema,
    authentication_and_identification_enum_g_example,
)


address_line_type_enum_g_schema = JsonSchema(
    title='Datex2AddressLineTypeEnumG',
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
    'Datex2AddressLineTypeEnumG', address_line_type_enum_g_schema, address_line_type_enum_g_example
)


type_of_identifier_enum_g_schema = JsonSchema(
    title='Datex2TypeOfIdentifierEnumG',
    description='Type of external identifier.',
    properties={
        'value': StringField(description='Identifier type.'),
        'extendedValueG': StringField(required=False, description='Extended value, e.g. operatorId.'),
    },
)

type_of_identifier_enum_g_example = {'value': 'extendedG', 'extendedValueG': 'operatorId'}

type_of_identifier_enum_g_component = Component(
    'Datex2TypeOfIdentifierEnumG', type_of_identifier_enum_g_schema, type_of_identifier_enum_g_example
)


service_type_enum_g_schema = JsonSchema(
    title='Datex2ServiceTypeEnumG',
    description='Type of service at a station.',
    properties={
        'value': StringField(description='Service type: physicalAttendance, unattended.'),
        'extendedValueG': StringField(required=False, description='Extended value.'),
    },
)

service_type_enum_g_example = {'value': 'unattended'}

service_type_enum_g_component = Component(
    'Datex2ServiceTypeEnumG', service_type_enum_g_schema, service_type_enum_g_example
)


# --- Structural schemas ---

datex2_connector_schema = JsonSchema(
    title='Datex2Connector',
    description='Parameters and description of a charging interface available at a charging point.',
    properties={
        'connectorType': Reference(
            obj='Datex2ConnectorTypeEnumG',
            description='Specification of the connector / charging interface type.',
        ),
        'maxPowerAtSocket': NumericField(description='Maximum power at the socket in kW.'),
        'voltage': NumericField(required=False, description='Voltage at the connector in volts.'),
        'maximumCurrent': NumericField(required=False, description='Maximum current in ampere.'),
        'connectorFormat': Reference(
            obj='Datex2ConnectorFormatTypeEnumG',
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

datex2_connector_component = Component('Datex2Connector', datex2_connector_schema, datex2_connector_example)


electric_energy_schema = JsonSchema(
    title='Datex2ElectricEnergy',
    description='Information about the electric energy provided.',
    properties={
        'isGreenEnergy': BooleanField(required=False, description='Whether the energy is from renewable sources.'),
    },
)

electric_energy_example = {'isGreenEnergy': True}

electric_energy_component = Component('Datex2ElectricEnergy', electric_energy_schema, electric_energy_example)


electric_charging_point_schema = JsonSchema(
    title='Datex2ElectricChargingPoint',
    description='Technical infrastructure that facilitates electric charging of one vehicle at a time.',
    properties={
        'idG': StringField(description='Unique identifier of the charging point.'),
        'versionG': StringField(description='Version timestamp (ISO 8601).'),
        'deliveryUnit': Reference(obj='Datex2DeliveryUnitEnumG', description='Measurement unit for energy delivery.'),
        'currentType': Reference(obj='Datex2CurrentTypeEnumG', description='The type of current (AC/DC).'),
        'numberOfConnectors': IntegerField(minimum=0, required=False, description='Number of connectors.'),
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
        'electricEnergy': ArrayField(
            items=Reference(obj='Datex2ElectricEnergy'),
            required=False,
            description='Information about the electric energy mix.',
        ),
        'connector': ArrayField(
            items=Reference(obj='Datex2Connector'),
            description='List of available connectors.',
        ),
    },
)

electric_charging_point_example = {
    'idG': 'EVSE-1',
    'versionG': '2026-01-01T00:00:00+00:00',
    'deliveryUnit': {'value': 'kWh'},
    'currentType': {'value': 'ac'},
    'numberOfConnectors': 1,
    'availableVoltage': [400.0],
    'availableChargingPower': [22.0],
    'connector': [
        {
            'connectorType': {'value': 'iec62196T2'},
            'maxPowerAtSocket': 22.0,
            'voltage': 400.0,
            'maximumCurrent': 32.0,
            'connectorFormat': {'value': 'socket'},
        },
    ],
}

electric_charging_point_component = Component(
    'Datex2ElectricChargingPoint', electric_charging_point_schema, electric_charging_point_example
)


refill_point_g_schema = JsonSchema(
    title='Datex2RefillPointG',
    description='A refill point providing an electric charging point.',
    properties={
        'aegiElectricChargingPoint': Reference(
            obj='Datex2ElectricChargingPoint',
            description='The electric charging point at this refill point.',
        ),
    },
)

refill_point_g_example = {'aegiElectricChargingPoint': electric_charging_point_example}

refill_point_g_component = Component('Datex2RefillPointG', refill_point_g_schema, refill_point_g_example)


service_type_schema = JsonSchema(
    title='Datex2ServiceType',
    description='Type of service available at a station.',
    properties={
        'serviceType': Reference(obj='Datex2ServiceTypeEnumG', description='The service type.'),
    },
)

service_type_example = {'serviceType': {'value': 'unattended'}}

service_type_component = Component('Datex2ServiceType', service_type_schema, service_type_example)


energy_infrastructure_station_schema = JsonSchema(
    title='Datex2EnergyInfrastructureStation',
    description='A station within a site where vehicles can be supplied with energy.',
    properties={
        'idG': StringField(description='Unique identifier of the station.'),
        'versionG': StringField(description='Version timestamp (ISO 8601).'),
        'numberOfRefillPoints': IntegerField(minimum=0, description='Number of refill points at the station.'),
        'totalMaximumPower': NumericField(required=False, description='Total maximum power in kW.'),
        'serviceType': ArrayField(
            items=Reference(obj='Datex2ServiceType'),
            required=False,
            description='Types of service available.',
        ),
        'authenticationAndIdentificationMethods': ArrayField(
            items=Reference(obj='Datex2AuthenticationAndIdentificationEnumG'),
            required=False,
            description='Available authentication and identification methods.',
        ),
        'userInterfaceLanguage': ArrayField(
            items=StringField(maxLength=2),
            required=False,
            description='Languages available on the user interface.',
        ),
        'locationReference': Reference(
            obj='Datex2LocationReferenceG',
            required=False,
            description='Location reference for the station.',
        ),
        'refillPoint': ArrayField(
            items=Reference(obj='Datex2RefillPointG'),
            description='List of refill points at this station.',
        ),
    },
)

energy_infrastructure_station_example = {
    'idG': 'CS-1',
    'versionG': '2026-01-01T00:00:00+00:00',
    'numberOfRefillPoints': 2,
    'refillPoint': [refill_point_g_example],
}

energy_infrastructure_station_component = Component(
    'Datex2EnergyInfrastructureStation', energy_infrastructure_station_schema, energy_infrastructure_station_example
)


# --- Location reference schemas ---

point_coordinates_schema = JsonSchema(
    title='Datex2PointCoordinates',
    description='A pair of coordinates (WGS 84).',
    properties={
        'latitude': NumericField(description='Latitude in decimal degrees.'),
        'longitude': NumericField(description='Longitude in decimal degrees.'),
    },
)

point_coordinates_example = {'latitude': 52.52003, 'longitude': 13.40489}

point_coordinates_component = Component('Datex2PointCoordinates', point_coordinates_schema, point_coordinates_example)


address_line_schema = JsonSchema(
    title='Datex2AddressLine',
    description='One line of a postal address.',
    properties={
        'order': IntegerField(minimum=0, description='Sequence order for display.'),
        'type': Reference(obj='Datex2AddressLineTypeEnumG', description='Type of address line element.'),
        'text': Reference(obj='Datex2MultilingualString', description='Text content of the address line.'),
    },
)

address_line_example = {
    'order': 1,
    'type': {'value': 'street'},
    'text': {'values': [{'lang': 'de', 'value': 'Musterstraße'}]},
}

address_line_component = Component('Datex2AddressLine', address_line_schema, address_line_example)


address_schema = JsonSchema(
    title='Datex2Address',
    description='A street-oriented addressing structure.',
    properties={
        'postcode': StringField(required=False, description='Postal code.'),
        'city': Reference(obj='Datex2MultilingualString', required=False, description='City name.'),
        'countryCode': StringField(maxLength=2, required=False, description='ISO 3166-1 alpha-2 country code.'),
        'addressLine': ArrayField(
            items=Reference(obj='Datex2AddressLine'),
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

address_component = Component('Datex2Address', address_schema, address_example)


facility_location_schema = JsonSchema(
    title='Datex2FacilityLocation',
    description='A location with time zone and address information.',
    properties={
        'timeZone': StringField(required=False, description='IANA time zone identifier.'),
        'address': Reference(obj='Datex2Address', required=False, description='Address of the facility.'),
    },
)

facility_location_example = {'address': address_example}

facility_location_component = Component('Datex2FacilityLocation', facility_location_schema, facility_location_example)


location_extension_type_g_schema = JsonSchema(
    title='Datex2LocationExtensionTypeG',
    description='Extension for location referencing with facility location details.',
    properties={
        'FacilityLocation': Reference(
            obj='Datex2FacilityLocation',
            required=False,
            description='Facility location with address.',
        ),
    },
)

location_extension_type_g_example = {'FacilityLocation': facility_location_example}

location_extension_type_g_component = Component(
    'Datex2LocationExtensionTypeG', location_extension_type_g_schema, location_extension_type_g_example
)


area_location_schema = JsonSchema(
    title='Datex2AreaLocation',
    description='A location defined by an area with display coordinates.',
    properties={
        'coordinatesForDisplay': Reference(
            obj='Datex2PointCoordinates',
            required=False,
            description='Coordinates for display purposes.',
        ),
    },
)

area_location_example = {'coordinatesForDisplay': point_coordinates_example}

area_location_component = Component('Datex2AreaLocation', area_location_schema, area_location_example)


point_location_schema = JsonSchema(
    title='Datex2PointLocation',
    description='A point location with optional coordinates and facility location extension.',
    properties={
        'coordinatesForDisplay': Reference(
            obj='Datex2PointCoordinates',
            required=False,
            description='Coordinates for display purposes.',
        ),
        'locLocationExtensionG': Reference(
            obj='Datex2LocationExtensionTypeG',
            required=False,
            description='Extension with facility location details.',
        ),
    },
)

point_location_example = {'locLocationExtensionG': location_extension_type_g_example}

point_location_component = Component('Datex2PointLocation', point_location_schema, point_location_example)


location_reference_g_schema = JsonSchema(
    title='Datex2LocationReferenceG',
    description='A location reference combining area and point location information.',
    properties={
        'locAreaLocation': Reference(
            obj='Datex2AreaLocation',
            required=False,
            description='Area location with display coordinates.',
        ),
        'locPointLocation': Reference(
            obj='Datex2PointLocation',
            required=False,
            description='Point location with facility details.',
        ),
    },
)

location_reference_g_example = {
    'locAreaLocation': area_location_example,
    'locPointLocation': point_location_example,
}

location_reference_g_component = Component(
    'Datex2LocationReferenceG', location_reference_g_schema, location_reference_g_example
)


# --- Organisation schemas ---

external_identifier_schema = JsonSchema(
    title='Datex2ExternalIdentifier',
    description='An identifier used in an external system.',
    properties={
        'identifier': StringField(description='The identifier value.'),
        'typeOfIdentifier': Reference(obj='Datex2TypeOfIdentifierEnumG', description='Type of the identifier.'),
    },
)

external_identifier_example = {
    'identifier': 'DE*ABC',
    'typeOfIdentifier': {'value': 'extendedG', 'extendedValueG': 'operatorId'},
}

external_identifier_component = Component(
    'Datex2ExternalIdentifier', external_identifier_schema, external_identifier_example
)


an_organisation_schema = JsonSchema(
    title='Datex2AnOrganisation',
    description='An organisation with name and optional external identifiers.',
    properties={
        'name': Reference(obj='Datex2MultilingualString', description='Name of the organisation.'),
        'externalIdentifier': ArrayField(
            items=Reference(obj='Datex2ExternalIdentifier'),
            required=False,
            description='External identifiers for the organisation.',
        ),
    },
)

an_organisation_example = {
    'name': {'values': [{'lang': 'de', 'value': 'Electro Inc'}]},
}

an_organisation_component = Component('Datex2AnOrganisation', an_organisation_schema, an_organisation_example)


contact_information_schema = JsonSchema(
    title='Datex2ContactInformation',
    description='Contact information for an organisation.',
    properties={
        'telephoneNumber': StringField(required=False, description='Telephone number.'),
    },
)

contact_information_example = {'telephoneNumber': '+49123456789'}

contact_information_component = Component(
    'Datex2ContactInformation', contact_information_schema, contact_information_example
)


contact_information_g_schema = JsonSchema(
    title='Datex2ContactInformationG',
    description='Contact information wrapper.',
    properties={
        'afacContactInformation': Reference(
            obj='Datex2ContactInformation',
            required=False,
            description='Contact information details.',
        ),
    },
)

contact_information_g_example = {'afacContactInformation': contact_information_example}

contact_information_g_component = Component(
    'Datex2ContactInformationG', contact_information_g_schema, contact_information_g_example
)


organisation_unit_schema = JsonSchema(
    title='Datex2OrganisationUnit',
    description='A unit within an organisation.',
    properties={
        'contactInformation': ArrayField(
            items=Reference(obj='Datex2ContactInformationG'),
            required=False,
            description='Contact information for this unit.',
        ),
    },
)

organisation_unit_example = {'contactInformation': [contact_information_g_example]}

organisation_unit_component = Component('Datex2OrganisationUnit', organisation_unit_schema, organisation_unit_example)


referenceable_organisation_schema = JsonSchema(
    title='Datex2ReferenceableOrganisation',
    description='A referenceable organisation with ID, version, and contact details.',
    properties={
        'idG': StringField(description='Unique identifier.'),
        'versionG': StringField(description='Version identifier.'),
        'name': Reference(obj='Datex2MultilingualString', description='Name of the organisation.'),
        'organisationUnit': ArrayField(
            items=Reference(obj='Datex2OrganisationUnit'),
            required=False,
            description='Organisation units.',
        ),
    },
)

referenceable_organisation_example = {
    'idG': 'HELP',
    'versionG': '2026-01-01T00:00:00+00:00',
    'name': {'values': [{'lang': 'de', 'value': 'Helpdesk'}]},
    'organisationUnit': [organisation_unit_example],
}

referenceable_organisation_component = Component(
    'Datex2ReferenceableOrganisation', referenceable_organisation_schema, referenceable_organisation_example
)


organisation_g_schema = JsonSchema(
    title='Datex2OrganisationG',
    description='An organisation reference. Exactly one of the properties should be used.',
    properties={
        'afacAnOrganisation': Reference(
            obj='Datex2AnOrganisation',
            required=False,
            description='An inline organisation.',
        ),
        'afacReferenceableOrganisation': Reference(
            obj='Datex2ReferenceableOrganisation',
            required=False,
            description='A referenceable organisation with ID and contact details.',
        ),
    },
)

organisation_g_example = {'afacAnOrganisation': an_organisation_example}

organisation_g_component = Component('Datex2OrganisationG', organisation_g_schema, organisation_g_example)


# --- Operating hours ---

open_all_hours_schema = JsonSchema(
    title='Datex2OpenAllHours',
    description='Indicates that the facility is open 24/7. Empty object.',
    properties={},
)

open_all_hours_example = {}

open_all_hours_component = Component('Datex2OpenAllHours', open_all_hours_schema, open_all_hours_example)


operating_hours_g_schema = JsonSchema(
    title='Datex2OperatingHoursG',
    description='Operating hours specification. Exactly one of the properties should be used.',
    properties={
        'afacOpenAllHours': Reference(
            obj='Datex2OpenAllHours',
            required=False,
            description='Indicates 24/7 operation.',
        ),
    },
)

operating_hours_g_example = {'afacOpenAllHours': {}}

operating_hours_g_component = Component('Datex2OperatingHoursG', operating_hours_g_schema, operating_hours_g_example)


# --- Site / Table / Publication / Payload ---

energy_infrastructure_site_schema = JsonSchema(
    title='Datex2EnergyInfrastructureSite',
    description='A site where vehicles can be supplied with energy, including all stations and associated services.',
    properties={
        'idG': StringField(description='Unique identifier of the site.'),
        'versionG': StringField(description='Version timestamp (ISO 8601).'),
        'additionalInformation': ArrayField(
            items=Reference(obj='Datex2MultilingualString'),
            required=False,
            description='Additional information such as the site name.',
        ),
        'operatingHours': Reference(
            obj='Datex2OperatingHoursG',
            required=False,
            description='Operating hours of the site.',
        ),
        'locationReference': Reference(
            obj='Datex2LocationReferenceG',
            required=False,
            description='Geographic and address location of the site.',
        ),
        'operator': Reference(
            obj='Datex2OrganisationG',
            required=False,
            description='The operator of this site.',
        ),
        'helpdesk': Reference(
            obj='Datex2OrganisationG',
            required=False,
            description='A helpdesk service for the site.',
        ),
        'energyInfrastructureStation': ArrayField(
            items=Reference(obj='Datex2EnergyInfrastructureStation'),
            required=False,
            description='Charging stations at this site.',
        ),
    },
)

energy_infrastructure_site_example = {
    'idG': 'LOCATION-1',
    'versionG': '2026-01-01T00:00:00+00:00',
    'additionalInformation': [{'values': [{'lang': 'de', 'value': 'Test Location'}]}],
    'operatingHours': {'afacOpenAllHours': {}},
    'locationReference': location_reference_g_example,
    'operator': organisation_g_example,
    'energyInfrastructureStation': [energy_infrastructure_station_example],
}

energy_infrastructure_site_component = Component(
    'Datex2EnergyInfrastructureSite', energy_infrastructure_site_schema, energy_infrastructure_site_example
)


energy_infrastructure_table_schema = JsonSchema(
    title='Datex2EnergyInfrastructureTable',
    description='A table of sites where vehicles can be supplied with energy.',
    properties={
        'idG': StringField(description='Table identifier.'),
        'versionG': StringField(description='Table version.'),
        'energyInfrastructureSite': ArrayField(
            items=Reference(obj='Datex2EnergyInfrastructureSite'),
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
    'Datex2EnergyInfrastructureTable', energy_infrastructure_table_schema, energy_infrastructure_table_example
)


international_identifier_schema = JsonSchema(
    title='Datex2InternationalIdentifier',
    description='An international identifier with country and national identifier.',
    properties={
        'country': StringField(maxLength=2, description='ISO 3166-1 alpha-2 country code.'),
        'nationalIdentifier': StringField(description='National identifier of the data publisher.'),
    },
)

international_identifier_example = {'country': 'DE', 'nationalIdentifier': 'OCPDB'}

international_identifier_component = Component(
    'Datex2InternationalIdentifier', international_identifier_schema, international_identifier_example
)


energy_infrastructure_table_publication_schema = JsonSchema(
    title='Datex2EnergyInfrastructureTablePublication',
    description='A publication of static information on electric vehicle charging infrastructure.',
    properties={
        'lang': StringField(maxLength=2, description='Publication language (ISO 639-1).'),
        'publicationTime': StringField(description='Publication timestamp (ISO 8601).'),
        'publicationCreator': Reference(
            obj='Datex2InternationalIdentifier',
            description='Creator of the publication.',
        ),
        'energyInfrastructureTable': ArrayField(
            items=Reference(obj='Datex2EnergyInfrastructureTable'),
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
    'Datex2EnergyInfrastructureTablePublication',
    energy_infrastructure_table_publication_schema,
    energy_infrastructure_table_publication_example,
)


payload_publication_g_schema = JsonSchema(
    title='Datex2PayloadPublicationG',
    description='DATEX II payload publication with version information and table publication.',
    properties={
        'modelBaseVersionG': StringField(description='Base model version.'),
        'versionG': StringField(required=False, description='Schema version.'),
        'profileNameG': StringField(required=False, description='Profile name.'),
        'profileVersionG': StringField(required=False, description='Profile version.'),
        'aegiEnergyInfrastructureTablePublication': Reference(
            obj='Datex2EnergyInfrastructureTablePublication',
            required=False,
            description='Energy infrastructure table publication.',
        ),
    },
)

payload_publication_g_example = {
    'modelBaseVersionG': '3',
    'versionG': '3.5',
    'profileNameG': 'Afir Energy Infrastructure',
    'profileVersionG': '01-00-00',
    'aegiEnergyInfrastructureTablePublication': energy_infrastructure_table_publication_example,
}

payload_publication_g_component = Component(
    'Datex2PayloadPublicationG', payload_publication_g_schema, payload_publication_g_example
)


datex2_v35_static_payload_schema = JsonSchema(
    title='Datex2V35StaticPayload',
    description='DATEX II v3.5 static payload for energy infrastructure.',
    properties={
        'payload': Reference(obj='Datex2PayloadPublicationG', required=False, description='The payload publication.'),
    },
)

datex2_v35_static_payload_example = {'payload': payload_publication_g_example}

datex2_v35_static_payload_component = Component(
    'Datex2V35StaticPayload', datex2_v35_static_payload_schema, datex2_v35_static_payload_example
)


# --- Component list for use with @document ---

all_datex2_v35_static_components = [
    address_component,
    address_line_component,
    address_line_type_enum_g_component,
    an_organisation_component,
    area_location_component,
    authentication_and_identification_enum_g_component,
    connector_format_type_enum_g_component,
    connector_type_enum_g_component,
    contact_information_component,
    contact_information_g_component,
    current_type_enum_g_component,
    datex2_connector_component,
    datex2_v35_static_payload_component,
    delivery_unit_enum_g_component,
    electric_charging_point_component,
    electric_energy_component,
    energy_infrastructure_site_component,
    energy_infrastructure_station_component,
    energy_infrastructure_table_component,
    energy_infrastructure_table_publication_component,
    external_identifier_component,
    facility_location_component,
    international_identifier_component,
    location_extension_type_g_component,
    location_reference_g_component,
    multilingual_string_component,
    multilingual_string_value_component,
    open_all_hours_component,
    operating_hours_g_component,
    organisation_g_component,
    organisation_unit_component,
    payload_publication_g_component,
    point_coordinates_component,
    point_location_component,
    referenceable_organisation_component,
    refill_point_g_component,
    service_type_component,
    service_type_enum_g_component,
    type_of_identifier_enum_g_component,
]
