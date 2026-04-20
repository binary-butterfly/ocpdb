"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from validataclass.exceptions import InvalidValidatorOptionException
from validataclass.validators import DataclassValidator, T_Dataclass

from webapp.common.validation.multi_dict_validator import MultiDictValidationError, MultiDictValidator


class MultiValidataclassValidationError(MultiDictValidationError):
    """
    Raised by `MultiValidataclassValidator` when the input data does not match any of the configured validataclasses.

    Carries the validation errors collected from every attempted validator, keyed by the dataclass name.
    """

    code = 'multi_dataclass_validation_error'


class MultiValidataclassValidator(MultiDictValidator):
    """
    A `MultiDictValidator` variant that accepts multiple validataclasses.

    For each provided validataclass a `DataclassValidator` is created and registered with the parent
    `MultiDictValidator` under the dataclass' own `__name__`. On `validate()` the input is tried against every
    validator in the order the dataclasses were passed. The first one that validates successfully wins and its
    instance is returned. If none of them validate, a `MultiValidataclassValidationError` is raised containing every
    validator's error keyed by the dataclass name.
    """

    dataclass_classes: list[type]
    validation_error_class = MultiValidataclassValidationError

    def __init__(self, *dataclass_classes: type[T_Dataclass]) -> None:
        if not dataclass_classes:
            raise InvalidValidatorOptionException(
                'MultiValidataclassValidator requires at least one validataclass.',
            )

        validators = [DataclassValidator(dataclass_cls) for dataclass_cls in dataclass_classes]
        self.dataclass_classes = [validator.dataclass_cls for validator in validators]

        super().__init__({validator.dataclass_cls.__name__: validator for validator in validators})
