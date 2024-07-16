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

from pycountry import countries

from webapp.services.import_services.models import (
    BusinessUpdate,
    ConnectorUpdate,
    EvseUpdate,
    ExceptionalPeriodUpdate,
    ImageUpdate,
    LocationUpdate,
    RegularHoursUpdate,
)
from webapp.services.import_services.ocpi.ocpi_validators import BusinessDetailsInput, ConnectorInput, EvseInput, ImageInput, LocationInput


class OcpiMapper:

    def map_location(self, location_input: LocationInput, source: str) -> LocationUpdate:
        location_update = LocationUpdate(
            uid=location_input.id,
            source=source,
            name=location_input.name,
            address=location_input.address,
            postal_code=location_input.postal_code,
            city=location_input.city,
            state=location_input.state,
            country=countries.get(alpha_3=location_input.country).alpha_2,
            lat=location_input.coordinates.latitude,
            lon=location_input.coordinates.longitude,
            directions=location_input.directions,
            parking_type=location_input.parking_type,
            time_zone=location_input.time_zone,
            last_updated=location_input.last_updated,
            evses=[],
        )
        for evse_input in location_input.evses:
            location_update.evses.append(self.map_evse(evse_input))

        for business_type in ('operator', 'suboperator', 'owner'):
            if not getattr(location_input, business_type):
                continue

            setattr(location_update, business_type, self.map_business(business_input=getattr(location_input, business_type)))

        if location_input.opening_times:
            location_update.twentyfourseven = location_input.opening_times.twentyfourseven
            if location_input.opening_times.regular_hours:
                location_update.regular_hours = []
                for regular_hour_input in location_input.opening_times.regular_hours:
                    location_update.regular_hours.append(RegularHoursUpdate(**regular_hour_input.to_dict()))

            if location_input.opening_times.exceptional_openings:
                location_update.exceptional_openings = []
                for exceptional_opening_input in location_input.opening_times.exceptional_openings:
                    location_update.exceptional_openings.append(ExceptionalPeriodUpdate(**exceptional_opening_input.to_dict()))

            if location_input.opening_times.exceptional_closings:
                location_update.exceptional_closings = []
                for exceptional_closings_input in location_input.opening_times.exceptional_closings:
                    location_update.exceptional_closings.append(ExceptionalPeriodUpdate(**exceptional_closings_input.to_dict()))

        return location_update

    def map_evse(self, evse_input: EvseInput) -> EvseUpdate:
        evse_update = EvseUpdate(
            uid=evse_input.evse_id,
            status=evse_input.status,
            floor_level=evse_input.floor_level,
            physical_reference=evse_input.physical_reference,
            last_updated=evse_input.last_updated,
            capabilities=evse_input.capabilities,
            parking_restrictions=evse_input.parking_restrictions,
            # TODO: directions
            connectors=[],
        )

        if evse_input.coordinates:
            evse_update.lat = evse_input.coordinates.latitude
            evse_update.lon = evse_input.coordinates.longitude

        for connector_input in evse_input.connectors:
            evse_update.connectors.append(self.map_connector(connector_input))

        return evse_update

    @staticmethod
    def map_connector(connector_input: ConnectorInput) -> ConnectorUpdate:
        return ConnectorUpdate(
            uid=connector_input.id,
            standard=connector_input.standard,
            format=connector_input.format,
            power_type=connector_input.power_type,
            max_voltage=connector_input.max_voltage,
            max_amperage=connector_input.max_amperage,
            max_electric_power=connector_input.max_electric_power,
            last_updated=connector_input.last_updated,
            terms_and_conditions=connector_input.terms_and_conditions,
        )

    def map_business(self, business_input: BusinessDetailsInput) -> BusinessUpdate:
        business_update = BusinessUpdate(
            name=business_input.name,
            website=business_input.website,
        )
        if business_input.logo:
            business_update.logo = self.map_image(business_input.logo)

        return business_update

    @staticmethod
    def map_image(image_input: ImageInput) -> ImageUpdate:
        return ImageUpdate(
            external_url=image_input.url,
            width=image_input.width,
            category=image_input.category,
            type=image_input.type,
            height=image_input.height,
        )
