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

from flask import Flask
from yaml import safe_load

from webapp.common.constants import BaseConfig
from webapp.common.remote_helper import RemoteServerType, RemoteServer


class ConfigLoader:
    @staticmethod
    def configure_app(app: Flask) -> None:
        """
        Initializes the app config with default values and loads the actual config from a YAML file.
        """
        # Load base config (containing constants and default values)
        app.config.from_object(BaseConfig)

        # load all OCPDB-prefixed values from prefixed ENV
        app.config.from_prefixed_env('OCPDB')

        # load db credentials from env
        if os.getenv('OCPDB_POSTGRES_USER') \
                and os.getenv('OCPDB_POSTGRES_DB') \
                and os.getenv('OCPDB_POSTGRES_PASSWORD') \
                and os.getenv('OCPDB_POSTGRES_HOST'):
            app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("OCPDB_POSTGRES_USER")}:{os.getenv("OCPDB_POSTGRES_PASSWORD")}' \
                                                    f'@{os.getenv("OCPDB_POSTGRES_HOST")}/{os.getenv("OCPDB_POSTGRES_DB")}'

        # Load config from yaml file
        config_path = os.path.join(app.config['PROJECT_ROOT'], os.pardir, os.getenv('CONFIG_FILE', 'config.yaml'))
        app.config.from_file(config_path, safe_load)
        app.config['MODE'] = os.getenv('APPLICATION_MODE', 'DEVELOPMENT')

        # Transform REMOTE_SERVERS entries into RemoteServer dataclass objects
        app.config['REMOTE_SERVERS'] = {
            RemoteServerType[key]: RemoteServer(
                url=server['url'],
                user=server.get('user'),
                password=server.get('password'),
                cert=server.get('cert'),
            )
            for key, server in app.config['REMOTE_SERVERS'].items()
        }

        # Ensure that important config values are set
        config_check = [key for key in app.config['ENFORCE_CONFIG_VALUES'] if key not in app.config]
        if len(config_check) > 0:
            raise Exception('missing config values: %s' % ', '.join(config_check))
