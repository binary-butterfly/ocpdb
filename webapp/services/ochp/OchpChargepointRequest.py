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
from datetime import datetime
from flask import current_app
from .Helper import get_nsmap
from .SaveChargepoint import save_chargepoints
from .OchpRequest import ochp_request, OchpRequestException
from ...models import Option
from ...common.helpers import get_now
from ...extensions import logger
from .SaveChargepointLive import save_chargepoints_live


def ochp_get_chargepoint_list():
    start = get_now()
    nsmap = get_nsmap('request')
    em = builder.ElementMaker(namespace=nsmap['ns'], nsmap=nsmap)
    try:
        result = ochp_request(
            em.GetChargePointListRequest(),
            current_app.config['LADENETZ_SERVICE_URL'],
            'http://ochp.eu/1.4/GetChargePointList',
            'ochp.get-chargepoint-list'
        )
    except OchpRequestException:
        return
    between = get_now()
    logger.info('ochp.get-chargepoint-list', 'got data in %s s' % (between - start).total_seconds())
    save_chargepoints(result)
    logger.info('ochp.get-chargepoint-list', 'stored data in %s s' % (get_now() - between).total_seconds())
    Option.set('ochp-get-chargepoint-list-last-update', start, 'datetime')


def ochp_get_chargepoint_list_update(full: bool = False):
    start = get_now()
    nsmap = get_nsmap('request')
    em = builder.ElementMaker(namespace=nsmap['ns'], nsmap=nsmap)
    last_update = datetime(2000, 1, 1) if full else Option.get('ochp-get-chargepoint-list-last-update', datetime(2000, 1, 1))
    request_xml = em.GetChargePointListUpdates(
        em.lastUpdate(
            em.DateTime(
                last_update.strftime('%Y-%m-%dT%H:%M:%SZ')
            )
        )
    )
    try:
        result = ochp_request(
            request_xml,
            current_app.config['LADENETZ_SERVICE_URL'],
            'http://ochp.eu/1.4/GetChargePointListUpdates',
            'ochp.get-chargepoint-list-update'
        )
    except OchpRequestException:
        return
    between = get_now()
    logger.info('ochp.get-chargepoint-list-update', 'got data in %s s' % (between - start).total_seconds())
    save_chargepoints(result)
    logger.info('ochp.get-chargepoint-list-update', 'stored data in %s s' % (get_now() - between).total_seconds())
    Option.set('ochp-get-chargepoint-list-last-update', start, 'datetime')


def ochp_get_status(full: bool = False):
    start = get_now()
    nsmap = get_nsmap('request')
    em = builder.ElementMaker(namespace=nsmap['ns'], nsmap=nsmap)
    last_update = Option.get('ochp-get-status-last-update')
    if last_update is None or full is True:
        request_xml = em.GetStatusRequest()
    else:
        request_xml = em.GetStatusRequest(
            em.startDateTime(
                em.DateTime(
                    last_update.strftime('%Y-%m-%dT%H:%M:%SZ')
                )
            )
        )
    try:
        result = ochp_request(
            request_xml,
            current_app.config['LADENETZ_LIVE_URL'],
            'http://ochp.e-clearing.net/service/GetStatus',
            'ochp.get-status'
        )
    except OchpRequestException:
        return
    between = get_now()
    logger.info('ochp.get-status', 'got data in %s s' % (between - start).total_seconds())
    save_chargepoints_live(result)
    logger.info('ochp.get-status', 'stored data in %s s' % (get_now() - between).total_seconds())
    Option.set('ochp-get-status-last-update', start, 'datetime')
