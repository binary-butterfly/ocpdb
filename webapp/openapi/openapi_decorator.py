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

from enum import Enum
from functools import wraps
from typing import Optional, List, Any, Union, Type
from dataclasses import dataclass


class EndpointTag(Enum):
    pass


class SearchParameter:
    pass


@dataclass
class Request:
    schema: Optional[Union[str, dict]] = None
    example: Optional[Union[str, List[str], dict, List[dict]]] = None
    mimetype: str = 'application/json'


@dataclass
class ResponseData:
    schema: Optional[Union[str, dict]] = None
    example: Optional[Union[str, List[str], dict, List[dict]]] = None
    mimetype: str = 'application/json'


@dataclass
class Response:
    data: List[ResponseData]
    description: str = 'operation successful'
    http_status: int = 200


# for injecting default error responses
class ErrorResponse:
    pass


# for an empty response
class EmptyResponse:
    pass


@dataclass(init=False)
class Parameter:
    name: str
    description: Optional[str]
    schema: Optional[Union[dict, Type[int], Type[str], Type[float]]]
    example: Optional[Any]

    def __init__(
            self,
            name: str,
            description: Optional[str] = None,
            schema: Optional[Union[dict, Type[int], Type[str], Type[float]]] = None,
            example: Optional[Any] = None):
        self.name = name
        self.description = description
        if type(schema) is dict:
            self.schema = schema
        elif schema is int:
            self.schema = {'type': 'integer'}
        elif schema is str:
            self.schema = {'type': 'string'}
        elif schema is float:
            self.schema = {'type': 'float'}
        self.example = example


@dataclass
class Schema:
    name: str
    schema: Union[str, dict]
    example: Optional[Union[str, dict]] = None


class EndpointDocumentation:
    summary: Optional[str]
    description: Optional[str]
    basic_auth: Optional[bool]
    tags: List[Enum]
    query: List[Parameter]
    path: List[Parameter]
    request: List[Request]
    response: List[Union[Response, ErrorResponse, EmptyResponse]]

    def __init__(
            self,
            summary: Optional[str] = None,
            description: Optional[str] = None,
            basic_auth: Optional[bool] = None,
            tags: List[Enum] = None,
            query: Optional[Union[Union[Parameter, SearchParameter], List[Union[Parameter, SearchParameter]]]] = None,
            path: Optional[Union[Parameter, List[Parameter]]] = None,
            request: Optional[Union[Request, List[Request]]] = None,
            response: Optional[List[Union[Response, ErrorResponse]]] = None,
            components: Optional[List[Schema]] = None):
        self.summary = summary
        self.description = description
        self.basic_auth = basic_auth
        self.tags = [] if tags is None else tags
        self.query = [] if query is None else (query if type(query) is list else [query])
        self.path = [] if path is None else (path if type(path) is list else [path])
        self.request = [] if request is None else (request if type(request) is list else [request])
        self.response = [] if response is None else (response if type(response) is list else [response])
        self.components = [] if components is None else (components if type(components) is list else[components])


def document(
        summary: Optional[str] = None,
        description: Optional[str] = None,
        basic_auth: Optional[bool] = None,
        tags: List[Enum] = None,
        query: Optional[Union[Union[Parameter, SearchParameter], List[Union[Parameter, SearchParameter]]]] = None,
        path: Optional[List[Parameter]] = None,
        request: Optional[Union[Request, List[Request]]] = None,
        response: Optional[List[Union[Response, ErrorResponse]]] = None,
        components: Optional[List[Schema]] = None):
    def wrapped(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            return func(*args, **kwargs)
        wrapped_function.documentation = EndpointDocumentation(
            summary=summary,
            description=description,
            basic_auth=basic_auth,
            tags=tags,
            query=query,
            path=path,
            request=request,
            response=response,
            components=components
        )
        return wrapped_function

    return wrapped
