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
from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.exceptions import InvalidValidatorOptionException, ValidationError
from validataclass.validators import IntegerValidator, StringValidator

from webapp.common.validation import (
    MultiValidataclassValidationError,
    MultiValidataclassValidator,
)


@validataclass
class _StringShape(ValidataclassMixin):
    name: str = StringValidator()
    label: str = StringValidator(), Default('default-label')


@validataclass
class _IntegerShape(ValidataclassMixin):
    amount: int = IntegerValidator()


@validataclass
class _MixedShape(ValidataclassMixin):
    name: str = StringValidator()
    amount: int = IntegerValidator()


class MultiValidataclassValidatorTest:
    """Tests for MultiValidataclassValidator and MultiValidataclassValidationError."""

    @staticmethod
    def test_requires_at_least_one_dataclass():
        with pytest.raises(InvalidValidatorOptionException):
            MultiValidataclassValidator()

    @staticmethod
    def test_validates_against_first_matching_dataclass():
        validator = MultiValidataclassValidator(_StringShape, _IntegerShape)

        result = validator.validate({'name': 'hello'})

        assert isinstance(result, _StringShape)
        assert result.name == 'hello'
        assert result.label == 'default-label'

    @staticmethod
    def test_validates_against_second_dataclass_when_first_fails():
        validator = MultiValidataclassValidator(_StringShape, _IntegerShape)

        result = validator.validate({'amount': 42})

        assert isinstance(result, _IntegerShape)
        assert result.amount == 42

    @staticmethod
    def test_returns_first_successful_match_when_multiple_would_match():
        # Input that matches both _StringShape (name required) and _MixedShape (name + amount required)
        validator = MultiValidataclassValidator(_MixedShape, _StringShape)

        result = validator.validate({'name': 'hello', 'amount': 7})

        assert isinstance(result, _MixedShape)
        assert result.name == 'hello'
        assert result.amount == 7

    @staticmethod
    def test_raises_multi_error_when_none_matches():
        validator = MultiValidataclassValidator(_StringShape, _IntegerShape)

        with pytest.raises(MultiValidataclassValidationError) as exc_info:
            validator.validate({'unrelated': 'value'})

        error = exc_info.value
        assert error.code == 'multi_dataclass_validation_error'
        assert set(error.validator_errors.keys()) == {'_StringShape', '_IntegerShape'}
        assert all(isinstance(inner, ValidationError) for inner in error.validator_errors.values())

    @staticmethod
    def test_multi_error_to_dict_includes_all_validator_errors():
        validator = MultiValidataclassValidator(_StringShape, _IntegerShape)

        with pytest.raises(MultiValidataclassValidationError) as exc_info:
            validator.validate({'unrelated': 'value'})

        error_dict = exc_info.value.to_dict()

        assert error_dict['code'] == 'multi_dataclass_validation_error'
        assert set(error_dict['validator_errors'].keys()) == {'_StringShape', '_IntegerShape'}
        # Inner errors are recursively converted
        for inner_dict in error_dict['validator_errors'].values():
            assert 'code' in inner_dict

    @staticmethod
    def test_multi_error_repr_includes_validator_errors():
        validator = MultiValidataclassValidator(_StringShape, _IntegerShape)

        with pytest.raises(MultiValidataclassValidationError) as exc_info:
            validator.validate({'unrelated': 'value'})

        error_repr = repr(exc_info.value)

        assert 'validator_errors' in error_repr
        assert '_StringShape' in error_repr
        assert '_IntegerShape' in error_repr

    @staticmethod
    def test_non_dict_input_raises_multi_error():
        validator = MultiValidataclassValidator(_StringShape, _IntegerShape)

        with pytest.raises(MultiValidataclassValidationError) as exc_info:
            validator.validate('not-a-dict')

        assert set(exc_info.value.validator_errors.keys()) == {'_StringShape', '_IntegerShape'}

    @staticmethod
    def test_dataclass_classes_are_exposed():
        validator = MultiValidataclassValidator(_StringShape, _IntegerShape)

        assert validator.dataclass_classes == [_StringShape, _IntegerShape]

    @staticmethod
    def test_is_subclass_of_multi_dict_validator():
        from webapp.common.validation.multi_dict_validator import MultiDictValidator

        validator = MultiValidataclassValidator(_StringShape)

        assert isinstance(validator, MultiDictValidator)

    @staticmethod
    def test_multi_validataclass_error_is_subclass_of_multi_dict_error():
        from webapp.common.validation.multi_dict_validator import MultiDictValidationError

        assert issubclass(MultiValidataclassValidationError, MultiDictValidationError)

    @staticmethod
    def test_single_dataclass_behaves_like_dataclass_validator():
        validator = MultiValidataclassValidator(_StringShape)

        result = validator.validate({'name': 'solo'})

        assert isinstance(result, _StringShape)
        assert result.name == 'solo'

    @staticmethod
    def test_validation_error_is_raised_as_multi_error_with_single_dataclass():
        validator = MultiValidataclassValidator(_StringShape)

        with pytest.raises(MultiValidataclassValidationError) as exc_info:
            validator.validate({})

        assert list(exc_info.value.validator_errors.keys()) == ['_StringShape']
