from unittest.mock import Mock

import pytest

import webapp.common.config
from webapp.models import Business
from webapp.public_api.business_api.business_handler import BusinessHandler, BusinessSearchQuery
from webapp.repositories.business_repository import BusinessRepository


@pytest.fixture
def business_repository_mock():
    return Mock(BusinessRepository)


@pytest.fixture
def business_handler_mock():
    return Mock(BusinessHandler)


@pytest.fixture
def config_helper_mock():
    return Mock(webapp.common.config.ConfigHelper)


@pytest.fixture
def business_query_mock():
    return Mock(BusinessSearchQuery(name='EN'))


def test_business_handler_get_business_by_id(business_repository_mock, config_helper_mock):
    business = Business()
    business.id = 1
    business.name = 'test'

    business_repository_mock.fetch_by_id.return_value = business
    handler = BusinessHandler(
        business_repository=business_repository_mock,
        config_helper=config_helper_mock,
    )
    assert handler.get_business_by_id(1) == {'name': 'test'}
    business_repository_mock.fetch_by_id.assert_called_with(1)
