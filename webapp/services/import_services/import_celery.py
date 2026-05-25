"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2023 binary butterfly GmbH

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
from pathlib import Path

from webapp.common.logging.models import LogMessageType
from webapp.dependencies import dependencies
from webapp.extensions import celery
from webapp.services.import_services.datex2.v3_5.base_datex2_v3_5_import_service import BaseDatex2V35ImportService

logger = logging.getLogger(__name__)


@celery.task
def bnetza_import_by_file(import_file_path: str):
    dependencies.get_import_services().bnetza_import_service.load_and_save_from_file(Path(import_file_path))


@celery.task
def datex2_v3_5_realtime_import_by_file(source_uid: str, import_file_path: str) -> None:
    """
    Apply a queued DATEX II v3.5 realtime payload via the source's import service.

    All import logic lives on :class:`BaseDatex2V35ImportService`; this task is just the celery
    entry point that resolves the importer by ``source_uid`` and ensures the persisted payload
    file is removed once processing finishes.
    """
    path = Path(import_file_path)
    try:
        importer = dependencies.get_import_services().importer_by_uid.get(source_uid)
        if not isinstance(importer, BaseDatex2V35ImportService):
            logger.error(
                'DATEX2 realtime import task received unknown / non-DATEX2 source %r — dropping payload %s.',
                source_uid,
                import_file_path,
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            return
        importer.import_realtime_data_from_file(path)
    finally:
        try:
            path.unlink(missing_ok=True)
        except OSError as e:
            logger.warning(
                'Could not remove processed DATEX2 realtime payload %s: %s',
                import_file_path,
                e,
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
