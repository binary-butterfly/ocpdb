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

from typing import Any, TYPE_CHECKING

from flask.views import MethodView
from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator, T_Dataclass

from webapp.common.config import ConfigHelper
from webapp.common.unset_parameter import UnsetParameter
from .exceptions import InputValidationException
from .request_helper import RequestHelper

if TYPE_CHECKING:
    from webapp.common.logger import Logger


class BaseMethodView(MethodView):
    """
    Base class derived from Flask's `MethodView` for rest API views.
    """

    # Dependencies
    logger: 'Logger'
    request_helper: RequestHelper
    config_helper: ConfigHelper

    def __init__(
        self,
        *,
        logger: 'Logger',
        request_helper: RequestHelper,
        config_helper: ConfigHelper,
    ):
        self.logger = logger
        self.request_helper = request_helper
        self.config_helper = config_helper

    def validate_query_args(self, validator: DataclassValidator[T_Dataclass]) -> T_Dataclass:
        """
        Gets the query arguments from the current request and validates them using a `DataclassValidator`.

        If the validator raises a `ValidationError`, it is caught and wrapped inside an `InputValidationException`.
        """
        try:
            raw_input = self.request_helper.get_query_args(skip_empty=True)
            return validator.validate(raw_input)
        except ValidationError as e:
            raise InputValidationException('Validation errors in query parameters.', data=e.to_dict())

    def validate_request(self, validator: DataclassValidator[T_Dataclass], *, default: Any = UnsetParameter) -> T_Dataclass:
        """
        Gets the parsed JSON body from the current request and validates it using a `DataclassValidator`.

        If no valid JSON body is present in the request a `WrongContentTypeException` is raised, unless the `default`
        parameter is set, in which case the value of it will be used as input for the validator.

        If the validator raises a `ValidationError`, it is caught and wrapped inside an `InputValidationException`.
        """
        try:
            raw_input = self.request_helper.get_parsed_json(default=default)
            return validator.validate(raw_input)
        except ValidationError as e:
            raise InputValidationException('Validation errors in request body.', data=e.to_dict())

