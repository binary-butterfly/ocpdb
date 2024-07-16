"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2024 binary butterfly GmbH

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

from butterfly_pubsub.giroe import ChargeConnectorStatus

from webapp.models.evse import EvseStatus


class EvseMapper:

    @staticmethod
    def map_charge_connector_status_to_evse_status(charge_connector_status: ChargeConnectorStatus) -> EvseStatus:
        return {
            ChargeConnectorStatus.AVAILABLE: EvseStatus.AVAILABLE,
            ChargeConnectorStatus.BLOCKED: EvseStatus.BLOCKED,
            ChargeConnectorStatus.CHARGING: EvseStatus.CHARGING,
            ChargeConnectorStatus.INOPERATIVE: EvseStatus.INOPERATIVE,
            ChargeConnectorStatus.OUTOFORDER: EvseStatus.OUTOFORDER,
            ChargeConnectorStatus.PLANNED: EvseStatus.PLANNED,
            ChargeConnectorStatus.REMOVED: EvseStatus.REMOVED,
            ChargeConnectorStatus.RESERVED: EvseStatus.RESERVED,
            ChargeConnectorStatus.UNKNOWN: EvseStatus.UNKNOWN,
            ChargeConnectorStatus.PREPARING: EvseStatus.CHARGING,
            ChargeConnectorStatus.SUSPENDED_EVSE: EvseStatus.CHARGING,
            ChargeConnectorStatus.SUSPENDED_EV: EvseStatus.CHARGING,
            ChargeConnectorStatus.FINISHING: EvseStatus.CHARGING,
        }.get(charge_connector_status)
