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

from http import HTTPStatus

from tests.integration.helpers import OpenApiFlaskClient


def test_server_openapi_json_renders(test_client: OpenApiFlaskClient) -> None:
    """
    The server (admin) OpenAPI document must render without errors. A regression
    here caused HTTP 500 because legacy config converters and undocumented
    blueprints leaked exceptions through the documentation route.
    """
    response = test_client.get('/documentation/server.json')

    assert response.status_code == HTTPStatus.OK
    body = response.get_json()

    assert body['openapi'].startswith('3.')
    assert body['info']['title']

    # All four server blueprints should report under /api/server/v1.
    server_url_prefixes = [server['url'] for server in body['servers']]
    assert any(url.endswith('/api/server/v1') for url in server_url_prefixes)

    # All routes from `documented = True` blueprints under /api/server/v1 appear in paths and
    # have their documented HTTP methods populated.
    paths = body['paths']
    assert set(paths['/giroe/locations/{location_id}'].keys()) == {'put', 'delete'}
    assert set(paths['/giroe/connectors/{connector_uid}'].keys()) == {'patch'}
    assert set(paths['/bnetza/'].keys()) == {'post'}
    # flask_openapi does not (yet) document HEAD operations, so only POST is listed here.
    assert set(paths['/datex/v3.5/{source_uid}/realtime'].keys()) == {'post'}

    # Schemas declared via components show up in the spec.
    schemas = body['components']['schemas']
    assert 'GiroeLocationInput' in schemas
    assert 'GiroeConnectorPatch' in schemas
    assert 'errorResponse' in schemas


def test_server_openapi_html_renders(test_client: OpenApiFlaskClient) -> None:
    """The Stoplight-Elements HTML wrapper page must load without errors."""
    response = test_client.get('/documentation/server.html')

    assert response.status_code == HTTPStatus.OK
    assert b'apiDescriptionUrl' in response.data
