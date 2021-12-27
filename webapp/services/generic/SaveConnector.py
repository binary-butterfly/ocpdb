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

from typing import Optional
from dataclasses import dataclass, asdict
from validataclass.helpers import OptionalUnsetNone, UnsetValue
from webapp.models import Connector, Chargepoint
from webapp.extensions import logger, db
from webapp.enums import ConnectorType, ConnectorFormat


@dataclass
class ConnectorUpdate:
    source: str  # TODO: this should not be part of an update
    uid: str  # TODO: this should not be part of an update
    standard: OptionalUnsetNone[ConnectorType] = UnsetValue
    format: OptionalUnsetNone[ConnectorFormat] = UnsetValue
    max_electric_power: OptionalUnsetNone[int] = UnsetValue
    max_voltage: OptionalUnsetNone[int] = UnsetValue


def upsert_connector(
        connector_update: ConnectorUpdate,
        chargepoint: Chargepoint,
        old_connector: Optional[Connector] = None,
        commit: Optional[bool] = True) -> Connector:
    connector = old_connector if old_connector else Connector.query\
        .filter_by(chargepoint_id=chargepoint.id)\
        .filter_by(uid=connector_update.uid)\
        .filter_by(source=connector_update.source)\
        .first()
    if connector:
        update_required = False
        for field, value in asdict(connector_update).items():
            if field in ['max_voltage']:
                continue
            if value is not UnsetValue and getattr(connector, field) != value:
                update_required = True
                break
        if not update_required:
            return connector
    else:
        connector = Connector()
        connector.chargepoint_id = chargepoint.id
    for field, value in asdict(connector_update).items():
        if value is UnsetValue:
            continue
        setattr(connector, field, value)
    connector.guess_power_type()
    connector.guess_voltage_amperage()
    if commit:
        db.session.add(connector)
        db.session.commit()
        logger.info('ochp.connector.update', 'updated connector %s' % connector.id)
    return connector

