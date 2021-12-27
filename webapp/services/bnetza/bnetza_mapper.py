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

from typing import List
from decimal import Decimal
from webapp.services.generic.SaveLocation import LocationUpdate
from webapp.services.generic.SaveChargepoint import ChargepointUpdate
from webapp.services.generic.SaveConnector import ConnectorUpdate
from webapp.enums import ChargepointStatus, ConnectorType, ConnectorFormat
from .bnetza_validators import BnetzaRowInput, BnetzaConnectorType


class BnetzaMapper:

    def map_rows_to_location(self, location_uid: str, rows: List[BnetzaRowInput]):
        row = rows[0]
        location_update = LocationUpdate(
            source='bnetza',
            uid=location_uid,
            address='%s %s' % (row.address, row.housenumber),
            postal_code=row.postcode,
            city=row.locality,
            lat=Decimal(str(row.lat)),
            lon=Decimal(str(row.lon)),
            country='DE',
            last_updated=row.launch_date,
            # TODO: operator
            chargepoints=[]
        )
        for line in range(len(rows)):
            location_update.chargepoints += self.map_row_to_chargepoints(location_uid, rows[line], line)
        return location_update

    def map_row_to_chargepoints(self, location_uid: str, row: BnetzaRowInput, line: int) -> List[ChargepointUpdate]:
        result = []
        """
        This is fundamentally broken: sometimes multiple connector types in a single inline counter mean multiple
        EVSEs (eg DC Kupplung Combo, DC CHAdeMO), sometimes it means the same EVSE (eg AC Steckdose Typ 2, AC Schuko).
        There is no way to decide this in a reliable way. We assume one inline counter is one EVSE (but we don't have
        EVSEs anyway, so ...). 
        """
        for inline_counter in range(1, 5):
            if len(getattr(row, 'connector_%s_type' % inline_counter)) == 0:  # ignore empty connector type entries
                continue
            result.append(ChargepointUpdate(
                source='bnetza',
                uid='%s-%s-%s' % (location_uid, line, inline_counter),
                evse_id='BNETZA*%s*%s*%s' % (location_uid, line, inline_counter),
                status=ChargepointStatus.STATIC,
                connectors=self.map_row_to_connector(location_uid, row, line, inline_counter),
                last_updated=row.launch_date,
            ))
        return result

    def map_row_to_connector(self, location_uid: str, row: BnetzaRowInput, line: int, inline_counter: int) -> List[ConnectorUpdate]:
        result = []
        for connector_counter in range(len(getattr(row, 'connector_%s_type' % inline_counter))):
            if getattr(row, 'connector_%s_power' % inline_counter) is None:  # should not happen, but it does happen ...
                continue
            connector_type = getattr(row, 'connector_%s_type' % inline_counter)[connector_counter]
            result.append(ConnectorUpdate(
                source='bnetza',
                uid='%s-%s-%s-%s' % (location_uid, line, inline_counter, connector_counter),
                standard=self.map_connector_type(connector_type),
                max_electric_power=self.map_max_electrical_power(row, inline_counter, connector_counter),
                format=ConnectorFormat.CABLE if connector_type == BnetzaConnectorType.IEC_62196_T2_WIRED else ConnectorFormat.SOCKET,
            ))
        return result

    def map_connector_type(self, bnetza_connector_type: BnetzaConnectorType) -> ConnectorType:
        return {
            BnetzaConnectorType.CHADEMO: ConnectorType.CHADEMO,
            BnetzaConnectorType.DOMESTIC_F: ConnectorType.DOMESTIC_F,
            BnetzaConnectorType.IEC_60309_2_single_16: ConnectorType.IEC_60309_2_single_16,
            BnetzaConnectorType.IEC_60309_2_three_any: ConnectorType.IEC_60309_2_three_32,  # map to 32 A because no basis for a decision
            BnetzaConnectorType.IEC_62196_T1: ConnectorType.IEC_62196_T1,
            BnetzaConnectorType.IEC_62196_T2: ConnectorType.IEC_62196_T2,
            BnetzaConnectorType.IEC_62196_T2_WIRED: ConnectorType.IEC_62196_T2,
            BnetzaConnectorType.IEC_62196_T2_COMBO: ConnectorType.IEC_62196_T2_COMBO,
            BnetzaConnectorType.TESLA_S_1: ConnectorType.TESLA_S,
            BnetzaConnectorType.TESLA_S_2: ConnectorType.TESLA_S  # map to TESLA S because no basis fpr decision
        }.get(bnetza_connector_type, ConnectorType.IEC_62196_T2)

    def map_max_electrical_power(self, row: BnetzaRowInput, inline_counter: int, connector_counter: int) -> int:
        power = int(getattr(row, 'connector_%s_power' % inline_counter) * 1000)
        # there are several connectors where there's 22kW for SchuKo which is impossible, so we cap max power there
        if power > 3700 and getattr(row, 'connector_%s_type' % inline_counter)[connector_counter] == BnetzaConnectorType.DOMESTIC_F:
            return 3700
        return power
