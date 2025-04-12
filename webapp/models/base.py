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

from datetime import datetime, timezone

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import UserDefinedType
from sqlalchemy_utc import UtcDateTime

from webapp.extensions import db


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_unicode_ci',
    }

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    created: Mapped[datetime] = mapped_column(
        UtcDateTime(), nullable=False, default=lambda: datetime.now(tz=timezone.utc)
    )
    modified: Mapped[datetime] = mapped_column(
        UtcDateTime(),
        nullable=False,
        default=datetime.now(tz=timezone.utc),
        onupdate=datetime.now(tz=timezone.utc),
    )

    def to_dict(self, fields: list[str] | None = None, ignore: list[str] | None = None) -> dict:
        result = {}
        for field in self.metadata.tables[self.__tablename__].c.keys():
            if fields is not None and field not in fields:
                continue
            if ignore is not None and field in ignore:
                continue
            result[field] = getattr(self, field)
        return result


class Point(UserDefinedType):
    cache_ok = True

    def get_col_spec(self) -> str:
        dialect_name = db.session.get_bind().dialect.name
        if dialect_name == 'postgresql':
            return 'GEOMETRY'
        if dialect_name == 'mysql':
            return 'POINT'
        raise Exception('unsupported dialect')
