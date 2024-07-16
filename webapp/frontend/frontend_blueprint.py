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

from flask import Blueprint, jsonify, render_template
from flask.views import MethodView

from webapp.common.config import ConfigHelper
from webapp.dependencies import dependencies


class FrontendBlueprint(Blueprint):
    documentation_base = True

    def __init__(self):
        super().__init__('frontend', __name__, url_prefix='', template_folder='templates')

        self.add_url_rule(
            '/',
            view_func=FrontendFrontpageMethodView.as_view(
                'frontpage',
                config_helper=dependencies.get_config_helper(),
            ),
        )


class FrontendFrontpageMethodView(MethodView):
    config_helper: ConfigHelper

    def __init__(self, *args, config_helper: ConfigHelper, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_helper = config_helper

    def get(self):
        if self.config_helper.get('SHOW_MAP'):
            return render_template('frontpage.html')

        return jsonify({
            'application': 'ocpdb',
            'documentation': {
                'public': f'{self.config_helper.get("PROJECT_URL")}/documentation/public.html',
                'server': f'{self.config_helper.get("PROJECT_URL")}/documentation/server.html',
            },
        })
