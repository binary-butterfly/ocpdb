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

import redis
from typing import Union, Optional
from datetime import timedelta


class RedisClient:

    def __init__(self, app=None, strict=True, config_prefix="REDIS", **kwargs):
        self._redis_client = None
        self.provider_class = redis.StrictRedis if strict else redis.Redis
        self.provider_kwargs = kwargs
        self.config_prefix = config_prefix

        if app is not None:
            self.init_app(app)

    def init_app(self, app, **kwargs):
        redis_url = app.config.get('%s_URL' % self.config_prefix, "redis://localhost:6379/0")

        self.provider_kwargs.update(kwargs)
        self._redis_client = self.provider_class.from_url(
            redis_url, **self.provider_kwargs
        )

        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions[self.config_prefix.lower()] = self

    def set(self,
            name: str,
            value: str,
            ex: Optional[Union[timedelta, int]] = None,
            px: Optional[Union[timedelta, int]] = None,
            nx: Optional[bool] = False,
            xx: Optional[bool] = False,
            keepttl: bool = False):
        return self._redis_client.set(name, value, ex, px, nx, xx, keepttl)

    def eval(self, script: str, numkeys: int, *keys_and_args):
        return self._redis_client.eval(script, numkeys, *keys_and_args)

