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

import json
from abc import ABC

from celery import Task
from flask import Flask
from flask_celery import Celery
from kombu.serialization import register

from webapp.common.json import DefaultJSONEncoder


class LogErrorsCelery(Celery):
    def init_app(self, app: Flask):
        # register custom encoder, so Enumerations do not make json.dump exceptions In some tutorials they recommend
        # registering an own ContentType when setting encoders because if you set content_type = application/json you
        # will overwrite the old encoder. But if we just want another encoder, this is exactly what we want. We
        # tested this, but if something breaks some time later this might be a place to start.
        register(
            'extended_json',
            lambda obj: json.dumps(obj, cls=DefaultJSONEncoder),
            lambda obj: json.loads(obj),
            content_type='application/json',
            content_encoding='utf-8',
        )
        # use custom encoder
        app.config['accept_content'] = ['extended_json']
        app.config['task_serializer'] = 'extended_json'
        app.config['result_serializer'] = 'extended_json'

        super().init_app(app)

        class ContextTask(Task, ABC):
            def __init__(self):
                from webapp.extensions import logger
                self.logger = logger

            def __call__(self, *args, **kwargs):
                with app.app_context() as app_context:
                    return self.run(*args, **kwargs)

            def on_failure(self, exc, _task_id, _args, _kwargs, exc_info):
                self.logger.critical('app', str(exc).strip(), str(exc_info).strip())

        setattr(ContextTask, 'abstract', True)
        setattr(self, 'Task', ContextTask)
