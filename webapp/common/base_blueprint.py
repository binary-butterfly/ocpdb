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

from flask import Blueprint as FlaskBlueprint

from webapp.dependencies import dependencies


class BaseBlueprint(FlaskBlueprint):
    documentation_base: bool = False
    documentation_auth: bool = False
    documented: bool = False

    @staticmethod
    def get_base_handler_dependencies() -> dict:
        return {
            'logger': dependencies.get_logger(),
            'config_helper': dependencies.get_config_helper(),
        }

    @staticmethod
    def get_base_method_view_dependencies() -> dict:
        return {
            'logger': dependencies.get_logger(),
            'request_helper': dependencies.get_request_helper(),
            'config_helper': dependencies.get_config_helper(),
        }
