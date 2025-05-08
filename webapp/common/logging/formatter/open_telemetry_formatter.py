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

import logging
import secrets

from .base_attribute_formatter import BaseAttributeFormatter


class OpenTelemetryFormatter(BaseAttributeFormatter):
    log_level_mapping: dict[int, int] = {
        logging.DEBUG: 5,
        logging.INFO: 10,
        logging.WARNING: 15,
        logging.ERROR: 20,
        logging.CRITICAL: 25,
    }

    def build_payload(self, record: logging.LogRecord) -> dict:
        trace_id = getattr(record, 'trace_id', secrets.token_hex(16))
        span_id = getattr(record, 'span_id', secrets.token_hex(8))

        return {
            'Timestamp': int(record.created * 1e9),
            'Attributes': {
                **self.build_attributes(record),
                'logger.file_name': record.filename,
                'logger.module_path': record.name,
                'logger.module': record.module,
            },
            'Resource': {
                'service.name': self.service_name,
                'service.pid': record.process,
            },
            'TraceId': trace_id,
            'SpanId': span_id,
            'SeverityText': 'WARN' if record.levelno == logging.WARNING else record.levelname,
            'SeverityNumber': self.log_level_mapping[record.levelno],
            'Body': record.msg,
        }
