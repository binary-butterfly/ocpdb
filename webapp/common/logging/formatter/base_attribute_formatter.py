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

import functools
import json
import logging
import string
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any

from webapp.common.json import DefaultJSONEncoder


class BaseAttributeFormatter(logging.Formatter, ABC):
    label_allowed_chars: str = f'{string.ascii_letters}{string.digits}_'
    service_name: str
    prefix: str

    def __init__(self, *args, prefix: str, service_name: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = prefix
        self.service_name = service_name

    def format(self, record: logging.LogRecord) -> str:
        return json.dumps(self.build_payload(record), cls=DefaultJSONEncoder)

    def add_additional_attributes(self, record_attributes: dict[str, Any]):
        pass

    @functools.lru_cache(256)  # noqa: B019
    def format_label(self, label: str | Enum) -> str | None:
        if isinstance(label, Enum):
            label = label.name

        # The label uses way fewer characters then allowed, just a-z0-9_
        cleaned_label = ''.join(char for char in label if char in self.label_allowed_chars)
        if len(cleaned_label) == 0:
            return None
        return f'{self.prefix}.{cleaned_label.lower()}'

    def build_attributes(self, record: logging.LogRecord) -> dict[str, Any]:
        record_attributes: dict[str, Any] = {}

        self.add_additional_attributes(record_attributes)

        if hasattr(record, 'attributes'):
            record_attributes.update(getattr(record, 'attributes'))

        attributes = {}

        for attribute_name, attribute_value in record_attributes.items():
            cleared_name = self.format_label(attribute_name)
            if cleared_name is not None:
                attributes[cleared_name] = attribute_value

        return attributes

    @abstractmethod
    def build_payload(self, record: logging.LogRecord) -> dict[str, Any]: ...
