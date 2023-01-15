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
import sys
import traceback
from functools import wraps

from webapp.extensions import logger


def catch_exception(func):
    @wraps(func)
    def with_catch_exception(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # catch error just if we don't have a TTY = started by cron
            if os.isatty(sys.stdin.fileno()):
                raise
            logger.error('cli', '%s' % e, traceback.format_exc())

    return with_catch_exception
