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


from re import sub
from enum import Enum
from typing import Callable, Optional, List, Union
from flask import current_app


class EndpointTag(Enum):
    ocpi = 'endpoints for ocpi'


class EndpointArgs(Enum):
    start = 'start'


class Endpoint:
    methods: List[str] = []
    path: Union[str, None] = None

    arg_presets = {
        EndpointArgs.start: {
            'name': 'start',
            'description': 'start id for pagination',
            'schema': {
                'type': 'integer',
                'default': 1
            },
            'required': False
        }
    }

    @property
    def args(self):
        result = []
        for arg in self._args:
            if type(arg) != EndpointArgs:
                result.append(arg)
                continue
            if arg not in self.arg_presets:
                raise Exception('invalid default arg')
            result.append(self.arg_presets[arg])
        return result

    def __init__(self,
                 view_function: Callable,
                 request: Optional[dict] = None,
                 response: Optional[dict] = None,
                 tags: Optional[List[EndpointTag]] = None,
                 summary: Optional[str] = '',
                 description: Optional[str] = '',
                 path_params: Optional[dict] = None,
                 args: Optional[list] = None,
                 request_schema: Optional[Union[str, dict]] = None,
                 request_schema_multi: Optional[dict] = None,
                 response_schema: Optional[Union[str, dict]] = None,
                 response_schema_multi: Optional[dict] = None,
                 basic_auth: bool = False):
        self.view_function = view_function
        self.request = request
        self.response = response
        self.tags = tags if tags else []
        self.summary = summary
        self.description = description
        self.path_params = path_params if path_params else {}
        self._args = args if args else []
        self.basic_auth = basic_auth
        if request_schema_multi:
            self.request_schema = request_schema_multi
        elif request_schema:
            self.request_schema = {
                'application/json': request_schema
            }
        else:
            self.request_schema = None
        if response_schema_multi:
            self.response_schema = response_schema_multi
        elif response_schema:
            self.response_schema = {
                'application/json': response_schema
            }
        else:
            self.response_schema = None


class ApiDocumentation:
    endpoints = {}

    def register(self, **kwargs):
        def decorator(f):
            self.endpoints[f] = Endpoint(f, **kwargs)
            return f
        return decorator

    def data(self):
        for rule in current_app.url_map.iter_rules():
            if current_app.view_functions[rule.endpoint] not in self.endpoints:
                continue
            self.endpoints[current_app.view_functions[rule.endpoint]].methods = [method.lower() for method in rule.methods if method in ['GET', 'POST']]
            self.endpoints[current_app.view_functions[rule.endpoint]].path = sub(r'<(\w*):(\w*)>', r'{\2}', rule.rule)\
                .replace('<', '{').replace('>', '}')
        return self.endpoints.values()


def filter_schema(schema):
    for delete_key in ['$id', '$schema']:
        if delete_key in schema:
            del schema[delete_key]
    return schema


def encapsulate_response(schema, mimetype):
    if mimetype != 'application/json':
        return schema
    return {
        'title': 'response object',
        'type': 'object',
        'required': [
            'status'
        ],
        'properties': {
            'status': {
                'type': 'integer',
                'description': 'whether request is sucessful or not. 0 means success, negative values are errors'
            },
            'errors': {
                'type': 'array',
                'description': 'if there is an error this object describes it',
                'items': {
                    'type': 'string'
                }
            },
            'data': schema
        }
    }


def listify_schema(schema):
    return {
        'title': 'list of objects',
        'type': 'array',
        'items': schema
    }


def path_param(name, description, data_type):
    return {
        'name': name,
        'description': description,
        'schema': {
            'type': data_type
        }
    }
