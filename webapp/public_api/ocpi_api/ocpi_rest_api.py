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

from flask import jsonify
from flask_cors import cross_origin

from webapp.common.base_blueprint import BaseBlueprint
from webapp.dependencies import dependencies
from flask_openapi.decorator import document, Response, ResponseData, ErrorResponse, Schema
from .ocpi_handler import OcpiHandler
from webapp.common.rest import BaseMethodView


class OcpiBlueprint(BaseBlueprint):
    documented = True
    ocpi_handler: OcpiHandler

    def __init__(self):
        self.ocpi_handler = OcpiHandler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
        )
        super().__init__('locations', __name__, url_prefix='/api/ocpi/2.2/location')

        self.add_url_rule(
            '/<int:location_id>',
            view_func=LocationsMethodView.as_view(
                'location',
                **self.get_base_method_view_dependencies(),
                ocpi_handler=self.ocpi_handler,
            ),
        )


class OcpiBaseMethodView(BaseMethodView):
    ocpi_handler: OcpiHandler

    def __init__(self, *args, ocpi_handler: OcpiHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.ocpi_handler = ocpi_handler


class LocationsMethodView(OcpiBaseMethodView):

    @document(
        description='Get location with all details',
        response=[Response([ResponseData('location-reply', 'location-reply-example')]), ErrorResponse()],
        components=[
            Schema('Location', 'location-schema', 'location-example'),
            Schema('GeoLocation', 'geo-location-schema', 'geo-location-example'),
            Schema('Hours', 'hours-schema', 'hours-example'),
            Schema('RegularHours', 'regular-hours-schema', 'regular-hours-example'),
            Schema('ExceptionalPeriod', 'exceptional-period-schema', 'exceptional-period-example'),
            Schema('Evse', 'evse-schema', 'evse-example'),
            Schema('Connector', 'connector-schema', 'connector-example')
        ]
    )
    @cross_origin()
    def get(self, location_id: int):
        return jsonify(self.ocpi_handler.get_location(location_id))

