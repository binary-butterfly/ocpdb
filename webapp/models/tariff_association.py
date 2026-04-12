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

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, ForeignKey, Index, String
from sqlalchemy import Enum as SqlalchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utc import UtcDateTime

from .base import BaseModel
from .connector_tariff_association import ConnectorTariffAssociation
from .enums import TariffAudience
from .evse_tariff_association import EvseTariffAssociation

if TYPE_CHECKING:
    from .connector import Connector
    from .evse import Evse
    from .tariff import Tariff


class TariffAssociation(BaseModel):
    __tablename__ = 'tariff_association'
    __table_args__ = (Index('ix_tariff_association_uid_source', 'uid', 'source'),)

    tariff: Mapped['Tariff'] = relationship('Tariff', back_populates='tariff_associations')
    tariff_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('tariff.id', use_alter=True),
        nullable=False,
        index=True,
    )

    evses: Mapped[list['Evse']] = relationship(
        'Evse',
        secondary=EvseTariffAssociation.__table__,
        back_populates='tariff_associations',
    )
    connectors: Mapped[list['Connector']] = relationship(
        'Connector',
        secondary=ConnectorTariffAssociation.__table__,
        back_populates='tariff_associations',
    )

    uid: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    source: Mapped[str] = mapped_column(String(64), index=True, nullable=False)

    audience: Mapped[TariffAudience | None] = mapped_column(SqlalchemyEnum(TariffAudience), nullable=True)

    start_date_time: Mapped[datetime] = mapped_column(UtcDateTime(), nullable=False)
    last_updated: Mapped[datetime] = mapped_column(UtcDateTime(), nullable=False)

    def to_dict(self, *args, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []
        ignore += [
            'created',
            'modified',
            'tariff_id',
        ]

        result = super().to_dict(*args, ignore=ignore, **kwargs)

        result['id'] = str(self.id)

        return result
