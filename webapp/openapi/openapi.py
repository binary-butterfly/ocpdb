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

from flask import jsonify, render_template
from webapp.common.base_blueprint import BaseBlueprint
from .openapi_cli import documentation_generate
from .openapi_generator import generate_openapi


openapi_json_blueprint = BaseBlueprint('openapi_json', 'openapi_json')


@openapi_json_blueprint.route('/<base_path>.html')
def render_documentation_html(base_path: str):
    return render_template('openapi.html', base_path=base_path)


@openapi_json_blueprint.route('/<base_path>.json')
def render_documentation_json(base_path: str):
    return jsonify(generate_openapi(base_path))


class OpenApiDocumentation(BaseBlueprint):

    def __init__(self):
        super().__init__('openapi', __name__, url_prefix='/documentation', template_folder='templates')

        self.cli.add_command(documentation_generate)

        self.register_blueprint(openapi_json_blueprint)


