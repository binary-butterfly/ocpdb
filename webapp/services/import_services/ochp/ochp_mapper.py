"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2022 binary butterfly GmbH

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
from typing import Any, Dict, List

from pycountry import countries

from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import Capability, EvseStatus, ParkingRestriction
from webapp.models.image import ImageCategory
from webapp.models.location import ParkingType
from webapp.services.import_services.models import (
    ConnectorUpdate,
    EvseUpdate,
    ImageUpdate,
    LocationUpdate,
    RegularHoursUpdate,
)

from .ochp_models import (
    OchpAuthMethodType,
    OchpChargePointType,
    OchpConnectorFormat,
    OchpConnectorStandard,
    OchpImageCategory,
    OchpLocationType,
    OchpMajorStatus,
    OchpMinorStatus,
    OchpParkingRestrictionType,
    OchpStaticStatus,
)
from .ochp_validators import ChargePointInput, ChargePointStatusInput, ConnectorInput, ImageInput


class OchpMapper:
    @staticmethod
    def clean_list(items: List[Any]) -> List[Any]:
        return list({item for item in items if item is not None})

    @staticmethod
    def map_connector_format(ochp_format: OchpConnectorFormat) -> ConnectorFormat:
        return {
            OchpConnectorFormat.Cable: ConnectorFormat.CABLE,
            OchpConnectorFormat.Socket: ConnectorFormat.SOCKET,
        }.get(ochp_format)

    @staticmethod
    def map_connector_standard(ochp_standard: OchpConnectorStandard) -> ConnectorType:
        return {
            OchpConnectorStandard.Chademo: ConnectorType.CHADEMO,
            OchpConnectorStandard.IEC_62196_T1: ConnectorType.IEC_62196_T1,
            OchpConnectorStandard.IEC_62196_T1_COMBO: ConnectorType.IEC_62196_T1_COMBO,
            OchpConnectorStandard.IEC_62196_T2: ConnectorType.IEC_62196_T2,
            OchpConnectorStandard.IEC_62196_T2_COMBO: ConnectorType.IEC_62196_T2_COMBO,
            OchpConnectorStandard.IEC_62196_T3A: ConnectorType.IEC_62196_T3A,
            OchpConnectorStandard.IEC_62196_T3C: ConnectorType.IEC_62196_T3C,
            OchpConnectorStandard.DOMESTIC_A: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_B: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_C: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_D: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_E: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_F: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_G: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_H: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_I: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_J: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_K: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.DOMESTIC_L: ConnectorType.DOMESTIC_A,
            OchpConnectorStandard.TESLA_R: ConnectorType.TESLA_R,
            OchpConnectorStandard.TESLA_S: ConnectorType.TESLA_S,
            OchpConnectorStandard.IEC_60309_2_single_16: ConnectorType.IEC_60309_2_single_16,
            OchpConnectorStandard.IEC_60309_2_three_16: ConnectorType.IEC_60309_2_three_16,
            OchpConnectorStandard.IEC_60309_2_three_32: ConnectorType.IEC_60309_2_three_32,
            OchpConnectorStandard.IEC_60309_2_three_64: ConnectorType.IEC_60309_2_three_64,
        }.get(ochp_standard)

    @staticmethod
    def map_ochp_static_status_to_evse_status(ochp_static_status: OchpStaticStatus) -> EvseStatus:
        return {
            OchpStaticStatus.Unknown: EvseStatus.UNKNOWN,
            OchpStaticStatus.Operative: EvseStatus.AVAILABLE,
            OchpStaticStatus.Inoperative: EvseStatus.INOPERATIVE,
            OchpStaticStatus.Planned: EvseStatus.PLANNED,
            OchpStaticStatus.Closed: EvseStatus.REMOVED,
        }.get(ochp_static_status)

    @staticmethod
    def map_ochp_major_status_to_evse_status(ochp_major_status: OchpMajorStatus) -> EvseStatus:
        return {
            OchpMajorStatus.available: EvseStatus.AVAILABLE,
            OchpMajorStatus.not_available: EvseStatus.INOPERATIVE,
            OchpMajorStatus.unknown: EvseStatus.UNKNOWN,
        }.get(ochp_major_status)

    @staticmethod
    def map_ochp_minor_status_to_evse_status(ochp_minor_status: OchpMinorStatus) -> EvseStatus:
        return {
            OchpMinorStatus.available: EvseStatus.AVAILABLE,
            OchpMinorStatus.reserved: EvseStatus.RESERVED,
            OchpMinorStatus.blocked: EvseStatus.BLOCKED,
            OchpMinorStatus.charging: EvseStatus.CHARGING,
            OchpMinorStatus.outoforder: EvseStatus.OUTOFORDER,
        }.get(ochp_minor_status)

    @staticmethod
    def map_parking_restriction(ochp_parking_restriction: OchpParkingRestrictionType) -> ParkingRestriction:
        return {
            OchpParkingRestrictionType.evonly: ParkingRestriction.EV_ONLY,
            OchpParkingRestrictionType.plugged: ParkingRestriction.PLUGGED,
            OchpParkingRestrictionType.disabled: ParkingRestriction.DISABLED,
            OchpParkingRestrictionType.customers: ParkingRestriction.CUSTOMERS,
            OchpParkingRestrictionType.motorcycles: ParkingRestriction.MOTORCYCLES,
            OchpParkingRestrictionType.carsharing: ParkingRestriction.CARSHARING,
        }.get(ochp_parking_restriction)

    @staticmethod
    def map_image_category(image_category: OchpImageCategory) -> ImageCategory:
        return {
            OchpImageCategory.networkLogo: ImageCategory.NETWORK,
            OchpImageCategory.operatorLogo: ImageCategory.OPERATOR,
            OchpImageCategory.ownerLogo: ImageCategory.OWNER,
            OchpImageCategory.stationPhoto: ImageCategory.CHARGER,
            OchpImageCategory.locationPhoto: ImageCategory.LOCATION,
            OchpImageCategory.entrancePhoto: ImageCategory.ENTRANCE,
            OchpImageCategory.otherPhoto: ImageCategory.OTHER,
            OchpImageCategory.otherLogo: ImageCategory.OTHER,
            OchpImageCategory.otherGraphic: ImageCategory.OTHER,
        }.get(image_category)

    @staticmethod
    def map_charge_point_type_to_power_type(charge_point_type: OchpChargePointType) -> PowerType:
        return {
            OchpChargePointType.AC: PowerType.AC_3_PHASE,
            OchpChargePointType.DC: PowerType.DC,
        }.get(charge_point_type)

    @staticmethod
    def map_auth_method_to_capability(auth_method: OchpAuthMethodType) -> Capability:
        return {
            OchpAuthMethodType.Public: Capability.PUBLIC,
            OchpAuthMethodType.LocalKey: Capability.LOCAL_KEY,
            OchpAuthMethodType.DirectCash: Capability.CASH,
            OchpAuthMethodType.DirectCreditcard: Capability.CREDIT_CARD_PAYABLE,
            OchpAuthMethodType.DirectDebitcard: Capability.DEBIT_CARD_PAYABLE,
            OchpAuthMethodType.RfidMifareCls: Capability.RFID_READER,
            OchpAuthMethodType.RfidMifareDes: Capability.RFID_READER,
            OchpAuthMethodType.Iec15118: Capability.IEC15118,
            OchpAuthMethodType.OchpDirectAuth: Capability.REMOTE_START_STOP_CAPABLE,
            OchpAuthMethodType.OperatorAuth: Capability.DIRECT_REMOTE,
            OchpAuthMethodType.RfidCalypso: Capability.RFID_READER,
        }.get(auth_method)

    @staticmethod
    def map_ochp_location_type_to_parking_type(location_type: OchpLocationType) -> ParkingType:
        return {
            OchpLocationType.on_street: ParkingType.ON_STREET,
            OchpLocationType.parking_garage: ParkingType.PARKING_GARAGE,
            OchpLocationType.underground_garage: ParkingType.UNDERGROUND_GARAGE,
            OchpLocationType.parking_lot: ParkingType.PARKING_LOT,
            OchpLocationType.private: ParkingType.PRIVATE,
        }.get(location_type)

    def map_chargepoint_to_location_update(self, charge_point_inputs: List[ChargePointInput]) -> LocationUpdate:
        # location data is all the same
        charge_point_input = charge_point_inputs[0]

        charge_point_address = charge_point_input.chargePointAddress.address.strip()
        if (
            charge_point_input.chargePointAddress.houseNumber is not None
            and charge_point_input.chargePointAddress.houseNumber != '0'
        ):
            charge_point_address += ' ' + charge_point_input.chargePointAddress.houseNumber.strip()

        location_update = LocationUpdate(
            source='ochp',
            uid=charge_point_input.locationId,
            last_updated=charge_point_input.timestamp or datetime.now(tz=timezone.utc),
            name=charge_point_input.locationName,
            address=charge_point_address.strip().replace('  ', ' '),
            postal_code=charge_point_input.chargePointAddress.zipCode,
            city=charge_point_input.chargePointAddress.city,
            country=countries.get(alpha_3=charge_point_input.chargePointAddress.country).alpha_2,
            lat=charge_point_input.chargePointLocation.lat,
            lon=charge_point_input.chargePointLocation.lon,
            time_zone=charge_point_input.timeZone,
            parking_type=self.map_ochp_location_type_to_parking_type(charge_point_input.location),
            evses=[
                self.map_chargepoint_to_evse(single_charge_point_input)
                for single_charge_point_input in charge_point_inputs
            ],
            # ignored: locationNameLang
            # ignored: relatedLocation
        )

        if charge_point_input.openingTimes:
            if charge_point_input.openingTimes.twentyfourseven is not None:
                location_update.twentyfourseven = charge_point_input.openingTimes.twentyfourseven
            elif charge_point_input.openingTimes.regularHours is not None:
                location_update.regular_hours = []
                for regular_hour_input in charge_point_input.openingTimes.regularHours:
                    location_update.regular_hours.append(
                        RegularHoursUpdate(
                            weekday=regular_hour_input.weekday,
                            period_begin=regular_hour_input.periodBegin.hour * 3600
                            + regular_hour_input.periodBegin.minute * 60,
                            period_end=regular_hour_input.periodEnd.hour * 3600
                            + regular_hour_input.periodEnd.minute * 60,
                        ),
                    )

        # Images like logos can appear multiple times, so we group them
        # TODO: image deduplication beyond urls
        images_by_url: Dict[str, ImageUpdate] = {}
        for charge_point_input in charge_point_inputs:
            for image_input in charge_point_input.images:
                if image_input.uri in images_by_url:
                    continue
                images_by_url[image_input.uri] = self.map_image(image_input)

        location_update.images = list(images_by_url.values())

        return location_update

    def map_chargepoint_to_evse(self, charge_point_input: ChargePointInput) -> EvseUpdate:
        evse_update = EvseUpdate(
            uid=charge_point_input.evseId,
            last_updated=charge_point_input.timestamp or datetime.now(tz=timezone.utc),
            status=OchpMapper.map_ochp_static_status_to_evse_status(charge_point_input.status),
            phone=charge_point_input.telephoneNumber,
            parking_restrictions=[
                self.map_parking_restriction(restriction) for restriction in charge_point_input.parkingRestriction
            ],
            connectors=[],
            images=[],
        )

        for connector_position, connector_input in enumerate(charge_point_input.connectors):
            evse_update.connectors.append(self.map_connector(connector_input, connector_position))

        for image_input in charge_point_input.images:
            if image_input.class_ == OchpImageCategory.stationPhoto:
                evse_update.images.append(self.map_image(image_input))

        return evse_update

    def map_evse_status_to_update(self, evse_status: ChargePointStatusInput) -> EvseUpdate:
        evse_update = EvseUpdate(
            uid=evse_status.evseId,
            last_updated=evse_status.ttl,
        )

        if evse_status.minor is None:
            evse_update.status = self.map_ochp_major_status_to_evse_status(evse_status.major)
        else:
            evse_update.status = self.map_ochp_minor_status_to_evse_status(evse_status.minor)

        return evse_update

    @staticmethod
    def map_connector(ochp_connector: ConnectorInput, position: int) -> ConnectorUpdate:
        return ConnectorUpdate(
            format=OchpMapper.map_connector_format(ochp_connector.connectorFormat),
            standard=OchpMapper.map_connector_standard(ochp_connector.connectorStandard),
            uid=str(position),
        )

    def map_image(self, image_input: ImageInput) -> ImageUpdate:
        return ImageUpdate(
            external_url=image_input.uri,
            type=image_input.type,
            category=self.map_image_category(image_input.class_),
            width=image_input.width,
            height=image_input.width,
        )
