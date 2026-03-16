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

from flask import jsonify
from flask_cors import cross_origin

from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.public_api.base_blueprint import BaseBlueprint

from .datex2_handler import Datex2Handler


class Datex2Blueprint(BaseBlueprint):
    documented = True
    datex2_handler: Datex2Handler

    def __init__(self):
        self.datex2_handler = Datex2Handler(
            **self.get_base_handler_dependencies(),
            location_repository=dependencies.get_location_repository(),
        )

        super().__init__('datex2', __name__, url_prefix='/api/public/datex/v3.6/recharging')

        self.add_url_rule(
            '/static',
            view_func=Datex2StaticMethodView.as_view(
                'datex_recharging_static',
                **self.get_base_method_view_dependencies(),
                datex2_handler=self.datex2_handler,
            ),
        )

        self.add_url_rule(
            '/realtime',
            view_func=Datex2RealtimeMethodView.as_view(
                'datex_recharging_realtime',
                **self.get_base_method_view_dependencies(),
                datex2_handler=self.datex2_handler,
            ),
        )


class Datex2StaticMethodView(BaseMethodView):
    datex2_handler: Datex2Handler

    def __init__(self, *args, datex2_handler: Datex2Handler, **kwargs):
        super().__init__(*args, **kwargs)
        self.datex2_handler = datex2_handler

    @cross_origin()
    def get(self):
        result = self.datex2_handler.get_datex2_payload()
        return jsonify(result)


class Datex2RealtimeMethodView(BaseMethodView):
    datex2_handler: Datex2Handler

    def __init__(self, *args, datex2_handler: Datex2Handler, **kwargs):
        super().__init__(*args, **kwargs)
        self.datex2_handler = datex2_handler

    @cross_origin()
    def get(self):
        result = self.datex2_handler.get_datex2_realtime_payload()
        return jsonify(result)
