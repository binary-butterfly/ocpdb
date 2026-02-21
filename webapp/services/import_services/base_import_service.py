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

from abc import ABC, abstractmethod
from datetime import datetime, timezone

from celery.schedules import crontab

from webapp.common.contexts import TelemetryContext
from webapp.common.remote_mixin import RemoteMixin
from webapp.models import Business, ChargingStation, Connector, Evse, Image, Location, Source
from webapp.models.source import SourceStatus
from webapp.repositories import (
    ConnectorRepository,
    EvseRepository,
    LocationRepository,
    ObjectNotFoundException,
    SourceRepository,
)
from webapp.repositories.business_repository import BusinessRepository
from webapp.repositories.image_repository import ImageRepository
from webapp.services.base_service import BaseService
from webapp.services.import_services.models import (
    ChargingStationUpdate,
    ConnectorUpdate,
    EvseRealtimeUpdate,
    EvseUpdate,
    ImageUpdate,
    LocationUpdate,
    SourceInfo,
)


class BaseImportService(BaseService, RemoteMixin, ABC):
    source_repository: SourceRepository
    location_repository: LocationRepository
    evse_repository: EvseRepository
    connector_repository: ConnectorRepository
    business_repository: BusinessRepository
    image_repository: ImageRepository

    schedule: crontab | None = None
    required_config_keys: list[str] = []

    @property
    @abstractmethod
    def source_info(self) -> SourceInfo:
        pass

    @abstractmethod
    def fetch_static_data(self): ...

    def __init__(
        self,
        *args,
        source_repository: SourceRepository,
        location_repository: LocationRepository,
        evse_repository: EvseRepository,
        connector_repository: ConnectorRepository,
        business_repository: BusinessRepository,
        image_repository: ImageRepository,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.source_repository = source_repository
        self.location_repository = location_repository
        self.evse_repository = evse_repository
        self.connector_repository = connector_repository
        self.business_repository = business_repository
        self.image_repository = image_repository

    def save_evse_updates(self, evse_updates: list[EvseUpdate | EvseRealtimeUpdate]):
        """
        Separated and optimized function for storing realtime EVSE updates
        """
        evses = self.evse_repository.fetch_evses_by_source_and_uids(
            self.source_info.uid,
            uids=[evse_update.uid for evse_update in evse_updates],
        )
        evses_by_uid: dict[str, Evse] = {evse.uid: evse for evse in evses}
        for evse_update in evse_updates:
            if evse_update.uid not in evses_by_uid:
                continue

            evse = evses_by_uid[evse_update.uid]
            if evse_update.status == evse.status:
                continue

            evse.last_updated = evse_update.last_updated or datetime.now(tz=timezone.utc)

            for key, value in evse_update.to_dict().items():
                if key == 'last_updated':
                    continue
                setattr(evse, key, value)

            self.evse_repository.save_evse(evse, commit=False)

        self.evse_repository.session.commit()

    def save_location_updates(self, location_updates: list[LocationUpdate]):
        # get old location ids
        old_location_ids = self.location_repository.fetch_location_ids_by_source(self.source_info.uid)

        # Business and Images are shared, so we just cache them to prevent sql queries
        businesses_by_name = {business.name: business for business in self.business_repository.fetch_businesses()}
        images_by_url = {image.external_url: image for image in self.image_repository.fetch_images()}

        # EVSE UIDs are critical because they are unique, so we fetch them related to location id in order to check them before saving
        # TODO: actually use this
        # evse_uids = {item[0]: item[1] for item in self.evse_repository.fetch_extended_evse_uids()}

        for location_update in location_updates:
            self.save_location_update(location_update, businesses_by_name, old_location_ids, images_by_url)

        # delete locations which are not part of the updated dataset anymore
        for old_location_id in old_location_ids:
            self.location_repository.delete_location(
                self.location_repository.fetch_location_by_id(old_location_id),
            )

    def save_location_update(
        self,
        location_update: LocationUpdate,
        businesses_by_name: dict[str, Business] | None = None,
        old_location_ids: list[int] | None = None,
        images_by_url: dict[str, Image] | None = None,
    ):
        try:
            location = self.location_repository.fetch_location_by_uid(
                self.source_info.uid,
                location_update.uid,
                include_children=True,
            )
        except ObjectNotFoundException:
            location = Location()

        location.last_updated = location_update.last_updated or datetime.now(tz=timezone.utc)

        for key, value in location_update.to_dict().items():
            if key in ['last_updated']:
                continue
            setattr(location, key, value)

        # Convert opening times dataclasses to dicts for JSON storage
        if location_update.regular_hours is not None:
            location.regular_hours = [rh.to_dict() for rh in location_update.regular_hours]
        if location_update.exceptional_openings is not None:
            location.exceptional_openings = [eo.to_dict() for eo in location_update.exceptional_openings]
        if location_update.exceptional_closings is not None:
            location.exceptional_closings = [ec.to_dict() for ec in location_update.exceptional_closings]
        if location_update.energy_mix is not None:
            location.energy_mix = location_update.energy_mix.to_dict() if location_update.energy_mix else None
        if location_update.max_power is not None:
            if location_update.max_power:
                location.max_power_unit = location_update.max_power.unit
                location.max_power_value = location_update.max_power.value
            else:
                location.max_power_unit = None
                location.max_power_value = None

        self.set_business(location, location_update, 'operator', businesses_by_name)
        self.set_business(location, location_update, 'suboperator', businesses_by_name)
        self.set_business(location, location_update, 'owner', businesses_by_name)
        self.set_image_list(location, location_update.images, images_by_url)

        old_charging_stations_by_uid = {
            charging_station.id: charging_station for charging_station in location.charging_pool
        }
        new_charging_stations: list[ChargingStation] = []
        for charging_station_update in location_update.charging_pool:
            new_charging_stations.append(
                self.get_charging_station(
                    charging_station_update=charging_station_update,
                    old_charging_stations_by_uid=old_charging_stations_by_uid,
                    images_by_url=images_by_url,
                ),
            )
        location.charging_pool = new_charging_stations

        self.location_repository.save_location(location)

        if old_location_ids is not None and location.id in old_location_ids:
            old_location_ids.remove(location.id)

    def get_charging_station(
        self,
        charging_station_update: ChargingStationUpdate,
        old_charging_stations_by_uid: dict[str, ChargingStation],
        images_by_url: dict[str, Image] | None,
    ) -> ChargingStation:
        charging_station = old_charging_stations_by_uid.get(charging_station_update.uid, ChargingStation())

        charging_station.last_updated = charging_station_update.last_updated or datetime.now(tz=timezone.utc)

        for key, value in charging_station_update.to_dict().items():
            if key == 'last_updated':
                continue
            setattr(charging_station, key, value)

        if charging_station_update.max_power is not None:
            if charging_station_update.max_power:
                charging_station.max_power_unit = charging_station_update.max_power.unit
                charging_station.max_power_value = charging_station_update.max_power.value
            else:
                charging_station.max_power_unit = None
                charging_station.max_power_value = None

        old_evses_by_uid = {evse.uid: evse for evse in charging_station.evses}
        new_evses: list[Evse] = []
        for evse_update in charging_station_update.evses:
            new_evses.append(
                self.get_evse(
                    evse_update=evse_update,
                    old_evses_by_uid=old_evses_by_uid,
                    images_by_url=images_by_url,
                ),
            )

        charging_station.evses = new_evses

        return charging_station

    def get_evse(
        self,
        evse_update: EvseUpdate,
        old_evses_by_uid: dict[str, Evse],
        images_by_url: dict[str, Image] | None,
    ) -> Evse:
        evse = old_evses_by_uid.get(evse_update.uid, Evse())

        evse.last_updated = evse_update.last_updated or datetime.now(tz=timezone.utc)

        for key, value in evse_update.to_dict().items():
            if key == 'last_updated':
                continue
            setattr(evse, key, value)

        old_connectors_by_uid = {connector.uid: connector for connector in evse.connectors}
        new_connectors: list[Connector] = []
        for connector_update in evse_update.connectors:
            new_connectors.append(
                self.get_connector(
                    connector_update=connector_update,
                    old_connectors_by_uid=old_connectors_by_uid,
                ),
            )
        evse.connectors = new_connectors

        self.set_image_list(
            primary_object=evse,
            image_updates=evse_update.images,
            images_by_url=images_by_url,
        )

        return evse

    @staticmethod
    def get_connector(connector_update: ConnectorUpdate, old_connectors_by_uid: dict[str, Connector]) -> Connector:
        connector = old_connectors_by_uid.get(connector_update.uid, Connector())

        connector.last_updated = connector_update.last_updated or datetime.now(tz=timezone.utc)

        for key, value in connector_update.to_dict().items():
            if key == 'last_updated':
                continue
            setattr(connector, key, value)

        return connector

    def set_business(
        self,
        location: Location,
        location_update: LocationUpdate,
        location_key: str,
        businesses_by_name: dict[str, Business] | None = None,
    ):
        business_update = getattr(location_update, location_key)
        if business_update is None:
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

        if business_update.logo is not None:
            if not business.logo:
                business.logo = Image()

            for key, value in business_update.logo.to_dict().items():
                setattr(business.logo, key, value)

        setattr(location, location_key, business)

    def set_image_list(
        self,
        primary_object: Location | ChargingStation | Evse,
        image_updates: list[ImageUpdate] | None,
        images_by_url: dict[str, Image] | None = None,
    ):
        if image_updates is None:
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

    def get_source(self) -> Source:
        self.context_helper.set_telemetry_context(TelemetryContext.SOURCE, self.source_info.uid)

        try:
            return self.source_repository.fetch_source_by_uid(self.source_info.uid)
        except ObjectNotFoundException:
            source = Source()
            for key, value in self.source_info.to_dict().items():
                setattr(source, key, value)
            self.source_repository.save_source(source)

            return source

    def update_source(
        self,
        source: Source,
        static_error_count: int | None = None,
        realtime_error_count: int | None = None,
        static_status: SourceStatus | None = None,
        static_data_updated_at: datetime | None = None,
        realtime_status: SourceStatus | None = None,
        realtime_data_updated_at: datetime | None = None,
    ):
        for key, value in self.source_info.to_dict().items():
            setattr(source, key, value)

        if static_status is not None:
            source.static_status = static_status
        if realtime_status is not None:
            source.realtime_status = realtime_status

        if static_error_count is not None:
            source.static_data_updated_at = static_data_updated_at or datetime.now(tz=timezone.utc)
            source.static_error_count = static_error_count
            source.static_status = SourceStatus.ACTIVE
        if realtime_error_count is not None:
            source.realtime_data_updated_at = realtime_data_updated_at or datetime.now(tz=timezone.utc)
            source.realtime_error_count = realtime_error_count
            if source.static_status == SourceStatus.ACTIVE:
                source.realtime_status = SourceStatus.ACTIVE

        self.source_repository.save_source(source)
