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
from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.public_api.location_api.location_handler import LocationHandler


class OcpiLocationBlueprint(BaseBlueprint):
    documented = True
    location_handler: LocationHandler

    def __init__(self):
        self.location_handler = LocationHandler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
        )
        super().__init__('ocpi_locations', __name__, url_prefix='/locations')

        self.add_url_rule(
            '/<int:location_id>',
            view_func=LocationsMethodView.as_view(
                'location',
                **self.get_base_method_view_dependencies(),
                location_handler=self.location_handler,
            ),
        )


class OcpiLegacyLocationBlueprint(BaseBlueprint):
    """Backward compatibility: /api/ocpi/2.2/location"""

    location_handler: LocationHandler

    def __init__(self):
        self.location_handler = LocationHandler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
        )
        super().__init__('ocpi_legacy_locations', __name__, url_prefix='/location')

        self.add_url_rule(
            '/<int:location_id>',
            view_func=LocationsMethodView.as_view(
                'location',
                **self.get_base_method_view_dependencies(),
                location_handler=self.location_handler,
            ),
        )


class OcpiBaseMethodView(BaseMethodView):
    location_handler: LocationHandler

    def __init__(self, *args, location_handler: LocationHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_handler = location_handler


class LocationsMethodView(OcpiBaseMethodView):
    @cross_origin()
    def get(self, location_id: int):
        location = self.location_handler.get_location(location_id)
        return jsonify(location)
