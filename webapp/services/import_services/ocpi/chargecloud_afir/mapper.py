"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from decimal import Decimal

from webapp.services.import_services.models import (
    LocationUpdate,
    PriceComponentUpdate,
    RestrictionsUpdate,
    TariffElementUpdate,
    TariffUpdate,
)
from webapp.services.import_services.ocpi.ocpi_mapper import OcpiMapper

from .validators import ChargecloudAfirLocationInput, ChargecloudAfirRestrictionInput, ChargecloudAfirTariffInput


class ChargecloudAfirMapper(OcpiMapper):
    def map_location(self, location_input: ChargecloudAfirLocationInput, source: str) -> LocationUpdate:
        location_update = super().map_location(location_input, source)

        """
        TODO: re-activate as soon as data source fixed their structure
        for evse_input in location_input.evses:
            if not evse_input.tariffs:
                continue
            evse_update = next(
                evse for evse in location_update.charging_pool[0].evses if evse.evse_id == evse_input.evse_id
            )
            evse_update.tariff_association = []
            seen_tariff_ids: set[str] = set()
            for tariff_input in evse_input.tariffs:
                if tariff_input.id in seen_tariff_ids:
                    continue
                seen_tariff_ids.add(tariff_input.id)
                tariff_uid = f'{evse_update.uid}:{tariff_input.id}'
                tariff_update = self._map_tariff(tariff_input, tariff_uid, source)
                evse_update.tariff_association.append(
                    TariffAssociationUpdate(
                        uid=tariff_uid,
                        source=source,
                        tariff=tariff_update,
                        last_updated=evse_update.last_updated,
                    ),
                )
        """

        return location_update

    @staticmethod
    def _map_tariff(tariff_input: ChargecloudAfirTariffInput, tariff_uid: str, source: str) -> TariffUpdate:
        tariff_elements: list[TariffElementUpdate] = []
        for element_input in tariff_input.elements:
            price_components = [
                PriceComponentUpdate(
                    type=pc.type,
                    price=Decimal(str(pc.price)),
                )
                for pc in element_input.price_components
            ]
            restrictions = None
            if element_input.restrictions:
                restrictions = ChargecloudAfirMapper._map_restriction(element_input.restrictions[0])
            tariff_elements.append(TariffElementUpdate(price_components=price_components, restrictions=restrictions))

        return TariffUpdate(
            uid=tariff_uid,
            source=source,
            currency=tariff_input.currency,
            elements=tariff_elements,
        )

    @staticmethod
    def _map_restriction(restriction_input: ChargecloudAfirRestrictionInput) -> RestrictionsUpdate:
        return RestrictionsUpdate(
            start_time=restriction_input.start_time,
            end_time=restriction_input.end_time,
            min_duration=restriction_input.min_duration,
            max_duration=restriction_input.max_duration,
        )
