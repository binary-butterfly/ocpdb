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

from typing import Optional, List, TYPE_CHECKING
from dataclasses import dataclass, asdict
from ...enums import RelatedResourceType
from ...models import RelatedResource, Chargepoint
from ...extensions import db
if TYPE_CHECKING:
    from .SaveChargepoint import ChargepointUpdate


@dataclass
class RelatedResourceUpdate:
    url: str
    types: List[RelatedResourceType]


@dataclass
class RelatedResourceUpdates:
    update_required: Optional[bool] = None
    related_resources: Optional[List[RelatedResource]] = None
    new_related_resources: Optional[List[RelatedResource]] = None
    deleted_related_resources: Optional[List[int]] = None


related_resource_mapping = {
    'operatorMap': RelatedResourceType.OPERATOR_MAP,
    'operatorPayment': RelatedResourceType.OPERATOR_PAYMENT,
    'stationInfo': RelatedResourceType.STATION_INFO,
    'surroundingInfo': RelatedResourceType.SURROUNDING_INFO,
    'ownerHomepage': RelatedResourceType.OWNER_HOMEPAGE,
    'feedbackForm': RelatedResourceType.FEEDBACK_FORM,
    'openingTimes': RelatedResourceType.OPENING_TIMES
}


def get_related_resource_updates(
        chargepoint: Chargepoint,
        chargepoint_update: 'ChargepointUpdate',
        related_resources: Optional[List[RelatedResource]] = None) -> RelatedResourceUpdates:
    if related_resources is None:
        related_resources = RelatedResource.query.filter_by(chargepoint_id=chargepoint.id).all() if chargepoint else []
    old_ids = [related_resource.id for related_resource in related_resources]
    related_resource_updates = RelatedResourceUpdates(related_resources=related_resources)
    related_resource_updates.new_related_resources = []
    related_resource_updates.deleted_related_resources = []
    if chargepoint_update.related_resources is None:
        return related_resource_updates
    for related_resource_update in chargepoint_update.related_resources:
        old_id = next((related_resource.id for related_resource in related_resources if related_resource.url == related_resource_update.url), None)
        if old_id is not None and old_id in old_ids:
            old_ids.remove(old_id)
        else:
            related_resource = RelatedResource()
            for field in asdict(related_resource_update):
                setattr(related_resource, field, getattr(related_resource_update, field))
            related_resource_updates.new_related_resources.append(related_resource)
    related_resource_updates.update_required = len(related_resource_updates.new_related_resources) > 0 or \
        len(related_resource_updates.deleted_related_resources) > 0
    return related_resource_updates


def save_related_resources(chargepoint: Chargepoint, related_resource_updates: RelatedResourceUpdates):
    for related_resource in related_resource_updates.new_related_resources:
        related_resource.chargepoint_id = chargepoint.id
        db.session.add(related_resource)
    db.session.commit()
    if len(related_resource_updates.deleted_related_resources):
        RelatedResource.query \
            .filter(RelatedResource.id.in_(related_resource_updates.deleted_related_resources)) \
            .delete(synchronize_session=False)
