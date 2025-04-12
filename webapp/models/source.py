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

from datetime import datetime
from enum import Enum

from sqlalchemy import Enum as SqlalchemyEnum
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utc import UtcDateTime

from .base import BaseModel


class SourceStatus(Enum):
    DISABLED = 'DISABLED'
    ACTIVE = 'ACTIVE'
    FAILED = 'FAILED'
    PROVISIONED = 'PROVISIONED'


class Source(BaseModel):
    __tablename__ = 'source'

    uid: Mapped[str] = mapped_column(String(256), nullable=False, index=True, unique=True)
    name: Mapped[str | None] = mapped_column(String(256), nullable=True)
    public_url: Mapped[str | None] = mapped_column(String(4096), nullable=True)

    static_data_updated_at: Mapped[datetime | None] = mapped_column(UtcDateTime(), nullable=True)
    realtime_data_updated_at: Mapped[datetime | None] = mapped_column(UtcDateTime(), nullable=True)

    attribution_license: Mapped[str | None] = mapped_column(Text, nullable=True)
    attribution_contributor: Mapped[str | None] = mapped_column(String(256), nullable=True)
    attribution_url: Mapped[str | None] = mapped_column(String(256), nullable=True)

    static_status: Mapped[SourceStatus] = mapped_column(
        SqlalchemyEnum(SourceStatus),
        nullable=False,
        default=SourceStatus.PROVISIONED,
    )
    realtime_status: Mapped[SourceStatus] = mapped_column(
        SqlalchemyEnum(SourceStatus),
        nullable=False,
        default=SourceStatus.PROVISIONED,
    )

    static_error_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    realtime_error_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    @property
    def combined_status(self) -> SourceStatus:
        if self.static_status != SourceStatus.ACTIVE or self.realtime_status in [
            SourceStatus.PROVISIONED,
            SourceStatus.DISABLED,
        ]:
            return self.static_status
        return self.realtime_status

    @property
    def combined_updated_at(self) -> datetime:
        if self.static_data_updated_at and self.realtime_data_updated_at:
            return max(self.static_data_updated_at, self.realtime_data_updated_at)
        if self.realtime_data_updated_at:
            return self.realtime_data_updated_at
        if self.static_data_updated_at:
            return self.static_data_updated_at
        return self.modified_at
