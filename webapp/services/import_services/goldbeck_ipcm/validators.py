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

from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from zoneinfo import ZoneInfo

from pycountry import countries
from validataclass.dataclasses import Default, validataclass
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    EnumValidator,
    FloatToDecimalValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import EvseStatus
from webapp.services.import_services.models import (
    BusinessUpdate,
    ChargingStationUpdate,
    ConnectorUpdate,
    EvseUpdate,
    LocationUpdate,
)

FORMAT_MAPPING: dict[str, ConnectorFormat] = {}

STANDARD_MAPPING: dict[str, ConnectorType] = {
    'AC3': ConnectorType.IEC_62196_T2,
}


class GoldbeckEvseStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    PREPARING = 'PREPARING'
    CHARGING = 'CHARGING'
    SUSPENDED_EVSE = 'SUSPENDED_EVSE'
    SUSPENDED_EV = 'SUSPENDED_EV'
    FINISHING = 'FINISHING'
    RESERVED = 'RESERVED'
    UNAVAILABLE = 'UNAVAILABLE'
    FAULTED = 'FAULTED'

    def to_evse_status(self) -> EvseStatus:
        return {
            self.AVAILABLE: EvseStatus.AVAILABLE,
            self.PREPARING: EvseStatus.CHARGING,
            self.CHARGING: EvseStatus.CHARGING,
            self.SUSPENDED_EVSE: EvseStatus.CHARGING,
            self.SUSPENDED_EV: EvseStatus.CHARGING,
            self.FINISHING: EvseStatus.CHARGING,
            self.UNAVAILABLE: EvseStatus.INOPERATIVE,
            self.FAULTED: EvseStatus.OUTOFORDER,
        }.get(self)


@validataclass
class Attribute:
    key: str = StringValidator()
    value: str | None = StringValidator(), Default(None)


@validataclass
class Outlet:
    attributes: list[Attribute] = ListValidator(DataclassValidator(Attribute))
    evseId: str = StringValidator()
    nativeStatus: GoldbeckEvseStatus | None = EnumValidator(GoldbeckEvseStatus), Default(None)

    def get_attribute_by_key(self, key: str) -> str | None:
        for attribute in self.attributes:
            if attribute.key == key:
                return attribute.value
        return None


@validataclass
class Position:
    latitude: Decimal = FloatToDecimalValidator(allow_integers=True)
    longitude: Decimal = FloatToDecimalValidator(allow_integers=True)


@validataclass
class PostalAddress:
    city: str = StringValidator()
    country: str = StringValidator()
    id: int = IntegerValidator()
    name: str = StringValidator()
    street1: str = StringValidator()
    street2: str = StringValidator(), Default('')
    zip: str = StringValidator()


@validataclass
class Tenant:
    id: int = IntegerValidator()
    name: str = StringValidator()


@validataclass
class GoldbeckIpcmChargePoint:
    attributes: list[Attribute] = ListValidator(DataclassValidator(Attribute))
    id: int = IntegerValidator()
    lastUpdatedAt: datetime = DateTimeValidator(
        local_timezone=ZoneInfo('Europe/Berlin'),
        target_timezone=timezone.utc,
    )
    name: str | None = StringValidator(), Default(None)
    outlets: list[Outlet] = ListValidator(DataclassValidator(Outlet))
    position: Position = DataclassValidator(Position)
    postalAddress: PostalAddress = DataclassValidator(PostalAddress)
    tenant: Tenant = DataclassValidator(Tenant)

    def to_location_update(self, location_update: LocationUpdate | None) -> LocationUpdate:
        if location_update is None:
            if self.postalAddress.street2:
                address = f'{self.postalAddress.street1} {self.postalAddress.street2}'
            else:
                address = self.postalAddress.street1
            location_update = LocationUpdate(
                uid=str(self.postalAddress.id),
                source='heilbronn_neckarbogen',
                time_zone='Europe/Berlin',
                address=address,
                postal_code=self.postalAddress.zip,
                city=self.postalAddress.city,
                country=countries.get(alpha_2=self.postalAddress.country).alpha_3,
                lat=self.position.latitude,
                lon=self.position.longitude,
                operator=BusinessUpdate(name=self.tenant.name),
                charging_pool=[
                    ChargingStationUpdate(uid=str(self.postalAddress.id), evses=[]),
                ],
            )

        for outlet in self.outlets:
            evse_update = EvseUpdate(
                last_updated=self.lastUpdatedAt,
                uid=outlet.evseId,
                evse_id=outlet.evseId,
                status=EvseStatus.STATIC if outlet.nativeStatus is None else outlet.nativeStatus.to_evse_status(),
                connectors=[
                    ConnectorUpdate(
                        uid='1',
                        format=FORMAT_MAPPING.get(outlet.get_attribute_by_key('FORMAT')),
                        max_voltage=int(outlet.get_attribute_by_key('MAX_VOLTAGE')),
                        standard=STANDARD_MAPPING.get(outlet.get_attribute_by_key('POWER_TYPE')),
                        max_amperage=int(outlet.get_attribute_by_key('MAX_AMPERAGE')),
                        max_electric_power=int(outlet.get_attribute_by_key('MAX_ELECTRIC_POWER')),
                        power_type=PowerType.AC_3_PHASE,
                        last_updated=self.lastUpdatedAt,
                    ),
                ],
            )

            location_update.charging_pool[0].evses.append(evse_update)

        return location_update

    def to_realtime_evse_updates(self) -> list[EvseUpdate]:
        evse_updates: list[EvseUpdate] = []
        for outlet in self.outlets:
            evse_updates.append(
                EvseUpdate(
                    last_updated=self.lastUpdatedAt,
                    uid=outlet.evseId,
                    evse_id=outlet.evseId,
                    status=EvseStatus.STATIC if outlet.nativeStatus is None else outlet.nativeStatus.to_evse_status(),
                ),
            )
        return evse_updates
