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

from pathlib import Path

from webapp.server_rest_api.base_handler import ServerApiBaseHandler
from webapp.services.import_services.bnetza import BnetzaImportService
from webapp.services.import_services.import_celery import bnetza_import_by_file
from webapp.dependencies import dependencies


class BnetzaImportHandler(ServerApiBaseHandler):
    bnetza_import_service: BnetzaImportService

    def __init__(self, *args, bnetza_import_service: BnetzaImportService, **kwargs):
        super().__init__(*args, **kwargs)
        self.bnetza_import_service = bnetza_import_service

    @staticmethod
    def handle_import_by_file(import_path: Path) -> str:
        helper = dependencies.get_celery_helper()
        helper.delay(bnetza_import_by_file, str(import_path))
        return "Import started"
