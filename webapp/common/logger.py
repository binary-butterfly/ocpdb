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
from logging.handlers import WatchedFileHandler
from ..config import Config


class Logger:
    registered_logs = []

    def __init__(self):
        if not os.path.exists(Config.LOG_DIR):
            os.mkdir(Config.LOG_DIR)

    def get_log(self, log_name):
        logger = logging.getLogger(log_name)
        if log_name in self.registered_logs:
            return logger
        logger.setLevel(logging.INFO)

        # Init File Handler
        file_name = os.path.join(Config.LOG_DIR, '%s.log' % log_name)
        file_handler = WatchedFileHandler(file_name)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s ')
        )
        logger.addHandler(file_handler)

        file_name = os.path.join(Config.LOG_DIR, '%s.err' % log_name)
        file_handler = WatchedFileHandler(file_name)
        file_handler.setLevel(logging.ERROR)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s ')
        )
        logger.addHandler(file_handler)

        if Config.DEBUG:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_format = logging.Formatter('%(message)s')
            console_handler.setFormatter(console_format)
            logger.addHandler(console_handler)

        self.registered_logs.append(log_name)
        return logger

    def debug(self, log_name, message):
        self.get_log(log_name).debug(message)

    def info(self, log_name, message):
        self.get_log(log_name).info(message)

    def warn(self, log_name, message):
        self.get_log(log_name).warning(message)

    def error(self, log_name, message, details=None):
        self.get_log(log_name).error(message)
        #send_notification.delay('error', log_name, message, details)

    def exception(self, log_name, message, details=None):
        self.get_log(log_name).exception("%s:\n%s" % (message, details))
        #send_notification.delay('exception', log_name, message, details)

    def critical(self, log_name, message, details=None):
        self.get_log(log_name).critical("%s:\n%s" % (message, details))
        #send_notification.delay('critical', log_name, message, details)


"""
@celery.task
def send_notification(level, log_name, message, details):
    try:
        if current_app.config['DEBUG']:
            return
        msg = Message(
            "%s %s Fehler" % (current_app.config['PROJECT_NAME'], current_app.config['MODE']),
            sender=current_app.config['MAILS_FROM'],
            recipients=current_app.config['ADMINS'],
            body="Auf %s %s ist im Bereich %s folgender Fehler der Klasse %s aufgetreten %s\n\nDetails:\n%s" % (
                current_app.config['PROJECT_NAME'],
                current_app.config['MODE'],
                log_name,
                level,
                message,
                details if details else 'keine'
            )
        )
        mail.send(msg)
    except:
        pass
"""
