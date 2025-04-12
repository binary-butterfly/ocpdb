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

import re
from typing import Generator

import pytest
from sqlalchemy import create_engine, text

from tests.integration.helpers import empty_all_tables
from webapp import launch
from webapp.common.flask_app import App
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.extensions import db as flask_sqlalchemy


@pytest.fixture(scope='session')
def flask_app() -> Generator[App, None, None]:
    app = launch(
        config_overrides={
            'TESTING': True,
            'DEBUG': True,
        }
    )

    # Create the database and the database tables
    # db_path should be 'mysql+pymysql://root:root@mysql' if
    # SQLALCHEMY_DATABASE_URI: 'mysql+pymysql://root:root@mysql/backend?charset=utf8mb4' is set in test_config.yaml
    db_path: str = re.sub(r'/[^/]+$', '', app.config.get('SQLALCHEMY_DATABASE_URI'))

    engine = create_engine(db_path)

    # We use DROP + CREATE here because it's faster and more reliable in case of foreign keys
    with engine.connect() as connection:
        connection.execute(text('DROP DATABASE IF EXISTS `post-salad-backend`;'))
        connection.execute(text('CREATE DATABASE IF NOT EXISTS `post-salad-backend`;'))

    with app.app_context():
        flask_sqlalchemy.create_all()

        yield app  # type: ignore


@pytest.fixture
def db(flask_app: App) -> Generator[SQLAlchemy, None, None]:
    """
    Yields the database as a function-scoped fixture with freshly emptied tables.
    """
    empty_all_tables(db=flask_sqlalchemy)

    yield flask_sqlalchemy
