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

from typing import List, Dict, Union, Optional

from validataclass.helpers import OptionalUnset, UnsetValue

from webapp.common.remote_helper import RemoteHelper
from webapp.models import Location, Business, Image, Evse, Connector, RegularHours
from webapp.repositories import LocationRepository, EvseRepository, ConnectorRepository, ObjectNotFoundException, OptionRepository
from webapp.repositories.business_repository import BusinessRepository
from webapp.repositories.image_repository import ImageRepository
from webapp.services.base_service import BaseService
from webapp.services.import_services.models import LocationUpdate, EvseUpdate, ConnectorUpdate, ImageUpdate, RegularHoursUpdate


class BaseImportService(BaseService):
    remote_helper: RemoteHelper

    location_repository: LocationRepository
    evse_repository: EvseRepository
    connector_repository: ConnectorRepository
    business_repository: BusinessRepository
    image_repository: ImageRepository
    option_repository: OptionRepository

    def __init__(
            self,
            *args,
            remote_helper: RemoteHelper,
            location_repository: LocationRepository,
            evse_repository: EvseRepository,
            connector_repository: ConnectorRepository,
            business_repository: BusinessRepository,
            image_repository: ImageRepository,
            option_repository: OptionRepository,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.remote_helper = remote_helper
        self.location_repository = location_repository
        self.evse_repository = evse_repository
        self.connector_repository = connector_repository
        self.business_repository = business_repository
        self.image_repository = image_repository
        self.option_repository = option_repository

    def save_location_updates(self, location_updates: List[LocationUpdate], source: str):
        # get old location ids
        old_location_ids = self.location_repository.fetch_location_ids_by_source(source)

        # Business and Images are shared, so we just cache them to prevent sql queries
        businesses_by_name = {business.name: business for business in self.business_repository.fetch_businesses()}
        images_by_url = {image.external_url: image for image in self.image_repository.fetch_images()}

        # EVSE UIDs are critical because they are unique, so we fetch them related to location id in order to check them before saving
        # TODO: actually use this
        # evse_uids = {item[0]: item[1] for item in self.evse_repository.fetch_extended_evse_uids()}

        for location_update in location_updates:
            self.save_location_update(source, location_update, businesses_by_name, old_location_ids, images_by_url)

        # delete locations which are not part of the updated dataset anymore
        for old_location_id in old_location_ids:
            self.location_repository.delete_location(
                self.location_repository.fetch_location_by_id(old_location_id),
            )

    def save_location_update(
            self,
            source: str,
            location_update: LocationUpdate,
            businesses_by_name: Optional[Dict[str, Business]] = None,
            old_location_ids: Optional[List[int]] = None,
            images_by_url: Optional[Dict[str, Image]] = None,
    ):
        try:
            location = self.location_repository.fetch_location_by_uid(source, location_update.uid, include_children=True)
        except ObjectNotFoundException:
            location = Location()
        for key, value in location_update.to_dict().items():
            setattr(location, key, value)

        self.set_business(location, location_update, 'operator', businesses_by_name)
        self.set_business(location, location_update, 'suboperator', businesses_by_name)
        self.set_business(location, location_update, 'owner', businesses_by_name)
        self.set_image_list(location, location_update.images, images_by_url)
        self.set_opening_times(location, location_update.regular_hours)

        old_evse_by_uid = {evse.uid: evse for evse in location.evses}
        new_evses = []
        for evse_update in location_update.evses:
            # TODO: check for overlapping UIDs
            new_evses.append(self.get_evse(evse_update, old_evse_by_uid, images_by_url))

        location.evses = new_evses
        self.location_repository.save_location(location)

        if old_location_ids is not None and location.id in old_location_ids:
            old_location_ids.remove(location.id)

    def save_evse_updates(self, source: str, evse_updates: List[EvseUpdate]):
        for evse_update in evse_updates:
            self.save_evse_update(source, evse_update)

    def save_evse_update(self, source: str, evse_update: EvseUpdate):
        try:
            evse = self.evse_repository.fetch_by_uid(source, evse_update.uid)
        except ObjectNotFoundException:
            return

        for key, value in evse_update.to_dict().items():
            setattr(evse, key, value)

        self.evse_repository.save_evse(evse)

    def get_evse(self, evse_update: EvseUpdate, old_evse_by_uid: Dict[str, Evse], images_by_url: Optional[Dict[str, Image]]) -> Evse:
        evse = old_evse_by_uid.get(evse_update.uid, Evse())

        for key, value in evse_update.to_dict().items():
            setattr(evse, key, value)

        old_connectors_by_uid = {connector.uid: connector for connector in evse.connectors}
        new_connectors = []
        for connector_update in evse_update.connectors:
            new_connectors.append(self.get_connector(connector_update, old_connectors_by_uid))
        evse.connectors = new_connectors

        self.set_image_list(evse, evse_update.images, images_by_url)

        return evse

    @staticmethod
    def get_connector(connector_update: ConnectorUpdate, old_connectors_by_uid: Dict[str, Connector]) -> Connector:
        connector = old_connectors_by_uid.get(connector_update.uid, Connector())

        for key, value in connector_update.to_dict().items():
            setattr(connector, key, value)

        return connector

    def set_business(
            self,
            location: Location,
            location_update: LocationUpdate,
            location_key: str,
            businesses_by_name: Optional[Dict[str, Business]] = None,
    ):
        business_update = getattr(location_update, location_key)
        if business_update is UnsetValue:
            return

        business = getattr(location, location_key)
        if not business or business.name != business_update.name:
            # if businesses_by_name is None we save a single location and therefore have no pre-fetched businesses
            if businesses_by_name is None:
                try:
                    business = self.business_repository.fetch_business_by_name(business_update.name)
                except ObjectNotFoundException:
                    business = Business()
            elif business_update.name in businesses_by_name:
                business = businesses_by_name[business_update.name]
            else:
                business = Business()
                if businesses_by_name is not None:
                    businesses_by_name[business_update.name] = business

        for key, value in business_update.to_dict().items():
            setattr(business, key, value)

        if business_update.logo is not UnsetValue:
            if not business_update.logo:
                business.logo = Image()

            for key, value in business_update.logo.to_dict().items():
                setattr(business.logo, key, value)

        setattr(location, location_key, business)

    def set_image_list(
            self,
            primary_object: Union[Location, Evse],
            image_updates: OptionalUnset[List[ImageUpdate]],
            images_by_url: Optional[Dict[str, Image]] = None,
    ):
        if image_updates is UnsetValue:
            return

        old_images_by_url = {image.url: image for image in primary_object.images}

        new_images = []
        for image_update in image_updates:

            if image_update.external_url in old_images_by_url:
                image = old_images_by_url[image_update.external_url]

            # if images_by_url is None we save a single location and therefore have no pre-fetched images
            elif images_by_url is None:
                try:
                    image = self.image_repository.fetch_image_by_url(image_update.external_url)
                except ObjectNotFoundException:
                    image = Image()
            elif image_update.external_url in images_by_url:
                image = images_by_url[image_update.external_url]
            else:
                image = Image()
                images_by_url[image_update.external_url] = Image()

            for key, value in image_update.to_dict().items():
                setattr(image, key, value)

            new_images.append(image)

        # TODO: this emits unnecessary SQL UPDATE due re-ordering at many to many relationships
        primary_object.images = new_images

    @staticmethod
    def set_opening_times(location: Location, regular_hours_updates: OptionalUnset[List[RegularHoursUpdate]]):
        if regular_hours_updates is UnsetValue:
            return
        old_regular_hours_items = location.regular_hours
        new_regular_hours_items = []
        for position, regular_hours_update in enumerate(regular_hours_updates):
            if position < len(old_regular_hours_items):
                regular_hours = old_regular_hours_items[position]
            else:
                regular_hours = RegularHours()
            for key, value in regular_hours_update.to_dict().items():
                setattr(regular_hours, key, value)
            new_regular_hours_items.append(regular_hours)
        location.regular_hours = new_regular_hours_items
