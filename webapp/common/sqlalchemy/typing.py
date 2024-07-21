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

from typing import TypeVar, Union

from sqlalchemy.orm import QueryableAttribute

__all__ = [
    'Mapped',
]

"""
Define type alias for proper type hinting in models.

Usage:
    some_integer: Mapped[int] = db.Column(db.Integer, nullable=False, ...)
    nullable_integer: Mapped[Optional[int]] = db.Column(db.Integer, nullable=True, ...)
    some_related_things: Mapped[List[Foo]] = db.relationship('Foo')
"""

T = TypeVar('T')

# Note: SQLAlchemy actually comes with a class `sqlalchemy.orm.Mapped` which is exactly for the purpose of type hinting.
# Sadly, this is supported either by PyCharm nor by typeshed (as of 2022-11-08), so we define our own type alias here.
Mapped = Union[QueryableAttribute, T]
