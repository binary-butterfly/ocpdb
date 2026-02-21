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

from dataclasses import asdict, dataclass
from datetime import datetime
from decimal import Decimal
from math import sqrt

from webapp.models.charging_station import Capability
from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import EvseStatus, ParkingRestriction, PresenceStatus
from webapp.models.image import ImageCategory
from webapp.models.location import ChargingRateUnit, EnergySourceCategory, EnvironmentalImpactCategory, ParkingType


@dataclass(kw_only=True)
class SourceInfo:
    uid: str
    name: str
    public_url: str
    has_realtime_data: bool | None
    timezone: str = 'Europe/Berlin'
    source_url: str | None = None
    attribution_license: str | None = None
    attribution_url: str | None = None
    attribution_contributor: str | None = None

    def to_dict(self) -> dict:
        return {key: value for key, value in asdict(self).items() if value is not None}


@dataclass(kw_only=True)
class BaseUpdate:
    _object_keys = ()

    def to_dict(self) -> dict:
        return {key: value for key, value in asdict(self).items() if key not in self._object_keys}


@dataclass(kw_only=True)
class ImageUpdate(BaseUpdate):
    external_url: str | None = None
    type: str | None = None
    category: ImageCategory | None = None
    width: int | None = None
    height: int | None = None
    last_download: datetime | None = None


@dataclass(kw_only=True)
class BusinessUpdate(BaseUpdate):
    _object_keys = ('logo',)

    logo: ImageUpdate | None = None
    name: str | None = None
    website: str | None = None


@dataclass(kw_only=True)
class ConnectorUpdate(BaseUpdate):
    uid: str
    standard: ConnectorType
    format: ConnectorFormat
    power_type: PowerType | None = None
    max_voltage: int | None = None
    max_amperage: int | None = None
    max_electric_power: int | None = None
    last_updated: datetime | None = None
    terms_and_conditions: str | None = None

    def __post_init__(self):
        """
        Sadly, a lot of data sources don't provide max_voltage and max_amperage, but both are required. Therefore, we
        try to calculate it by best effort.
        """
        # First: try to calculate if not there
        if self.power_type is None:
            if self.standard in [
                ConnectorType.IEC_62196_T2_COMBO,
                ConnectorType.IEC_62196_T1_COMBO,
                ConnectorType.CHADEMO,
                ConnectorType.GBT_DC,
                ConnectorType.SAE_J3400,
                ConnectorType.TESLA_S,
                ConnectorType.PANTOGRAPH_TOP_DOWN,
                ConnectorType.PANTOGRAPH_BOTTOM_UP,
                ConnectorType.MCS,
            ]:
                self.power_type = PowerType.DC
            elif self.standard in [
                ConnectorType.IEC_62196_T1,
                ConnectorType.IEC_62196_T2,
                ConnectorType.IEC_62196_T3C,
                ConnectorType.IEC_60309_2_three_32,
                ConnectorType.IEC_60309_2_three_16,
                ConnectorType.IEC_60309_2_three_64,
                ConnectorType.NEMA_10_30,
                ConnectorType.NEMA_10_50,
                ConnectorType.NEMA_14_30,
                ConnectorType.NEMA_14_50,
            ]:
                self.power_type = PowerType.AC_3_PHASE
            else:
                self.power_type = PowerType.AC_1_PHASE

        if self.max_electric_power is None and self.max_voltage is not None and self.max_amperage is not None:
            self.max_electric_power = self.max_voltage * self.max_amperage
            if self.power_type == PowerType.AC_3_PHASE:
                self.max_electric_power * sqrt(3)

        elif self.max_electric_power is not None and (self.max_voltage is None or self.max_amperage is None):
            # DC Chargers
            if self.standard in [
                ConnectorType.IEC_62196_T2_COMBO,
                ConnectorType.IEC_62196_T1_COMBO,
                ConnectorType.CHADEMO,
                ConnectorType.GBT_DC,
                ConnectorType.SAE_J3400,
                ConnectorType.TESLA_S,
                ConnectorType.PANTOGRAPH_TOP_DOWN,
                ConnectorType.PANTOGRAPH_BOTTOM_UP,
            ]:
                self.max_voltage = 400
                self.max_amperage = int(self.max_electric_power / self.max_voltage)

            # 400 V / 230 V based AC Chargers
            elif self.standard in [
                ConnectorType.IEC_62196_T1,
                ConnectorType.IEC_62196_T2,
                ConnectorType.IEC_62196_T3C,
                ConnectorType.IEC_60309_2_three_32,
                ConnectorType.IEC_60309_2_three_16,
                ConnectorType.IEC_60309_2_three_64,
                ConnectorType.TESLA_R,
                ConnectorType.GBT_AC,
                ConnectorType.DOMESTIC_A,
                ConnectorType.DOMESTIC_B,
                ConnectorType.DOMESTIC_C,
                ConnectorType.DOMESTIC_D,
                ConnectorType.DOMESTIC_E,
                ConnectorType.DOMESTIC_F,
                ConnectorType.DOMESTIC_G,
                ConnectorType.DOMESTIC_H,
                ConnectorType.DOMESTIC_I,
                ConnectorType.DOMESTIC_J,
                ConnectorType.DOMESTIC_K,
                ConnectorType.DOMESTIC_L,
                ConnectorType.IEC_60309_2_single_16,
                ConnectorType.IEC_62196_T3A,
            ]:
                if self.power_type == PowerType.AC_3_PHASE:
                    self.max_voltage = 400
                else:
                    self.max_voltage = 230
                self.max_amperage = int(self.max_electric_power / self.max_voltage)
                if self.power_type == PowerType.AC_3_PHASE:
                    self.max_amperage = int(self.max_voltage / sqrt(3))

            # 120 V based AC Chargers
            elif self.standard in [
                ConnectorType.NEMA_5_20,
                ConnectorType.NEMA_6_30,
                ConnectorType.NEMA_6_50,
                ConnectorType.NEMA_10_30,
                ConnectorType.NEMA_10_50,
                ConnectorType.NEMA_14_30,
                ConnectorType.NEMA_14_50,
            ]:
                self.max_voltage = 120  # TODO: is this correct for AC_3_PHASE?
                self.max_amperage = int(self.max_electric_power / self.max_voltage)
                if self.power_type == PowerType.AC_3_PHASE:
                    self.max_amperage = int(self.max_voltage / sqrt(3))

            # Special cases
            elif self.standard == ConnectorType.MCS:
                self.max_voltage = 1000
                self.max_amperage = int(self.max_electric_power / self.max_voltage)
            else:
                self.max_voltage = 0
                self.max_amperage = 0

        elif self.max_electric_power is None and (self.max_voltage is None or self.max_amperage is None):
            # DC Chargers
            if self.standard in [
                ConnectorType.IEC_62196_T2_COMBO,
                ConnectorType.IEC_62196_T1_COMBO,
                ConnectorType.CHADEMO,
                ConnectorType.GBT_DC,
                ConnectorType.SAE_J3400,
                ConnectorType.TESLA_S,
                ConnectorType.PANTOGRAPH_TOP_DOWN,
                ConnectorType.PANTOGRAPH_BOTTOM_UP,
            ]:
                self.max_electric_power = 150000
                self.max_voltage = 400
                self.max_amperage = 375

            # 3-phase 400 V / 230 V AC Chargers
            elif self.standard in [
                ConnectorType.IEC_62196_T1,
                ConnectorType.IEC_62196_T2,
                ConnectorType.IEC_62196_T3C,
                ConnectorType.IEC_60309_2_three_32,
            ]:
                if self.power_type == PowerType.AC_3_PHASE:
                    self.max_electric_power = 22000
                    self.max_voltage = 400
                else:
                    self.max_electric_power = 7250
                    self.max_voltage = 230
                self.max_amperage = 32
            elif self.standard == ConnectorType.IEC_60309_2_three_16:
                if self.power_type == PowerType.AC_3_PHASE:
                    self.max_electric_power = 11000
                    self.max_voltage = 400
                else:
                    self.max_electric_power = 3650
                    self.max_voltage = 230
                self.max_voltage = 400
                self.max_amperage = 16
            elif self.standard == ConnectorType.IEC_60309_2_three_64:
                self.max_electric_power = 43000
                self.max_voltage = 400
                self.max_amperage = 64

            # 1-phase 230 V based AC Chargers
            elif self.standard == ConnectorType.TESLA_R:
                self.max_electric_power = 15000
                self.max_voltage = 230
                self.max_amperage = 65
            elif self.standard == ConnectorType.GBT_AC:
                self.max_electric_power = 7350
                self.max_voltage = 230
                self.max_amperage = 32
            elif self.standard in [
                ConnectorType.DOMESTIC_A,
                ConnectorType.DOMESTIC_B,
                ConnectorType.DOMESTIC_C,
                ConnectorType.DOMESTIC_D,
                ConnectorType.DOMESTIC_E,
                ConnectorType.DOMESTIC_F,
                ConnectorType.DOMESTIC_G,
                ConnectorType.DOMESTIC_H,
                ConnectorType.DOMESTIC_I,
                ConnectorType.DOMESTIC_J,
                ConnectorType.DOMESTIC_K,
                ConnectorType.DOMESTIC_L,
                ConnectorType.IEC_60309_2_single_16,
                ConnectorType.IEC_62196_T3A,
            ]:
                self.max_electric_power = 3650
                self.max_voltage = 230
                self.max_amperage = 16

            # 120 V based AC Chargers
            elif self.standard == ConnectorType.NEMA_5_20:
                self.max_electric_power = 2400
                self.max_voltage = 120
                self.max_amperage = 20
            elif self.standard == ConnectorType.NEMA_6_30:
                self.max_electric_power = 3600
                self.max_voltage = 120
                self.max_amperage = 30
            elif self.standard == ConnectorType.NEMA_6_50:
                self.max_electric_power = 6000
                self.max_voltage = 120
                self.max_amperage = 50
            elif self.standard in [ConnectorType.NEMA_10_30, ConnectorType.NEMA_14_30]:
                self.max_electric_power = 6200
                self.max_voltage = 120
                self.max_amperage = 30
            elif self.standard in [ConnectorType.NEMA_10_50, ConnectorType.NEMA_14_50]:
                self.max_electric_power = 10350
                self.max_voltage = 120
                self.max_amperage = 50

            # Special cases
            elif self.standard == ConnectorType.MCS:
                self.max_electric_power = 1000000
                self.max_voltage = 1000
                self.max_amperage = 1000
            else:
                self.max_electric_power = 0
                self.max_voltage = 0
                self.max_amperage = 0


@dataclass(kw_only=True)
class EvseUpdate(BaseUpdate):
    _object_keys = ('connectors', 'images')

    uid: str
    evse_id: str

    connectors: list[ConnectorUpdate]
    images: list[ImageUpdate] | None = None

    status: EvseStatus | None = None
    presence: PresenceStatus | None = None

    lat: Decimal | None = None
    lon: Decimal | None = None
    directions: str | None = None

    floor_level: str | None = None
    physical_reference: str | None = None
    help_phone: str | None = None

    last_updated: datetime | None = None
    status_last_updated: datetime | None = None
    max_reservation: float | None = None
    capabilities: list[Capability] | None = None
    parking_restrictions: list[ParkingRestriction] | None = None

    terms_and_conditions: str | None = None
    calibration_info_url: str | None = None

    def __post_init__(self):
        if self.lat is not None:
            self.lat = self.lat.quantize(Decimal('.0000001'))
        if self.lon is not None:
            self.lon = self.lon.quantize(Decimal('.0000001'))


@dataclass(kw_only=True)
class EvseRealtimeUpdate(BaseUpdate):
    uid: str
    evse_id: str
    status: EvseStatus
    last_updated: datetime | None = None
    status_last_updated: datetime | None = None


@dataclass(kw_only=True)
class MaxPowerUpdate(BaseUpdate):
    unit: ChargingRateUnit
    value: float


@dataclass(kw_only=True)
class ChargingStationUpdate(BaseUpdate):
    _object_keys = ('evses', 'images')

    uid: str
    evses: list[EvseUpdate]

    capabilities: list[Capability] | None = None
    floor_level: str | None = None
    physical_reference: str | None = None
    last_updated: datetime | None = None

    lat: Decimal | None = None
    lon: Decimal | None = None
    directions: str | None = None
    images: list[ImageUpdate] | None = None

    max_power: MaxPowerUpdate | None = None

    def __post_init__(self):
        if self.lat is not None:
            self.lat = self.lat.quantize(Decimal('.0000001'))
        if self.lon is not None:
            self.lon = self.lon.quantize(Decimal('.0000001'))


@dataclass(kw_only=True)
class RegularHoursUpdate(BaseUpdate):
    weekday: int
    period_begin: int
    period_end: int


@dataclass(kw_only=True)
class ExceptionalPeriodUpdate(BaseUpdate):
    period_begin: datetime
    period_end: datetime


@dataclass(kw_only=True)
class EnergySourceUpdate(BaseUpdate):
    source: EnergySourceCategory
    percentage: float


@dataclass(kw_only=True)
class EnvironmentalImpactUpdate(BaseUpdate):
    category: EnvironmentalImpactCategory
    amount: float


@dataclass(kw_only=True)
class EnergyMixUpdate(BaseUpdate):
    is_green_energy: bool | None = None
    energy_sources: list[EnergySourceUpdate] | None = None
    environ_impact: list[EnvironmentalImpactUpdate] | None = None
    supplier_name: str | None = None
    energy_product_name: str | None = None


@dataclass(kw_only=True)
class DisplayTextUpdate(BaseUpdate):
    language: str  # Max 2 chars
    text: str  # Max 512 chars


@dataclass(kw_only=True)
class AdditionalGeoLocationUpdate(BaseUpdate):
    name: DisplayTextUpdate | None = None
    latitude: Decimal
    longitude: Decimal


@dataclass(kw_only=True)
class LocationUpdate(BaseUpdate):
    _object_keys = (
        'charging_pool',
        'images',
        'operator',
        'suboperator',
        'owner',
        'max_power',
    )

    uid: str
    source: str
    charging_pool: list[ChargingStationUpdate]
    images: list[ImageUpdate] | None = None
    operator: BusinessUpdate | None = None
    suboperator: BusinessUpdate | None = None
    owner: BusinessUpdate | None = None
    exceptional_closings: list[ExceptionalPeriodUpdate] | None = None
    exceptional_openings: list[ExceptionalPeriodUpdate] | None = None
    regular_hours: list[RegularHoursUpdate] | None = None
    energy_mix: EnergyMixUpdate | None = None
    max_power: MaxPowerUpdate | None = None

    name: str | None = None
    address: str | None = None
    postal_code: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    lat: Decimal
    lon: Decimal

    directions: str | None = None
    related_locations: list[AdditionalGeoLocationUpdate] | None = None
    parking_type: ParkingType | None = None
    time_zone: str

    last_updated: datetime | None = None

    terms_and_conditions: str | None = None
    twentyfourseven: bool | None = None
    charging_when_closed: bool | None = None
    help_phone: str | None = None

    def __post_init__(self):
        if self.lat is not None:
            self.lat = self.lat.quantize(Decimal('.0000001'))
        if self.lon is not None:
            self.lon = self.lon.quantize(Decimal('.0000001'))
