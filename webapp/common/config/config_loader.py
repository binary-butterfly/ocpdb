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

import logging
import os
from pathlib import Path
from urllib.parse import urlparse

from flask import Flask
from yaml import safe_load

from webapp.common.constants import BaseConfig
from webapp.common.logging.models import LogMessageType

logger = logging.getLogger(__name__)


class ConfigLoader:
    @staticmethod
    def configure_app(app: Flask, config_overrides: None = None) -> None:
        """
        Initializes the app config with default values and loads the actual config from a YAML file.
        """
        # Load base config (containing constants and default values)
        app.config.from_object(BaseConfig)

        # load all OCPDB-prefixed values from prefixed ENV
        app.config.from_prefixed_env('OCPDB')

        # load db credentials from env
        if (
            os.getenv('OCPDB_POSTGRES_USER')
            and os.getenv('OCPDB_POSTGRES_DB')
            and os.getenv('OCPDB_POSTGRES_PASSWORD')
            and os.getenv('OCPDB_POSTGRES_HOST')
        ):
            app.config['SQLALCHEMY_DATABASE_URI'] = (
                f'postgresql://{os.getenv("OCPDB_POSTGRES_USER")}:{os.getenv("OCPDB_POSTGRES_PASSWORD")}'
                f'@{os.getenv("OCPDB_POSTGRES_HOST")}/{os.getenv("OCPDB_POSTGRES_DB")}'
            )

        # Load config from yaml file
        config_path = Path(app.config['PROJECT_ROOT']).parent.joinpath(os.getenv('CONFIG_FILE', 'config.yaml'))
        app.config.from_file(config_path, safe_load)

        # load additional secrets config from yaml file (if it exists)
        config_secrets_filename = os.getenv('CONFIG_SECRETS_FILE', 'config.secrets.yaml')
        config_secrets_path = Path(app.config['PROJECT_ROOT']).parent.joinpath(config_secrets_filename)
        if config_secrets_path.exists():
            app.config.from_file(config_secrets_path, safe_load)

        app.config['MODE'] = os.getenv('APPLICATION_MODE', 'DEVELOPMENT')

        # Legacy config converter
        if 'REMOTE_SERVERS' in app.config:
            mapping: dict[str, str] = {
                'BNETZA': 'bnetza_excel',
                'CHARGEIT': 'lichtblick',
                'GIROE': 'giroe',
                'OCHP_LADENETZ': 'ochp_ladenetz',
                'OCHP_ALBWERK': 'ochp_albwerk',
                'STADTNAVI': 'ocpi_stadtnavi',
                'SW_STUTTGART': 'chargecloud_stuttgart',
                'PFORZHEIM': 'chargecloud_pforzheim',
            }
            logger.warning(
                'The REMOTE_SERVERS config value is deprecated. Please use the SOURCES config value instead.',
                extra={'attributes': {'type': LogMessageType.MAIN}},
            )
            for key, values in app.config['REMOTE_SERVERS'].items():
                app.config['SOURCES'][mapping[key]] = values

        if config_overrides is not None:
            app.config.update(config_overrides)

        # Ensure that important config values are set
        config_check = [key for key in app.config['ENFORCE_CONFIG_VALUES'] if key not in app.config]
        if len(config_check) > 0:
            raise Exception('missing config values: %s' % ', '.join(config_check))

        # Ensure that all sources are dicts
        for source, source_config in app.config['SOURCES'].items():
            if source_config is None:
                app.config['SOURCES'][source] = {}
            elif not isinstance(source_config, dict):
                raise Exception(f'Source config {source} has to be a dictionary, but is {source_config}')

        # Set PROJECT_PATH based on PROJECT_URL
        url = urlparse(app.config['PROJECT_URL'])
        app.config['PROJECT_PATH'] = url.path
