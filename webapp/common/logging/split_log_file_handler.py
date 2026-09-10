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

from logging import Formatter, Handler, LogRecord
from logging.handlers import WatchedFileHandler
from pathlib import Path

from webapp.common.logging.models import LogMessageType


class SplitLogFileHandler(Handler):
    _file_handlers: dict[LogMessageType, WatchedFileHandler]

    def __init__(self, log_path: str, **kwargs):
        # Has to be set before Handler.__init__(), as that calls createLock(), which iterates over the file handlers.
        self._file_handlers = {}
        super().__init__()
        for log_type in LogMessageType:
            log_name = log_type.value.lower().replace('_', '-')
            self._file_handlers[log_type] = WatchedFileHandler(
                filename=Path(log_path, f'{log_name}.log'),
                **kwargs,
            )

    def emit(self, record: LogRecord):
        log_type: LogMessageType = getattr(record, 'attributes', {}).get('type', LogMessageType.MAIN)
        self._file_handlers.get(log_type, self._file_handlers[LogMessageType.MAIN]).emit(record)

    def close(self):
        for handler in self._file_handlers.values():
            handler.close()
        super().close()

    def setFormatter(self, formatter: Formatter):
        for handler in self._file_handlers.values():
            handler.setFormatter(formatter)

    def createLock(self):
        super().createLock()
        for handler in self._file_handlers.values():
            handler.createLock()

    def acquire(self):
        super().acquire()
        for handler in self._file_handlers.values():
            handler.acquire()

    def release(self):
        for handler in self._file_handlers.values():
            handler.release()
        super().release()

    def setLevel(self, level: int):
        super().setLevel(level)
        for handler in self._file_handlers.values():
            handler.setLevel(level)

    def flush(self):
        for handler in self._file_handlers.values():
            handler.flush()
