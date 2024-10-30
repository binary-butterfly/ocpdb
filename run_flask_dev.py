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

from flask_failsafe import failsafe
from werkzeug.middleware.proxy_fix import ProxyFix


@failsafe
def create_app():
    from webapp import launch
    app = launch()
    # Apply the "ProxyFix" to trust the X-Forwarded-Proto header
    app.wsgi_app = ProxyFix(app.wsgi_app)
    return app


if __name__ == "__main__":
    create_app().run(debug=True, host='0.0.0.0')
