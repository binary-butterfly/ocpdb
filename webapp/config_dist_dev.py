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
from .common.constants import BaseConfig


class Config(BaseConfig):
    PROJECT_URL = ''

    DEBUG = True

    ADMINS = []
    MAILS_FROM = ''

    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@mysql/ocpdb'
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_size': 100, 'pool_recycle': 600}

    SOCKETIO_QUEUE = 'amqp://rabbitmq'

    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    CELERY_BROKER_URL = 'amqp://rabbitmq'

    OCPI_SOURCES = {
        'stadtnavi': {
            'url': 'https://api.dev.stadtnavi.eu/herrenberg/charging-stations/charging-stations-ocpi.json'
        }
    }
