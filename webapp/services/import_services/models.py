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
from typing import List, Optional

from validataclass.helpers import OptionalUnset, UnsetValue

from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import Capability, EvseStatus, ParkingRestriction
from webapp.models.image import ImageCategory
from webapp.models.location import ParkingType
from webapp.models.related_resource import RelatedResourceType


@dataclass
class SourceInfo:
    uid: str
    name: str
    public_url: str
    has_realtime_data: Optional[bool]
    timezone: str = 'Europe/Berlin'
    source_url: Optional[str] = None
    attribution_license: Optional[str] = None
    attribution_url: Optional[str] = None
    attribution_contributor: Optional[str] = None

    def to_dict(self) -> dict:
        return {key: value for key, value in asdict(self).items() if value is not None}


@dataclass
class BaseUpdate:
    _object_keys = ()

    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in asdict(self).items()
            if value is not UnsetValue and key not in self._object_keys
        }


@dataclass
class ImageUpdate(BaseUpdate):
    external_url: OptionalUnset[str] = UnsetValue
    type: OptionalUnset[str] = UnsetValue
    category: OptionalUnset[ImageCategory] = UnsetValue
    width: OptionalUnset[int] = UnsetValue
    height: OptionalUnset[int] = UnsetValue
    last_download: OptionalUnset[datetime] = UnsetValue


@dataclass
class BusinessUpdate(BaseUpdate):
    _object_keys = ('logo',)

    logo: OptionalUnset[ImageUpdate] = UnsetValue
    name: OptionalUnset[str] = UnsetValue
    website: OptionalUnset[str] = UnsetValue


@dataclass
class RelatedResourceUpdate(BaseUpdate):
    url: OptionalUnset[str] = UnsetValue
    types: OptionalUnset[List[RelatedResourceType]] = UnsetValue


@dataclass
class RegularHoursUpdate(BaseUpdate):
    weekday: int
    period_begin: int
    period_end: int


@dataclass
class ExceptionalPeriodUpdate(BaseUpdate):
    period_begin: OptionalUnset[datetime] = UnsetValue
    period_end: OptionalUnset[datetime] = UnsetValue


@dataclass
class ConnectorUpdate(BaseUpdate):
    uid: str
    standard: OptionalUnset[ConnectorType] = UnsetValue
    format: OptionalUnset[ConnectorFormat] = UnsetValue
    power_type: OptionalUnset[PowerType] = UnsetValue
    max_voltage: OptionalUnset[int] = UnsetValue
    max_amperage: OptionalUnset[int] = UnsetValue
    max_electric_power: OptionalUnset[int] = UnsetValue
    last_updated: OptionalUnset[datetime] = UnsetValue
    terms_and_conditions: OptionalUnset[str] = UnsetValue


@dataclass
class EvseUpdate(BaseUpdate):
    _object_keys = ('connectors', 'images', 'related_resource')

    uid: str
    evse_id: str

    connectors: OptionalUnset[List[ConnectorUpdate]] = UnsetValue
    images: OptionalUnset[List[ImageUpdate]] = UnsetValue
    related_resource: OptionalUnset[List[RelatedResourceUpdate]] = UnsetValue

    status: OptionalUnset[EvseStatus] = UnsetValue

    lat: OptionalUnset[Decimal] = UnsetValue
    lon: OptionalUnset[Decimal] = UnsetValue

    floor_level: OptionalUnset[str] = UnsetValue
    physical_reference: OptionalUnset[str] = UnsetValue
    directions: OptionalUnset[str] = UnsetValue
    phone: OptionalUnset[str] = UnsetValue

    parking_uid: OptionalUnset[str] = UnsetValue
    parking_floor_level: OptionalUnset[str] = UnsetValue
    parking_spot_number: OptionalUnset[str] = UnsetValue

    last_updated: OptionalUnset[datetime] = UnsetValue
    max_reservation: OptionalUnset[float] = UnsetValue
    capabilities: OptionalUnset[List[Capability]] = UnsetValue
    parking_restrictions: OptionalUnset[List[ParkingRestriction]] = UnsetValue

    terms_and_conditions: OptionalUnset[str] = UnsetValue

    def __post_init__(self):
        if self.lat is not UnsetValue:
            self.lat = self.lat.quantize(Decimal('.0000001'))
        if self.lon is not UnsetValue:
            self.lon = self.lon.quantize(Decimal('.0000001'))


@dataclass
class LocationUpdate(BaseUpdate):
    _object_keys = (
        'evses',
        'images',
        'operator',
        'suboperator',
        'owner',
        'exceptional_closings',
        'exceptional_openings',
        'regular_hours',
    )

    uid: str
    source: str
    evses: OptionalUnset[List[EvseUpdate]] = UnsetValue
    images: OptionalUnset[List[ImageUpdate]] = UnsetValue
    operator: OptionalUnset[BusinessUpdate] = UnsetValue
    suboperator: OptionalUnset[BusinessUpdate] = UnsetValue
    owner: OptionalUnset[BusinessUpdate] = UnsetValue
    exceptional_closings: OptionalUnset[List[ExceptionalPeriodUpdate]] = UnsetValue
    exceptional_openings: OptionalUnset[List[ExceptionalPeriodUpdate]] = UnsetValue
    regular_hours: OptionalUnset[List[RegularHoursUpdate]] = UnsetValue

    name: OptionalUnset[str] = UnsetValue
    address: OptionalUnset[str] = UnsetValue
    postal_code: OptionalUnset[str] = UnsetValue
    city: OptionalUnset[str] = UnsetValue
    state: OptionalUnset[str] = UnsetValue
    country: OptionalUnset[str] = UnsetValue
    lat: OptionalUnset[Decimal] = UnsetValue
    lon: OptionalUnset[Decimal] = UnsetValue

    directions: OptionalUnset[str] = UnsetValue
    parking_type: OptionalUnset[ParkingType] = UnsetValue
    time_zone: OptionalUnset[str] = UnsetValue

    last_updated: OptionalUnset[datetime] = UnsetValue

    terms_and_conditions: OptionalUnset[str] = UnsetValue
    twentyfourseven: OptionalUnset[bool] = UnsetValue

    def __post_init__(self):
        if self.lat is not UnsetValue:
            self.lat = self.lat.quantize(Decimal('.0000001'))
        if self.lon is not UnsetValue:
            self.lon = self.lon.quantize(Decimal('.0000001'))
