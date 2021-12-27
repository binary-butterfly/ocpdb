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

from typing import Optional
from flask import current_app, Config
from webapp.common.logger import Logger
from webapp.dependencies import dependencies


class PublicApiBaseHandler:
    """
    Base class for API handler classes (`auth.AuthHandler`, etc.)
    """
    logger: Logger
    _config: Config

    def __init__(self, logger: Optional[Logger] = None, config: Optional[Config] = None):
        self.logger = logger if logger else dependencies.logger
        self._config = config

    @property
    def config(self):
        return self._config if self._config else current_app.config
