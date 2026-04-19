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

import pytest
from validataclass.exceptions import InvalidValidatorOptionException, ValidationError
from validataclass.validators import DictValidator, IntegerValidator, StringValidator

from webapp.common.validation.multi_dict_validator import MultiDictValidationError, MultiDictValidator


def _string_shape_validator() -> DictValidator:
    return DictValidator(field_validators={'name': StringValidator()})


def _integer_shape_validator() -> DictValidator:
    return DictValidator(field_validators={'amount': IntegerValidator()})


def _mixed_shape_validator() -> DictValidator:
    return DictValidator(
        field_validators={
            'name': StringValidator(),
            'amount': IntegerValidator(),
        },
    )


class MultiDictValidatorTest:
    """Tests for MultiDictValidator and MultiDictValidationError."""

    @staticmethod
    def test_requires_at_least_one_validator():
        with pytest.raises(InvalidValidatorOptionException):
            MultiDictValidator({})

    @staticmethod
    def test_requires_at_least_one_validator_when_not_provided():
        with pytest.raises(InvalidValidatorOptionException):
            MultiDictValidator()

    @staticmethod
    def test_validates_against_first_matching_validator():
        validator = MultiDictValidator(
            {
                'string_shape': _string_shape_validator(),
                'integer_shape': _integer_shape_validator(),
            },
        )

        result = validator.validate({'name': 'hello'})

        assert result == {'name': 'hello'}

    @staticmethod
    def test_validates_against_second_validator_when_first_fails():
        validator = MultiDictValidator(
            {
                'string_shape': _string_shape_validator(),
                'integer_shape': _integer_shape_validator(),
            },
        )

        result = validator.validate({'amount': 42})

        assert result == {'amount': 42}

    @staticmethod
    def test_returns_first_successful_match_in_iteration_order():
        # Both validators would accept this input, but 'first_string' comes first in the dict.
        validator = MultiDictValidator(
            {
                'first_string': _string_shape_validator(),
                'mixed': _mixed_shape_validator(),
            },
        )

        result = validator.validate({'name': 'hello', 'amount': 7})

        assert result == {'name': 'hello'}

    @staticmethod
    def test_raises_multi_error_when_none_matches():
        validator = MultiDictValidator(
            {
                'string_shape': _string_shape_validator(),
                'integer_shape': _integer_shape_validator(),
            },
        )

        with pytest.raises(MultiDictValidationError) as exc_info:
            validator.validate({'unrelated': 'value'})

        error = exc_info.value
        assert error.code == 'multi_dict_validation_error'
        assert set(error.validator_errors.keys()) == {'string_shape', 'integer_shape'}
        assert all(isinstance(inner, ValidationError) for inner in error.validator_errors.values())

    @staticmethod
    def test_multi_error_to_dict_recurses_into_inner_errors():
        validator = MultiDictValidator(
            {
                'string_shape': _string_shape_validator(),
                'integer_shape': _integer_shape_validator(),
            },
        )

        with pytest.raises(MultiDictValidationError) as exc_info:
            validator.validate({'unrelated': 'value'})

        error_dict = exc_info.value.to_dict()

        assert error_dict['code'] == 'multi_dict_validation_error'
        assert set(error_dict['validator_errors'].keys()) == {'string_shape', 'integer_shape'}
        for inner_dict in error_dict['validator_errors'].values():
            assert 'code' in inner_dict

    @staticmethod
    def test_multi_error_repr_mentions_validator_errors():
        validator = MultiDictValidator(
            {
                'string_shape': _string_shape_validator(),
                'integer_shape': _integer_shape_validator(),
            },
        )

        with pytest.raises(MultiDictValidationError) as exc_info:
            validator.validate({'unrelated': 'value'})

        error_repr = repr(exc_info.value)

        assert 'validator_errors' in error_repr
        assert 'string_shape' in error_repr
        assert 'integer_shape' in error_repr

    @staticmethod
    def test_non_dict_input_raises_multi_error():
        validator = MultiDictValidator(
            {
                'string_shape': _string_shape_validator(),
                'integer_shape': _integer_shape_validator(),
            },
        )

        with pytest.raises(MultiDictValidationError) as exc_info:
            validator.validate('not-a-dict')

        assert set(exc_info.value.validator_errors.keys()) == {'string_shape', 'integer_shape'}

    @staticmethod
    def test_is_subclass_of_dict_validator():
        validator = MultiDictValidator({'string_shape': _string_shape_validator()})

        assert isinstance(validator, DictValidator)

    @staticmethod
    def test_custom_subclass_can_override_validation_error_class():
        class CustomError(MultiDictValidationError):
            code = 'custom_multi_dict_error'

        class CustomMultiDictValidator(MultiDictValidator):
            validation_error_class = CustomError

        validator = CustomMultiDictValidator({'string_shape': _string_shape_validator()})

        with pytest.raises(CustomError) as exc_info:
            validator.validate({'unrelated': 'value'})

        assert exc_info.value.code == 'custom_multi_dict_error'
        assert set(exc_info.value.validator_errors.keys()) == {'string_shape'}

    @staticmethod
    def test_subclass_can_declare_dict_validators_as_class_attribute():
        class PresetMultiDictValidator(MultiDictValidator):
            dict_validators = {
                'string_shape': _string_shape_validator(),
                'integer_shape': _integer_shape_validator(),
            }

        validator = PresetMultiDictValidator()
        result = validator.validate({'amount': 99})

        assert result == {'amount': 99}

    @staticmethod
    def test_dict_validators_is_copied_not_referenced():
        validators = {'string_shape': _string_shape_validator()}
        validator = MultiDictValidator(validators)

        validators['integer_shape'] = _integer_shape_validator()

        assert 'integer_shape' not in validator.dict_validators
