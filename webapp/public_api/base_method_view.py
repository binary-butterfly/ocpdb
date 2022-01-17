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

from flask.views import MethodView

from webapp.common.logger import Logger
from webapp.common.request_helper import RequestHelper
from webapp.common.config import ConfigHelper


class PublicApiBaseMethodView(MethodView):
    """
    Base class derived from Flask MethodView for API views.
    """
    logger: Logger
    request_helper: RequestHelper
    config_helper: ConfigHelper
    documentation: list

    def __init__(self, logger: Logger, request_helper: RequestHelper, config_helper: ConfigHelper):
        self.logger = logger
        self.config_helper = config_helper
        self.request_helper = request_helper
        self.documentation = []
