"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2023 binary butterfly GmbH

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

from webapp.public_api.base_blueprint import BaseBlueprint
from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from .location_handler import LocationHandler


class LocationBlueprint(BaseBlueprint):
    location_handler: LocationHandler

    def __init__(self):
        self.location_handler = LocationHandler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
        )

        super().__init__('location', __name__, url_prefix='/api/public/v1/locations')

        self.add_url_rule(
            '/<int:location_id>',
            view_func=LocationIdMethodView.as_view(
                'id',
                **self.get_base_method_view_dependencies(),
                location_handler=self.location_handler,
            ),

        )


class LocationIdMethodView(BaseMethodView):
    location_handler: LocationHandler

    def __init__(self, *args, location_handler: LocationHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_handler = location_handler

    @cross_origin()
    def get(self, location_id: int):
        location = self.location_handler.get_location_by_id(location_id)
        return location
