# encoding: utf-8

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
import traceback
from flask import Flask, jsonify

from webapp.config import Config
from .common.filter import register_global_filters
from .extensions import db, celery, redis, migrate

# Blueprints
from .ocpi import ocpi_controller
from .ochp import ochp_controller
from .api_documentation.Controller import api_documentation_blueprint
from .tiles import tiles_controller

__all__ = ['launch']

BLUEPRINTS = [
    ocpi_controller,
    ochp_controller,
    api_documentation_blueprint,
    tiles_controller
]


def launch():
    app = Flask(
        Config.PROJECT_NAME,
        instance_path=Config.INSTANCE_FOLDER_PATH,
        instance_relative_config=True
    )
    configure_app(app)
    configure_hook(app)
    configure_blueprints(app)
    configure_extensions(app)
    configure_filters(app)
    configure_error_handlers(app)
    return app


def configure_app(app):
    app.config.from_object(Config)
    app.config['MODE'] = os.getenv('APPLICATION_MODE', 'DEVELOPMENT')
    print("Running in %s mode" % app.config['MODE'])


def configure_extensions(app):
    celery.init_app(app)
    redis.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def configure_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def configure_filters(app):
    register_global_filters(app)


def configure_hook(app):
    @app.before_request
    def before_request():
        pass


def configure_error_handlers(app):
    @app.errorhandler(403)
    def error_403(error):
        return jsonify({
            'status': -1,
            'error': 403
        }), 403

    @app.errorhandler(404)
    def error_404(error):
        return jsonify({
            'status': -1,
            'error': 404
        }), 404

    @app.errorhandler(500)
    def error_500(error):
        from .extensions import logger
        logger.critical('app', str(error), traceback.format_exc())
        return jsonify({
            'status': -1,
            'error': 500
        }), 500

    if not app.config['DEBUG']:
        @app.errorhandler(Exception)
        def internal_server_error(error):
            from .extensions import logger
            logger.critical('app', str(error), traceback.format_exc())
            return jsonify({
                'status': -1,
                'error': 500
            }), 500

