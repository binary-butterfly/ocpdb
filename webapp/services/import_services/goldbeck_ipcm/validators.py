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

from datetime import datetime
from decimal import Decimal
from enum import Enum

from validataclass.dataclasses import validataclass, Default
from validataclass.validators import IntegerValidator, ListValidator, DataclassValidator, DateTimeValidator, StringValidator, \
    DecimalValidator

from webapp.services.import_services.models import LocationUpdate, EvseUpdate


class GoldbeckEvseStatus(Enum):
    AVAILABLE = "AVAILABLE"
    CHARGING = "CHARGING"


@validataclass
class Attribute:
    key: str = StringValidator()
    value: str = StringValidator()


@validataclass
class Outlet:
    attributes: list[Attribute] = ListValidator(DataclassValidator(Attribute))
    evseId: str = StringValidator()
    nativeStatus: str = StringValidator()


@validataclass
class Position:
    latitude: Decimal = DecimalValidator()
    longitude: Decimal = DecimalValidator()


@validataclass
class PostalAddress:
    city: str = StringValidator()
    country: str = StringValidator()
    id: int = IntegerValidator()
    name: str = StringValidator()
    street1: str = StringValidator()
    street2: str = StringValidator()
    zip: str = StringValidator()


@validataclass
class Tenant:
    id: int = IntegerValidator()
    name: str = StringValidator()


@validataclass
class GoldbeckIpcmChargePoint:
    attributes: list[Attribute] = ListValidator(DataclassValidator(Attribute))
    id: int = IntegerValidator()
    lastUpdatedAt: datetime = DateTimeValidator()
    name: str | None = StringValidator(), Default(None)
    outlets: list[Outlet] = ListValidator(DataclassValidator(Outlet))
    position: Position = DataclassValidator(Position)
    postalAddress: PostalAddress = DataclassValidator(PostalAddress)
    tenant: Tenant = DataclassValidator(Tenant)

    def to_location_update(self) -> LocationUpdate:
        location_update = LocationUpdate(
            uid=str(self.postalAddress.id),
            last_updated=self.lastUpdatedAt,
            source='heilbronn_neckarbogen',
            time_zone='Europe/Berlin',
        )

        return location_update
