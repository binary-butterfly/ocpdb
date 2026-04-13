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
from flask_openapi.schema import ArrayField, JsonSchema, Reference, StringField

# --- Shared schemas ---

facility_object_versioned_reference_g_schema = JsonSchema(
    title='Datex2V37RealtimeFacilityObjectVersionedReferenceG',
    description='A versioned reference to a facility object in the static data.',
    properties={
        'targetClass': StringField(description='Target class, always "FacilityObject".'),
        'idG': StringField(description='Unique identifier of the referenced object.'),
        'versionG': StringField(required=False, description='Version timestamp (ISO 8601).'),
    },
)

facility_object_versioned_reference_g_example = {
    'targetClass': 'FacilityObject',
    'idG': 'LOCATION-1',
    'versionG': '2026-01-01T00:00:00+00:00',
}

facility_object_versioned_reference_g_component = Component(
    'Datex2V37RealtimeFacilityObjectVersionedReferenceG',
    facility_object_versioned_reference_g_schema,
    facility_object_versioned_reference_g_example,
)


international_identifier_schema = JsonSchema(
    title='Datex2V37RealtimeInternationalIdentifier',
    description='An international identifier with country and national identifier.',
    properties={
        'country': StringField(maxLength=2, description='ISO 3166-1 alpha-2 country code.'),
        'nationalIdentifier': StringField(description='National identifier of the data publisher.'),
    },
)

international_identifier_example = {'country': 'DE', 'nationalIdentifier': 'OCPDB'}

international_identifier_component = Component(
    'Datex2V37RealtimeInternationalIdentifier', international_identifier_schema, international_identifier_example
)


# --- Refill point status schemas ---

refill_point_status_enum_g_schema = JsonSchema(
    title='Datex2V37RealtimeRefillPointStatusEnumG',
    description='Status of a refill point / EVSE.',
    properties={
        'value': StringField(
            description='Status value: available, blocked, charging, faulted, inoperative, occupied, '
            'outOfOrder, outOfStock, planned, removed, reserved, unavailable, unknown.'
        ),
        'extendedValueG': StringField(required=False, description='Extended value for custom status.'),
    },
)

refill_point_status_enum_g_example = {'value': 'available'}

refill_point_status_enum_g_component = Component(
    'Datex2V37RealtimeRefillPointStatusEnumG',
    refill_point_status_enum_g_schema,
    refill_point_status_enum_g_example,
)


refill_point_status_schema = JsonSchema(
    title='Datex2V37RealtimeRefillPointStatus',
    description='Status information for a single refill point / EVSE.',
    properties={
        'reference': Reference(
            obj='Datex2V37RealtimeFacilityObjectVersionedReferenceG',
            description='Reference to the EVSE in the static data.',
        ),
        'lastUpdated': StringField(required=False, description='Last status update timestamp (ISO 8601).'),
        'status': Reference(
            obj='Datex2V37RealtimeRefillPointStatusEnumG',
            description='Current status of the refill point.',
        ),
    },
)

refill_point_status_example = {
    'reference': {
        'targetClass': 'FacilityObject',
        'idG': 'EVSE-1',
        'versionG': '2026-01-01T00:00:00+00:00',
    },
    'lastUpdated': '2026-01-01T00:00:00Z',
    'status': {'value': 'available'},
}

refill_point_status_component = Component(
    'Datex2V37RealtimeRefillPointStatus', refill_point_status_schema, refill_point_status_example
)


refill_point_status_g_schema = JsonSchema(
    title='Datex2V37RealtimeRefillPointStatusG',
    description='Wrapper for a refill point status. Exactly one of the properties should be used.',
    properties={
        'aegiRefillPointStatus': Reference(
            obj='Datex2V37RealtimeRefillPointStatus',
            required=False,
            description='Standard refill point status.',
        ),
    },
)

refill_point_status_g_example = {'aegiRefillPointStatus': refill_point_status_example}

refill_point_status_g_component = Component(
    'Datex2V37RealtimeRefillPointStatusG', refill_point_status_g_schema, refill_point_status_g_example
)


# --- Station and site status schemas ---

energy_infrastructure_station_status_schema = JsonSchema(
    title='Datex2V37RealtimeEnergyInfrastructureStationStatus',
    description='Status information for a charging station.',
    properties={
        'reference': Reference(
            obj='Datex2V37RealtimeFacilityObjectVersionedReferenceG',
            description='Reference to the charging station in the static data.',
        ),
        'refillPointStatus': ArrayField(
            items=Reference(obj='Datex2V37RealtimeRefillPointStatusG'),
            required=False,
            description='Status of each refill point / EVSE at this station.',
        ),
    },
)

energy_infrastructure_station_status_example = {
    'reference': {
        'targetClass': 'FacilityObject',
        'idG': 'CS-1',
        'versionG': '2026-01-01T00:00:00+00:00',
    },
    'refillPointStatus': [refill_point_status_g_example],
}

energy_infrastructure_station_status_component = Component(
    'Datex2V37RealtimeEnergyInfrastructureStationStatus',
    energy_infrastructure_station_status_schema,
    energy_infrastructure_station_status_example,
)


energy_infrastructure_site_status_schema = JsonSchema(
    title='Datex2V37RealtimeEnergyInfrastructureSiteStatus',
    description='Status information for an energy infrastructure site / location.',
    properties={
        'reference': Reference(
            obj='Datex2V37RealtimeFacilityObjectVersionedReferenceG',
            description='Reference to the location in the static data.',
        ),
        'lastUpdated': StringField(required=False, description='Last update timestamp (ISO 8601).'),
        'energyInfrastructureStationStatus': ArrayField(
            items=Reference(obj='Datex2V37RealtimeEnergyInfrastructureStationStatus'),
            required=False,
            description='Status of each charging station at this site.',
        ),
    },
)

energy_infrastructure_site_status_example = {
    'reference': facility_object_versioned_reference_g_example,
    'lastUpdated': '2026-01-01T00:00:00Z',
    'energyInfrastructureStationStatus': [energy_infrastructure_station_status_example],
}

energy_infrastructure_site_status_component = Component(
    'Datex2V37RealtimeEnergyInfrastructureSiteStatus',
    energy_infrastructure_site_status_schema,
    energy_infrastructure_site_status_example,
)


# --- Publication and payload schemas ---

energy_infrastructure_status_publication_schema = JsonSchema(
    title='Datex2V37RealtimeEnergyInfrastructureStatusPublication',
    description='A publication of realtime status information on electric vehicle charging infrastructure.',
    properties={
        'lang': StringField(maxLength=2, description='Publication language (ISO 639-1).'),
        'publicationTime': StringField(description='Publication timestamp (ISO 8601).'),
        'publicationCreator': Reference(
            obj='Datex2V37RealtimeInternationalIdentifier',
            description='Creator of the publication.',
        ),
        'energyInfrastructureSiteStatus': ArrayField(
            items=Reference(obj='Datex2V37RealtimeEnergyInfrastructureSiteStatus'),
            required=False,
            description='Status of each energy infrastructure site.',
        ),
    },
)

energy_infrastructure_status_publication_example = {
    'lang': 'de',
    'publicationTime': '2026-01-01T00:00:00Z',
    'publicationCreator': international_identifier_example,
    'energyInfrastructureSiteStatus': [energy_infrastructure_site_status_example],
}

energy_infrastructure_status_publication_component = Component(
    'Datex2V37RealtimeEnergyInfrastructureStatusPublication',
    energy_infrastructure_status_publication_schema,
    energy_infrastructure_status_publication_example,
)


payload_publication_g_schema = JsonSchema(
    title='Datex2V37RealtimePayloadPublicationG',
    description='DATEX II v3.7 realtime payload publication with version information and status publication.',
    properties={
        'modelBaseVersionG': StringField(description='Base model version.'),
        'versionG': StringField(required=False, description='Schema version.'),
        'profileNameG': StringField(required=False, description='Profile name.'),
        'profileVersionG': StringField(required=False, description='Profile version.'),
        'aegiEnergyInfrastructureStatusPublication': Reference(
            obj='Datex2V37RealtimeEnergyInfrastructureStatusPublication',
            required=False,
            description='Energy infrastructure status publication.',
        ),
    },
)

payload_publication_g_example = {
    'modelBaseVersionG': '3',
    'versionG': '3.7',
    'profileNameG': 'Afir Energy Infrastructure',
    'profileVersionG': '01-00-00',
    'aegiEnergyInfrastructureStatusPublication': energy_infrastructure_status_publication_example,
}

payload_publication_g_component = Component(
    'Datex2V37RealtimePayloadPublicationG', payload_publication_g_schema, payload_publication_g_example
)


datex2_v37_realtime_payload_schema = JsonSchema(
    title='Datex2V37RealtimePayload',
    description='DATEX II v3.7 realtime payload for energy infrastructure status.',
    properties={
        'payload': Reference(
            obj='Datex2V37RealtimePayloadPublicationG',
            required=False,
            description='The payload publication.',
        ),
    },
)

datex2_v37_realtime_payload_example = {'payload': payload_publication_g_example}

datex2_v37_realtime_payload_component = Component(
    'Datex2V37RealtimePayload', datex2_v37_realtime_payload_schema, datex2_v37_realtime_payload_example
)


# --- Component list for use with @document ---

all_datex2_v37_realtime_components = [
    datex2_v37_realtime_payload_component,
    energy_infrastructure_site_status_component,
    energy_infrastructure_station_status_component,
    energy_infrastructure_status_publication_component,
    facility_object_versioned_reference_g_component,
    international_identifier_component,
    payload_publication_g_component,
    refill_point_status_component,
    refill_point_status_enum_g_component,
    refill_point_status_g_component,
]
