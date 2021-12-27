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
import logging
from typing import Optional
from flask import Flask, Config
from logging import Logger as PythonLogger
from logging.handlers import WatchedFileHandler


class Logger:
    config: Config
    registered_logs = []

    def init_app(self, app: Flask):
        self.config = app.config

    def get_log(self, log_name: str) -> PythonLogger:
        logger = logging.getLogger('%s%s' % (self.config['LOGGING_PREFIX'], log_name))
        if log_name in self.registered_logs:
            return logger
        logger.setLevel(logging.INFO)

        # Init File Handler
        file_name = os.path.join(self.config['LOG_DIR'], '%s.log' % log_name)
        file_handler = WatchedFileHandler(file_name)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s ')
        )
        logger.addHandler(file_handler)

        file_name = os.path.join(self.config['LOG_DIR'], '%s.err' % log_name)
        file_handler = WatchedFileHandler(file_name)
        file_handler.setLevel(logging.ERROR)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s ')
        )
        logger.addHandler(file_handler)

        if self.config['DEBUG']:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_format = logging.Formatter('%(message)s')
            console_handler.setFormatter(console_format)
            logger.addHandler(console_handler)

        self.registered_logs.append(log_name)
        return logger

    def debug(self, log_name: str, message: str, details: Optional[str] = None):
        self.get_log(log_name).debug(message if details is None else "%s:\n%s" % (message, details))

    def info(self, log_name: str, message: str, details: Optional[str] = None):
        self.get_log(log_name).info(message if details is None else "%s:\n%s" % (message, details))

    def warn(self, log_name: str, message: str, details: Optional[str] = None):
        self.get_log(log_name).warning(message if details is None else "%s:\n%s" % (message, details))

    def error(self, log_name: str, message: str, details: Optional[str] = None):
        self.get_log(log_name).error(message if details is None else "%s:\n%s" % (message, details))

    def exception(self, log_name: str, message: str, details: Optional[str] = None):
        self.get_log(log_name).exception(message if details is None else "%s:\n%s" % (message, details))

    def critical(self, log_name: str, message: str, details: Optional[str] = None):
        self.get_log(log_name).critical(message if details is None else "%s:\n%s" % (message, details))
