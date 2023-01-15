"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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

import functools
from typing import Callable, TYPE_CHECKING

from flask import current_app
from sqlalchemy.orm import Session

from webapp.common.config import ConfigHelper
from webapp.common.contexts import ContextHelper
from webapp.common.remote_helper import RemoteHelper
from webapp.common.rest import RequestHelper
from webapp.repositories import (
    LocationRepository,
    EvseRepository,
    ConnectorRepository,
    BusinessRepository,
    ImageRepository, OptionRepository,
)
from webapp.services.import_services import ImportServices
from webapp.services.matching_service import MatchingService

if TYPE_CHECKING:
    from webapp.common.logger import Logger
    from webapp.common.server_auth import ServerAuthHelper


def cache_dependency(fn: Callable):
    """
    Decorator for methods of the Dependencies class that caches their return value inside the _cached_dependencies dict.
    """
    # Get name of wrapped function minus the "get_" prefix
    name = fn.__name__
    name = name[4:] if name.startswith('get_') else name

    @functools.wraps(fn)
    def wrapper(*args):
        self = args[0]
        # Check if dependency is cached
        if name not in self._cached_dependencies:
            # Create dependency by calling the wrapped function and cache it
            self._cached_dependencies[name] = fn(self)

        # Return the dependency from cache
        return self._cached_dependencies[name]
    return wrapper


class Dependencies:
    """
    Container class for dependency injection.

    Dependencies will be created as needed and cached in a dictionary by the "get_" methods.
    """

    # Dictionary for caching the dependencies
    _cached_dependencies: dict

    def __init__(self):
        self._cached_dependencies = {}

    # Common
    @cache_dependency
    def get_logger(self) -> 'Logger':
        # Late import (don't initialize all the extensions unless needed)
        from webapp.extensions import logger
        return logger

    @cache_dependency
    def get_config_helper(self) -> ConfigHelper:
        return ConfigHelper()

    @cache_dependency
    def get_request_helper(self) -> RequestHelper:
        return RequestHelper()

    @cache_dependency
    def get_remote_helper(self) -> RemoteHelper:
        return RemoteHelper(
            config_helper=self.get_config_helper(),
            logger=self.get_logger(),
        )

    @cache_dependency
    def get_context_helper(self) -> ContextHelper:
        return ContextHelper()

    @cache_dependency
    def get_server_auth_helper(self) -> 'ServerAuthHelper':
        # Avoid import loops ...
        from webapp.common.server_auth import ServerAuthDatabase, ServerAuthHelper
        server_auth_users = ServerAuthDatabase.create_from_config(current_app.config)
        return ServerAuthHelper(
            server_auth_users=server_auth_users,
            context_helper=self.get_context_helper(),
        )

    # Database
    @cache_dependency
    def get_db_session(self) -> Session:
        # Late import (don't initialize all the extensions unless needed)
        from webapp.extensions import db
        return db.session

    # Repositories
    @cache_dependency
    def get_location_repository(self) -> LocationRepository:
        return LocationRepository(
            session=self.get_db_session(),
        )

    @cache_dependency
    def get_evse_repository(self) -> EvseRepository:
        return EvseRepository(
            session=self.get_db_session(),
        )

    @cache_dependency
    def get_connector_repository(self) -> ConnectorRepository:
        return ConnectorRepository(
            session=self.get_db_session(),
        )

    @cache_dependency
    def get_business_repository(self) -> BusinessRepository:
        return BusinessRepository(
            session=self.get_db_session(),
        )

    @cache_dependency
    def get_image_repository(self) -> ImageRepository:
        return ImageRepository(
            session=self.get_db_session(),
        )

    @cache_dependency
    def get_option_repository(self) -> OptionRepository:
        return OptionRepository(
            session=self.get_db_session(),
        )

    # Services
    def get_base_service_dependencies(self) -> dict:
        return {
            'logger': self.get_logger(),
            'config_helper': self.get_config_helper(),
        }

    @cache_dependency
    def get_import_services(self) -> ImportServices:
        return ImportServices(
            **self.get_base_service_dependencies(),
            remote_helper=self.get_remote_helper(),
            location_repository=self.get_location_repository(),
            evse_repository=self.get_evse_repository(),
            connector_repository=self.get_evse_repository(),
            business_repository=self.get_business_repository(),
            image_repository=self.get_image_repository(),
            option_repository=self.get_option_repository(),
        )

    @cache_dependency
    def get_matching_service(self) -> MatchingService:
        return MatchingService(
            **self.get_base_service_dependencies(),
            location_repository=self.get_location_repository(),
        )


# Instantiate one global dependencies object so we don't need to clutter the environment with lots of globals
dependencies = Dependencies()
