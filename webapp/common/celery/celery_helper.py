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


class CeleryHelper:
    """
    Helper class for wrapping calls to celery tasks.

    The purpose of this class is to make code that calls/starts celery tasks better unit-testable by wrapping the celery calls.
    For example, `celery_helper.delay(some_task, args...)` would effectively call `some_task.delay(args)`. When writing unit tests,
    you can simply mock the CeleryHelper and just check whether the `delay()` method was called with the correct task.
    """

    # Note: No type hint for the task parameter because PyCharm does not recognize functions with the @celery.task decorator as Tasks...
    @staticmethod
    def delay(task, *args, **kwargs):
        """
        Queues a celery task. Effectively just calls `task.delay(*args, **kwargs)`.
        """
        return task.delay(*args, **kwargs)

    @staticmethod
    def apply_async(task, *args, **kwargs):
        """
        Queues a celery task. Effectively just calls `task.apply_async(*args, **kwargs)`.
        """
        return task.apply_async(*args, **kwargs)

    @staticmethod
    def with_delay(task, delay_seconds: int, *args, **kwargs):
        """
        Queues a celery task with a specified delay.
        """
        return task.apply_async(args=args, kwargs=kwargs, countdown=delay_seconds)
