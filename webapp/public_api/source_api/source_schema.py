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
from flask_openapi.schema import DateTimeField, EnumField, IntegerField, JsonSchema, StringField, UriField

from webapp.models import SourceStatus

source_schema = JsonSchema(
    title='Source',
    description='A data source providing charging station information.',
    properties={
        'id': IntegerField(minimum=1, description='Unique internal ID of the source.'),
        'uid': StringField(maxLength=256, description='Unique identifier of the source.'),
        'name': StringField(maxLength=256, required=False, nullable=True, description='Display name of the source.'),
        'public_url': UriField(required=False, nullable=True, description='Public URL of the source.'),
        'static_data_updated_at': DateTimeField(
            required=False, nullable=True, description='Timestamp when static data was last updated.'
        ),
        'realtime_data_updated_at': DateTimeField(
            required=False, nullable=True, description='Timestamp when realtime data was last updated.'
        ),
        'attribution_license': StringField(required=False, nullable=True, description='License for attribution.'),
        'attribution_contributor': StringField(
            maxLength=256, required=False, nullable=True, description='Contributor for attribution.'
        ),
        'attribution_url': StringField(
            maxLength=256, required=False, nullable=True, description='URL for attribution.'
        ),
        'static_status': EnumField(
            enum=SourceStatus,
            description='Status of static data import.',
        ),
        'realtime_status': EnumField(
            enum=SourceStatus,
            description='Status of realtime data import.',
        ),
        'static_error_count': IntegerField(minimum=0, description='Number of consecutive static import errors.'),
        'realtime_error_count': IntegerField(minimum=0, description='Number of consecutive realtime import errors.'),
        'created': DateTimeField(description='Timestamp when this source was created.'),
        'modified': DateTimeField(description='Timestamp when this source was last modified.'),
    },
)

source_example = {
    'id': 1,
    'uid': 'example-source',
    'name': 'Example Source',
    'public_url': 'https://example.com',
    'static_status': 'ACTIVE',
    'realtime_status': 'ACTIVE',
    'static_error_count': 0,
    'realtime_error_count': 0,
    'created': '2025-01-01T00:00:00Z',
    'modified': '2025-01-01T00:00:00Z',
}


source_component = Component('Source', source_schema, source_example)
