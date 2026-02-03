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

from decimal import Decimal
from pathlib import Path

import pytest
from sqlalchemy import text

from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.models import Location
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.models import LocationUpdate, SourceInfo


class TestingImportService(BaseImportService):
    """
    Minimal version of a BaseImportService subclass for testing purposes.
    """

    @property
    def source_info(self) -> SourceInfo:
        return SourceInfo(
            uid='test_regional_code_source',
            name='test_regional_code',
            public_url='test_url',
            has_realtime_data=None,
        )

    def fetch_static_data(self): ...


@pytest.fixture
def testing_import_service() -> TestingImportService:
    return TestingImportService(
        **dependencies.get_base_service_dependencies(),
        location_repository=dependencies.get_location_repository(),
        evse_repository=dependencies.get_evse_repository(),
        connector_repository=dependencies.get_connector_repository(),
        business_repository=dependencies.get_business_repository(),
        image_repository=dependencies.get_image_repository(),
        source_repository=dependencies.get_source_repository(),
        official_region_code_repository=dependencies.get_official_region_code_repository(),
    )


@pytest.fixture
def regionalschluessel_table(db: SQLAlchemy):
    """
    Creates the regionalschluessel table with test data and cleans up after the test.
    """
    sql_path = Path(__file__).parent / 'regionalschluessel.sql'
    with sql_path.open() as sql_file:
        create_table_sql = sql_file.read()

    with db.engine.connect() as connection:
        connection.execute(text('DROP TABLE IF EXISTS regionalschluessel CASCADE'))
        connection.execute(text('DROP SEQUENCE IF EXISTS regionalschluessel_id_seq CASCADE'))
        connection.commit()

        connection.execute(text(create_table_sql))
        connection.commit()

        # Insert test data with a polygon covering Berlin area (approximately 52.52°N, 13.405°E)
        # Using a simple square polygon around Berlin coordinates
        insert_sql = """
            INSERT INTO regionalschluessel (
                id,
                "regioschlüsselaufgefüllt",
                geografischername_gen,
                geom
            ) VALUES (
                1,
                '110000000000',
                'Berlin',
                ST_SetSRID(ST_GeomFromText('MULTIPOLYGON(((13.0 52.0, 14.0 52.0, 14.0 53.0, 13.0 53.0, 13.0 52.0)))'), 4326)
            )
        """
        connection.execute(text(insert_sql))

        # Insert test data with a polygon covering Munich area (approximately 48.137°N, 11.576°E)
        insert_sql_munich = """
            INSERT INTO regionalschluessel (
                id,
                "regioschlüsselaufgefüllt",
                geografischername_gen,
                geom
            ) VALUES (
                2,
                '091620000000',
                'München',
                ST_SetSRID(ST_GeomFromText('MULTIPOLYGON(((11.0 48.0, 12.0 48.0, 12.0 49.0, 11.0 49.0, 11.0 48.0)))'), 4326)
            )
        """
        connection.execute(text(insert_sql_munich))
        connection.commit()

    yield db

    with db.engine.connect() as connection:
        connection.execute(text('DROP TABLE IF EXISTS regionalschluessel CASCADE'))
        connection.execute(text('DROP SEQUENCE IF EXISTS regionalschluessel_id_seq CASCADE'))
        connection.commit()


def test_save_location_updates_sets_official_region_code(
    db: SQLAlchemy,
    regionalschluessel_table: SQLAlchemy,
    testing_import_service: BaseImportService,
) -> None:
    """
    Test that save_location_updates correctly sets official_region_code from regionalschluessel table.
    """
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='berlin_location',
            source='test_regional_code_source',
            lat=Decimal('52.52'),
            lon=Decimal('13.405'),
            country='DEU',
        )
    ])

    location = db.session.query(Location).filter_by(uid='berlin_location').one()
    assert location.official_region_code == '110000000000'


def test_save_location_updates_sets_official_region_code_for_multiple_locations(
    db: SQLAlchemy,
    regionalschluessel_table: SQLAlchemy,
    testing_import_service: BaseImportService,
) -> None:
    """
    Test that save_location_updates correctly sets official_region_code for multiple locations.
    """
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='berlin_location',
            source='test_regional_code_source',
            lat=Decimal('52.52'),
            lon=Decimal('13.405'),
            country='DEU',
        ),
        LocationUpdate(
            uid='munich_location',
            source='test_regional_code_source',
            lat=Decimal('48.137'),
            lon=Decimal('11.576'),
            country='DEU',
        ),
    ])

    berlin_location = db.session.query(Location).filter_by(uid='berlin_location').one()
    assert berlin_location.official_region_code == '110000000000'

    munich_location = db.session.query(Location).filter_by(uid='munich_location').one()
    assert munich_location.official_region_code == '091620000000'


def test_save_location_updates_no_region_code_for_non_german_location(
    db: SQLAlchemy,
    regionalschluessel_table: SQLAlchemy,
    testing_import_service: BaseImportService,
) -> None:
    """
    Test that save_location_updates does not set official_region_code for non-German locations.
    """
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='paris_location',
            source='test_regional_code_source',
            lat=Decimal('48.8566'),
            lon=Decimal('2.3522'),
            country='FRA',
        )
    ])

    location = db.session.query(Location).filter_by(uid='paris_location').one()
    assert location.official_region_code is None


def test_save_location_updates_no_region_code_for_location_outside_polygons(
    db: SQLAlchemy,
    regionalschluessel_table: SQLAlchemy,
    testing_import_service: BaseImportService,
) -> None:
    """
    Test that save_location_updates does not set official_region_code for locations outside any polygon.
    """
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='outside_location',
            source='test_regional_code_source',
            lat=Decimal('50.0'),
            lon=Decimal('8.0'),
            country='DEU',
        )
    ])

    location = db.session.query(Location).filter_by(uid='outside_location').one()
    assert location.official_region_code is None


def test_save_location_updates_preserves_existing_region_code(
    db: SQLAlchemy,
    regionalschluessel_table: SQLAlchemy,
    testing_import_service: BaseImportService,
) -> None:
    """
    Test that save_location_updates preserves existing official_region_code and does not overwrite it.
    """
    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='berlin_location',
            source='test_regional_code_source',
            lat=Decimal('52.52'),
            lon=Decimal('13.405'),
            country='DEU',
        )
    ])

    location = db.session.query(Location).filter_by(uid='berlin_location').one()
    assert location.official_region_code == '110000000000'

    location.official_region_code = 'custom_code'
    db.session.commit()

    testing_import_service.save_location_updates([
        LocationUpdate(
            uid='berlin_location',
            source='test_regional_code_source',
            lat=Decimal('52.52'),
            lon=Decimal('13.405'),
            country='DEU',
        )
    ])

    location = db.session.query(Location).filter_by(uid='berlin_location').one()
    assert location.official_region_code == 'custom_code'
