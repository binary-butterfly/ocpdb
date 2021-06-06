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

import os
import json
from flask import Blueprint, current_app, render_template, jsonify
from ..extensions import api_documentation
from .ApiDocumentation import EndpointTag, filter_schema, encapsulate_response

api_documentation_blueprint = Blueprint('api_documentation', __name__, template_folder='templates')


@api_documentation_blueprint.route('/documentation')
def documentation():
    return render_template('documentation.html')


@api_documentation_blueprint.route('/api/documentation/openapi.json')
def api_documentation_swagger():
    paths = {}
    for endpoint in api_documentation.data():
        if endpoint.path not in paths:
            paths[endpoint.path] = {}
        for method in endpoint.methods:
            if method not in paths[endpoint.path]:
                paths[endpoint.path][method] = {
                    'summary': endpoint.summary,
                    'description': endpoint.description,
                    'tags': [tag.name for tag in endpoint.tags],
                    'parameters': [{'in': 'query', **arg} for arg in endpoint.args]
                                  + [{'in': 'path', 'required': True, **arg} for arg in endpoint.path_params],
                    'responses': {
                        '200': {
                            'description': 'response'
                        }
                    }
                }
                if method == 'post' and endpoint.request_schema:
                    paths[endpoint.path][method]['requestBody'] = {
                        'required': True,
                        'content': {}
                    }
                    for mimetype, schema in endpoint.request_schema.items():
                        if type(schema) not in [str, dict]:
                            raise Exception('not implemented')
                        if type(schema) == dict:
                            paths[endpoint.path][method]['requestBody']['content'][mimetype] = {
                                'schema': filter_schema(schema)
                            }
                            continue
                        if not(os.path.exists(schema)):
                            raise Exception('request schema file not found')
                        with open(schema) as request_schema:
                            paths[endpoint.path][method]['requestBody']['content'][mimetype] = {
                                'schema': filter_schema(json.load(request_schema))
                            }

                if endpoint.response_schema:
                    paths[endpoint.path][method]['responses']['200']['content'] = {}
                    for mimetype, schema in endpoint.response_schema.items():
                        if type(schema) not in [str, dict]:
                            raise Exception('not implemented')
                        if type(schema) == dict:
                            paths[endpoint.path][method]['responses']['200']['content'][mimetype] = {
                                'schema': encapsulate_response(filter_schema(schema), mimetype)
                            }
                            continue
                        if not(os.path.exists(schema)):
                            raise Exception('response schema file not found')
                        with open(schema) as response_schema:
                            paths[endpoint.path][method]['responses']['200']['content'][mimetype] = {
                                'schema': encapsulate_response(filter_schema(json.load(response_schema)), mimetype)
                            }

                if endpoint.basic_auth:
                    paths[endpoint.path][method]['security'] = [{
                        'basicAuth': []
                    }]

    return jsonify({
        'openapi': '3.0.3',
        'info': {
            'title': 'Chargepoint API',
            'description': 'Chargepoint API',
            'version': current_app.config['PROJECT_VERSION'],
            'termsOfService': current_app.config['OPENAPI_TOS'],
            'contact': {
                'email': current_app.config['OPENAPI_CONTACT_MAIL']
            },
            'license': {
                'name': 'CC-BY-3.0',
                'url': 'https://creativecommons.org/licenses/by/3.0/de/'
            },
        },
        'servers': current_app.config['OPENAPI_SERVERS'],
        'tags': [{'name': name, 'description': enum.value} for name, enum in EndpointTag.__members__.items()],
        'components': {
            'securitySchemes': {
                'basicAuth': {
                    'type': 'http',
                    'scheme': 'basic'
                }
            }
        },
        'paths': paths
    })
