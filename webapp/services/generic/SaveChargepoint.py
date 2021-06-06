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

from typing import List, Optional
from datetime import datetime
from dataclasses import dataclass, asdict
from ...models import Chargepoint, Location, RelatedResource
from ...extensions import logger, db
from ...enums import ChargepointStatus, ParkingRestriction, Capability

from .SaveRelatedResources import RelatedResourceUpdate, get_related_resource_updates, save_related_resources


@dataclass
class ChargepointUpdate:
    evse_id: Optional[str] = None
    phone: Optional[str] = None
    parking_uid: Optional[str] = None
    parking_floor_level: Optional[str] = None
    parking_spot_number: Optional[str] = None
    capabilities: Optional[List[Capability]] = None
    parking_restrictions: Optional[List[ParkingRestriction]] = None
    status: Optional[ChargepointStatus] = None
    related_resources: Optional[List[RelatedResourceUpdate]] = None
    last_updated: Optional[datetime] = None


def upsert_chargepoint(
        chargepoint_update: ChargepointUpdate,
        location: Location,
        old_chargepoint: Optional[Chargepoint] = None,
        old_related_resources: Optional[List[RelatedResource]] = None,
        commit: bool = True) -> Chargepoint:
    chargepoint = old_chargepoint if old_chargepoint else Chargepoint.query\
        .filter_by(evse_id=chargepoint_update.evse_id)\
        .first()
    related_resource_updates = get_related_resource_updates(chargepoint, chargepoint_update, old_related_resources)
    update_required = related_resource_updates.update_required
    if chargepoint and not update_required:
        for field in asdict(chargepoint_update):
            if field in ['status', 'related_resources', 'last_updated']:
                continue
            if getattr(chargepoint, field) != getattr(chargepoint_update, field):
                update_required = True
                break
        if chargepoint_update.status == ChargepointStatus.AVAILABLE:
            if chargepoint.status in [item for item in list(ChargepointStatus) if item != ChargepointStatus.AVAILABLE]:
                update_required = True
        elif chargepoint.status != chargepoint_update.status:
            update_required = True
    elif not chargepoint:
        update_required = True
        chargepoint = Chargepoint()
        chargepoint.location_id = location.id
    for field in asdict(chargepoint_update):
        if field in ['related_resouces', 'status', 'last_updated']:
            continue
        setattr(chargepoint, field, getattr(chargepoint_update, field))
    if not chargepoint_update.last_updated or not chargepoint.last_updated or chargepoint_update.last_updated > chargepoint.last_updated:
        chargepoint.last_updated = chargepoint_update.last_updated

    if chargepoint_update.status == ChargepointStatus.AVAILABLE:
        if chargepoint.status in [item for item in list(ChargepointStatus) if item != ChargepointStatus.AVAILABLE] or chargepoint.status is None:
            chargepoint.status = ChargepointStatus.AVAILABLE
    elif chargepoint.status != chargepoint_update.status:
        chargepoint.status = chargepoint_update.status

    if not update_required:
        return chargepoint

    if commit:
        db.session.add(chargepoint)
        db.session.commit()
        save_related_resources(chargepoint, related_resource_updates)
        logger.info('ochp.chargepoint.update', 'updated chargepoint %s' % chargepoint.id)
    return chargepoint
