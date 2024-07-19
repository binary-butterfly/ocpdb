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
from typing import Optional

from sqlalchemy.orm import Mapped
from sqlalchemy_utc import UtcDateTime

from webapp.extensions import db

from .base import BaseModel


class SourceStatus(Enum):
    DISABLED = 'DISABLED'
    ACTIVE = 'ACTIVE'
    FAILED = 'FAILED'
    PROVISIONED = 'PROVISIONED'


class Source(db.Model, BaseModel):
    __tablename__ = 'source'

    uid: Mapped[str] = db.Column(db.String(256), nullable=False, index=True)
    name: Mapped[str] = db.Column(db.String(256), nullable=True)
    public_url: Mapped[Optional[str]] = db.Column(db.String(4096), nullable=True)

    static_data_updated_at: Mapped[Optional[datetime]] = db.Column(UtcDateTime(), nullable=True)
    realtime_data_updated_at: Mapped[Optional[datetime]] = db.Column(UtcDateTime(), nullable=True)

    attribution_license: Mapped[Optional[str]] = db.Column(db.Text(), nullable=True)
    attribution_contributor: Mapped[Optional[str]] = db.Column(db.String(256), nullable=True)
    attribution_url: Mapped[Optional[str]] = db.Column(db.String(256), nullable=True)

    static_status: Mapped[SourceStatus] = db.Column(db.Enum(SourceStatus), nullable=False, default=SourceStatus.PROVISIONED)
    realtime_status: Mapped[SourceStatus] = db.Column(db.Enum(SourceStatus), nullable=False, default=SourceStatus.PROVISIONED)

    static_error_count: Mapped[int] = db.Column(db.Integer(), nullable=False, default=0)
    realtime_error_count: Mapped[int] = db.Column(db.Integer(), nullable=False, default=0)

    @property
    def combined_status(self) -> SourceStatus:
        if self.static_status != SourceStatus.ACTIVE or self.realtime_status in [SourceStatus.PROVISIONED, SourceStatus.DISABLED]:
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
