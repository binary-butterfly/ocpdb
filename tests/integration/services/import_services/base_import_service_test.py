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

from decimal import Decimal

import pytest

from webapp.dependencies import dependencies
from webapp.models import Connector, Evse, Location, Tariff, TariffAssociation
from webapp.models.charging_station import ChargingStation
from webapp.models.connector import ConnectorFormat, ConnectorType
from webapp.models.enums import TariffDimensionType
from webapp.models.evse import EvseStatus
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.models import (
    ChargingStationUpdate,
    ConnectorUpdate,
    EvseUpdate,
    LocationUpdate,
    PriceComponentUpdate,
    SourceInfo,
    TariffAssociationUpdate,
    TariffElementUpdate,
    TariffUpdate,
)


class TestingImportService(BaseImportService):
    """
    Minimal version of a BaseImportService subclass for testing puroposes
    """

    @property
    def source_info(self) -> SourceInfo:
        return SourceInfo(
            uid='test_source_uid',
            name='test_source',
            public_url='test_url',
            has_realtime_data=None,
        )

    def fetch_static_data(self): ...


@pytest.fixture
def testing_import_service():
    return TestingImportService(
        **dependencies.get_base_service_dependencies(),
        location_repository=dependencies.get_location_repository(),
        evse_repository=dependencies.get_evse_repository(),
        connector_repository=dependencies.get_connector_repository(),
        business_repository=dependencies.get_business_repository(),
        image_repository=dependencies.get_image_repository(),
        source_repository=dependencies.get_source_repository(),
        official_region_code_repository=dependencies.get_official_region_code_repository(),
        tariff_repository=dependencies.get_tariff_repository(),
    )


def test_save_location_updates_simple(db, testing_import_service: BaseImportService):
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='test',
            source='test',
            lat=Decimal('2.0'),
            lon=Decimal('2.0'),
            time_zone='Europe/Berlin',
            charging_pool=[],
        )
    ])
    assert db.session.query(Location).count() == 1


def test_save_location_updates_with_evses_and_connectors(db, testing_import_service: BaseImportService):
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.7758'),
            lon=Decimal('9.1829'),
            time_zone='Europe/Berlin',
            charging_pool=[
                ChargingStationUpdate(
                    uid='cs1',
                    evses=[
                        EvseUpdate(
                            uid='evse1',
                            evse_id='DE*TST*E001',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn1',
                                    standard=ConnectorType.IEC_62196_T2,
                                    format=ConnectorFormat.SOCKET,
                                    max_electric_power=22000,
                                ),
                                ConnectorUpdate(
                                    uid='conn2',
                                    standard=ConnectorType.IEC_62196_T2_COMBO,
                                    format=ConnectorFormat.CABLE,
                                    max_electric_power=50000,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ])

    assert db.session.query(Location).count() == 1
    assert db.session.query(ChargingStation).count() == 1
    assert db.session.query(Evse).count() == 1
    assert db.session.query(Connector).count() == 2


def test_save_location_updates_multiple_charging_stations(db, testing_import_service: BaseImportService):
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.7758'),
            lon=Decimal('9.1829'),
            time_zone='Europe/Berlin',
            charging_pool=[
                ChargingStationUpdate(
                    uid='cs1',
                    evses=[
                        EvseUpdate(
                            uid='evse1',
                            evse_id='DE*TST*E001',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn1',
                                    standard=ConnectorType.IEC_62196_T2,
                                    format=ConnectorFormat.SOCKET,
                                    max_electric_power=22000,
                                ),
                            ],
                        ),
                    ],
                ),
                ChargingStationUpdate(
                    uid='cs2',
                    evses=[
                        EvseUpdate(
                            uid='evse2',
                            evse_id='DE*TST*E002',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn2',
                                    standard=ConnectorType.CHADEMO,
                                    format=ConnectorFormat.CABLE,
                                    max_electric_power=50000,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ])

    assert db.session.query(Location).count() == 1
    assert db.session.query(ChargingStation).count() == 2
    assert db.session.query(Evse).count() == 2
    assert db.session.query(Connector).count() == 2


def test_save_location_updates_replaces_old_locations(db, testing_import_service: BaseImportService):
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.0'),
            lon=Decimal('9.0'),
            time_zone='Europe/Berlin',
            charging_pool=[],
        ),
        LocationUpdate(
            uid='loc2',
            source='test_source_uid',
            lat=Decimal('49.0'),
            lon=Decimal('10.0'),
            time_zone='Europe/Berlin',
            charging_pool=[],
        ),
    ])
    assert db.session.query(Location).count() == 2

    # Re-import with only loc1 — loc2 should be deleted
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.0'),
            lon=Decimal('9.0'),
            time_zone='Europe/Berlin',
            charging_pool=[],
        ),
    ])
    assert db.session.query(Location).count() == 1
    assert db.session.query(Location).first().uid == 'loc1'


def _create_location_with_evse_and_connector(testing_import_service: BaseImportService):
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.7758'),
            lon=Decimal('9.1829'),
            time_zone='Europe/Berlin',
            charging_pool=[
                ChargingStationUpdate(
                    uid='cs1',
                    evses=[
                        EvseUpdate(
                            uid='evse1',
                            evse_id='DE*TST*E001',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn1',
                                    standard=ConnectorType.IEC_62196_T2,
                                    format=ConnectorFormat.SOCKET,
                                    max_electric_power=22000,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ])


def test_save_tariff_updates_with_evse_association(db, testing_import_service: BaseImportService):
    _create_location_with_evse_and_connector(testing_import_service)

    testing_import_service.save_tariff_updates(
        tariff_updates=[
            TariffUpdate(
                uid='tariff1',
                source='test_source_uid',
                currency='EUR',
                elements=[
                    TariffElementUpdate(
                        price_components=[
                            PriceComponentUpdate(type=TariffDimensionType.ENERGY, price=Decimal('0.30')),
                        ],
                    ),
                ],
            ),
        ],
        tariff_association_updates=[
            TariffAssociationUpdate(
                uid='ta1',
                source='test_source_uid',
                tariff_uid='tariff1',
                evse_uid='evse1',
            ),
        ],
    )

    assert db.session.query(Tariff).count() == 1
    assert db.session.query(TariffAssociation).count() == 1

    evse = db.session.query(Evse).first()
    assert len(evse.tariff_associations) == 1
    assert evse.tariff_associations[0].uid == 'ta1'


def test_save_tariff_updates_with_connector_association(db, testing_import_service: BaseImportService):
    _create_location_with_evse_and_connector(testing_import_service)

    testing_import_service.save_tariff_updates(
        tariff_updates=[
            TariffUpdate(
                uid='tariff1',
                source='test_source_uid',
                currency='EUR',
                elements=[
                    TariffElementUpdate(
                        price_components=[
                            PriceComponentUpdate(type=TariffDimensionType.ENERGY, price=Decimal('0.30')),
                        ],
                    ),
                ],
            ),
        ],
        tariff_association_updates=[
            TariffAssociationUpdate(
                uid='ta1',
                source='test_source_uid',
                tariff_uid='tariff1',
                evse_uid='evse1',
                connector_uid='conn1',
            ),
        ],
    )

    assert db.session.query(TariffAssociation).count() == 1

    evse = db.session.query(Evse).first()
    assert len(evse.tariff_associations) == 1

    connector = db.session.query(Connector).first()
    assert len(connector.tariff_associations) == 1
    assert connector.tariff_associations[0].uid == 'ta1'


def test_save_location_updates_with_evse_inline_tariff_association(db, testing_import_service: BaseImportService):
    # First create tariffs
    testing_import_service.save_tariff_updates(
        tariff_updates=[
            TariffUpdate(
                uid='tariff1',
                source='test_source_uid',
                currency='EUR',
                elements=[],
            ),
        ],
        tariff_association_updates=[],
    )
    assert db.session.query(Tariff).count() == 1

    # Now save locations with inline tariff association on EVSE
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.7758'),
            lon=Decimal('9.1829'),
            time_zone='Europe/Berlin',
            charging_pool=[
                ChargingStationUpdate(
                    uid='cs1',
                    evses=[
                        EvseUpdate(
                            uid='evse1',
                            evse_id='DE*TST*E001',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn1',
                                    standard=ConnectorType.IEC_62196_T2,
                                    format=ConnectorFormat.SOCKET,
                                    max_electric_power=22000,
                                ),
                            ],
                            tariff_association=TariffAssociationUpdate(
                                uid='ta_evse1',
                                source='test_source_uid',
                                tariff_uid='tariff1',
                                evse_uid='evse1',
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ])

    assert db.session.query(Evse).count() == 1
    assert db.session.query(TariffAssociation).count() == 1

    evse = db.session.query(Evse).first()
    assert len(evse.tariff_associations) == 1
    assert evse.tariff_associations[0].uid == 'ta_evse1'
    assert evse.tariff_associations[0].tariff.uid == 'tariff1'


def test_save_location_updates_with_connector_inline_tariff_association(db, testing_import_service: BaseImportService):
    # First create tariffs
    testing_import_service.save_tariff_updates(
        tariff_updates=[
            TariffUpdate(
                uid='tariff1',
                source='test_source_uid',
                currency='EUR',
                elements=[],
            ),
        ],
        tariff_association_updates=[],
    )

    # Now save locations with inline tariff association on connector
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.7758'),
            lon=Decimal('9.1829'),
            time_zone='Europe/Berlin',
            charging_pool=[
                ChargingStationUpdate(
                    uid='cs1',
                    evses=[
                        EvseUpdate(
                            uid='evse1',
                            evse_id='DE*TST*E001',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn1',
                                    standard=ConnectorType.IEC_62196_T2,
                                    format=ConnectorFormat.SOCKET,
                                    max_electric_power=22000,
                                    tariff_association=TariffAssociationUpdate(
                                        uid='ta_conn1',
                                        source='test_source_uid',
                                        tariff_uid='tariff1',
                                        evse_uid='evse1',
                                        connector_uid='conn1',
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ])

    assert db.session.query(Connector).count() == 1
    assert db.session.query(TariffAssociation).count() == 1

    connector = db.session.query(Connector).first()
    assert len(connector.tariff_associations) == 1
    assert connector.tariff_associations[0].uid == 'ta_conn1'
    assert connector.tariff_associations[0].tariff.uid == 'tariff1'


def test_save_location_updates_with_evse_and_connector_tariff_associations(
    db,
    testing_import_service: BaseImportService,
):
    # Create tariffs
    testing_import_service.save_tariff_updates(
        tariff_updates=[
            TariffUpdate(
                uid='tariff1',
                source='test_source_uid',
                currency='EUR',
                elements=[],
            ),
        ],
        tariff_association_updates=[],
    )

    # Save location with tariff associations on both EVSE and connector
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.7758'),
            lon=Decimal('9.1829'),
            time_zone='Europe/Berlin',
            charging_pool=[
                ChargingStationUpdate(
                    uid='cs1',
                    evses=[
                        EvseUpdate(
                            uid='evse1',
                            evse_id='DE*TST*E001',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn1',
                                    standard=ConnectorType.IEC_62196_T2,
                                    format=ConnectorFormat.SOCKET,
                                    max_electric_power=22000,
                                    tariff_association=TariffAssociationUpdate(
                                        uid='ta_conn1',
                                        source='test_source_uid',
                                        tariff_uid='tariff1',
                                        evse_uid='evse1',
                                        connector_uid='conn1',
                                    ),
                                ),
                            ],
                            tariff_association=TariffAssociationUpdate(
                                uid='ta_evse1',
                                source='test_source_uid',
                                tariff_uid='tariff1',
                                evse_uid='evse1',
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ])

    assert db.session.query(TariffAssociation).count() == 2

    evse = db.session.query(Evse).first()
    assert len(evse.tariff_associations) == 1
    assert evse.tariff_associations[0].uid == 'ta_evse1'

    connector = db.session.query(Connector).first()
    assert len(connector.tariff_associations) == 1
    assert connector.tariff_associations[0].uid == 'ta_conn1'


def test_save_location_updates_without_tariff_skips_association(db, testing_import_service: BaseImportService):
    # Save locations with tariff association referencing non-existent tariff
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.7758'),
            lon=Decimal('9.1829'),
            time_zone='Europe/Berlin',
            charging_pool=[
                ChargingStationUpdate(
                    uid='cs1',
                    evses=[
                        EvseUpdate(
                            uid='evse1',
                            evse_id='DE*TST*E001',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn1',
                                    standard=ConnectorType.IEC_62196_T2,
                                    format=ConnectorFormat.SOCKET,
                                    max_electric_power=22000,
                                ),
                            ],
                            tariff_association=TariffAssociationUpdate(
                                uid='ta1',
                                source='test_source_uid',
                                tariff_uid='nonexistent_tariff',
                                evse_uid='evse1',
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ])

    # Location and EVSE should be saved, but no tariff association created
    assert db.session.query(Evse).count() == 1
    assert db.session.query(TariffAssociation).count() == 0


def test_save_tariff_updates_reimport_is_idempotent(db, testing_import_service: BaseImportService):
    _create_location_with_evse_and_connector(testing_import_service)

    tariff_updates = [
        TariffUpdate(
            uid='tariff1',
            source='test_source_uid',
            currency='EUR',
            elements=[],
        ),
    ]
    association_updates = [
        TariffAssociationUpdate(
            uid='ta1',
            source='test_source_uid',
            tariff_uid='tariff1',
            evse_uid='evse1',
        ),
    ]

    # Import twice
    testing_import_service.save_tariff_updates(
        tariff_updates=tariff_updates,
        tariff_association_updates=association_updates,
    )
    testing_import_service.save_tariff_updates(
        tariff_updates=tariff_updates,
        tariff_association_updates=association_updates,
    )

    assert db.session.query(Tariff).count() == 1
    assert db.session.query(TariffAssociation).count() == 1

    evse = db.session.query(Evse).first()
    assert len(evse.tariff_associations) == 1


def test_save_location_updates_two_evses_share_same_tariff_association(
    db,
    testing_import_service: BaseImportService,
):
    # Create tariff first
    testing_import_service.save_tariff_updates(
        tariff_updates=[
            TariffUpdate(
                uid='tariff1',
                source='test_source_uid',
                currency='EUR',
                elements=[],
            ),
        ],
        tariff_association_updates=[],
    )

    # Two EVSEs reference the same tariff_association (same uid)
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='loc1',
            source='test_source_uid',
            lat=Decimal('48.7758'),
            lon=Decimal('9.1829'),
            time_zone='Europe/Berlin',
            charging_pool=[
                ChargingStationUpdate(
                    uid='cs1',
                    evses=[
                        EvseUpdate(
                            uid='evse1',
                            evse_id='DE*TST*E001',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn1',
                                    standard=ConnectorType.IEC_62196_T2,
                                    format=ConnectorFormat.SOCKET,
                                    max_electric_power=22000,
                                ),
                            ],
                            tariff_association=TariffAssociationUpdate(
                                uid='ta_shared',
                                source='test_source_uid',
                                tariff_uid='tariff1',
                                evse_uid='evse1',
                            ),
                        ),
                        EvseUpdate(
                            uid='evse2',
                            evse_id='DE*TST*E002',
                            status=EvseStatus.AVAILABLE,
                            connectors=[
                                ConnectorUpdate(
                                    uid='conn2',
                                    standard=ConnectorType.IEC_62196_T2_COMBO,
                                    format=ConnectorFormat.CABLE,
                                    max_electric_power=50000,
                                ),
                            ],
                            tariff_association=TariffAssociationUpdate(
                                uid='ta_shared',
                                source='test_source_uid',
                                tariff_uid='tariff1',
                                evse_uid='evse2',
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ])

    assert db.session.query(Evse).count() == 2
    assert db.session.query(TariffAssociation).count() == 1

    association = db.session.query(TariffAssociation).first()
    assert association.uid == 'ta_shared'
    assert len(association.evses) == 2

    evse1 = db.session.query(Evse).filter(Evse.uid == 'evse1').first()
    evse2 = db.session.query(Evse).filter(Evse.uid == 'evse2').first()
    assert len(evse1.tariff_associations) == 1
    assert len(evse2.tariff_associations) == 1
    assert evse1.tariff_associations[0].id == evse2.tariff_associations[0].id
