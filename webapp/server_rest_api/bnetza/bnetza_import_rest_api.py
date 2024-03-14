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
from uuid import uuid4

from flask import jsonify
from flask_cors import cross_origin
from flask_openapi.decorator import ErrorResponse

from webapp.common.rest import BaseMethodView
from webapp.common.rest.exceptions import InputValidationException
from webapp.common.server_auth import require_role, ServerAuthRole
from webapp.server_rest_api.base_blueprint import ServerApiBaseBlueprint
from webapp.server_rest_api.bnetza.bnetza_import_handler import BnetzaImportHandler


class BnetzaImportBlueprint(ServerApiBaseBlueprint):
    bnetza_import_handler: BnetzaImportHandler

    def __init__(self):
        self.bnetza_import_handler = BnetzaImportHandler
        super().__init__('import', __name__, url_prefix='/bnetza')

        self.add_url_rule(
            '/',
            view_func=BnetzaImportBaseMethodView.as_view(
                '',
                **self.get_base_method_view_dependencies(),
                bnetza_import_handler=self.bnetza_import_handler,
            ),
            methods=['POST'],
        )


class BnetzaImportBaseMethodView(BaseMethodView):
    bnetza_import_handler: BnetzaImportHandler

    def __init__(self, *args, bnetza_import_handler: BnetzaImportHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.bnetza_import_handler = bnetza_import_handler

    @require_role(ServerAuthRole.BNETZA)
    @cross_origin()
    def post(self):
        bnetza_import_handler = self.bnetza_import_handler
        data = self.request_helper.get_request_body()
        base_path = Path("temp/bnetza_import/")

        if not base_path.is_dir():
            base_path.mkdir(parents=True, exist_ok=True)
        if data:
            import_path = base_path.joinpath(f"{str(uuid4())}.xlsx")
            with import_path.open('wb') as data_file:
                data_file.write(data)
            return jsonify(bnetza_import_handler.handle_import_by_file(import_path))
        else:
            raise InputValidationException(message='no import file')
