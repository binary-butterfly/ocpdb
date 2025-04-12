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

from flask import request

from webapp.cli import register_cli_to_app
from webapp.common.config import ConfigLoader
from webapp.common.constants import BaseConfig
from webapp.common.error_handling import ErrorDispatcher
from webapp.common.flask_app import App
from webapp.common.rest import RestApiErrorHandler
from webapp.dependencies import dependencies
from webapp.extensions import celery, cors, db, logger, migrate, openapi
from webapp.frontend import FrontendBlueprint
from webapp.prometheus_api import PrometheusRestApi
from webapp.public_api import PublicApi
from webapp.server_rest_api import ServerRestApi

__all__ = ['launch']


def launch(config_overrides: dict | None = None) -> App:
    app = App(BaseConfig.PROJECT_NAME)
    configure_app(app, config_overrides)
    configure_extensions(app)
    configure_blueprints(app)
    configure_error_handlers(app)
    configure_periodic_tasks()
    return app


def configure_app(app: App, config_overrides: dict | None = None) -> None:
    config_loader = ConfigLoader()
    config_loader.configure_app(app, config_overrides)


def configure_extensions(app: App) -> None:
    logger.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    celery.init_app(app)
    cors.init_app(app)
    openapi.init_app(app)

    dependencies.get_config_helper().init_app(app)


def configure_blueprints(app: App) -> None:
    app.register_blueprint(PublicApi())
    app.register_blueprint(FrontendBlueprint())
    app.register_blueprint(ServerRestApi())
    app.register_blueprint(PrometheusRestApi())
    register_cli_to_app(app)


def configure_error_handlers(app: App) -> None:
    # ErrorDispatcher: Class that passes errors either to FrontendErrorHandler (rendering error HTML pages) or
    # to RestApiErrorHandler (returning JSON responses) depending on the request path.
    error_handler_kwargs = {
        'logger': dependencies.get_logger(),
        'db_session': dependencies.get_db_session(),
        'debug': bool(app.config['DEBUG']),
    }
    error_dispatcher = ErrorDispatcher(RestApiErrorHandler(**error_handler_kwargs))

    @app.errorhandler(Exception)
    def handle_exception(error: Exception):
        return error_dispatcher.dispatch_error(error, request)


@celery.on_after_configure.connect
def configure_periodic_tasks(**kwargs):
    task_runner = dependencies.get_generic_import_runner()
    task_runner.start()
