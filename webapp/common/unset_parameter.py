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

__all__ = ['UnsetParameter', 'UnsetParameterType']


class UnsetParameterType:
    """
    The `UnsetParameter` sentinel object can be used as a default value for optional function parameters to distinguish it from None.
    """

    def __call__(self):
        return self

    def __repr__(self):
        return 'UnsetParameter'

    def __str__(self):
        return '<UnsetParameter>'

    def __bool__(self):
        return False


# Create sentinel object UnsetParameter
UnsetParameter = UnsetParameterType()
UnsetParameterType.__new__ = lambda cls: UnsetParameter
