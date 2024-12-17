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

from datetime import datetime
from typing import List, Optional

from lxml import builder, etree
from lxml.etree import XMLSyntaxError
from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.config import ConfigHelper
from webapp.common.remote_helper import RemoteHelper, RemoteServerType

from .ochp_helper import xml_to_dict
from .ochp_validators import GetChargePointListInput, GetStatusEnvelopeInput


class OchpApiClient:
    config_helper: ConfigHelper
    remote_helper: RemoteHelper
    request_nsmap = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'ns': 'http://ochp.eu/1.4',
    }
    get_charge_point_list_validator = DataclassValidator(GetChargePointListInput)
    get_status_validator = DataclassValidator(GetStatusEnvelopeInput)

    def __init__(self, config_helper: ConfigHelper, remote_helper: RemoteHelper):
        self.config_helper = config_helper
        self.remote_helper = remote_helper

    def download_base_data(self) -> List[dict]:
        em = builder.ElementMaker(namespace=self.request_nsmap['ns'], nsmap=self.request_nsmap)
        input_xml = self.ochp_request(
            path='/service/ochp/v1.4',
            request_data=em.GetChargePointListRequest(),
            action='http://ochp.eu/1.4/GetChargePointList',
        )
        input_dict = xml_to_dict(
            tag=input_xml,
            ensure_array_keys=[
                ('GetChargePointListResponse', 'chargePointInfoArray'),
                ('chargePointInfoArray', 'relatedResource'),
                ('chargePointInfoArray', 'images'),
                ('chargePointInfoArray', 'statusSchedule'),
                ('chargePointInfoArray', 'parkingSpot'),
                ('chargePointInfoArray', 'restriction'),
                ('chargePointInfoArray', 'authMethods'),
                ('chargePointInfoArray', 'connectors'),
                ('chargePointInfoArray', 'relatedLocation'),
                ('chargePointInfoArray', 'userInterfaceLang'),
                ('openingTimes', 'regularHours'),
                ('openingTimes', 'exceptionalOpenings'),
                ('openingTimes', 'exceptionalClosings'),
                ('parkingSpot', 'restriction'),
                ('relatedResource', 'class_'),
            ],
            remote_type_tags=[
                'DateTime',
                'ConnectorStandard',
                'ConnectorFormat',
                'RestrictionType',
                'ChargePointStatusType',
                'GeneralLocationType',
                'AuthMethodType',
            ],
        )
        result: GetChargePointListInput = self.get_charge_point_list_validator.validate(input_dict)

        return result.Envelope.Body.GetChargePointListResponse.chargePointInfoArray

    def download_live_data(self, last_update: Optional[datetime] = None) -> List[dict]:
        em = builder.ElementMaker(namespace=self.request_nsmap['ns'], nsmap=self.request_nsmap)
        input_xml = self.ochp_request(
            path='/live/ochp/v1.4',
            request_data=em.GetStatusRequest(
                *(
                    []
                    if last_update is None
                    else [em.startDateTime(em.DateTime(last_update.strftime('%Y-%m-%dT%H:%M:%SZ')))]
                ),
            ),
            action='http://ochp.e-clearing.net/service/GetStatus',
        )
        input_dict = xml_to_dict(
            tag=input_xml,
            ensure_array_keys=[
                ('GetStatusResponse', 'evse'),
            ],
            remote_type_tags=[],
        )
        input_data: GetStatusEnvelopeInput = self.get_status_validator.validate(input_dict)

        return input_data.Envelope.Body.GetStatusResponse.evse

    def ochp_request(self, path: str, request_data: etree, action: str) -> etree.Element:
        request_nsmap = {
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'ns': 'http://ochp.eu/1.4',
        }
        em = builder.ElementMaker(namespace=request_nsmap['soapenv'], nsmap=request_nsmap)
        request_xml = em.Envelope(
            em.Header(self.get_security_header()),
            em.Body(request_data),
        )
        result = self.remote_helper.post(
            url=self.config_helper.get('REMOTE_SERVERS')[RemoteServerType.LADENETZ].url,
            path=path,
            data=etree.tostring(request_xml).decode(),
            headers={'content-type': 'text/xml', 'SOAPAction': action},
            raw=True,
        )
        try:
            return etree.fromstring(result.decode('latin-1'))  # noqa: S320
        except XMLSyntaxError:
            raise ValidationError(code='invalid_xml', reason='Invalid XML')

    def get_security_header(self):
        nsmap_sec = {
            'wsse': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd',
            **self.request_nsmap,
        }
        nsmap_user = {
            'wsu': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd',
            **nsmap_sec,
        }
        em_sec = builder.ElementMaker(namespace=nsmap_sec['wsse'], nsmap=nsmap_sec)
        em_user = builder.ElementMaker(namespace=nsmap_user['wsse'], nsmap=nsmap_user)

        username_token = em_user.UsernameToken(
            em_user.Username(self.config_helper.get('REMOTE_SERVERS')[RemoteServerType.LADENETZ].user),
            em_user.Password(
                self.config_helper.get('REMOTE_SERVERS')[RemoteServerType.LADENETZ].password,
                Type='http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText',
            ),
        )
        username_token.attrib['{%s}Id' % nsmap_user['wsu']] = 'UsernameToken-1'

        result = em_sec.Security(username_token)
        result.attrib['{%s}mustUnderstand' % self.request_nsmap['soapenv']] = '1'
        return result
