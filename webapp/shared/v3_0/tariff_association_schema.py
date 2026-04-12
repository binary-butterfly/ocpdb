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
from flask_openapi.schema import ArrayField, DateTimeField, EnumField, JsonSchema, Reference, StringField

from webapp.models.enums import TariffAudience

tariff_association_evse_schema = JsonSchema(
    title='TariffAssociationEvse',
    description='Reference to an EVSE linked to a TariffAssociation.',
    properties={
        'evse_uid': StringField(maxLength=36, description='UID of the associated EVSE.'),
    },
)

tariff_association_evse_component = Component(
    'TariffAssociationEvse',
    tariff_association_evse_schema,
    {},
)


tariff_association_connector_schema = JsonSchema(
    title='TariffAssociationConnector',
    description='Reference to a Connector linked to a TariffAssociation.',
    properties={
        'connector_id': StringField(maxLength=36, description='ID of the associated Connector.'),
    },
)

tariff_association_connector_component = Component(
    'TariffAssociationConnector',
    tariff_association_connector_schema,
    {},
)


tariff_association_schema = JsonSchema(
    title='TariffAssociation',
    description='A TariffAssociation links a Tariff to EVSEs and Connectors.',
    properties={
        'id': StringField(maxLength=36, description='Uniquely identifies the tariff association.'),
        'original_id': StringField(maxLength=64, description='Original UID of the tariff association from the source.'),
        'source': StringField(maxLength=64, description='Source identifier.'),
        'tariff_id': StringField(maxLength=36, description='ID of the associated Tariff.'),
        'audience': EnumField(enum=TariffAudience, required=False, description='Target audience for this tariff.'),
        'evses': ArrayField(items=Reference(obj='TariffAssociationEvse'), description='List of associated EVSEs.'),
        'connectors': ArrayField(
            items=Reference(obj='TariffAssociationConnector'),
            description='List of associated Connectors.',
        ),
        'start_date_time': DateTimeField(description='The time when this tariff association becomes active.'),
        'last_updated': DateTimeField(description='Timestamp when this TariffAssociation was last updated.'),
    },
)


tariff_association_example = {}


tariff_association_component = Component('TariffAssociation', tariff_association_schema, tariff_association_example)


all_tariff_association_components = [
    tariff_association_component,
    tariff_association_evse_component,
    tariff_association_connector_component,
]
