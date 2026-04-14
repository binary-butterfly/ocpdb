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

from flask_openapi.decorator import Parameter
from flask_openapi.schema import AnyOfField, DateTimeField, IntegerField, NumericField, StringField

location_search_query_parameters = [
    Parameter(
        'sorted_by',
        schema=AnyOfField(allowed_values=['name', 'created', 'modified'], required=False, default='name'),
    ),
    Parameter('name', schema=StringField(required=False)),
    Parameter('source_uid', schema=StringField(required=False), example='bnetza_api'),
    Parameter(
        'source_uids',
        schema=StringField(required=False),
        example='bnetza_api,something_else',
        description='Comma separated list of sources',
    ),
    Parameter(
        'exclude_source_uid',
        schema=StringField(required=False),
        example='bnetza_api',
        description='Sources to exclude',
    ),
    Parameter(
        'exclude_source_uids',
        schema=StringField(required=False),
        example='bnetza_api,something_else',
        description='Comma separated list of sources which should be excluded',
    ),
    Parameter('address', schema=StringField(required=False), example='Erlenweg', description='Contain query'),
    Parameter('postal_code', schema=StringField(required=False), example='59423'),
    Parameter('city', schema=StringField(required=False), example='Bad Gateway', description='Contain query'),
    Parameter('country', schema=StringField(required=False), example='59423'),
    Parameter('operator_name', schema=StringField(required=False), example='Electro Inc'),
    Parameter(
        'lat',
        schema=NumericField(required=False),
        example='51.58',
        description='Radius, lat and lon always have to be set together.',
    ),
    Parameter(
        'lon',
        schema=NumericField(required=False),
        example='7.67',
        description='Radius, lat and lon always have to be set together.',
    ),
    Parameter(
        'radius',
        schema=IntegerField(required=False),
        example='1000',
        description='In meter. Radius, lat and lon always have to be set together.',
    ),
    Parameter('lat_min', schema=NumericField(), example=55.0, description='Bounding box'),
    Parameter('lat_max', schema=NumericField(), example=55.5, description='Bounding box'),
    Parameter('lon_min', schema=NumericField(), example=5.0, description='Bounding box'),
    Parameter('lon_max', schema=NumericField(), example=5.5, description='Bounding box'),
    Parameter('last_updated_since', schema=DateTimeField(), example='2023-01-01T00:00:00Z'),
    Parameter('evse_status_last_updated_since', schema=DateTimeField(), example='2023-01-01T00:00:00Z'),
    Parameter('limit', schema=IntegerField(maximum=1000, required=False, default=100)),
]
