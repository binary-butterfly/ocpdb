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

from typing import Any
from lxml import etree


def get_nsmap(context: str = 'response', ochp_version='1.4') -> dict:
    if context == 'request':
        return {
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'ns': 'http://ochp.eu/%s' % ochp_version
        }
    return {
        'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
        'ns': 'http://ochp.eu/%s' % ochp_version
    }


def get_field(xml_data: etree, field: str, nsmap: dict, text: bool = True, default: Any = None, list: bool = False):
    results = xml_data.xpath('./ns:%s' % field, namespaces=nsmap)
    if not len(results):
        return default
    if list and text:
        return [item.text for item in results]
    if list:
        return results
    if text:
        return results[0].text
    return results[0]
