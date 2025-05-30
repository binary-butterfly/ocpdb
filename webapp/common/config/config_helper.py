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

from typing import TYPE_CHECKING, Any, Optional

from flask import Config

if TYPE_CHECKING:
    from webapp.common.flask_app import App


class ConfigHelper:
    """
    Helper class that wraps the application config.
    """

    app: 'App'

    def __init__(self, app: Optional['App'] = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: 'App'):
        self.app = app

    def get_config(self) -> Config:
        return self.app.config

    def get(self, key: str, default: Any = None) -> Any:
        return self.app.config.get(key, default)
