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

import random
import string
from datetime import datetime, timedelta, date, timezone


def get_random_password(length=16):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))


def get_current_time():
    return datetime.utcnow()


def get_current_time_plus(days=0, hours=0, minutes=0, seconds=0):
    return get_current_time() + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)


def is_offline() -> bool:
    """
    helper which normally gives status: online, but can be modified for tests
    :return: date
    """
    return False


def get_today() -> date:
    """
    helper which normally gives back current date, but can be modified for tests
    :return: date
    """
    return date.today()


def get_now() -> datetime:
    """
    helper which normally gives back current utc datetime, but can be modified for tests
    :return: utc datetime
    """
    return datetime.utcnow()


def get_now_localized() -> datetime:
    """
    helper which normally gives back current utc datetime, but can be modified for tests
    :return: utc datetime
    """
    return datetime.utcnow().replace(tzinfo=timezone.utc)
