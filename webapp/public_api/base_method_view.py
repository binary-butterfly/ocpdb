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
from validataclass.validators import IntegerValidator

from webapp.common.logger import Logger
from webapp.common.request_helper import RequestHelper
from webapp.dependencies import dependencies


class PublicApiBaseMethodView(MethodView):
    """
    Base class derived from Flask MethodView for API views.
    """
    logger: Logger
    request_helper: RequestHelper
    documentation: list
    id_validator = IntegerValidator(min_value=1)

    def __init__(self, logger: Logger = None, request_helper: RequestHelper = None):
        self.logger = logger if logger else dependencies.logger
        self.request_helper = request_helper if request_helper else RequestHelper()
        self.documentation = []
