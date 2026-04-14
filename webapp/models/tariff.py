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
from dataclasses import dataclass, fields
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Index, String, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utc import UtcDateTime

from webapp.common.dataclass import DataclassMixin
from webapp.common.json import DefaultJSONEncoder

from .base import BaseModel

if TYPE_CHECKING:
    from .tariff_association import TariffAssociation


@dataclass(kw_only=True)
class DisplayText(DataclassMixin):
    language: str | None = None
    text: str | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'DisplayText':
        return cls(
            language=data.get('language'),
            text=data.get('text'),
        )

    def to_dict(self) -> dict:
        result = {}
        if self.language is not None:
            result['language'] = self.language
        if self.text is not None:
            result['text'] = self.text
        return result


@dataclass(kw_only=True)
class TariffTaxAmount(DataclassMixin):
    name: str | None = None
    amount: float | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'TariffTaxAmount':
        return cls(
            name=data.get('name'),
            amount=data.get('amount'),
        )

    def to_dict(self) -> dict:
        result = {}
        if self.name is not None:
            result['name'] = self.name
        if self.amount is not None:
            result['amount'] = self.amount
        return result


@dataclass(kw_only=True)
class TariffPrice(DataclassMixin):
    before_taxes: float | None = None
    taxes: list[TariffTaxAmount] | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'TariffPrice':
        taxes = None
        if data.get('taxes') is not None:
            taxes = [TariffTaxAmount.from_dict(t) for t in data['taxes']]
        return cls(
            before_taxes=data.get('before_taxes'),
            taxes=taxes,
        )

    def to_dict(self) -> dict:
        result = {}
        if self.before_taxes is not None:
            result['before_taxes'] = self.before_taxes
        if self.taxes is not None:
            result['taxes'] = [t.to_dict() for t in self.taxes]
        return result


@dataclass(kw_only=True)
class TariffEnergySource(DataclassMixin):
    source: str | None = None
    percentage: float | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'TariffEnergySource':
        return cls(
            source=data.get('source'),
            percentage=data.get('percentage'),
        )

    def to_dict(self) -> dict:
        result = {}
        if self.source is not None:
            result['source'] = self.source
        if self.percentage is not None:
            result['percentage'] = self.percentage
        return result


@dataclass(kw_only=True)
class TariffEnvironmentalImpact(DataclassMixin):
    category: str | None = None
    amount: float | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'TariffEnvironmentalImpact':
        return cls(
            category=data.get('category'),
            amount=data.get('amount'),
        )

    def to_dict(self) -> dict:
        result = {}
        if self.category is not None:
            result['category'] = self.category
        if self.amount is not None:
            result['amount'] = self.amount
        return result


@dataclass(kw_only=True)
class TariffEnergyMix(DataclassMixin):
    is_green_energy: bool | None = None
    energy_sources: list[TariffEnergySource] | None = None
    environ_impact: list[TariffEnvironmentalImpact] | None = None
    supplier_name: str | None = None
    energy_product_name: str | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'TariffEnergyMix':
        energy_sources = None
        if data.get('energy_sources') is not None:
            energy_sources = [TariffEnergySource.from_dict(es) for es in data['energy_sources']]
        environ_impact = None
        if data.get('environ_impact') is not None:
            environ_impact = [TariffEnvironmentalImpact.from_dict(ei) for ei in data['environ_impact']]
        return cls(
            is_green_energy=data.get('is_green_energy'),
            energy_sources=energy_sources,
            environ_impact=environ_impact,
            supplier_name=data.get('supplier_name'),
            energy_product_name=data.get('energy_product_name'),
        )

    def to_dict(self) -> dict:
        result = {}
        if self.is_green_energy is not None:
            result['is_green_energy'] = self.is_green_energy
        if self.energy_sources is not None:
            result['energy_sources'] = [es.to_dict() for es in self.energy_sources]
        if self.environ_impact is not None:
            result['environ_impact'] = [ei.to_dict() for ei in self.environ_impact]
        if self.supplier_name is not None:
            result['supplier_name'] = self.supplier_name
        if self.energy_product_name is not None:
            result['energy_product_name'] = self.energy_product_name
        return result


@dataclass(kw_only=True)
class TariffTax(DataclassMixin):
    name: str | None = None
    percentage: float | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'TariffTax':
        return cls(
            name=data.get('name'),
            percentage=data.get('percentage'),
        )

    def to_dict(self) -> dict:
        result = {}
        if self.name is not None:
            result['name'] = self.name
        if self.percentage is not None:
            result['percentage'] = self.percentage
        return result


@dataclass(kw_only=True)
class TariffPriceComponent(DataclassMixin):
    type: str | None = None
    price: float | int | None = None
    taxes: list[TariffTax] | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'TariffPriceComponent':
        taxes = None
        if data.get('taxes') is not None:
            taxes = [TariffTax.from_dict(t) for t in data['taxes']]
        return cls(
            type=data.get('type'),
            price=round(float(data.get('price')), 4),
            taxes=taxes,
        )

    def to_dict(self) -> dict:
        result = {}
        if self.type is not None:
            result['type'] = self.type
        if self.price is not None:
            result['price'] = self.price
        if self.taxes is not None:
            result['taxes'] = [t.to_dict() for t in self.taxes]
        return result


@dataclass(kw_only=True)
class TariffRestrictions(DataclassMixin):
    start_time: str | None = None
    end_time: str | None = None
    min_energy: float | None = None
    max_energy: float | None = None
    min_current: float | None = None
    max_current: float | None = None
    min_power: float | None = None
    max_power: float | None = None
    min_duration: int | None = None
    max_duration: int | None = None
    min_restrictions_duration: int | None = None
    day_of_week: list[str] | None = None
    reservation: str | None = None
    vehicle_requesting_power: bool | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'TariffRestrictions':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def to_dict(self) -> dict:
        return {
            field.name: getattr(self, field.name) for field in fields(self) if getattr(self, field.name) is not None
        }


@dataclass(kw_only=True)
class TariffElement(DataclassMixin):
    price_components: list[TariffPriceComponent] | None = None
    restrictions: TariffRestrictions | None = None

    @classmethod
    def from_dict(cls, data: dict) -> 'TariffElement':
        price_components = None
        if data.get('price_components') is not None:
            price_components = [TariffPriceComponent.from_dict(pc) for pc in data['price_components']]
        restrictions = None
        if data.get('restrictions') is not None:
            restrictions = TariffRestrictions.from_dict(data['restrictions'])
        return cls(price_components=price_components, restrictions=restrictions)

    def to_dict(self) -> dict:
        result = {}
        if self.price_components is not None:
            result['price_components'] = [pc.to_dict() for pc in self.price_components]
        if self.restrictions is not None:
            result['restrictions'] = self.restrictions.to_dict()
        return result


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
    def tariff_alt_text(self) -> list[DisplayText] | None:
        if self._tariff_alt_text is None:
            return None
        return [DisplayText.from_dict(dt) for dt in json.loads(self._tariff_alt_text)]

    @tariff_alt_text.setter
    def tariff_alt_text(self, tariff_alt_text: list[DisplayText] | None) -> None:
        if tariff_alt_text is None:
            self._tariff_alt_text = None
            return
        self._tariff_alt_text = json.dumps([dt.to_dict() for dt in tariff_alt_text], cls=DefaultJSONEncoder)

    @hybrid_property
    def min_price(self) -> TariffPrice | None:
        if self._min_price is None:
            return None
        return TariffPrice.from_dict(json.loads(self._min_price))

    @min_price.setter
    def min_price(self, min_price: TariffPrice | None) -> None:
        if min_price is None:
            self._min_price = None
            return
        self._min_price = json.dumps(min_price.to_dict(), cls=DefaultJSONEncoder)

    @hybrid_property
    def max_price(self) -> TariffPrice | None:
        if self._max_price is None:
            return None
        return TariffPrice.from_dict(json.loads(self._max_price))

    @max_price.setter
    def max_price(self, max_price: TariffPrice | None) -> None:
        if max_price is None:
            self._max_price = None
            return
        self._max_price = json.dumps(max_price.to_dict(), cls=DefaultJSONEncoder)

    @hybrid_property
    def energy_mix(self) -> TariffEnergyMix | None:
        if self._energy_mix is None:
            return None
        return TariffEnergyMix.from_dict(json.loads(self._energy_mix))

    @energy_mix.setter
    def energy_mix(self, energy_mix: TariffEnergyMix | None) -> None:
        if energy_mix is None:
            self._energy_mix = None
            return
        self._energy_mix = json.dumps(energy_mix.to_dict(), cls=DefaultJSONEncoder)

    @hybrid_property
    def elements(self) -> list[TariffElement]:
        return [TariffElement.from_dict(element) for element in json.loads(self._elements)]

    @elements.setter
    def elements(self, elements: list[TariffElement]) -> None:
        self._elements = json.dumps([element.to_dict() for element in elements], cls=DefaultJSONEncoder)

    def to_dict(self, *args, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []
        ignore += [
            'created',
            'modified',
            'tariff_alt_text',
            'min_price',
            'max_price',
            'energy_mix',
            'elements',
        ]

        result = super().to_dict(*args, ignore=ignore, **kwargs)

        result['id'] = str(self.id)
        result['elements'] = [element.to_dict() for element in self.elements]
        result['tariff_alt_text'] = [dt.to_dict() for dt in self.tariff_alt_text] if self.tariff_alt_text else None
        result['min_price'] = self.min_price.to_dict() if self.min_price else None
        result['max_price'] = self.max_price.to_dict() if self.max_price else None
        result['energy_mix'] = self.energy_mix.to_dict() if self.energy_mix else None

        return result
