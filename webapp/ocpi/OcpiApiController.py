# encoding: utf-8

"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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

import os
from flask import Blueprint
from ..models import Location
from ..extensions import api_documentation
from ..api_documentation.ApiDocumentation import EndpointTag
from ..common.response import json_response

ocpi_controller = Blueprint('ocpi', __name__)

from . import OcpiCli


@ocpi_controller.route('/api/ocpi/2.2/locations')
def ocpi_api_list():
    features = []
    for location in Location.query.all():
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(location.lon), float(location.lat)]
            },
            "properties": {
                "id": location.id,
                "name": location.name
            }
        })
    return json_response({
        'type': 'FeatureCollection',
        'features': features
    })


@ocpi_controller.route('/api/ocpi/2.2/location/<int:location_id>')
@api_documentation.register(
    summary='get location details',
    tags=[EndpointTag.ocpi],
    response_schema=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'schema', 'location-reply.json')
)
def ocpi_api_single(location_id: int):
    location = Location.query.get_or_404(location_id)
    location_dict = filter_none(location.to_dict(ignore=['giroe_id', 'owner_id', 'owner_id', 'suboperator_id', 'created', 'modified', 'id', 'geometry'], transform_ocpi=True))
    location_dict['evses'] = []
    for regular_hours in location.regular_hours:
        if 'regular_hours' not in location_dict['opening_times']:
            location_dict['opening_times']['regular_hours'] = []
        location_dict['opening_times']['regular_hours'].append(regular_hours.to_dict(ignore=['location_id', 'chargepoint_id', 'created', 'modified', 'id'], transform_ocpi=True))
    for exceptional_opening in location.exceptional_openings:
        if 'exceptional_openings' not in location_dict['opening_times']:
            location_dict['opening_times']['exceptional_openings'] = []
        location_dict['opening_times']['exceptional_openings'].append(exceptional_opening.to_dict(ignore=['chargepoint_id', 'created', 'modified', 'id']))
    for exceptional_closing in location.exceptional_closings:
        if 'exceptional_closings' not in location_dict['opening_times']:
            location_dict['opening_times']['exceptional_closings'] = []
        location_dict['opening_times']['exceptional_closings'].append(exceptional_closing.to_dict(ignore=['chargepoint_id', 'created', 'modified', 'id']))
    for chargepoint in location.chargepoints:
        chargepoint_dict = chargepoint.to_dict(ignore=['external_id', 'giroe_id', 'location_id', 'created', 'modified', 'id'], transform_ocpi=True)
        chargepoint_dict['connectors'] = []
        for connector in chargepoint.connectors:
            connector_dict = filter_none(connector.to_dict(ignore=['external_id', 'giroe_id', 'chargepoint_id', 'created', 'modified', 'id']))
            chargepoint_dict['connectors'].append(connector_dict)
        for image in chargepoint.images:
            if 'images' not in chargepoint_dict:
                chargepoint_dict['images'] = []
            chargepoint_dict['images'].append(filter_none(image.to_dict(ignore=['chargepoint_id', 'location_id', 'created', 'modified', 'id', 'external_url'])))
        for related_resource in chargepoint.related_resource:
            if 'related_resource' not in chargepoint_dict:
                chargepoint_dict['related_resource'] = []
            chargepoint_dict['related_resource'].append(related_resource.to_dict(ignore=['chargepoint_id', 'created', 'modified', 'id']))

        location_dict['evses'].append(filter_none(chargepoint_dict))

    return json_response(location_dict, cors=True)


def filter_none(data: dict) -> dict:
    return {key: value for key, value in data.items() if value is not None}
