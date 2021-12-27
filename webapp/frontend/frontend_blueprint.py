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

from flask import Blueprint, Flask, render_template
from flask.views import MethodView


class FrontendBlueprint(Blueprint):
    documentation_base = True

    def __init__(self, app: Flask):
        super().__init__('frontend', __name__, url_prefix='', template_folder='templates')

        self.add_url_rule(
            '/',
            view_func=FrontendFrontpageMethodView.as_view('frontpage')
        )


class FrontendFrontpageMethodView(MethodView):
    def get(self):
        return render_template('frontpage.html')
