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
from flask_openapi.schema import (
    ArrayField,
    BooleanField,
    DateTimeField,
    DecimalField,
    EnumField,
    IntegerField,
    JsonSchema,
    NumericField,
    Reference,
    RegexpField,
    StringField,
    UriField,
)

from webapp.models.enums import ChargingRateUnit
from webapp.models.evse import EvseStatus
from webapp.models.image import ImageCategory
from webapp.models.location import EnergySourceCategory, EnvironmentalImpactCategory, Facility, ParkingType, TokenType

additional_geo_location_schema = JsonSchema(
    title='AdditionalGeoLocation',
    description='This class defines an additional geo location that is relevant for the Charge Point. The geodetic system to be used is '
    'WGS 84.',
    properties={
        'latitude': DecimalField(
            precision=9,
            scale=7,
            description='Latitude of the point in decimal degree. Example: 50.770774. Decimal separator: "." '
            r'Regex: -?[0-9]{1,2}\.[0-9]{5,7}',
        ),
        'longitude': DecimalField(
            precision=10,
            scale=7,
            description='Longitude of the point in decimal degree. Example: -126.104965. Decimal separator: "." '
            r'Regex: -?[0-9]{1,3}\.[0-9]{5,7},',
        ),
        'name': Reference(
            obj='DisplayText',
            required=False,
            description='Name of the point in local language or as written at the location. For example the street name of a parking lot '
            "entrance or it's number.",
        ),
    },
)


additional_geo_location_example = {}


additional_geo_location_component = Component(
    'AdditionalGeoLocation', additional_geo_location_schema, additional_geo_location_example
)


business_details_schema = JsonSchema(
    title='BusinessDetails',
    properties={
        'name': StringField(maxLength=100, description='Name of the operator.'),
        'website': UriField(required=False, description="Link to the operator's website."),
        'logo': Reference(obj='Image', required=False, description="Image link to the operator's logo."),
    },
)


business_details_example = {}


business_details_component = Component('BusinessDetails', business_details_schema, business_details_example)


display_text_schema = JsonSchema(
    title='DisplayText',
    properties={
        'language': StringField(minLength=2, maxLength=2, description='Language Code ISO 639-1.'),
        'text': StringField(
            maxLength=512,
            description='Text to be displayed to a end user. No markup, html etc. allowed.',
        ),
    },
)


display_text_example = {}


display_text_component = Component('DisplayText', display_text_schema, display_text_example)


energy_mix_schema = JsonSchema(
    title='EnergyMix',
    description='This type is used to specify the energy mix and environmental impact of the supplied energy at a location or in a tariff.',
    properties={
        'is_green_energy': BooleanField(
            description='True if 100% from regenerative sources. (CO2 and nuclear waste is zero)',
        ),
        'energy_sources': ArrayField(
            items=Reference(obj='EnergySource'),
            required=False,
            description="Key-value pairs (enum + percentage) of energy sources of this location's tariff.",
        ),
        'environ_impact': ArrayField(
            items=Reference(obj='EnvironmentalImpact'),
            required=False,
            description="Key-value pairs (enum + percentage) of nuclear waste and CO2 exhaust of this location's tariff.",
        ),
        'supplier_name': StringField(
            maxLength=64,
            required=False,
            description='Name of the energy supplier, delivering the energy for this location or tariff.*',
        ),
        'energy_product_name': StringField(
            maxLength=64,
            required=False,
            description='Name of the energy suppliers product/tariff plan used at this location.*',
        ),
    },
)


energy_mix_example = {}


energy_mix_component = Component('EnergyMix', energy_mix_schema, energy_mix_example)


energy_source_schema = JsonSchema(
    title='EnergySource',
    description='Key-value pairs (enum + percentage) of energy sources. All given values of all categories should add up to 100 percent.',
    properties={
        'source': EnumField(enum=EnergySourceCategory, description='The type of energy source.'),
        'percentage': NumericField(description='Percentage of this source (0-100) in the mix.'),
    },
)


energy_source_example = {}


energy_source_component = Component('EnergySource', energy_source_schema, energy_source_example)


environmental_impact_schema = JsonSchema(
    title='EnvironmentalImpact',
    description='Amount of waste produced/emitted per kWh.',
    properties={
        'category': EnumField(
            enum=EnvironmentalImpactCategory,
            description='The environmental impact category of this value.',
        ),
        'amount': NumericField(description='Amount of this portion in g/kWh.'),
    },
)


environmental_impact_example = {}


environmental_impact_component = Component(
    'EnvironmentalImpact', environmental_impact_schema, environmental_impact_example
)


exceptional_period_schema = JsonSchema(
    title='ExceptionalPeriod',
    description='Specifies one exceptional period for opening or access hours.',
    properties={
        'period_begin': DateTimeField(
            description='Begin of the exception. In UTC, time_zone field can be used to convert to local time.',
        ),
        'period_end': DateTimeField(
            description='End of the exception. In UTC, time_zone field can be used to convert to local time.',
        ),
    },
)


exceptional_period_example = {}


exceptional_period_component = Component('ExceptionalPeriod', exceptional_period_schema, exceptional_period_example)


geo_location_schema = JsonSchema(
    title='GeoLocation',
    description='This class defines the geo location of the Charge Point. The geodetic system to be used is WGS 84.',
    properties={
        'latitude': DecimalField(
            precision=9,
            scale=7,
            description='Latitude of the point in decimal degree. Example: 50.770774. Decimal separator: "." '
            r'Regex: -?[0-9]{1,2}\.[0-9]{5,7}',
        ),
        'longitude': DecimalField(
            precision=10,
            scale=7,
            description='Longitude of the point in decimal degree. Example: -126.104965. Decimal separator: "." '
            r'Regex: -?[0-9]{1,3}\.[0-9]{5,7},',
        ),
    },
)


geo_location_example = {}


geo_location_component = Component('GeoLocation', geo_location_schema, geo_location_example)


hours_schema = JsonSchema(
    title='Hours',
    description='Opening and access hours of the location.',
    properties={
        'twentyfourseven': BooleanField(
            description='True to represent 24 hours a day and 7 days a week, except the given exceptions.',
        ),
        'regular_hours': ArrayField(
            items=Reference(obj='RegularHours'),
            required=False,
            description='Regular hours, weekday-based. Only to be used if twentyfourseven=false, then this field needs to contain at least '
            'one RegularHours object.',
        ),
        'exceptional_openings': ArrayField(
            items=Reference(obj='ExceptionalPeriod'),
            required=False,
            description='Exceptions for specified calendar dates, time-range based. Periods the station is operating/accessible. '
            'Additional to regular_hours. May overlap regular rules.',
        ),
        'exceptional_closings': ArrayField(
            items=Reference(obj='ExceptionalPeriod'),
            required=False,
            description='Exceptions for specified calendar dates, time-range based. Periods the station is not operating/accessible. '
            'Overwriting regular_hours and exceptional_openings. Should not overlap exceptional_openings.',
        ),
    },
)


hours_example = {}


hours_component = Component('Hours', hours_schema, hours_example)


image_schema = JsonSchema(
    title='Image',
    description='This class references an image related to an EVSE in terms of a file name or url. According to the roaming connection '
    'between one EVSE Operator and one or more Navigation Service Providers, the hosting or file exchange of image payload '
    'data has to be defined. The exchange of this content data is out of scope of OCPI. However, the recommended setup is a '
    'public available web server hosted and updated by the EVSE Operator. Per charge point an unlimited number of images of '
    'each type is allowed. Recommended are at least two images where one is a network or provider logo and the second is a '
    'station photo. If two images of the same type are defined, not only one should be selected but both should be displayed '
    'together. Photo Dimensions: The recommended dimensions for all photos is a minimum width of 800 pixels and a minimum '
    'height of 600 pixels. Thumbnail should always have the same orientation as the original photo with a size of 200 by '
    '200 pixels. Logo Dimensions: The recommended dimensions for logos are exactly 512 pixels in width height. Thumbnail '
    'representations of logos should be exactly 128 pixels in width and height. If not squared, thumbnails should have the '
    'same orientation as the original.',
    properties={
        'url': UriField(description='URL from where the image data can be fetched through a web browser.'),
        'thumbnail': UriField(
            required=False,
            description='URL from where a thumbnail of the image can be fetched through a webbrowser.',
        ),
        'category': EnumField(enum=ImageCategory, description='Describes what the image is used for.'),
        'type': StringField(maxLength=4, description='Image type like: gif, jpeg, png, svg.'),
        'width': IntegerField(minimum=0, maximum=99999, description='Width of the full scale image.'),
        'height': IntegerField(minimum=0, maximum=99999, description='Height of the full scale image.'),
    },
)


image_example = {}


image_component = Component('Image', image_schema, image_example)


max_power_schema = JsonSchema(
    title='MaxPower',
    description='Maximum power of a Location or ChargingStation.',
    properties={
        'unit': EnumField(
            enum=ChargingRateUnit,
            required=False,
            description='Unit of the maximum power value.',
        ),
        'value': NumericField(
            required=False,
            description='Maximum power value.',
        ),
    },
)


max_power_example = {
    'unit': 'KW',
    'value': 150,
}


max_power_component = Component('MaxPower', max_power_schema, max_power_example)


location_schema = JsonSchema(
    title='Location',
    description='The Location object describes the location and its properties where a group of EVSEs that belong together are installed. '
    'Typically, the Location object is the exact location of the group of EVSEs, but it can also be the entrance of a parking '
    'garage which contains these EVSEs. The exact way to reach each EVSE can be further specified by its own properties.',
    properties={
        'country_code': StringField(
            minLength=3,
            maxLength=3,
            description="ISO-3166 alpha-3 country code of the CPO that 'owns' this Location.\n*In OCPI, this field is required. Most sources don't have it, though, so we cannot output it in OCPDB.*",
            required=False,
        ),
        'party_id': StringField(
            minLength=3,
            maxLength=3,
            description="ID of the CPO that 'owns' this Location (following the ISO-15118 standard).\n*In OCPI, this field is required. Most sources don't have it, though, so we cannot output it in OCPDB.*",
            required=False,
        ),
        'id': StringField(
            maxLength=36,
            description='Unique internal ID which identifies the location.',
        ),
        'publish': BooleanField(
            description='Defines if a Location may be published on an website or app etc. When this is set to false, only tokens '
            'identified in the field: publish_allowed_to are allowed to be shown this Location. When the same location has '
            "EVSEs that may be published and may not be published, two 'Locations' should be created.",
        ),
        'publish_allowed_to': ArrayField(
            items=Reference(obj='PublishTokenType'),
            required=False,
            description='This field may only be used when the publish field is set to false. Only owners of Tokens that match all the set '
            'fields of one PublishToken in the list are allowed to be shown this location.',
        ),
        'name': StringField(maxLength=255, required=False, description='Display name of the location.'),
        'address': StringField(maxLength=45, description='Street/block name and house number if available.'),
        'city': StringField(maxLength=45, description='City or town.'),
        'postal_code': StringField(
            maxLength=10,
            required=False,
            description='Postal code of the location, may only be omitted when the location has no postal code: in some countries charging '
            "locations at highways don't have postal codes.",
        ),
        'state': StringField(
            maxLength=20,
            required=False,
            description='State or province of the location, only to be used when relevant.',
        ),
        'country': StringField(
            minLength=3,
            maxLength=3,
            description='ISO 3166-1 alpha-3 code for the country of this location.',
        ),
        'coordinates': Reference(obj='GeoLocation', description='Coordinates of the location.'),
        'related_locations': ArrayField(
            items=Reference(obj='AdditionalGeoLocation'),
            required=False,
            description='Geographical location of related points relevant to the user.',
        ),
        'parking_type': EnumField(
            enum=ParkingType,
            required=False,
            description='The general type of parking at the charge point location.',
        ),
        'evses': ArrayField(
            items=Reference(obj='EVSE'),
            required=False,
            description='List of EVSEs that belong to this Location.',
        ),
        'directions': ArrayField(
            items=Reference(obj='DisplayText'),
            required=False,
            description='Human-readable directions on how to reach the location.',
        ),
        'operator': Reference(
            obj='BusinessDetails',
            required=False,
            description='Information of the operator. When not specified, the information retrieved from the Credentials module, selected '
            'by the country_code and party_id of this Location, should be used instead.',
        ),
        'sub_operator': Reference(
            obj='BusinessDetails',
            required=False,
            description='Information of the suboperator if available.',
        ),
        'owner': Reference(obj='BusinessDetails', required=False, description='Information of the owner if available.'),
        'facilities': ArrayField(
            items=EnumField(enum=Facility),
            required=False,
            description='Optional list of facilities this charging location directly belongs to.',
        ),
        'time_zone': StringField(
            maxLength=255,
            description='One of IANA tzdata\'s TZ-values representing the time zone of the location. Examples: "Europe/Oslo", '
            '"Europe/Zurich". (http://www.iana.org/time-zones)',
        ),
        'opening_times': Reference(
            obj='Hours',
            required=False,
            description='The times when the EVSEs at the location can be accessed for charging.',
        ),
        'charging_when_closed': BooleanField(
            required=False,
            default=True,
            description='Indicates if the EVSEs are still charging outside the opening hours of the location. E.g. when the parking garage '
            'closes its barriers over night, is it allowed to charge till the next morning? Default: true',
        ),
        'images': ArrayField(
            items=Reference(obj='Image'),
            required=False,
            description='Links to images related to the location such as photos or logos.',
        ),
        'energy_mix': Reference(
            obj='EnergyMix',
            required=False,
            description='Details on the energy supplied at this location.',
        ),
        'max_power': Reference(
            obj='MaxPower',
            required=False,
            description='Maximum power available at this location.',
        ),
        'last_updated': DateTimeField(
            description='Timestamp when this Location or one of its EVSEs or Connectors were last updated (or created).',
        ),
        'official_region_code': StringField(
            maxLength=36,
            required=False,
            description='Official region code. In Germany Regionalschlüssel.',
        ),
    },
)


publish_token_type_schema = JsonSchema(
    title='PublishTokenType',
    description='Defines the set of values that identify a token to which a Location might be published. At least one of the following '
    'fields SHALL be set: uid, visual_number, or group_id. When uid is set, type SHALL also be set. When visual_number is '
    'set, issuer SHALL also be set.',
    properties={
        'uid': StringField(
            maxLength=36,
            required=False,
            description='Unique ID by which this Token can be identified.',
        ),
        'type': EnumField(enum=TokenType, required=False, description='Type of the token.'),
        'visual_number': StringField(
            maxLength=64,
            required=False,
            description='Visual readable number/identification as printed on the Token (RFID card).',
        ),
        'issuer': StringField(
            maxLength=64,
            required=False,
            description='Issuing company, most of the times the name of the company printed on the token (RFID card), not necessarily the '
            'eMSP.',
        ),
        'group_id': StringField(
            maxLength=36,
            required=False,
            description='This ID groups a couple of tokens. This can be used to make two or more tokens work as one.',
        ),
    },
)


publish_token_type_example = {}


publish_token_type_component = Component('PublishTokenType', publish_token_type_schema, publish_token_type_example)


regular_hours_schema = JsonSchema(
    title='RegularHours',
    description='Regular recurring operation or access hours.',
    properties={
        'weekday': IntegerField(
            minimum=1,
            maximum=7,
            description='Number of day in the week, from Monday (1) till Sunday (7)',
        ),
        'period_begin': RegexpField(
            pattern='([0-1][0-9]|2[0-3]):[0-5][0-9]',
            description='Begin of the regular period, in local time, given in hours and minutes. Must be in 24h format with leading zeros. '
            'Example: "18:15". Hour/Minute separator: ":" Regex: ([0-1][0-9]|2[0-3]):[0-5][0-9].',
        ),
        'period_end': RegexpField(
            pattern='([0-1][0-9]|2[0-3]):[0-5][0-9]',
            description='End of the regular period, in local time, syntax as for period_begin. Must be later than period_begin.',
        ),
    },
)


regular_hours_example = {}


regular_hours_component = Component('RegularHours', regular_hours_schema, regular_hours_example)


status_schedule_schema = JsonSchema(
    title='StatusSchedule',
    description='This type is used to schedule status periods in the future. The eMSP can provide this information to '
    'the EV user for trip planning purposes. A period MAY have no end. Example: "This station will be '
    'running as of tomorrow. Today it is still planned and under construction."',
    properties={
        'period_begin': DateTimeField(
            description='Begin of the scheduled period.',
        ),
        'period_end': DateTimeField(
            description='Status value during the scheduled period.',
        ),
        'status': EnumField(
            enum=EvseStatus,
            description='Status value during the scheduled period.',
        ),
    },
)


status_schedule_example = {}

status_schedule_component = Component('StatusSchedule', status_schedule_schema, status_schedule_example)


all_business_components = [
    business_details_component,
    image_component,
]
