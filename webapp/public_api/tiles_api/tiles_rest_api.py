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

from webapp.common.base_blueprint import BaseBlueprint
from webapp.common.response import protobuf_response
from webapp.common.rest import BaseMethodView
from webapp.dependencies import dependencies
from webapp.openapi.openapi_decorator import document, Parameter
from .tiles_handler import TilesHandler


class TilesBlueprint(BaseBlueprint):
    documented = True
    tiles_handler: TilesHandler

    def __init__(self):
        self.tiles_handler = TilesHandler(
            **self.get_base_handler_dependencies(),
            location_respository=dependencies.get_location_repository(),
        )
        super().__init__('tiles', __name__, url_prefix='/tiles')

        self.add_url_rule(
            '/<int:z>/<int:x>/<int:y>.mvt',
            view_func=TilesMethodView.as_view(
                'tiles',
                **self.get_base_method_view_dependencies(),
                tiles_handler=self.tiles_handler,
            ),
        )


class TilesMethodView(BaseMethodView):
    tiles_handler: TilesHandler

    def __init__(self, *args, tiles_handler: TilesHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.tiles_handler = tiles_handler

    @document(
        description='Generates a tile.',
        path=[
            Parameter('x', schema=int, example=1),
            Parameter('y', schema=int, example=1),
            Parameter('z', schema=int, example=1)
        ]
    )
    def get(self, x: int, y: int, z: int):
        return protobuf_response(
            self.tiles_handler.generate_tile(x, y, z, static=self.request_helper.get_query_args().get('static') == '1')
        )

