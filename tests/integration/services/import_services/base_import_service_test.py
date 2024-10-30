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
from webapp.models import Location
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.models import LocationUpdate, SourceInfo


class TestingImportService(BaseImportService):
    """
    Minimal version of a BaseImportService subclass for testing puroposes
    """
    @property
    def source_info(self) -> SourceInfo:
        return SourceInfo(uid='test_source_uid', name='test_source', public_url='test_url', has_realtime_data=None)


@pytest.fixture
def testing_import_service():
    return TestingImportService(
        **dependencies.get_base_service_dependencies(),
        remote_helper=dependencies.get_remote_helper(),
        location_repository=dependencies.get_location_repository(),
        evse_repository=dependencies.get_evse_repository(),
        connector_repository=dependencies.get_evse_repository(),
        business_repository=dependencies.get_business_repository(),
        image_repository=dependencies.get_image_repository(),
        option_repository=dependencies.get_option_repository(),
        source_repository=dependencies.get_source_repository(),
    )


def test_save_location_updates_simple(db, testing_import_service: BaseImportService):
    testing_import_service.save_location_updates(
        [
            LocationUpdate(
                uid='test',
                source='test',
                lat=Decimal('2.0'),
                lon=Decimal('2.0'),
            )
        ]
    )
    assert db.session.query(Location).count() == 1
