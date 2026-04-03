"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from webapp.models.tariff_association import TariffAssociation
from webapp.public_api.base_handler import PublicApiBaseHandler


class TariffAssociationMapper:
    @staticmethod
    def map_tariff_association_to_ocpi(tariff_association: TariffAssociation) -> dict:
        result: dict = {
            'id': str(tariff_association.id),
            'original_id': tariff_association.uid,
            'source': tariff_association.source,
            'tariff_id': str(tariff_association.tariff_id),
            'start_date_time': tariff_association.start_date_time.isoformat(),
            'last_updated': tariff_association.last_updated.isoformat(),
        }

        if tariff_association.audience is not None:
            result['audience'] = tariff_association.audience.value

        result['evses'] = [{'evse_uid': str(evse.id)} for evse in tariff_association.evses]
        result['connectors'] = [{'connector_id': str(connector.id)} for connector in tariff_association.connectors]

        return PublicApiBaseHandler.filter_none(result)
