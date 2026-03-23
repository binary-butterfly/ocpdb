"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2023 binary butterfly GmbH

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

from flask_openapi.decorator import Schema as Component
from flask_openapi.schema import ArrayField, DateTimeField, EnumField, JsonSchema, Reference, StringField

from webapp.models.charging_station import Capability
from webapp.models.evse import EvseStatus, ParkingRestriction, PresenceStatus

from .connector_schema import connector_component
from .location_schema import geo_location_component, image_component

evse_schema = JsonSchema(
    title='EVSE',
    description='The EVSE object describes the part that controls the power supply to a single EV in a single session. It always belongs '
    'to a Location object. The object only contains directions to get from the location itself to the EVSE (i.e. floor, '
    'physical_reference or directions). When the directional properties of an EVSE are insufficient to reach the EVSE from '
    'the Location point, then it typically indicates that the EVSE should be put in a different Location object (sometimes '
    'with the same address but with different coordinates/directions). An EVSE object has a list of Connectors which can not '
    'be used simultaneously: only one connector per EVSE can be used at the time.',
    properties={
        'uid': StringField(
            maxLength=36,
            description='Uniquely identifies the EVSE within the CPOs platform (and suboperator platforms). This field can never be '
            "changed, modified or renamed. This is the 'technical' identification of the EVSE, not to be used as 'human "
            "readable' identification, use the field evse_id for that. This field is named uid instead of id, because id "
            'could be confused with evse_id which is an eMI3 defined field. Note that in order to fulfill both the requirement '
            "that an EVSE's uid be unique within a CPO's platform and the requirement that EVSEs are never deleted, a CPO will "
            'typically want to avoid using identifiers of the physical hardware for this uid property. If they do use such a '
            'physical identifier, they will find themselves breaking the uniqueness requirement for uid when the same physical '
            'EVSE is redeployed at another Location.',
        ),
        'evse_id': StringField(
            maxLength=48,
            required=False,
            description='Compliant with the following specification for EVSE ID from "eMI3 standard version V1.0" '
            '(http://emi3group.com/documents-links/) "Part 2: business objects." Optional because: if an evse_id is to be '
            're-used in the real world, the evse_id can be removed from an EVSE object if the status is set to REMOVED.',
        ),
        'status': EnumField(enum=EvseStatus, description='Indicates the current status of the EVSE.'),
        'presence': EnumField(
            enum=PresenceStatus,
            required=False,
            description='Indicates whether the EVSE is physically present, planned, or removed.',
        ),
        'status_schedule': ArrayField(
            items=Reference(obj='StatusSchedule'),
            required=False,
            description='Indicates a planned status update of the EVSE.',
        ),
        'capabilities': ArrayField(
            items=EnumField(enum=Capability),
            required=False,
            description='List of functionalities that the EVSE is capable of.',
        ),
        'connectors': ArrayField(
            items=Reference(obj='Connector'),
            minItems=1,
            description='List of available connectors on the EVSE.',
        ),
        'floor_level': StringField(
            maxLength=4,
            description='Level on which the Charge Point is located (in garage buildings) in the locally displayed numbering scheme.',
            required=False,
        ),
        'physical_reference': StringField(
            maxLength=16,
            required=False,
            description='A number/string printed on the outside of the EVSE for visual identification.',
        ),
        'parking_restrictions': ArrayField(
            items=EnumField(enum=ParkingRestriction),
            required=False,
            description='The restrictions that apply to the parking spot.',
        ),
        'images': ArrayField(
            items=Reference(obj='Image'),
            required=False,
            description='Links to images related to the EVSE such as photos or logos.',
        ),
        'last_updated': DateTimeField(
            description='Timestamp when this EVSE or one of its Connectors was last updated (or created).',
        ),
    },
)


evse_example = {}


evse_component = Component('EVSE', evse_schema, evse_example)


all_evse_components = [
    connector_component,
    evse_component,
    geo_location_component,
    image_component,
]
