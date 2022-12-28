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

import os
import json
from re import sub
from json.decoder import JSONDecodeError
from inspect import getfile
from dataclasses import asdict
from flask import current_app
from .openapi_decorator import ErrorResponse, EmptyResponse, Schema, SearchParameter, ResponseData, Response, Request


def remove_none(obj):
    if isinstance(obj, list):
        return [remove_none(item) for item in obj if item is not None]
    elif isinstance(obj, dict):
        return {key: remove_none(value) for key, value in obj.items() if value is not None}
    return obj


def generate_openapi(base_path: str):
    paths = {}
    schemas = {}
    examples = {}
    blueprint_paths = [
        path for path, blueprint in current_app.blueprints.items()
        if path.startswith(base_path) and hasattr(blueprint, 'documented') and blueprint.documented
    ]
    for blueprint_path in blueprint_paths:
        for rule in current_app.url_map.iter_rules():
            if not rule.endpoint.startswith(blueprint_path):
                continue
            path_str = sub(r'<(?:\w*:)?(\w*)>', r'{\1}', rule.rule)
            view_class = current_app.view_functions[rule.endpoint].view_class
            schema_dir = os.path.join(os.path.dirname(getfile(view_class)), 'schema')
            if path_str not in paths:
                paths[path_str] = {}
            for method in ['get', 'post', 'put', 'patch', 'delete']:
                if not hasattr(view_class, method):
                    continue
                if not hasattr(getattr(view_class, method), 'documentation'):
                    continue
                paths[path_str][method] = get_method_data(view_class, method, schema_dir, schemas, examples)

    result = {
        'openapi': '3.0.3',
        'info': {
            'title': current_app.config['OPENAPI_TITLE'],
            'description': current_app.config['OPENAPI_DESCRIPTION'],
            'version': current_app.config['PROJECT_VERSION'],
            'termsOfService': current_app.config['OPENAPI_TOS'],
            'contact': {
                'email': current_app.config['OPENAPI_CONTACT_MAIL']
            }
        },
        'servers': current_app.config['OPENAPI_SERVERS'] + ([{
               'url': current_app.config['PROJECT_URL'],
               'description': 'development'
           }] if current_app.config['DEBUG'] else []),
        'tags': [],
        'components': {
            'securitySchemes': {
                'basicAuth': {
                    'type': 'http',
                    'scheme': 'basic'
                }
            },
            'schemas': {
                'errorResponse': error_response_schema,
                **schemas
            },
            'examples': examples
        },
        'paths': remove_none(paths)
    }
    return result


def get_method_data(view_class, method: str, schema_dir: str, schemas: dict, examples: dict):
    endpoint = getattr(view_class, method).documentation
    method_data = {
        'summary': endpoint.summary,
        'description': endpoint.description,
        'tags': [tag.name for tag in endpoint.tags] if endpoint.tags else [],
        'parameters': [],
        'responses': {}
    }
    for path in endpoint.path:
        method_data['parameters'].append({**asdict(path), 'in': 'path', 'required': True})
    for query in endpoint.query:
        if type(query) is SearchParameter:
            method_data['parameters'] += pagination_parameters
            continue
        method_data['parameters'].append({**asdict(query), 'in': 'query'})
    if method in ['post', 'put', 'patch'] and endpoint.request is not None:
        method_data['requestBody'] = {
            'required': True,
            'content': {}
        }
        for request in endpoint.request:
            apply_request_schema(method_data, request, schema_dir)

    for response in endpoint.response:
        if type(response) is ErrorResponse:
            for key, value in error_schemas.items():
                method_data['responses'][key] = value
            continue
        if type(response) is EmptyResponse:
            for key, value in empty_response_schema.items():
                method_data['responses'][key] = value
            continue
        if str(response.http_status) in method_data['responses']:
            raise Exception('multiple responses for same http status')
        method_data['responses'][str(response.http_status)] = {
            'description': response.description,
            'content': {}
        }
        for response_data in response.data:
            apply_response_schema(method_data, response, response_data, schema_dir)

    if hasattr(getattr(view_class, method), 'basic_auth') \
            and getattr(getattr(view_class, method), 'basic_auth'):
        method_data['security'] = [{
            'basicAuth': []
        }]

    for component in endpoint.components:
        if type(component) is Schema and component.name in schemas:
            continue
        apply_component(component, schemas, examples, schema_dir)
    return method_data


def apply_request_schema(method_data: dict, request: Request, schema_dir: str):
    if str(request.mimetype) in method_data['requestBody']['content']:
        raise Exception('multiple responses for same mimetype')
    method_data['requestBody']['content'][request.mimetype] = {}
    if request.schema:
        if type(request.schema) is str:
            schema_file_path = os.path.join(schema_dir, '%s.json' % request.schema)
            if not os.path.exists(schema_file_path):
                raise Exception('schema file %s is missing' % schema_file_path)
            with open(schema_file_path) as schema_file:
                try:
                    method_data['requestBody']['content'][request.mimetype]['schema'] \
                        = filter_schema(json.load(schema_file))
                except JSONDecodeError:
                    raise Exception('schema file %s is invalid' % schema_file_path)

        else:
            method_data['requestBody']['content'][request.mimetype]['schema'] = request.schema

    if request.example:
        if type(request.example) is str:
            example_file_path = os.path.join(schema_dir, '%s.json' % request.example)
            if not os.path.exists(example_file_path):
                raise Exception('example file %s is missing' % example_file_path)
            with open(example_file_path) as example:
                try:
                    method_data['requestBody']['content'][request.mimetype]['example'] \
                        = filter_schema(json.load(example))
                except JSONDecodeError:
                    raise Exception('example file %s is invalid' % example_file_path)
        else:
            method_data['requestBody']['content'][request.mimetype]['example'] = request.example


def apply_response_schema(method_data: dict, response: Response, response_data: ResponseData, schema_dir: str):
    if response_data.mimetype in method_data['responses'][str(response.http_status)]['content']:
        raise Exception('multiple responses for mimetype')
    method_data['responses'][str(response.http_status)]['content'][response_data.mimetype] = {}
    if response_data.schema:
        if type(response_data.schema) is str:
            schema_file_path = os.path.join(schema_dir, '%s.json' % response_data.schema)
            if not os.path.exists(schema_file_path):
                raise Exception('schema file %s is missing' % schema_file_path)
            with open(schema_file_path) as schema_file:
                try:
                    method_data['responses'][str(response.http_status)]['content']  [response_data.mimetype]['schema'] \
                        = filter_schema(json.load(schema_file))
                except JSONDecodeError:
                    raise Exception('schema file %s is invalid' % schema_file_path)
        else:
            method_data['responses'][str(response.http_status)]['content']  [response_data.mimetype]['schema'] \
                = response_data.schema

    if response_data.example:
        if type(response_data.example) is str:
            example_file_path = os.path.join(schema_dir, '%s.json' % response_data.example)
            if not os.path.exists(example_file_path):
                raise Exception('example file %s is missing' % example_file_path)
            with open(example_file_path) as example:
                try:
                    method_data['responses'][str(response.http_status)]['content'][response_data.mimetype]['example'] \
                        = filter_schema(json.load(example))
                except JSONDecodeError:
                    raise Exception('example file %s is invalid' % example_file_path)
        else:
            method_data['responses'][str(response.http_status)]['content'] [response_data.mimetype]['example'] \
                = response_data.example


def apply_component(component: Schema, schemas: dict, examples: dict, schema_dir: str):
    if type(component.schema) is str:
        component_file_schema_path = os.path.join(schema_dir, '%s.json' % component.schema)
        if not os.path.exists(component_file_schema_path):
            raise Exception('schema file %s is missing' % component_file_schema_path)
        with open(component_file_schema_path) as component_file:
            schemas[component.name] = filter_schema(json.load(component_file))
    elif type(component.schema) is dict:
        schemas[component.name] = component.schema
    else:
        raise Exception('invalid schema %s' % component.schema)

    if type(component.example) is not None:
        schemas[component.name]['example'] = {
            '$ref': '#/components/examples/%s/value' % component.name
        }
    if type(component.example) is str:
        component_file_example_path = os.path.join(schema_dir, '%s.json' % component.example)
        if not os.path.exists(component_file_example_path):
            raise Exception('example file %s is missing' % component_file_example_path)
        with open(component_file_example_path) as component_file:
            examples[component.name] = {
                'summary': '%s default example' % component.name,
                'value': filter_schema(json.load(component_file))
            }
    elif component.example is not None:
        examples[component.name] = {
            'summary': '%s default example' % component.name,
            'value': component.example
        }


error_response_schema = {
    'type': 'object',
    'description': 'A generic error response supporting general and validation errors.',
    'properties': {
        'error': {
            'type': 'object',
            'required': ['code'],
            'properties': {
                'code': {
                    'type': 'string',
                    'description': 'error code'
                },
                'message': {
                    'type': 'string',
                    'description': 'human readable error message'
                },
                'data': {
                    'type': 'object',
                    'description': 'details about the error',
                    'properties': {

                    }
                },
                '_debug': {
                    'type': 'object',
                    'description': 'additional debug information if application debug is true',
                    'properties': {
                        'exception': {
                            'type': 'string',
                            'description': 'exception'
                        },
                        'traceback': {
                            'type': 'string',
                            'description': 'full python exception backtrace'
                        }
                    }
                }
            }
        }
    }
}


pagination_parameters = [
    {
        'in': 'query',
        'name': 'start',
        'description': 'the offset to search',
        'schema': {
            'type': 'integer',
            'min': 0
        },
        'default': 0
    },
    {
        'in': 'query',
        'name': 'limit',
        'description': '',
        'schema': {
            'type': 'integer',
            'min': 1,
            'max': 100
        },
        'default': 10
    },
    {
        'in': 'query',
        'name': 'created_since',
        'description': '',
        'schema': {
            'type': 'string',
            'format': 'datetime'
        }
    },
    {
        'in': 'query',
        'name': 'created_until',
        'description': '',
        'schema': {
            'type': 'string',
            'format': 'datetime'
        }
    },
    {
        'in': 'query',
        'name': 'modified_since',
        'description': '',
        'schema': {
            'type': 'string',
            'format': 'datetime'
        }
    },
    {
        'in': 'query',
        'name': 'modified_until',
        'description': '',
        'schema': {
            'type': 'string',
            'format': 'datetime'
        }
    }
]


empty_response_schema = {
    '200': {
        'description': 'operation successful',
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object'
                },
                'example': {}
            }
        }
    }
}

error_schemas = {
    '400': {
        'description': 'data validation failed',
        'content': {
            'application/json': {
                'schema': {
                    "$ref": "#/components/schemas/errorResponse"
                },
                'example': {
                    'error': {
                        'code': 'validation_error',
                        'data': {

                        }
                    }
                }
            }
        }
    },
    '404': {
        'description': 'object not found',
        'content': {
            'application/json': {
                'schema': {
                    "$ref": "#/components/schemas/errorResponse"
                },
                'example': {
                    'error': {
                        'code': 'not_found'
                    }
                }
            }
        }
    }
}


def filter_schema(schema):
    for delete_key in ['$id', '$schema']:
        if delete_key in schema:
            del schema[delete_key]
    return schema
