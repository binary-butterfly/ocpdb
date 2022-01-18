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


import json
from lxml import etree
from flask import make_response
from .misc import DefaultJSONEncoder


def xml_response(xml_tree):
    response = make_response(etree.tostring(xml_tree, pretty_print=False))
    response.mimetype = 'text/xml'
    return response


def protobuf_response(data: bytes):
    response = make_response(data)
    response.headers['Content-Type'] = 'application/x-protobuf'
    return response
