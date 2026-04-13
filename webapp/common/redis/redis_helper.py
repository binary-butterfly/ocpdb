"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from datetime import timedelta

from redis import Redis

from .exceptions import RedisKeyNotFoundException


class RedisHelper:
    redis: Redis

    def __init__(self, redis: Redis):
        self.redis = redis

    def set(self, key: str, value: str, expires_in: timedelta | None = None) -> None:
        self.redis.set(
            name=key,
            value=value,
            ex=expires_in,
        )

    def get(self, key: str) -> str:
        result = self.redis.get(key)

        if result is None:
            raise RedisKeyNotFoundException(message=f'Redis entry for key {key} not found')

        return result.decode()

    def delete(self, *keys) -> None:
        self.redis.delete(*keys)
