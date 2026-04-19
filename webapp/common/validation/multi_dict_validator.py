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

from typing import Any

from validataclass.exceptions import InvalidValidatorOptionException, ValidationError
from validataclass.validators import DictValidator


class MultiDictValidationError(ValidationError):
    """
    Raised by `MultiDictValidator` when the input data does not match any of the configured `DictValidator` sets.

    Carries the validation errors collected from every attempted validator, keyed by a caller-supplied name.
    """

    code = 'multi_dict_validation_error'
    validator_errors: dict[str, ValidationError]

    def __init__(self, *, validator_errors: dict[str, ValidationError], **kwargs: Any):
        super().__init__(**kwargs)
        self.validator_errors = validator_errors

    def _get_repr_dict(self) -> dict[str, str]:
        base_dict = super()._get_repr_dict()
        base_dict['validator_errors'] = repr(self.validator_errors)
        return base_dict

    def to_dict(self) -> dict[str, Any]:
        base_dict = super().to_dict()
        base_dict['validator_errors'] = {name: error.to_dict() for name, error in self.validator_errors.items()}
        return base_dict


class MultiDictValidator(DictValidator):
    """
    `DictValidator` variant that supports multiple sets of field validators.

    Each entry in `dict_validators` is a named `DictValidator` (or subclass, e.g. `DataclassValidator`) representing one
    accepted dictionary shape. On `validate()` the input is tried against every configured validator in iteration
    order. The first one that validates successfully wins and its output is returned. If none of them validate, a
    `MultiDictValidationError` (or the subclass configured via `validation_error_class`) is raised carrying every
    validator's error keyed by name.
    """

    dict_validators: dict[str, DictValidator]
    validation_error_class: type[MultiDictValidationError] = MultiDictValidationError

    def __init__(self, dict_validators: dict[str, DictValidator] | None = None) -> None:
        # Allow subclasses to declare `dict_validators` as a class attribute instead of passing it explicitly.
        if dict_validators is None:
            dict_validators = getattr(self, 'dict_validators', None)

        if not dict_validators:
            raise InvalidValidatorOptionException(
                'MultiDictValidator requires at least one named DictValidator.',
            )

        self.dict_validators = dict(dict_validators)

        # `DictValidator.__init__()` requires either `field_validators` or `default_validator`. We pass an empty dict
        # to satisfy that contract; `validate()` below is fully overridden, so the parent's single-dict behaviour is
        # never exercised.
        super().__init__(field_validators={})

    def validate(self, input_data: Any, **kwargs: Any) -> Any:
        validator_errors: dict[str, ValidationError] = {}

        for name, validator in self.dict_validators.items():
            try:
                return validator.validate(input_data, **kwargs)
            except ValidationError as error:
                validator_errors[name] = error

        raise self.validation_error_class(validator_errors=validator_errors)
