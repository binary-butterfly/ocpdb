"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2022 binary butterfly GmbH

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

from flask_sqlalchemy.query import Query as BaseQuery
from sqlalchemy import func


class Query(BaseQuery):
    def count_items(self):
        count_query = (self.statement.with_only_columns([func.count()]).order_by(None))
        return self.session.execute(count_query).scalar()
