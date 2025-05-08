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


class BaseConfig:
    INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')  # noqa: S108

    PROJECT_NAME = 'ocpdb'
    PROJECT_VERSION = '1.0'

    MAIL_SERVER = 'letterbox-online.de'
    MAIL_USE_TLS = True

    DEBUG = False
    TESTING = False
    LOGGING_PREFIX = ''

    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    DYNAMIC_IMAGE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir, 'data', 'images'))
    DEBUG_DUMP_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir, 'data', 'debug'))

    PUBLIC_IMAGE_PATH = '/data/images'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    ENFORCE_CONFIG_VALUES = [
        'PROJECT_URL',
        'SECRET_KEY',
        'SQLALCHEMY_DATABASE_URI',
        'CELERY_BROKER_URL',
    ]

    SHOW_MAP: bool = True

    OPENAPI_LOGIN_REQUIRED = False

    OPENAPI_TITLE = 'Open ChargePoint DataBase: Documentation'
    OPENAPI_DESCRIPTION = 'This service tries to collect and publish as many live data as possible.'
    OPENAPI_CONTACT_MAIL = 'ernesto.ruge@binary-butterfly.de'
    OPENAPI_TOS = 'https://binary-butterfly.de/ocpdb'
    OPENAPI_SERVERS = [
        {
            'url': 'https://api.ocpdb.de',
            'description': 'production',
        },
    ]

    MATCHING_FACTOR_THRESHOLD = 0.25

    SOURCES: dict[str, dict] = {}
    AUTO_FETCH_SOURCES: list[str] = []

    STATIC_PULL_HOUR = 1
    STATIC_PULL_MINUTE = 0
    REALTIME_PULL_FREQUENCY = 60  # In seconds
    IMAGE_PULL_HOUR = 4
    IMAGE_PULL_MINUTE = 0

    IMAGE_IMPORT_REQUEST_DELAY = 0.1  # Delay time between two requests, in seconds

    LOGGING = {
        'version': 1,
    }
