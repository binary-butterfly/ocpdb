# encoding: utf-8

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

import traceback
from lxml import etree
from typing import Union
from datetime import timedelta, datetime
from wtfjson import DictInput
from wtfjson.fields import StringField, DateTimeField, ListField, FloatField, IntegerField, BooleanField, ObjectField
from wtfjson.validators import Length, Regexp, AnyOf
from ...extensions import logger
from .SaveLocation import get_location_update
from ..generic.SaveLocation import upsert_location
from .SaveImage import get_image_updates
from ..generic.SaveImage import upsert_images
from .Helper import get_nsmap, get_field
from ...enums import ChargepointStatus, ParkingRestriction, Capability, PowerType, ExceptionalPeriodType
from .SaveConnector import get_connector_updates
from ..generic.SaveConnector import upsert_connector
from ...common.helpers import get_now_localized
from ..generic.SaveRelatedResources import RelatedResourceUpdate, related_resource_mapping
from ..generic.SaveChargepoint import ChargepointUpdate, upsert_chargepoint


def save_chargepoints(data_xml: etree, download: bool = True):
    start = get_now_localized() - timedelta(seconds=10)
    data_chargepoints = data_xml.xpath(
        '//soap:Envelope/soap:Body/ns:GetChargePointListResponse/ns:chargePointInfoArray',
        namespaces=get_nsmap()
    )

    updated_locations = {}
    for data_chargepoint in data_chargepoints:
        try:
            save_chargepoint(data_chargepoint, updated_locations, start, download)
        except:
            logger.error(
                'ochp.chargepoint',
                "error saving chargepoint %s\n%s" % (etree.tostring(data_chargepoint), traceback.format_exc())
            )


def save_chargepoint(data_chargepoint: etree, updated_locations: dict, start: datetime, download: bool = True):
    location_update = get_location_update(data_chargepoint)
    if not location_update:
        return
    if location_update.uid not in updated_locations:
        location = upsert_location(location_update)
        if not location:
            return
        updated_locations[location_update.uid] = location
    chargepoint_update = get_chargepoint_update(data_chargepoint)
    if not chargepoint_update or location_update.uid not in updated_locations:
        return
    chargepoint = upsert_chargepoint(chargepoint_update, updated_locations[location_update.uid])
    if not chargepoint:
        logger.error('ochp.chargepoint', 'invalid chargepoint found: %s' % chargepoint)
        return
    for connector_update in get_connector_updates(data_chargepoint):
        upsert_connector(connector_update, chargepoint)
    upsert_images(get_image_updates(data_chargepoint), chargepoint, start, download)


status_mapping = {
    'Unknown': ChargepointStatus.UNKNOWN,
    'Operative': ChargepointStatus.AVAILABLE,
    'Inoperative': ChargepointStatus.INOPERATIVE,
    'Planned': ChargepointStatus.PLANNED,
    'Closed': ChargepointStatus.REMOVED
}


parking_restriction_mapping = {
    'evonly': ParkingRestriction.EV_ONLY,
    'plugged': ParkingRestriction.PLUGGED,
    'disabled': ParkingRestriction.DISABLED,
    'customers': ParkingRestriction.CUSTOMERS,
    'motorcycles': ParkingRestriction.MOTORCYCLES,
    'carsharing': ParkingRestriction.CARSHARING
}

power_type_mapping = {
    'AC': PowerType.AC_3_PHASE,
    'DC': PowerType.DC
}

capability_mapping = {
    'Public': Capability.PUBLIC,
    'LocalKey': Capability.LOCAL_KEY,
    'DirectCash': Capability.CASH,
    'DirectCreditcard': Capability.CREDIT_CARD_PAYABLE,
    'DirectDebitcard': Capability.DEBIT_CARD_PAYABLE,
    'RfidMifareCls': Capability.RFID_READER,
    'RfidMifareDes': Capability.RFID_READER,
    'Iec15118': Capability.IEC15118,
    'OchpDirectAuth': Capability.REMOTE_START_STOP_CAPABLE,
    'OperatorAuth': Capability.DIRECT_REMOTE,
    'RfidCalypso': Capability.RFID_READER
}


def get_chargepoint_update(data_chargepoint: etree) -> Union[ChargepointUpdate, None]:
    chargepoint = {
        'related_resources': []
    }
    nsmap = get_nsmap()
    chargepoint['evse_id'] = get_field(data_chargepoint, 'evseId', nsmap)
    if get_field(data_chargepoint, 'telephoneNumber', nsmap):
        chargepoint['phone'] = get_field(data_chargepoint, 'telephoneNumber', nsmap)
    if get_field(data_chargepoint, 'status/ns:ChargePointStatusType', nsmap):
        chargepoint['status'] = get_field(data_chargepoint, 'status/ns:ChargePointStatusType', nsmap)
    chargepoint['capabilities'] = get_field(data_chargepoint, 'authMethods/ns:AuthMethodType', nsmap, list=True)

    for data_parking in get_field(data_chargepoint, 'parkingSpot', nsmap, list=True, text=False, default=[]):
        chargepoint['parking_uid'] = get_field(data_parking, 'parkingId', nsmap)
        if get_field(data_parking, 'parkingSpotNumber', nsmap):
            chargepoint['parking_spot_number'] = get_field(data_parking, 'parkingSpotNumber', nsmap)
        if get_field(data_parking, 'floorlevel', nsmap):
            chargepoint['parking_floor_level'] = get_field(data_parking, 'floorlevel', nsmap)
        chargepoint['parking_restrictions'] = get_field(data_parking, 'restriction/ns:RestrictionType', nsmap, list=True, default=[])
        # we just support one parking spot because OCPI supports just one
        break
    for related_resource in get_field(data_chargepoint, 'relatedResource', nsmap, list=True, text=False, default=[]):
        chargepoint['related_resources'].append({
            'url': get_field(related_resource, 'uri', nsmap),
            'types': get_field(related_resource, 'class', nsmap, list=True, default=[])
        })
    validator = ChargepointValidator(chargepoint)
    if not validator.validate():
        logger.error('ochp.chargepoint', 'invalid chargepoint found: %s - %s' % (chargepoint, validator.errors))
        return
    chargepoint_update = ChargepointUpdate(source='ochp', uid=validator.evse_id.out)
    validator.populate_obj(chargepoint_update)
    return chargepoint_update


class RelatedResourcesValidator(DictInput):
    url = StringField()
    types = ListField(StringField(
        validators=[AnyOf(list(related_resource_mapping.keys()))],
        output_filters=[lambda item: related_resource_mapping[item]]
    ))


class ChargepointValidator(DictInput):
    evse_id = StringField(validators=[Length(max=32)])  # standard says 15 max, but there are datasets with longer evse_ids
    phone = StringField(required=False, validators=[Length(max=20), Regexp(r'[\d -]+')])
    last_updated = DateTimeField(required=False)
    capabilities = ListField(StringField(
        validators=[AnyOf(list(capability_mapping.keys()))],
        output_filters=[lambda item: capability_mapping[item]]
    ), required=False, output_filters=[lambda item: sorted(list(set(item)), key=lambda item: item.value)])
    parking_restrictions = ListField(StringField(
        validators=[AnyOf(list(parking_restriction_mapping.keys()))],
        output_filters=[lambda item: parking_restriction_mapping[item]]
    ), required=False, output_filters=[lambda item: sorted(list(set(item)), key=lambda item: item.value)])
    parking_uid = StringField(required=False, validators=[Length(max=64)])  # standard says 30 max, but there are datasets with longer evse_ids
    parking_floor_level = StringField(required=False, validators=[Length(max=4)])
    parking_spot_number = StringField(required=False, validators=[Length(max=5)])
    max_reservation = FloatField(required=False)
    status = StringField(
        required=False,
        validators=[AnyOf(list(status_mapping.keys()))],
        output_filters=[lambda item: status_mapping[item]]
    )
    related_resources = ListField(ObjectField(
        RelatedResourcesValidator,
        output_filters=[lambda item: RelatedResourceUpdate(**item)]
    ), required=False)
