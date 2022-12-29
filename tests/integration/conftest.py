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

import pytest
from sqlalchemy import create_engine

from webapp import launch
from webapp.extensions import db as _db


@pytest.fixture(scope='session')
def app():
    test_app = launch()
    test_app.config.update(
        TESTING=True,
        DEBUG=True,
    )

    yield test_app


@pytest.fixture(scope='session')
def db(app):
    with app.app_context():
        # Create the database and the database tables

        # db_path should be 'mysql+pymysql://root:root@mysql' if
        # SQLALCHEMY_DATABASE_URI: 'mysql+pymysql://root:root@mysql/ocpdb' is set in test_config.yaml
        db_path: str = app.config.get('SQLALCHEMY_DATABASE_URI')[:-6]

        engine = create_engine(db_path)
        connection = engine.connect()
        connection.execute('DROP DATABASE IF EXISTS ocpdb;')
        connection.execute('CREATE DATABASE IF NOT EXISTS ocpdb;')
        _db.app = app  # this is needed for the db to have the app context
        _db.create_all()
        yield _db
