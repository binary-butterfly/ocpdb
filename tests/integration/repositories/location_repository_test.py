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

import pytest

from tests.integration.model_generators.location import LOCATION_UID_1, get_location_1
from tests.integration.model_generators.source import SOURCE_UID_1, SOURCE_UID_2
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.dependencies import dependencies
from webapp.repositories import ObjectNotFoundException


def test_fetch_location_by_uid_respects_source(db: SQLAlchemy) -> None:
    """Different sources can use the same location uid, so the source has to be part of the lookup."""
    db.session.add_all([
        get_location_1(source=SOURCE_UID_1, name='Location of source 1'),
        get_location_1(source=SOURCE_UID_2, name='Location of source 2'),
    ])
    db.session.commit()

    location_repository = dependencies.get_location_repository()

    assert location_repository.fetch_location_by_uid(SOURCE_UID_2, LOCATION_UID_1).name == 'Location of source 2'
    assert location_repository.fetch_location_by_uid(SOURCE_UID_1, LOCATION_UID_1).name == 'Location of source 1'
    with pytest.raises(ObjectNotFoundException):
        location_repository.fetch_location_by_uid('other_source', LOCATION_UID_1)
