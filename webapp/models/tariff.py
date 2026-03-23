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

import json
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Index, String, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utc import UtcDateTime

from webapp.common.json import DefaultJSONEncoder

from .base import BaseModel

if TYPE_CHECKING:
    from .tariff_association import TariffAssociation


class Tariff(BaseModel):
    __tablename__ = 'tariff'
    __table_args__ = (Index('ix_tariff_uid_source', 'uid', 'source'),)

    tariff_associations: Mapped[list['TariffAssociation']] = relationship(
        'TariffAssociation',
        back_populates='tariff',
        cascade='all, delete, delete-orphan',
    )

    uid: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    source: Mapped[str] = mapped_column(String(64), index=True, nullable=False)

    currency: Mapped[str | None] = mapped_column(String(3), nullable=True)

    _elements: Mapped[str] = mapped_column('elements', Text, nullable=False)

    tariff_alt_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    _tariff_alt_text: Mapped[str | None] = mapped_column('tariff_alt_text', Text, nullable=True)
    _min_price: Mapped[str | None] = mapped_column('min_price', Text, nullable=True)
    _max_price: Mapped[str | None] = mapped_column('max_price', Text, nullable=True)
    _energy_mix: Mapped[str | None] = mapped_column('energy_mix', Text, nullable=True)

    last_updated: Mapped[datetime] = mapped_column(UtcDateTime(), nullable=False)

    @hybrid_property
    def tariff_alt_text(self) -> list[dict] | None:
        if self._tariff_alt_text is None:
            return None
        return json.loads(self._tariff_alt_text)

    @tariff_alt_text.setter
    def tariff_alt_text(self, tariff_alt_text: list[dict] | None) -> None:
        if tariff_alt_text is None:
            self._tariff_alt_text = None
            return
        self._tariff_alt_text = json.dumps(tariff_alt_text, cls=DefaultJSONEncoder)

    @hybrid_property
    def min_price(self) -> dict | None:
        if self._min_price is None:
            return None
        return json.loads(self._min_price)

    @min_price.setter
    def min_price(self, min_price: dict | None) -> None:
        if min_price is None:
            self._min_price = None
            return
        self._min_price = json.dumps(min_price, cls=DefaultJSONEncoder)

    @hybrid_property
    def max_price(self) -> dict | None:
        if self._max_price is None:
            return None
        return json.loads(self._max_price)

    @max_price.setter
    def max_price(self, max_price: dict | None) -> None:
        if max_price is None:
            self._max_price = None
            return
        self._max_price = json.dumps(max_price, cls=DefaultJSONEncoder)

    @hybrid_property
    def energy_mix(self) -> dict | None:
        if self._energy_mix is None:
            return None
        return json.loads(self._energy_mix)

    @energy_mix.setter
    def energy_mix(self, energy_mix: dict | None) -> None:
        if energy_mix is None:
            self._energy_mix = None
            return
        self._energy_mix = json.dumps(energy_mix, cls=DefaultJSONEncoder)

    @hybrid_property
    def elements(self) -> list[dict]:
        return json.loads(self._elements)

    @elements.setter
    def elements(self, elements: list[dict]) -> None:
        self._elements = json.dumps(elements, cls=DefaultJSONEncoder)

    def to_dict(self, *args, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []
        ignore += [
            'created',
            'modified',
            'tariff_alt_text',
            'min_price',
            'max_price',
            'energy_mix',
        ]

        result = super().to_dict(*args, ignore=ignore, **kwargs)

        result['id'] = str(self.id)
        result['tariff_alt_text'] = self.tariff_alt_text
        result['min_price'] = self.min_price
        result['max_price'] = self.max_price
        result['energy_mix'] = self.energy_mix

        return result
