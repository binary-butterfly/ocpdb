"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from sqlalchemy import text

from webapp.common.sqlalchemy import SQLAlchemy


def empty_all_tables(db: SQLAlchemy) -> None:
    """
    empty all tables in the database
    (this is much faster than completely deleting the database and creating a new one)
    """
    db.session.close()
    with db.engine.connect() as connection:
        connection.execute(text('SET FOREIGN_KEY_CHECKS=0;'))
        for table_name in db.metadata.tables.keys():
            connection.execute(text(f'TRUNCATE `{table_name}`;'))
        connection.execute(text('SET FOREIGN_KEY_CHECKS=1;'))
