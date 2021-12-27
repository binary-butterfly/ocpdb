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
from webapp.models import Chargepoint, Location, RelatedResource
from webapp.extensions import logger, db
from webapp.enums import ChargepointStatus, ParkingRestriction, Capability
from validataclass.helpers import OptionalUnsetNone, UnsetValue
from .SaveConnector import ConnectorUpdate

from .SaveRelatedResources import RelatedResourceUpdate, get_related_resource_updates, save_related_resources


@dataclass
class ChargepointUpdate:
    source: str  # TODO: this should not be part of an update
    uid: str  # TODO: this should not be part of an update
    evse_id: OptionalUnsetNone[str] = UnsetValue
    phone: OptionalUnsetNone[str] = UnsetValue
    parking_uid: OptionalUnsetNone[str] = UnsetValue
    parking_floor_level: OptionalUnsetNone[str] = UnsetValue
    parking_spot_number: OptionalUnsetNone[str] = UnsetValue
    capabilities: OptionalUnsetNone[List[Capability]] = UnsetValue
    parking_restrictions: OptionalUnsetNone[List[ParkingRestriction]] = UnsetValue
    status: OptionalUnsetNone[ChargepointStatus] = UnsetValue
    related_resources: OptionalUnsetNone[List[RelatedResourceUpdate]] = UnsetValue
    last_updated: OptionalUnsetNone[datetime] = UnsetValue
    connectors: OptionalUnsetNone[List[ConnectorUpdate]] = UnsetValue


def upsert_chargepoint(
        chargepoint_update: ChargepointUpdate,
        location: Location,
        old_chargepoint: Optional[Chargepoint] = None,
        old_related_resources: Optional[List[RelatedResource]] = None,
        commit: bool = True) -> Chargepoint:
    chargepoint = old_chargepoint if old_chargepoint else Chargepoint.query\
        .filter_by(uid=chargepoint_update.uid)\
        .filter_by(source=chargepoint_update.source)\
        .first()
    related_resource_updates = get_related_resource_updates(chargepoint, chargepoint_update, old_related_resources)
    update_required = related_resource_updates.update_required
    if chargepoint and not update_required:
        for field, value in asdict(chargepoint_update).items():
            if field in ['status', 'related_resources', 'last_updated', 'connectors']:
                continue
            if value is not UnsetValue and getattr(chargepoint, field) != value:
                update_required = True
                break
        if chargepoint_update.status == ChargepointStatus.AVAILABLE:
            if chargepoint.status in [item for item in list(ChargepointStatus) if item != ChargepointStatus.AVAILABLE]:
                update_required = True
        elif chargepoint_update.status is not UnsetValue and chargepoint.status != chargepoint_update.status:
            update_required = True
    elif not chargepoint:
        update_required = True
        chargepoint = Chargepoint()
        chargepoint.location_id = location.id
    for field, value in asdict(chargepoint_update).items():
        if field in ['related_resouces', 'status', 'last_updated', 'connectors']:
            continue
        if value is UnsetValue:
            continue
        setattr(chargepoint, field, value)
    if chargepoint_update.last_updated is not UnsetValue and (
        not chargepoint_update.last_updated
        or not chargepoint.last_updated
        or chargepoint_update.last_updated > chargepoint.last_updated
    ):
        chargepoint.last_updated = chargepoint_update.last_updated

    if chargepoint_update.status == ChargepointStatus.AVAILABLE:
        if chargepoint.status in [item for item in list(ChargepointStatus) if item != ChargepointStatus.AVAILABLE] or chargepoint.status is None:
            chargepoint.status = ChargepointStatus.AVAILABLE
    elif chargepoint.status != chargepoint_update.status and chargepoint_update.status != UnsetValue:
        chargepoint.status = chargepoint_update.status
    if not update_required:
        return chargepoint

    if commit:
        db.session.add(chargepoint)
        db.session.commit()
        save_related_resources(chargepoint, related_resource_updates)
        logger.info('ochp.chargepoint.update', 'updated chargepoint %s' % chargepoint.id)
    return chargepoint
