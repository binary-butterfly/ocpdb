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

import uuid
from abc import ABC
from datetime import datetime, timezone
from json.decoder import JSONDecodeError
from pathlib import Path

from requests import Response, request
from requests.exceptions import ConnectionError, Timeout
from urllib3.exceptions import NewConnectionError

from webapp.common.config import ConfigHelper
from webapp.common.error_handling.exceptions import RemoteException
from webapp.services.import_services.models import SourceInfo


class RemoteMixin(ABC):
    config: dict
    source_info: SourceInfo
    config_helper: ConfigHelper

    @property
    def config(self) -> dict:
        return self.config_helper.get('SOURCES', {}).get(self.source_info.uid) or {}

    def json_request(self, fix_encoding: bool = False, **kwargs) -> dict | list:
        response = self.request(**kwargs)

        if fix_encoding:
            # Force UTF-8 encoding, because python requests sets ISO-8859-1 because of RFC 2616
            response.encoding = 'utf-8'
        try:
            return response.json()
        except JSONDecodeError as e:
            raise RemoteException(
                url=response.request.url,
                http_status=response.status_code,
                message='Invalid JSON',
            ) from e

    def request(self, *, method: str = 'get', url: str | None = None, path: str | None = None, **kwargs) -> Response:
        if url is None:
            url = self.config.get('url', self.source_info.source_url)
        if path is not None:
            url = f'{url}/{path}'

        try:
            response = request(
                method=method,
                url=url,
                timeout=600,
                **kwargs,
            )
        except (ConnectionError, NewConnectionError, Timeout) as e:
            raise RemoteException(url=url, message=f'Request failed: {e}') from e

        self._dump_response(response)
        if response.status_code < 200 or response.status_code >= 300:
            raise RemoteException(
                url=url,
                http_status=response.status_code,
                message=f'Invalid status code {response.status_code}',
            )

        return response

    def _dump_response(self, response: Response):
        if self.config.get('debug', False) is False:
            return

        debug_dump_dir = Path(self.config_helper.get('DEBUG_DUMP_DIR'), self.source_info.uid)
        debug_dump_dir.mkdir(exist_ok=True, parents=True)

        request_uid = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()
        metadata_file_path = Path(debug_dump_dir, f'{now}-meta-{request_uid}')
        request_body_file_path = Path(debug_dump_dir, f'{now}-request-{request_uid}')
        response_body_file_path = Path(debug_dump_dir, f'{now}-response-{request_uid}')

        metadata = [
            f'URL: {response.request.url}',
            f'Method: {response.request.method}',
            f'HTTP Status: {response.status_code}',
            '',
            'Request Headers:',
            *[f'{key}: {value}' for key, value in response.request.headers.items()],
            '',
            'Response Headers:',
            *[f'{key}: {value}' for key, value in response.headers.items()],
        ]

        with metadata_file_path.open('w') as metadata_file:
            metadata_file.writelines('\n'.join(metadata))

        if response.request.body:
            with request_body_file_path.open('w') as request_file:
                request_file.write(response.request.body)

        with response_body_file_path.open('wb') as response_file:
            for chunk in response.iter_content(chunk_size=128):
                response_file.write(chunk)
