"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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
from pathlib import Path

from validataclass.validators import DataclassValidator

from webapp.services.import_services.datex2.v3_5.base_datex2_v3_5_import_service import BaseDatex2V35ImportService
from webapp.services.import_services.datex2.v3_5.datex2_v3_5_json_static_mapper import Datex2V35JSONStaticMapper
from webapp.shared.datex2.models import MessageContainerWrapperInput, ProtocolTypeEnum
from webapp.shared.datex2.v3_5_json_static.models.location_reference_g_input import LocationReferenceGInput

REALTIME_DATA_PATH = Path(
    Path(__file__).parents[4],
    'integration',
    'services',
    'import_services',
    'datex2',
    'data',
    'datex2_enbw_realtime_reduced.json',
)


def _load_realtime_data() -> dict:
    with REALTIME_DATA_PATH.open() as realtime_file:
        return json.load(realtime_file)


def test_location_reference_without_facility_location() -> None:
    location_reference = DataclassValidator(LocationReferenceGInput).validate({
        'locPointLocation': {'pointByCoordinates': {'pointCoordinates': {'latitude': 47.67, 'longitude': 9.14}}},
    })

    assert Datex2V35JSONStaticMapper._get_facility_location_by_location_reference(location_reference) is None


def test_message_container_with_empty_extensions() -> None:
    data = _load_realtime_data()
    data['messageContainer']['exchangeInformation']['dynamicInformation']['exDynamicInformationExtensionG'] = {}

    message_container = DataclassValidator(MessageContainerWrapperInput).validate(data)

    assert message_container.messageContainer.exchangeInformation.dynamicInformation is not None


def test_wrap_realtime_payload_wraps_d2_payload() -> None:
    payload = _load_realtime_data()['messageContainer']['payload'][0]

    data = BaseDatex2V35ImportService.wrap_realtime_payload({'payload': payload})
    message_container = DataclassValidator(MessageContainerWrapperInput).validate(data)

    assert len(message_container.messageContainer.payload) == 1
    exchange_context = message_container.messageContainer.exchangeInformation.exchangeContext
    assert exchange_context.codedExchangeProtocol.value is ProtocolTypeEnum.SNAPSHOT_PULL


def test_wrap_realtime_payload_keeps_other_documents() -> None:
    message_container_data = _load_realtime_data()
    payload = message_container_data['messageContainer']['payload']
    # A payload list beside exchange information is neither a D2Payload nor a MessageContainer document
    invalid_data = {'payload': payload, 'exchangeInformation': message_container_data['messageContainer']}

    assert BaseDatex2V35ImportService.wrap_realtime_payload(message_container_data) is message_container_data
    assert BaseDatex2V35ImportService.wrap_realtime_payload(invalid_data) is invalid_data
    assert BaseDatex2V35ImportService.wrap_realtime_payload({'payload': payload}) == {'payload': payload}
