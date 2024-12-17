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

from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy
from sqlalchemy import MetaData

from .query import Query


class SQLAlchemy(BaseSQLAlchemy):
    """
    Custom app-specific extension of the `SQLAlchemy` class from Flask-SQLAlchemy.
    """

    # Naming convention for automatic naming of constraints
    _naming_convention = {
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_N_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_N_name)s',
        'pk': 'pk_%(table_name)s',
    }

    def __init__(self, *args, **kwargs):
        # Set custom query class and metadata
        kwargs.update(
            query_class=Query,
            metadata=MetaData(naming_convention=self._naming_convention),
        )

        # Initialize Flask SQLAlchemy
        super().__init__(*args, **kwargs)
