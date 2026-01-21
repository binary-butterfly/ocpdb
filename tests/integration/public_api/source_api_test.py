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
from tests.integration.model_generators.source import SOURCE_UID_1, SOURCE_UID_2, get_source
from webapp.common.sqlalchemy import SQLAlchemy


def test_get_sources(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    source1 = get_source(uid=SOURCE_UID_1, name='Source One')
    source2 = get_source(uid=SOURCE_UID_2, name='Source Two')
    db.session.add_all([source1, source2])
    db.session.commit()

    response = public_test_client.get(path='/api/public/v1/sources')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2
    assert len(response.json['items']) == 2

    # Sources should be sorted by uid by default
    assert response.json['items'][0]['uid'] == SOURCE_UID_1
    assert response.json['items'][0]['name'] == 'Source One'
    assert response.json['items'][1]['uid'] == SOURCE_UID_2
    assert response.json['items'][1]['name'] == 'Source Two'


def test_get_sources_sorted_by_name(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    source1 = get_source(uid=SOURCE_UID_1, name='Zebra Source')
    source2 = get_source(uid=SOURCE_UID_2, name='Alpha Source')
    db.session.add_all([source1, source2])
    db.session.commit()

    response = public_test_client.get(path='/api/public/v1/sources?sorted_by=name')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 2

    # Sources should be sorted by name
    assert response.json['items'][0]['name'] == 'Alpha Source'
    assert response.json['items'][1]['name'] == 'Zebra Source'


def test_get_sources_filter_by_name(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    source1 = get_source(uid=SOURCE_UID_1, name='Test Source')
    source2 = get_source(uid=SOURCE_UID_2, name='Other Source')
    db.session.add_all([source1, source2])
    db.session.commit()

    response = public_test_client.get(path='/api/public/v1/sources?name=Test')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 1
    assert response.json['items'][0]['name'] == 'Test Source'


def test_get_sources_with_pagination(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    source1 = get_source(uid='source-a', name='Source A')
    source2 = get_source(uid='source-b', name='Source B')
    source3 = get_source(uid='source-c', name='Source C')
    db.session.add_all([source1, source2, source3])
    db.session.commit()

    response = public_test_client.get(path='/api/public/v1/sources?limit=2')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 3
    assert len(response.json['items']) == 2


def test_get_sources_empty(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    response = public_test_client.get(path='/api/public/v1/sources')
    assert response.status_code == HTTPStatus.OK
    assert response.json['total_count'] == 0
    assert response.json['items'] == []


def test_get_source_by_id(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    source = get_source(
        uid=SOURCE_UID_1,
        name='Test Source',
        public_url='https://example.com',
        attribution_license='CC-BY-4.0',
        attribution_contributor='Example Contributor',
        attribution_url='https://example.com/attribution',
    )
    db.session.add(source)
    db.session.commit()

    response = public_test_client.get(path=f'/api/public/v1/sources/{source.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json['id'] == source.id
    assert response.json['uid'] == SOURCE_UID_1
    assert response.json['name'] == 'Test Source'
    assert response.json['public_url'] == 'https://example.com'
    assert response.json['attribution_license'] == 'CC-BY-4.0'
    assert response.json['attribution_contributor'] == 'Example Contributor'
    assert response.json['attribution_url'] == 'https://example.com/attribution'
