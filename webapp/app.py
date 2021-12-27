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
from yaml import safe_load
from flask import Flask

from webapp.extensions import db, celery, migrate, logger
from webapp.common.misc import DefaultJSONEncoder
from webapp.common.constants import BaseConfig
from webapp.common.config_helper import check_and_extend_config
from webapp.cli import register_cli_to_app

from webapp.public_api import PublicApi
from webapp.openapi.openapi import OpenApiDocumentation
from webapp.frontend import FrontendBlueprint
from webapp.server_api import ServerApi


__all__ = ['launch']


def launch():
    app = Flask(BaseConfig.PROJECT_NAME)
    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)
    return app


def configure_app(app):
    app.config.from_object(BaseConfig)
    config_path = os.path.join(app.config['PROJECT_ROOT'], os.pardir, os.getenv('CONFIG_FILE', 'config.yaml'))
    app.config.from_file(config_path, safe_load)
    app.config['MODE'] = os.getenv('APPLICATION_MODE', 'DEVELOPMENT')
    check_and_extend_config(app)
    app.json_encoder = DefaultJSONEncoder


def configure_extensions(app):
    logger.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    celery.init_app(app)
    celery.conf.update({'task_default_queue': app.config.get('CELERY_TASK_QUEUE', 'celery')})


def configure_blueprints(app):
    app.register_blueprint(PublicApi(app))
    app.register_blueprint(OpenApiDocumentation(app))
    app.register_blueprint(FrontendBlueprint(app))
    app.register_blueprint(ServerApi(app))
    register_cli_to_app(app)

