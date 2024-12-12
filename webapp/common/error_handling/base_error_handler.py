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

import traceback
from typing import TYPE_CHECKING, Callable, Optional, Type

from sqlalchemy.orm import scoped_session

if TYPE_CHECKING:
    from webapp.common.logger import Logger


class BaseErrorHandler:
    """
    Base class for error handlers.
    """

    # Mapping Exception->Callable
    _handlers: dict

    # Dependencies
    logger: 'Logger'
    db_session: scoped_session

    # Whether the application is running in debug mode. Error handlers may decide to log more detailed errors when in debug mode.
    debug: bool

    def __init__(self, *, logger: 'Logger', db_session: scoped_session, debug: bool = False):
        self._handlers = {}
        self.logger = logger
        self.db_session = db_session
        self.debug = debug

    def register(self, error_class: Type[Exception], func: Callable):
        """
        Registers a handler for a specific type of Exception.
        """
        self._handlers[error_class] = func

    def handle_error(self, error: Exception):
        """
        Looks up the handler for an exception and calls it. Returns the result of the handler, which should be a tuple of an
        HTTP response and a response code. If no handler is registered for the exception, None is returned.
        """
        # Rollback any database transaction that we might be in
        self._rollback_db_transaction()

        # Look up error handler and call it
        handler = self._find_handler(type(error))
        if handler:
            return handler(error)

        return None

    def _find_handler(self, error_class: Type[Exception]) -> Optional[Callable]:
        """
        Finds the most specific handler for this exception by traversing the inheritance hierarchy.
        E.g. for a NotFound exception: First lookup NotFound, then HTTPException, then Exception, then BaseException, then object.
        """
        for cls in error_class.__mro__:
            handler = self._handlers.get(cls)
            if handler is not None:
                return handler

        # No handler found
        return None

    def _rollback_db_transaction(self) -> None:
        """
        Rolls back the current database transaction if there is one.
        """
        self.db_session.rollback()

    def _log_critical(self, error: Exception):
        """
        Helper function to write critical errors to the log.
        """
        self.logger.critical('app', str(error), traceback.format_exc())
