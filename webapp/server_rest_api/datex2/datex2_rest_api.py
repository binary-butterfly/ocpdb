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

import json
from email.utils import format_datetime
from http import HTTPStatus
from pathlib import Path
from uuid import uuid4

from flask import Response
from flask_openapi.decorator import (
    ErrorResponse,
    Parameter,
    Request,
    ResponseData,
    document,
)
from flask_openapi.decorator import (
    Response as DocumentedResponse,
)
from flask_openapi.schema import StringField

from webapp.common.celery import CeleryHelper
from webapp.common.response import empty_json_response
from webapp.common.rest import BaseMethodView
from webapp.common.rest.exceptions import InputValidationException
from webapp.common.server_auth import skip_basic_auth
from webapp.dependencies import dependencies
from webapp.server_rest_api.base_blueprint import ServerApiBaseBlueprint
from webapp.services.import_services.exceptions import ImportException
from webapp.services.import_services.import_celery import datex2_v3_5_realtime_import_by_file

from .datex2_handler import Datex2Handler


class Datex2ImportBlueprint(ServerApiBaseBlueprint):
    documented = True
    skip_basic_auth = True

    def __init__(self):
        super().__init__('datex2', __name__, url_prefix='/datex')

        realtime_view = Datex2RealtimeMethodView.as_view(
            'datex2_v3_5_realtime',
            **self.get_base_method_view_dependencies(),
            datex2_handler=Datex2Handler(
                import_services=dependencies.get_import_services(),
                **self.get_base_handler_dependencies(),
            ),
            celery_helper=dependencies.get_celery_helper(),
        )
        self.add_url_rule(
            '/v3.5/<source_uid>/realtime',
            view_func=realtime_view,
            methods=['HEAD', 'POST'],
        )


class Datex2BaseMethodView(BaseMethodView):
    datex2_handler: Datex2Handler

    def __init__(self, *args, datex2_handler: Datex2Handler, **kwargs):
        super().__init__(*args, **kwargs)
        self.datex2_handler = datex2_handler


class Datex2RealtimeMethodView(Datex2BaseMethodView):
    decorators = [skip_basic_auth]
    celery_helper: CeleryHelper

    def __init__(self, *args, celery_helper: CeleryHelper, **kwargs):
        super().__init__(*args, **kwargs)
        self.celery_helper = celery_helper

    def head(self, source_uid: str) -> tuple[Response, HTTPStatus]:
        last_modified = self.datex2_handler.get_last_modified(
            source_uid=source_uid,
            key=self.request_helper.get_query_args().get('key'),
        )
        response = empty_json_response()
        if last_modified is not None:
            response.headers['Last-Modified'] = format_datetime(last_modified)

        # Mobilithek expects HTTP 200 instead of HTTP 204
        return response, HTTPStatus.OK

    @document(
        summary='Push DATEX II v3.5 realtime EVSE statuses',
        description=(
            'Accepts a Mobilithek-style DATEX II v3.5 JSON payload (`messageContainer.payload[0]` '
            '`aegiEnergyInfrastructureStatusPublication`). The payload is validated synchronously; '
            '`deltaPush` updates are small incremental changes and are applied directly, while any '
            'other exchange protocol (e.g. snapshots) is persisted to `DATEX2_IMPORT_DIR` and '
            'processed asynchronously by a Celery worker so very large payloads do not block the '
            "request thread. The `key` query parameter must match the source's configured `api_key`."
        ),
        path=[Parameter('source_uid', schema=StringField())],
        query=[
            Parameter('key', schema=StringField(), description='Per-source API key (matches `api_key` in `SOURCES`).')
        ],
        request=[Request(mimetype='application/json')],
        response=[
            DocumentedResponse(
                ResponseData(),
                http_status=HTTPStatus.OK,
                description='Realtime payload accepted for asynchronous processing.',
            ),
            ErrorResponse(error_codes=[HTTPStatus.BAD_REQUEST, HTTPStatus.UNAUTHORIZED, HTTPStatus.NOT_FOUND]),
        ],
    )
    def post(self, source_uid: str) -> tuple[Response, HTTPStatus]:
        # Validate the source + API key synchronously so unauthorized/unknown sources fail fast
        # before we touch the payload.
        service = self.datex2_handler.validate_realtime_request(
            source_uid=source_uid,
            key=self.request_helper.get_query_args().get('key'),
        )

        data = self.request_helper.get_request_body()
        if not data:
            raise InputValidationException(message='no realtime payload')

        try:
            parsed_data = json.loads(data)
        except json.JSONDecodeError as e:
            raise InputValidationException(message='invalid JSON realtime payload') from e

        # Validate the envelope up-front via the import service so malformed pushes fail fast.
        try:
            message_container = service.validate_realtime_data(parsed_data)
        except ImportException as e:
            raise InputValidationException(message=e.message) from e

        # deltaPush updates are small incremental changes - apply them directly. Everything else
        # (snapshots etc.) can be large, so hand it off to a celery worker via the import file.
        if service.is_delta_push(message_container):
            service.store_realtime_data(message_container)
            # Mobilithek expects HTTP 200 instead of HTTP 204
            return empty_json_response(), HTTPStatus.OK

        base_path = Path(self.config_helper.get('DATEX2_IMPORT_DIR'))
        if not base_path.is_dir():
            base_path.mkdir(parents=True, exist_ok=True)

        import_path = base_path.joinpath(f'{source_uid}_{uuid4()}.json')
        with import_path.open('wb') as data_file:
            data_file.write(data)

        self.celery_helper.delay(datex2_v3_5_realtime_import_by_file, source_uid, str(import_path))

        # Mobilithek expects HTTP 200 instead of HTTP 204
        return empty_json_response(), HTTPStatus.OK
