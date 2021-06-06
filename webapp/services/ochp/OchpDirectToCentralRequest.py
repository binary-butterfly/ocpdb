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

from lxml import builder
from datetime import date, timedelta
from flask import current_app
from .Helper import get_nsmap, get_field
from .OchpRequest import ochp_request, OchpRequestException
from ...extensions import logger


def ochp_add_service_endpoints():
    nsmap = get_nsmap('request')
    em = builder.ElementMaker(namespace=nsmap['ns'], nsmap=nsmap)
    request_xml = em.AddServiceEndpointsRequest(
        em.providerEndpointArray(
            em.url(current_app.config['PROJECT_URL'] + '/api/ochp/update'),
            em.namespaceUrl(nsmap['ns']),
            em.accessToken(current_app.config['LADENETZ_TOKEN']),
            em.validDate(em.DateTime((date.today() + timedelta(days=2)).isoformat() + 'T00:30:00Z')),
            em.whitelist('DEGLSD%')
        )
    )
    try:
        result_xml = ochp_request(
            request_xml,
            current_app.config['LADENETZ_SERVICE_URL'],
            'AddServiceEndpoints',
            'ochp.add-service-endpoints'
        )
    except OchpRequestException:
        return
    result = result_xml.xpath(
        '//soap:Envelope/soap:Body/ns:AddServiceEndpointsResponse/ns:result',
        namespaces=get_nsmap()
    )
    result_code = get_field(result, 'resultCode/ns:ResultCode', get_nsmap())
    if result_code != 'ok':
        logger.error('ochp.add-service-endpoints', 'bad result code %s' % result_code)


def ochp_get_service_endpoints():
    nsmap = get_nsmap('request')
    em = builder.ElementMaker(namespace=nsmap['ns'], nsmap=nsmap)
    try:
        result_xml = ochp_request(
            em.GetServiceEndpointsRequest(),
            current_app.config['LADENETZ_SERVICE_URL'],
            'GetServiceEndpoints',
            'ochp.get-service-endpoints'
        )
    except OchpRequestException:
        return
    # TODO: handle results
