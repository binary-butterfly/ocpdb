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

from lxml import etree
from typing import Optional, Union
from dataclasses import dataclass
from wtfjson import DictInput
from wtfjson.fields import StringField
from wtfjson.validators import Length, AnyOf
from ...models import Chargepoint
from ...extensions import logger, db
from .Helper import get_nsmap, get_field
from ...enums import ChargepointStatus
from ...common.helpers import get_now_localized


def save_chargepoints_live(data_xml: etree):
    data_chargepoints = data_xml.xpath(
        '//soap:Envelope/soap:Body/ns:GetStatusResponse/ns:evse',
        namespaces=get_nsmap()
    )
    for data_chargepoint in data_chargepoints:
        save_chargepoint_live(data_chargepoint)


status_mapping = {
    'unknown': ChargepointStatus.UNKNOWN,
    'available': ChargepointStatus.AVAILABLE,
    'not-available': ChargepointStatus.INOPERATIVE,
    'reserved': ChargepointStatus.RESERVED,
    'charging': ChargepointStatus.CHARGING,
    'blocked': ChargepointStatus.BLOCKED,
    'outoforder': ChargepointStatus.OUTOFORDER
}


@dataclass
class ChargepointLiveUpdate:
    status = Optional[str]
    evse_id = Optional[str]


def save_chargepoint_live(data_chargepoint: etree, commit: bool = True):
    chargepoint_update = get_chargepoint_data(data_chargepoint)
    if chargepoint_update is None:
        return
    upsert_chargepoint_live(chargepoint_update)


def get_chargepoint_data(data_chargepoint: etree) -> Union[ChargepointLiveUpdate, None]:
    chargepoint = {}
    chargepoint['status'] = data_chargepoint.get('minor') if data_chargepoint.get('minor') else data_chargepoint.get('major')
    chargepoint['evse_id'] = get_field(data_chargepoint, 'evseId', nsmap=get_nsmap())
    validator = ChargepointLiveValidator(chargepoint)
    if not validator.validate():
        logger.error('ochp.chargepoint', 'invalid chargepoint found: %s' % chargepoint)
        return
    chargepoint_live_update = ChargepointLiveUpdate()
    validator.populate_obj(chargepoint_live_update)
    return chargepoint_live_update


def upsert_chargepoint_live(
        chargepoint_live_update: ChargepointLiveUpdate,
        commit: bool = True) -> Union[Chargepoint, None]:
    chargepoint = Chargepoint.query.filter_by(evse_id=chargepoint_live_update.evse_id).first()
    if not chargepoint:
        return
    if chargepoint.status == chargepoint_live_update.status:
        return
    chargepoint.status = chargepoint_live_update.status
    chargepoint.last_updated = get_now_localized()
    if commit:
        db.session.add(chargepoint)
        db.session.commit()
        logger.info('ochp.chargepoint.update', 'updated chargepoint %s' % chargepoint.id)
    return chargepoint


class ChargepointLiveValidator(DictInput):
    status = StringField(
        validators=[AnyOf(list(status_mapping.keys()))],
        output_filters=[lambda item: status_mapping[item]]
    )
    evse_id = StringField(
        validators=[Length(min=1)]
    )
