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

import os
from typing import Generator

import pytest

from webapp import launch
from webapp.common.flask_app import App
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.extensions import db as flask_sqlalchemy


@pytest.fixture
def flask_app() -> Generator[App, None, None]:
    # Load default development config instead of config.yaml for testing to avoid issues with local setups
    os.environ['CONFIG_FILE'] = os.environ.get('TEST_CONFIG_FILE', 'config_dist_dev.yaml')

    app = launch(
        config_overrides={
            'TESTING': True,
            'DEBUG': True,
        }
    )

    with app.app_context():
        flask_sqlalchemy.drop_all()
        flask_sqlalchemy.create_all()

        yield app  # type: ignore


@pytest.fixture
def db(flask_app: App) -> Generator[SQLAlchemy, None, None]:
    """
    Yields the database as a function-scoped fixture with freshly emptied tables.
    """

    yield flask_sqlalchemy
