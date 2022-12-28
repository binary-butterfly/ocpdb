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

from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.repositories import LocationRepository


class OcpiHandler(PublicApiBaseHandler):
    location_repository: LocationRepository

    def __init__(self, *args, location_repository: LocationRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository

    def get_location(self, location_id: int):
        location = self.location_repository.fetch_location_by_id(location_id, include_children=True)
        location_dict = self.filter_none(location.to_dict(
            ignore=['giroe_id', 'owner_id', 'owner_id', 'suboperator_id', 'created', 'modified', 'id', 'geometry'],
            transform_ocpi=True,
        ))
        location_dict['evses'] = []
        for regular_hours in location.regular_hours:
            if 'regular_hours' not in location_dict['opening_times']:
                location_dict['opening_times']['regular_hours'] = []
            location_dict['opening_times']['regular_hours'].append(
                regular_hours.to_dict(
                    ignore=['location_id', 'chargepoint_id', 'created', 'modified', 'id'],
                    transform_ocpi=True,
                )
            )
        for exceptional_opening in location.exceptional_openings:
            if 'exceptional_openings' not in location_dict['opening_times']:
                location_dict['opening_times']['exceptional_openings'] = []
            location_dict['opening_times']['exceptional_openings'].append(
                exceptional_opening.to_dict(ignore=['chargepoint_id', 'created', 'modified', 'id']),
            )
        for exceptional_closing in location.exceptional_closings:
            if 'exceptional_closings' not in location_dict['opening_times']:
                location_dict['opening_times']['exceptional_closings'] = []
            location_dict['opening_times']['exceptional_closings'].append(
                exceptional_closing.to_dict(ignore=['chargepoint_id', 'created', 'modified', 'id']),
            )
        for evse in location.evses:
            chargepoint_dict = evse.to_dict(
                ignore=['external_id', 'giroe_id', 'location_id', 'created', 'modified', 'id'],
                transform_ocpi=True,
            )
            chargepoint_dict['connectors'] = []
            for connector in evse.connectors:
                connector_dict = self.filter_none(connector.to_dict(
                    ignore=['external_id', 'giroe_id', 'chargepoint_id', 'created', 'modified', 'id'],
                ))
                chargepoint_dict['connectors'].append(connector_dict)

            for image in evse.images:
                if 'images' not in chargepoint_dict:
                    chargepoint_dict['images'] = []
                chargepoint_dict['images'].append(self.filter_none(image.to_dict(
                    ignore=['chargepoint_id', 'location_id', 'created', 'modified', 'id', 'external_url']
                )))

            location_dict['evses'].append(self.filter_none(chargepoint_dict))

        return location_dict

    def filter_none(self, data: dict) -> dict:
        return {key: value for key, value in data.items() if value is not None}
