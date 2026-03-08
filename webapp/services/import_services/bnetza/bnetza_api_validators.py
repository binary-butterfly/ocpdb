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

from datetime import date, time
from decimal import Decimal
from enum import Enum

from validataclass.dataclasses import Default, validataclass
from validataclass.validators import (
    AnythingValidator,
    BooleanValidator,
    DataclassValidator,
    EnumValidator,
    IntegerValidator,
    ListValidator,
    Noneable,
    NumericValidator,
    StringValidator,
    TimeFormat,
    TimeValidator,
)

from webapp.common.validation import EmptystringToNoneable, ParsedDateValidator, PrintableStringValidator
from webapp.models.charging_station import Capability
from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.enums import ChargingRateUnit
from webapp.models.evse import EvseStatus
from webapp.services.import_services.models import (
    BusinessUpdate,
    ChargingStationUpdate,
    ConnectorUpdate,
    EvseUpdate,
    LocationUpdate,
    MaxPowerUpdate,
    RegularHoursUpdate,
)


class BnetzaConnectorType(Enum):
    IEC_62196_T2_SOCKET = 'AC Typ 2 Steckdose'
    IEC_62196_T2_CABLE = 'AC Typ 2 Fahrzeugkupplung'
    IEC_62196_T2_COMBO_CABLE = 'DC Fahrzeugkupplung Typ Combo 2 (CCS)'
    DOMESTIC_F_SOCKET = 'AC Schuko'
    CHADEMO_CABLE = 'DC CHAdeMO'
    IEC_62196_T1_SOCKET = 'AC Typ 1 Steckdose'
    TESLA_S_CABLE = 'DC Tesla Fahrzeugkupplung (Typ 2)'
    IEC_60309_2_SINGLE_16_SOCKET = 'AC CEE 3-polig'
    IEC_60309_2_THREE_32_SOCKET = 'AC CEE 5-polig'
    WIRELESS = 'Kabellos/Induktiv'
    MCS = 'DC Megawatt Charging System (MCS)'

    def to_connector_type(self) -> ConnectorType | None:
        return {
            self.IEC_62196_T2_SOCKET: ConnectorType.IEC_62196_T2,
            self.IEC_62196_T2_CABLE: ConnectorType.IEC_62196_T2,
            self.IEC_62196_T2_COMBO_CABLE: ConnectorType.IEC_62196_T2_COMBO,
            self.DOMESTIC_F_SOCKET: ConnectorType.DOMESTIC_F,
            self.CHADEMO_CABLE: ConnectorType.CHADEMO,
            self.IEC_62196_T1_SOCKET: ConnectorType.IEC_62196_T1,
            self.TESLA_S_CABLE: ConnectorType.TESLA_S,
            self.IEC_60309_2_SINGLE_16_SOCKET: ConnectorType.IEC_60309_2_single_16,
            self.IEC_60309_2_THREE_32_SOCKET: ConnectorType.IEC_60309_2_three_32,
        }.get(self)

    def to_connector_format(self) -> ConnectorFormat:
        return {
            self.IEC_62196_T2_SOCKET: ConnectorFormat.SOCKET,
            self.IEC_62196_T2_CABLE: ConnectorFormat.CABLE,
            self.IEC_62196_T2_COMBO_CABLE: ConnectorFormat.CABLE,
            self.DOMESTIC_F_SOCKET: ConnectorFormat.SOCKET,
            self.CHADEMO_CABLE: ConnectorFormat.CABLE,
            self.IEC_62196_T1_SOCKET: ConnectorFormat.SOCKET,
            self.TESLA_S_CABLE: ConnectorFormat.CABLE,
            self.IEC_60309_2_SINGLE_16_SOCKET: ConnectorFormat.SOCKET,
            self.IEC_60309_2_THREE_32_SOCKET: ConnectorFormat.SOCKET,
        }.get(self)

    def to_power_type(self, max_electric_power: Decimal | None) -> PowerType:
        if self in [self.CHADEMO_CABLE, self.IEC_62196_T2_COMBO_CABLE, self.TESLA_S_CABLE]:
            return PowerType.DC
        if self == self.DOMESTIC_F_SOCKET or (max_electric_power and max_electric_power < Decimal(11)):
            return PowerType.AC_1_PHASE
        return PowerType.AC_3_PHASE


class PaymentSystem(Enum):
    FREE = 'Kostenlos'
    CASH = 'Bargeld'
    CREDIT_CARD_READER = 'Kreditkarte (Lesegerät)'
    CREDIT_CARD_NFC = 'Kreditkarte (NFC)'
    CREDIT_CARD_WEBSITE_APP = 'Kreditkarte (Webseite / App)'
    DEBIT_CARD_READER = 'Debitkarte (Lesegerät)'
    DEBIT_CARD_NFC = 'Debitkarte (NFC)'
    DEBIT_CARD_WEBSITE_APP = 'Debitkarte (Webseite / App)'
    ONLINE_PAYMENT = 'Onlinezahlungsverfahren'
    RFID_READER = 'RFID-Karte'
    FREE_REGISTRATION = 'Kostenlos (Registrierung)'
    PLUG_AND_CHARGE = 'Plug & Charge'
    OTHER = 'Sonstige'

    def to_capabilities(self) -> list[Capability]:
        capabilities: list[Capability] = []
        if self in [self.CREDIT_CARD_READER, self.DEBIT_CARD_READER]:
            capabilities.append(Capability.CHIP_CARD_SUPPORT)
        if self in [self.CREDIT_CARD_NFC, self.DEBIT_CARD_NFC]:
            capabilities.append(Capability.CONTACTLESS_CARD_SUPPORT)
        if self in [self.CREDIT_CARD_READER, self.CREDIT_CARD_NFC]:
            capabilities.append(Capability.CREDIT_CARD_PAYABLE)
        if self in [self.DEBIT_CARD_READER, self.DEBIT_CARD_NFC]:
            capabilities.append(Capability.DEBIT_CARD_PAYABLE)
        if self == self.RFID_READER:
            capabilities.append(Capability.RFID_READER)
        if self in [self.CREDIT_CARD_WEBSITE_APP, self.DEBIT_CARD_WEBSITE_APP, self.ONLINE_PAYMENT]:
            capabilities.append(Capability.REMOTE_START_STOP_CAPABLE)
        return capabilities


class AccessRestriction(Enum):
    NONE = 'Keine Beschränkung'
    CUSTOMERS = 'Nur für Kunden/Besucher'


class OperationalStatus(Enum):
    AVAILABLE = 'In Betrieb'
    MAINTENANCE = 'In Wartung'

    def to_status(self) -> EvseStatus:
        return {
            self.AVAILABLE: EvseStatus.STATIC,
            self.MAINTENANCE: EvseStatus.INOPERATIVE,
        }.get(self)


class ChargingStationType(Enum):
    NORMAL = 'Normalladeeinrichtung'
    FAST = 'Schnellladeeinrichtung'


class BnetzaWeekday(Enum):
    MONDAY = 'Montag'
    TUESDAY = 'Dienstag'
    WEDNESDAY = 'Mittwoch'
    THURSDAY = 'Donnerstag'
    FRIDAY = 'Freitag'
    SATURDAY = 'Samstag'
    SUNDAY = 'Sonntag'

    def to_integer_weekday(self) -> int:
        return {
            self.MONDAY: 1,
            self.TUESDAY: 2,
            self.WEDNESDAY: 3,
            self.THURSDAY: 4,
            self.FRIDAY: 5,
            self.SATURDAY: 6,
            self.SUNDAY: 7,
        }.get(self)


class OpeningHoursSpecification(Enum):
    TWENTY_FOUR_SEVEN = '247'
    LIMITED = 'Eingeschränkt'
    NO_DATA = 'Keine Angabe'


@validataclass
class BnetzaResponseInput:
    chargingStations: list[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))


@validataclass
class BnetzaCoordinates:
    latitude: Decimal = NumericValidator()
    longitude: Decimal = NumericValidator()


@validataclass
class BnetzaOperator:
    companyName: str = PrintableStringValidator()
    displayName: str | None = Noneable(PrintableStringValidator()), Default(None)


@validataclass
class BnetzaConnector:
    connector_type: BnetzaConnectorType | None = Noneable(EnumValidator(BnetzaConnectorType)), Default(None)
    max_electric_power_connector: Decimal | None = Noneable(NumericValidator()), Default(None)

    def __post_init__(self):
        # There are several connectors where there's 22kW for SchuKo which is impossible, so we cap max power there
        if (
            self.connector_type == BnetzaConnectorType.DOMESTIC_F_SOCKET
            and self.max_electric_power_connector
            and self.max_electric_power_connector > Decimal('3.7')
        ):
            self.max_electric_power_connector = Decimal('3.7')

    def to_connector_update(self, counter: int) -> ConnectorUpdate | None:
        if not self.connector_type or not self.connector_type.to_connector_type():
            return None

        connector_update = ConnectorUpdate(
            uid=str(counter),
            standard=self.connector_type.to_connector_type(),
            format=self.connector_type.to_connector_format(),
            power_type=self.connector_type.to_power_type(self.max_electric_power_connector),
        )
        if self.max_electric_power_connector:
            connector_update.max_electric_power = int(self.max_electric_power_connector * 1000)

        return connector_update


@validataclass
class BnetzaEvse:
    connectors: list[BnetzaConnector] = ListValidator(DataclassValidator(BnetzaConnector))
    public_key_available: bool = BooleanValidator()
    evse_id: str | None = Noneable(PrintableStringValidator()), Default(None)

    def to_evse_update(
        self,
        location_id: int,
        counter: int,
        status: EvseStatus,
    ) -> EvseUpdate | None:
        uid = f'BNETZA*{location_id}*{counter}'
        if self.evse_id and len(self.evse_id) <= 48:
            evse_id = self.evse_id
        else:
            evse_id = uid
        evse_update = EvseUpdate(
            uid=uid,
            evse_id=evse_id,
            status=status,
            connectors=[],
        )

        for i, connector in enumerate(self.connectors):
            connector_update = connector.to_connector_update(
                counter=i + 1,
            )

            # Continue at invalid connectors
            if connector_update is None:
                continue

            evse_update.connectors.append(connector_update)

        # Empty connectors are invalid
        if len(evse_update.connectors) == 0:
            return None

        return evse_update


@validataclass
class BnetzaStatus:
    operational: OperationalStatus = EnumValidator(OperationalStatus)


@validataclass
class OpeningDay:
    day: BnetzaWeekday | None = Noneable(EnumValidator(BnetzaWeekday)), Default(None)
    open_from: time = TimeValidator(time_format=TimeFormat.NO_SECONDS)
    open_to: time = TimeValidator(time_format=TimeFormat.NO_SECONDS)


@validataclass
class BnetzaChargingStation:
    id: int = IntegerValidator()
    location_description: str | None = Noneable(PrintableStringValidator()), Default(None)
    street: str | None = Noneable(PrintableStringValidator()), Default(None)
    house_no: str | None = Noneable(PrintableStringValidator()), Default(None)
    address_addition: str | None = Noneable(PrintableStringValidator()), Default(None)
    district_independent_city: str = StringValidator()
    postal_code: str = StringValidator()
    city: str = PrintableStringValidator()
    state: str = StringValidator()
    coordinates: BnetzaCoordinates = DataclassValidator(BnetzaCoordinates)
    evses: list[BnetzaEvse] = ListValidator(DataclassValidator(BnetzaEvse))
    max_electric_power_station: Decimal | None = Noneable(NumericValidator()), Default(None)
    opening_days: list[OpeningDay] = ListValidator(DataclassValidator(OpeningDay))
    opening_hours_specification: OpeningHoursSpecification = EnumValidator(OpeningHoursSpecification)
    operator: BnetzaOperator = DataclassValidator(BnetzaOperator)
    payment_systems: list[PaymentSystem | None] = ListValidator(
        Noneable(EmptystringToNoneable(EnumValidator(PaymentSystem))),
    )
    # Not used, and the enumeration seems unstable anyway
    # access_restriction: AccessRestriction | None = Noneable(EnumValidator(AccessRestriction)), Default(None)
    status: BnetzaStatus = DataclassValidator(BnetzaStatus)
    type: ChargingStationType = EnumValidator(ChargingStationType)
    go_live_date: date = ParsedDateValidator(date_format='%d.%m.%Y')

    def to_location_update(self) -> LocationUpdate:
        if self.street and self.house_no and self.house_no != '0':
            address = f'{self.street} {self.house_no}'
        elif self.street:
            address = self.street
        else:
            address = None

        capabilities: list[Capability] = []
        for payment_system in self.payment_systems:
            # BNetzA has '' as list items, which is against their spec. We ignore them.
            if payment_system is None:
                continue
            capabilities += payment_system.to_capabilities()
        capabilities = list(set(capabilities))

        evse_updates: list[EvseUpdate] = []
        for i, evse in enumerate(self.evses):
            evse_update = evse.to_evse_update(
                location_id=self.id,
                counter=i + 1,
                status=self.status.operational.to_status(),
            )

            if evse_update is None:
                continue

            evse_updates.append(evse_update)

        charging_station_update = ChargingStationUpdate(
            uid=str(self.id),
            evses=evse_updates,
            capabilities=capabilities,
            go_live_date=self.go_live_date,
        )
        if self.max_electric_power_station:
            charging_station_update.max_power = MaxPowerUpdate(
                unit=ChargingRateUnit.KW,
                value=float(self.max_electric_power_station),
            )

        location_update = LocationUpdate(
            uid=str(self.id),
            source='bnetza_api',
            address=address,
            postal_code=self.postal_code,
            city=self.city,
            state=self.state,
            lat=self.coordinates.latitude,
            lon=self.coordinates.longitude,
            country='DEU',
            operator=BusinessUpdate(
                name=self.operator.companyName,
            ),
            charging_pool=[charging_station_update],
            time_zone='Europe/Berlin',
        )

        if self.opening_hours_specification == OpeningHoursSpecification.TWENTY_FOUR_SEVEN:
            location_update.twentyfourseven = True
        elif self.opening_days:
            location_update.twentyfourseven = False
            location_update.regular_hours = []
            for opening_day in self.opening_days:
                if opening_day.day is None:
                    continue
                location_update.regular_hours.append(
                    RegularHoursUpdate(
                        weekday=opening_day.day.to_integer_weekday(),
                        period_begin=opening_day.open_from.hour * 60 + opening_day.open_from.minute,
                        period_end=opening_day.open_to.hour * 60 + opening_day.open_to.minute,
                    ),
                )

        return location_update
