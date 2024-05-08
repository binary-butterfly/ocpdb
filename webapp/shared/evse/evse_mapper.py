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
            ChargeConnectorStatus.AVAILABLE: "AVAILABLE",
            ChargeConnectorStatus.BLOCKED: "BLOCKED",
            ChargeConnectorStatus.CHARGING: "CHARGING",
            ChargeConnectorStatus.INOPERATIVE: "INOPERATIVE",
            ChargeConnectorStatus.OUTOFORDER: "OUTOFORDER",
            ChargeConnectorStatus.PLANNED: "PLANNED",
            ChargeConnectorStatus.REMOVED: "REMOVED",
            ChargeConnectorStatus.RESERVED: "RESERVED",
            ChargeConnectorStatus.UNKNOWN: "UNKNOWN",
            ChargeConnectorStatus.PREPARING: "CHARGING",
            ChargeConnectorStatus.SUSPENDED_EVSE: "CHARGING",
            ChargeConnectorStatus.SUSPENDED_EV: "CHARGING",
            ChargeConnectorStatus.FINISHING: "CHARGING",
        }.get(charge_connector_status)

    @staticmethod
    def map_evse_status_to_charge_connector_status(evse_status: EvseStatus) -> ChargeConnectorStatus:
        return {
            EvseStatus.AVAILABLE: ChargeConnectorStatus.AVAILABLE,
            EvseStatus.BLOCKED: ChargeConnectorStatus.BLOCKED,
            EvseStatus.CHARGING: ChargeConnectorStatus.CHARGING,
            EvseStatus.INOPERATIVE: ChargeConnectorStatus.INOPERATIVE,
            EvseStatus.OUTOFORDER: ChargeConnectorStatus.OUTOFORDER,
            EvseStatus.PLANNED: ChargeConnectorStatus.PLANNED,
            EvseStatus.REMOVED: ChargeConnectorStatus.REMOVED,
            EvseStatus.RESERVED: ChargeConnectorStatus.RESERVED,
            EvseStatus.UNKNOWN: ChargeConnectorStatus.UNKNOWN,
            EvseStatus.PREPARING: ChargeConnectorStatus.PREPARING,
            EvseStatus.SUSPENDED_EVSE: ChargeConnectorStatus.SUSPENDED_EVSE,
            EvseStatus.SUSPENDED_EV: ChargeConnectorStatus.SUSPENDED_EV,
            EvseStatus.FINISHING: ChargeConnectorStatus.FINISHING,
        }.get(evse_status)
