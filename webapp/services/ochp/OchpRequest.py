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

import requests
from lxml import etree, builder
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError
from flask import current_app
from ...extensions import logger
from .Helper import get_nsmap


class OchpRequestException(Exception):
    pass


def ochp_request(request_body: etree, url: str, action: str, logname: str) -> etree:
    http_headers = {'Content-Type': 'text/xml', 'SOAPAction': action}
    xml_request = etree.tostring(generate_ochp_request(request_body))
    logger.info('ochp.dump.%s' % logname, 'requesting from %s with headers %s' % (url, http_headers))
    logger.info('ochp.dump.%s' % logname, xml_request)
    try:
        result = requests.post(url, xml_request, headers=http_headers)
    except (ConnectionError, NewConnectionError) as e:
        raise OchpRequestException
    if result.status_code != 200:
        raise OchpRequestException
    logger.info('ochp.dump.%s' % logname, result.text)
    return etree.fromstring(result.text)


def generate_ochp_request(body: etree) -> etree:
    nsmap = get_nsmap('request')
    em = builder.ElementMaker(namespace=nsmap['soapenv'], nsmap=nsmap)
    document = em.Envelope(em.Header(security_header()), em.Body(body))
    return document


def security_header():
    nsmap = get_nsmap('request')
    nsmap_sec = nsmap.copy()
    nsmap_sec['wsse'] = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd'
    nsmap_user = nsmap_sec.copy()
    nsmap_user['wsu'] = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd'
    em_sec = builder.ElementMaker(namespace=nsmap_sec['wsse'], nsmap=nsmap_sec)
    em_user = builder.ElementMaker(namespace=nsmap_user['wsse'], nsmap=nsmap_user)

    username_token = em_user.UsernameToken(
        em_user.Username(current_app.config['LADENETZ_USERNAME']),
        em_user.Password(
            current_app.config['LADENETZ_PASSWORD'],
            Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText"
        )
    )
    username_token.attrib['{%s}Id' % nsmap_user['wsu']] = 'UsernameToken-1'

    result = em_sec.Security(username_token)
    result.attrib['{%s}mustUnderstand' % nsmap['soapenv']] = '1'
    return result
