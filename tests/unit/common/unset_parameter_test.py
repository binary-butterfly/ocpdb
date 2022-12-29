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


from copy import copy

from webapp.common.unset_parameter import UnsetParameter, UnsetParameterType


class UnsetParameterTest:
    """ Tests for the UnsetParameter sentinel object and its type UnsetParameterType. """

    @staticmethod
    def test_unset_parameter():
        """ Test UnsetParameter and its magic methods. """
        assert type(UnsetParameter) is UnsetParameterType
        assert repr(UnsetParameter) == 'UnsetParameter'
        assert str(UnsetParameter) == '<UnsetParameter>'
        assert bool(UnsetParameter) is False

    @staticmethod
    def test_unset_parameter_unique():
        """ Test that UnsetParameter is a unique sentinel object, i.e. all UnsetParameter values are the same. """
        unset_parameter1 = UnsetParameter
        unset_parameter2 = copy(unset_parameter1)
        unset_parameter3 = UnsetParameterType()
        assert unset_parameter1 is unset_parameter2 is unset_parameter3 is UnsetParameter

        # Test that calling the UnsetParameter returns the UnsetParameter itself
        assert UnsetParameter() is UnsetParameter
