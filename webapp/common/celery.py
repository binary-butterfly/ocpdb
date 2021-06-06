# encoding: utf-8

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


from flask_celery import Celery


class LogErrorsCelery(Celery):
    def init_app(self, app):
        super().init_app(app)
        task_base = self.Task

        class ContextTask(task_base):

            def __call__(self, *_args, **_kwargs):
                from ..extensions import logger
                with app.app_context():
                    def on_failure(exc, task_id, args, kwargs, einfo):
                        self.handle_task_error(exc, task_id, args, kwargs, einfo)
                    setattr(self, 'on_failure', on_failure)

                    def handle_task_error(exc, task_id, args, kwargs, traceback):
                        logger.critical('app', str(exc).strip(), str(traceback).strip())
                    setattr(self, 'handle_task_error', handle_task_error)

                    return task_base.__call__(self, *_args, **_kwargs)

        setattr(ContextTask, 'abstract', True)
        setattr(self, 'Task', ContextTask)
