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


from flask import Flask, request

from webapp.common.error_handling import ErrorDispatcher
from webapp.common.rest import RestApiErrorHandler
from webapp.dependencies import dependencies
from webapp.extensions import db, celery, migrate, logger, cors
from webapp.common.misc import DefaultJSONEncoder
from webapp.common.constants import BaseConfig
from webapp.common.config import ConfigLoader
from webapp.cli import register_cli_to_app

from webapp.public_api import PublicApi
from webapp.openapi.openapi import OpenApiDocumentation
from webapp.frontend import FrontendBlueprint
from webapp.server_rest_api import ServerRestApi


__all__ = ['launch']


def launch():
    app = Flask(BaseConfig.PROJECT_NAME)
    app.json_encoder = DefaultJSONEncoder
    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)
    configure_error_handlers(app)
    return app


def configure_app(app):
    config_loader = ConfigLoader()
    config_loader.configure_app(app)


def configure_extensions(app):
    logger.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    celery.init_app(app)
    cors.init_app(app)


def configure_blueprints(app):
    app.register_blueprint(PublicApi())
    app.register_blueprint(OpenApiDocumentation())
    app.register_blueprint(FrontendBlueprint())
    app.register_blueprint(ServerRestApi())
    register_cli_to_app(app)


def configure_error_handlers(app: Flask):
    # ErrorDispatcher: Class that passes errors either to FrontendErrorHandler (rendering error HTML pages) or
    # to RestApiErrorHandler (returning JSON responses) depending on the request path.
    error_handler_kwargs = dict(
        logger=dependencies.get_logger(),
        db_session=dependencies.get_db_session(),
        debug=bool(app.config['DEBUG']),
    )
    error_dispatcher = ErrorDispatcher(
        RestApiErrorHandler(**error_handler_kwargs)
    )

    @app.errorhandler(Exception)
    def handle_exception(error: Exception):
        return error_dispatcher.dispatch_error(error, request)
