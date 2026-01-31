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
from typing import Callable, Generator

import pytest

from tests.integration.helpers import OpenApiFlaskClient, TestApp, empty_all_tables
from webapp import launch
from webapp.common.flask_app import App
from webapp.common.sqlalchemy import SQLAlchemy
from webapp.extensions import db as flask_sqlalchemy


@pytest.fixture(scope='session')
def flask_app() -> Generator[App, None, None]:
    # Load default development config instead of config.yaml for testing to avoid issues with local setups
    os.environ['CONFIG_FILE'] = os.environ.get('TEST_CONFIG_FILE', 'config_dist_dev.yaml')

    app = launch(
        app_class=TestApp,
        config_overrides={
            'TESTING': True,
            'DEBUG': True,
            'DISABLE_EVENTS': True,
            'SERVER_NAME': 'http://localhost:5010',
        },
    )

    with app.app_context():
        # Drop legacy tables that may exist from old migrations but are no longer in models
        with flask_sqlalchemy.engine.connect() as connection:
            connection.execute(flask_sqlalchemy.text('DROP TABLE IF EXISTS related_resource CASCADE'))
            connection.execute(flask_sqlalchemy.text('DROP TABLE IF EXISTS regular_hours CASCADE'))
            connection.execute(flask_sqlalchemy.text('DROP TABLE IF EXISTS exceptional_opening_period CASCADE'))
            connection.execute(flask_sqlalchemy.text('DROP TABLE IF EXISTS exceptional_closing_period CASCADE'))
            connection.commit()

        flask_sqlalchemy.drop_all()
        flask_sqlalchemy.create_all()

        yield app  # type: ignore


@pytest.fixture(scope='function')
def db(flask_app: App) -> Generator[SQLAlchemy, None, None]:
    """
    Yields the database as a function-scoped fixture with freshly emptied tables.
    """

    empty_all_tables(db=flask_sqlalchemy)

    yield flask_sqlalchemy


@pytest.fixture
def test_cli(flask_app: TestApp) -> Generator[Callable, None, None]:
    def check_cli(fnc: Callable, *args, **kwargs) -> None:
        runner = flask_app.test_cli_runner()
        cli_result = runner.invoke(fnc, args=args, **kwargs)

        if cli_result.exception:
            raise cli_result.exception

        assert cli_result.exit_code == 0

    yield check_cli


@pytest.fixture
def test_client(flask_app: TestApp) -> Generator[OpenApiFlaskClient, None, None]:
    with flask_app.test_client() as client:
        yield client  # type: ignore
