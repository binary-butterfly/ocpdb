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

from datetime import time
from typing import Any

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.validators import (
    AnythingValidator,
    DataclassValidator,
    EnumValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
    Noneable,
    StringValidator,
    TimeValidator,
)

from webapp.models.enums import TariffDimensionType
from webapp.services.import_services.ocpi.ocpi_validators import EvseInput, LocationInput


@validataclass
class ChargecloudAfirPriceComponentInput(ValidataclassMixin):
    type: TariffDimensionType = EnumValidator(TariffDimensionType)
    price: float = FloatValidator(allow_integers=True)
    step_size: int = IntegerValidator()


@validataclass
class ChargecloudAfirRestrictionInput(ValidataclassMixin):
    start_time: time | None = TimeValidator(), Default(None)
    end_time: time | None = TimeValidator(), Default(None)
    min_duration: int | None = IntegerValidator(), Default(None)
    max_duration: int | None = IntegerValidator(), Default(None)


@validataclass
class ChargecloudAfirTariffElementInput(ValidataclassMixin):
    price_components: list[ChargecloudAfirPriceComponentInput] = ListValidator(
        DataclassValidator(ChargecloudAfirPriceComponentInput),
        min_length=1,
    )
    restrictions: list[ChargecloudAfirRestrictionInput] | None = (
        ListValidator(DataclassValidator(ChargecloudAfirRestrictionInput)),
        Default(None),
    )


@validataclass
class ChargecloudAfirTariffInput(ValidataclassMixin):
    id: str = StringValidator(max_length=64)
    currency: str = StringValidator(min_length=3, max_length=3)
    elements: list[ChargecloudAfirTariffElementInput] = ListValidator(
        DataclassValidator(ChargecloudAfirTariffElementInput),
    )


@validataclass
class ChargecloudAfirEvseInput(EvseInput):
    tariffs: list[ChargecloudAfirTariffInput] | None = (
        ListValidator(DataclassValidator(ChargecloudAfirTariffInput)),
        Default(None),
    )


@validataclass
class ChargecloudAfirLocationInput(LocationInput):
    evses: list[ChargecloudAfirEvseInput] = ListValidator(DataclassValidator(ChargecloudAfirEvseInput)), Default([])


@validataclass
class ChargecloudAfirLocationsInput:
    next: str | None = Noneable(StringValidator()), Default(None)
    items: list[dict[str, Any]] = ListValidator(AnythingValidator(allowed_types=[dict]))
