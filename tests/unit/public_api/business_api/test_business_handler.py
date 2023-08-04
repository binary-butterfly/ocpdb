import pytest
from unittest.mock import Mock

import webapp.common.config
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
def logger_mock():
    return Mock(webapp.common.logger.Logger)


@pytest.fixture
def business_query_mock():
    return Mock(BusinessSearchQuery(name="EN"))


def test_business_handler_get_business_by_id(business_repository_mock, logger_mock, config_helper_mock):
    business_repository_mock.fetch_by_id.return_value = "teststring"
    handler = BusinessHandler(business_repository=business_repository_mock, logger=logger_mock,
                              config_helper=config_helper_mock)
    assert handler.get_business_by_id(1) is "teststring"
    business_repository_mock.fetch_by_id.assert_called_with(1)


def test_business_handler_get_by_name(business_repository_mock, business_query_mock, logger_mock, config_helper_mock):
    business_repository_mock.fetch_business_by_name.return_value = "teststring"
    handler = BusinessHandler(business_repository=business_repository_mock, logger=logger_mock,
                              config_helper=config_helper_mock)
    assert handler.get_business_by_name(BusinessSearchQuery(name="En")) is "teststring"
