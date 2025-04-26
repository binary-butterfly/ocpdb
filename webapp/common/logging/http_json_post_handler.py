"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from logging import NOTSET, Handler, LogRecord

from requests import Session


class HttpPostJsonHandler(Handler):
    url: str
    credentials: tuple[str, str] | None = None
    _session: Session | None = None

    def __init__(self, url: str, *, level: int = NOTSET, credentials: tuple[str, str] | None = None):
        super().__init__(level=level)

        self.url = url
        self.credentials = credentials

    @property
    def session(self) -> Session:
        if self._session is None:
            self._session = Session()
            self._session.auth = self.credentials

        return self._session

    def emit(self, record: LogRecord):
        data = self.format(record)

        self.session.post(self.url, data=data, headers={'Content-Type': 'application/json'})

    def close(self):
        if self._session is None:
            return

        self._session.close()
        self._session = None
