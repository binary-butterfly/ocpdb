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
from tests.integration.model_generators.business import get_business_1
from tests.integration.model_generators.evse import get_full_evse_1
from tests.integration.model_generators.location import get_location_1
from tests.integration.model_generators.tariff import (
    TARIFF_UID_1,
    TARIFF_UID_2,
    get_tariff_1,
    get_tariff_2,
    get_tariff_association,
)
from webapp.common.sqlalchemy import SQLAlchemy


def test_connector_outputs_tariff_uids_of_its_evse(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    """Sources publish tariffs per EVSE, so the connectors of an EVSE output its tariff uids."""
    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    evse = get_full_evse_1()
    evse.tariff_associations = [get_tariff_association(uid='TA-1', tariff=tariff)]
    db.session.add(get_location_1(evses=[evse], operator=get_business_1()))
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/connectors/1?strict=true')

    assert response.status_code == HTTPStatus.OK
    assert response.json['tariff_ids'] == [TARIFF_UID_1]


def test_connector_outputs_all_tariff_uids_of_its_evse(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    """An EVSE offered under several tariffs passes all of their uids to its connectors."""
    first_tariff = get_tariff_1()
    second_tariff = get_tariff_2()
    db.session.add_all([first_tariff, second_tariff])
    db.session.flush()

    evse = get_full_evse_1()
    evse.tariff_associations = [
        get_tariff_association(uid='TA-1', tariff=first_tariff),
        get_tariff_association(uid='TA-2', tariff=second_tariff),
    ]
    db.session.add(get_location_1(evses=[evse], operator=get_business_1()))
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/connectors/1?strict=true')

    assert response.status_code == HTTPStatus.OK
    assert sorted(response.json['tariff_ids']) == [TARIFF_UID_1, TARIFF_UID_2]


def test_connector_outputs_grouped_tariff_uid_only_once(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    """
    Identical tariffs of a source are grouped, so two associations of one EVSE can point at the same
    tariff. Its uid must not show up twice.
    """
    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    evse = get_full_evse_1()
    evse.tariff_associations = [
        get_tariff_association(uid='TA-1', tariff=tariff),
        get_tariff_association(uid='TA-2', tariff=tariff),
    ]
    db.session.add(get_location_1(evses=[evse], operator=get_business_1()))
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/connectors/1?strict=true')

    assert response.status_code == HTTPStatus.OK
    assert response.json['tariff_ids'] == [TARIFF_UID_1]


def test_connector_tariff_uids_take_precedence_over_the_evse_ones(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    """A connector carrying its own tariffs does not inherit the ones of its EVSE."""
    evse_tariff = get_tariff_1()
    connector_tariff = get_tariff_2()
    db.session.add_all([evse_tariff, connector_tariff])
    db.session.flush()

    evse = get_full_evse_1()
    evse.tariff_associations = [get_tariff_association(uid='TA-1', tariff=evse_tariff)]
    evse.connectors[0].tariff_associations = [get_tariff_association(uid='TA-2', tariff=connector_tariff)]
    db.session.add(get_location_1(evses=[evse], operator=get_business_1()))
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/connectors/1?strict=true')

    assert response.status_code == HTTPStatus.OK
    assert response.json['tariff_ids'] == [TARIFF_UID_2]


def test_connector_without_tariffs_omits_tariff_ids(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    """tariff_ids is optional in OCPI, so a connector without any tariff leaves it out."""
    db.session.add(get_location_1(evses=[get_full_evse_1()], operator=get_business_1()))
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/connectors/1?strict=true')

    assert response.status_code == HTTPStatus.OK
    assert 'tariff_ids' not in response.json


def test_evse_endpoint_outputs_connector_tariff_uids(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    """The connectors nested into an EVSE response carry the tariff uids too."""
    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    evse = get_full_evse_1()
    evse.tariff_associations = [get_tariff_association(uid='TA-1', tariff=tariff)]
    db.session.add(get_location_1(evses=[evse], operator=get_business_1()))
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/3.0/evses/1?strict=true')

    assert response.status_code == HTTPStatus.OK
    assert [connector['tariff_ids'] for connector in response.json['connectors']] == [[TARIFF_UID_1]]


def test_location_endpoint_outputs_connector_tariff_uids(
    db: SQLAlchemy,
    public_test_client: OpenApiFlaskClient,
) -> None:
    """
    The connectors nested into a location response carry the tariff uids too. OCPI 2.2 is the version
    which nests EVSEs and connectors into the location, so this checks the list endpoint there.
    """
    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    evse = get_full_evse_1()
    evse.tariff_associations = [get_tariff_association(uid='TA-1', tariff=tariff)]
    db.session.add(get_location_1(evses=[evse], operator=get_business_1()))
    db.session.commit()

    response = public_test_client.get(path='/api/public/ocpi/2.2/locations?strict=true')

    assert response.status_code == HTTPStatus.OK
    connectors = [
        connector
        for location in response.json['items']
        for evse in location['evses']
        for connector in evse['connectors']
    ]
    assert [connector['tariff_ids'] for connector in connectors] == [[TARIFF_UID_1]]


def test_single_location_endpoint_outputs_connector_tariff_uids(
    db: SQLAlchemy,
    test_client: OpenApiFlaskClient,
) -> None:
    """
    The single location endpoint loads its children through a separate path, so it is checked too. It
    always answers non-strict, hence the plain test_client.
    """
    tariff = get_tariff_1()
    db.session.add(tariff)
    db.session.flush()

    evse = get_full_evse_1()
    evse.tariff_associations = [get_tariff_association(uid='TA-1', tariff=tariff)]
    db.session.add(get_location_1(evses=[evse], operator=get_business_1()))
    db.session.commit()

    response = test_client.get(path='/api/public/ocpi/2.2/locations/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json['evses'][0]['connectors'][0]['tariff_ids'] == [TARIFF_UID_1]
