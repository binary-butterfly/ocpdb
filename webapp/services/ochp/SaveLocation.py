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

from lxml import etree
from typing import Union
from wtfjson import DictInput
from wtfjson.fields import StringField, DecimalField, DateTimeField, IntegerField, ListField, BooleanField, ObjectField
from wtfjson.validators import Length
from .Helper import get_field, get_nsmap
from ...extensions import logger
from ...enums import ParkingType, ExceptionalPeriodType
from ..generic.SaveLocation import LocationUpdate
from ..generic.SaveOpeningTimes import ExceptionalPeriodUpdate, RegularHoursUpdate


parking_type_mapping = {
    'on-street': ParkingType.ON_STREET,
    'parking-garage': ParkingType.PARKING_GARAGE,
    'underground-garage': ParkingType.UNDERGROUND_GARAGE,
    'parking-lot': ParkingType.PARKING_LOT
}

country_mapping = {
    'AFG': 'AF', 'ALB': 'AL', 'DZA': 'DZ', 'ASM': 'AS', 'AND': 'AD', 'AGO': 'AO', 'AIA': 'AI', 'ATA': 'AQ', 'ATG': 'AG',
    'ARG': 'AR', 'ARM': 'AM', 'ABW': 'AW', 'AUS': 'AU', 'AUT': 'AT', 'AZE': 'AZ', 'BHS': 'BS', 'BHR': 'BH', 'BGD': 'BD',
    'BRB': 'BB', 'BLR': 'BY', 'BEL': 'BE', 'BLZ': 'BZ', 'BEN': 'BJ', 'BMU': 'BM', 'BTN': 'BT', 'BOL': 'BO', 'BIH': 'BA',
    'BWA': 'BW', 'BVT': 'BV', 'BRA': 'BR', 'IOT': 'IO', 'BRN': 'BN', 'BGR': 'BG', 'BFA': 'BF', 'BDI': 'BI', 'KHM': 'KH',
    'CMR': 'CM', 'CAN': 'CA', 'CPV': 'CV', 'CYM': 'KY', 'CAF': 'CF', 'TCD': 'TD', 'CHL': 'CL', 'CHN': 'CN', 'CXR': 'CX',
    'CCK': 'CC', 'COL': 'CO', 'COM': 'KM', 'COG': 'CG', 'COD': 'CD', 'COK': 'CK', 'CRI': 'CR', 'CIV': 'CI', 'HRV': 'HR',
    'CUB': 'CU', 'CYP': 'CY', 'CZE': 'CZ', 'DNK': 'DK', 'DJI': 'DJ', 'DMA': 'DM', 'DOM': 'DO', 'ECU': 'EC', 'EGY': 'EG',
    'SLV': 'SV', 'GNQ': 'GQ', 'ERI': 'ER', 'EST': 'EE', 'ETH': 'ET', 'FLK': 'FK', 'FRO': 'FO', 'FJI': 'FJ', 'FIN': 'FI',
    'FRA': 'FR', 'GUF': 'GF', 'PYF': 'PF', 'ATF': 'TF', 'GAB': 'GA', 'GMB': 'GM', 'GEO': 'GE', 'DEU': 'DE', 'GHA': 'GH',
    'GIB': 'GI', 'GRC': 'GR', 'GRL': 'GL', 'GRD': 'GD', 'GLP': 'GP', 'GUM': 'GU', 'GTM': 'GT', 'GGY': 'GG', 'GIN': 'GN',
    'GNB': 'GW', 'GUY': 'GY', 'HTI': 'HT', 'HMD': 'HM', 'VAT': 'VA', 'HND': 'HN', 'HKG': 'HK', 'HUN': 'HU', 'ISL': 'IS',
    'IND': 'IN', 'IDN': 'ID', 'IRN': 'IR', 'IRQ': 'IQ', 'IRL': 'IE', 'IMN': 'IM', 'ISR': 'IL', 'ITA': 'IT', 'JAM': 'JM',
    'JPN': 'JP', 'JEY': 'JE', 'JOR': 'JO', 'KAZ': 'KZ', 'KEN': 'KE', 'KIR': 'KI', 'PRK': 'KP', 'KOR': 'KR', 'KWT': 'KW',
    'KGZ': 'KG', 'LAO': 'LA', 'LVA': 'LV', 'LBN': 'LB', 'LSO': 'LS', 'LBR': 'LR', 'LBY': 'LY', 'LIE': 'LI', 'LTU': 'LT',
    'LUX': 'LU', 'MAC': 'MO', 'MKD': 'MK', 'MDG': 'MG', 'MWI': 'MW', 'MYS': 'MY', 'MDV': 'MV', 'MLI': 'ML', 'MLT': 'MT',
    'MHL': 'MH', 'MTQ': 'MQ', 'MRT': 'MR', 'MUS': 'MU', 'MYT': 'YT', 'MEX': 'MX', 'FSM': 'FM', 'MDA': 'MD', 'MCO': 'MC',
    'MNG': 'MN', 'MNE': 'ME', 'MSR': 'MS', 'MAR': 'MA', 'MOZ': 'MZ', 'MMR': 'MM', 'NAM': 'NA', 'NRU': 'NR', 'NPL': 'NP',
    'NLD': 'NL', 'ANT': 'AN', 'NCL': 'NC', 'NZL': 'NZ', 'NIC': 'NI', 'NER': 'NE', 'NGA': 'NG', 'NIU': 'NU', 'NFK': 'NF',
    'MNP': 'MP', 'NOR': 'NO', 'OMN': 'OM', 'PAK': 'PK', 'PLW': 'PW', 'PSE': 'PS', 'PAN': 'PA', 'PNG': 'PG', 'PRY': 'PY',
    'PER': 'PE', 'PHL': 'PH', 'PCN': 'PN', 'POL': 'PL', 'PRT': 'PT', 'PRI': 'PR', 'QAT': 'QA', 'REU': 'RE', 'ROU': 'RO',
    'RUS': 'RU', 'RWA': 'RW', 'SHN': 'SH', 'KNA': 'KN', 'LCA': 'LC', 'SPM': 'PM', 'VCT': 'VC', 'WSM': 'WS', 'SMR': 'SM',
    'STP': 'ST', 'SAU': 'SA', 'SEN': 'SN', 'SRB': 'RS', 'SYC': 'SC', 'SLE': 'SL', 'SGP': 'SG', 'SVK': 'SK', 'SVN': 'SI',
    'SLB': 'SB', 'SOM': 'SO', 'ZAF': 'ZA', 'SGS': 'GS', 'SSD': 'SS', 'ESP': 'ES', 'LKA': 'LK', 'SDN': 'SD', 'SUR': 'SR',
    'SJM': 'SJ', 'SWZ': 'SZ', 'SWE': 'SE', 'CHE': 'CH', 'SYR': 'SY', 'TWN': 'TW', 'TJK': 'TJ', 'TZA': 'TZ', 'THA': 'TH',
    'TLS': 'TL', 'TGO': 'TG', 'TKL': 'TK', 'TON': 'TO', 'TTO': 'TT', 'TUN': 'TN', 'TUR': 'TR', 'TKM': 'TM', 'TCA': 'TC',
    'TUV': 'TV', 'UGA': 'UG', 'UKR': 'UA', 'ARE': 'AE', 'GBR': 'GB', 'USA': 'US', 'UMI': 'UM', 'URY': 'UY', 'UZB': 'UZ',
    'VUT': 'VU', 'VEN': 'VE', 'VNM': 'VN', 'VGB': 'VG', 'VIR': 'VI', 'WLF': 'WF', 'ESH': 'EH', 'YEM': 'YE', 'ZMB': 'ZM',
    'ZWE': 'ZW'
}


def get_location_update(data_location: etree) -> Union[LocationUpdate, None]:
    location = {
        'exceptional_openings': [],
        'exceptional_closings': [],
        'regular_hours': []
    }
    nsmap = get_nsmap()
    location['uid'] = get_field(data_location, 'locationId', nsmap)
    location['name'] = get_field(data_location, 'locationName', nsmap)
    location['last_updated'] = get_field(data_location, 'timestamp/ns:DateTime', nsmap)

    data_address = get_field(data_location, 'chargePointAddress', nsmap, text=False)
    if data_address is not None:
        location['address'] = get_field(data_address, 'address', nsmap, default='')
        if get_field(data_address, 'houseNumber', nsmap, default=''):
           location['address'] += ' ' + get_field(data_address, 'houseNumber', nsmap, default='')
        location['postal_code'] = get_field(data_address, 'zipCode', nsmap)
        location['city'] = get_field(data_address, 'city', nsmap)
        location['country'] = get_field(data_address, 'country', nsmap)

    for data_opening_times in get_field(data_location, 'openingTimes', nsmap, list=True, text=False, default=[]):
        if get_field(data_opening_times, 'twentyfourseven', nsmap) is not None:
            location['twentyfourseven'] = get_field(data_opening_times, 'twentyfourseven', nsmap).lower() == 'true'
        else:
            for data_regular_hour in get_field(data_opening_times, 'regularHours', nsmap, list=True, text=False, default=[]):
                location['regular_hours'].append({
                    'weekday': data_regular_hour.get('weekday'),
                    'period_begin': data_regular_hour.get('periodBegin'),
                    'period_end': data_regular_hour.get('periodEnd')
                })
        for exceptional_period in get_field(data_opening_times, 'exceptionalOpenings', nsmap, list=True, text=False, default=[]):
            location['exceptional_openings'].append({
                'period_begin': exceptional_period.get('periodBegin'),
                'period_end': exceptional_period.get('periodEnd')
            })
        for exceptional_period in get_field(data_opening_times, 'exceptionalClosings', nsmap, list=True, text=False, default=[]):
            location['exceptional_closings'].append({
                'period_begin': exceptional_period.get('periodBegin'),
                'period_end': exceptional_period.get('periodEnd')
            })
    latlon = get_field(data_location, 'chargePointLocation', nsmap, text=False)
    location['lat'] = latlon.get('lat', 0)
    location['lon'] = latlon.get('lon', 0)
    validator = LocationValidator(location)
    if not validator.validate():
        logger.error('ochp.chargepoint', 'invalid location found: %s - %s' % (validator.errors, location))
        return
    location_update = LocationUpdate(source='ochp', uid=validator.uid.out)
    validator.populate_obj(location_update)
    return location_update


class RegularHoursValidator(DictInput):
    weekday = IntegerField(input_filters=[lambda item: int(item)])
    period_begin = IntegerField(input_filters=[lambda item: int(item[0:2]) * 3600 + int(item[4:6]) * 60])
    period_end = IntegerField(input_filters=[lambda item: int(item[0:2]) * 3600 + int(item[4:6]) * 60])


class ExceptionalPeriodValidator(DictInput):
    period_begin = DateTimeField(localized=True)
    period_end = DateTimeField(localized=True)


class LocationValidator(DictInput):
    uid = StringField(validators=[Length(max=15)])
    name = StringField(required=False, validators=[Length(max=100)])
    address = StringField(validators=[Length(max=45)])
    postal_code = StringField(validators=[Length(max=10)])
    city = StringField(validators=[Length(max=45)])
    country = StringField(validators=[Length(min=3, max=3)], output_filters=[lambda item: country_mapping.get(item)])
    lat = DecimalField()
    lon = DecimalField()
    last_updated = DateTimeField(required=False, localized=True)
    twentyfourseven = BooleanField(required=False)
    regular_hours = ListField(ObjectField(
        RegularHoursValidator,
        output_filters=[lambda item: RegularHoursUpdate(**item)]
    ))
    exceptional_openings = ListField(ObjectField(
        ExceptionalPeriodValidator,
        output_filters=[lambda item: ExceptionalPeriodUpdate(type=ExceptionalPeriodType.opening, **item)]
    ))
    exceptional_closings = ListField(ObjectField(
        ExceptionalPeriodValidator,
        output_filters=[lambda item: ExceptionalPeriodUpdate(type=ExceptionalPeriodType.closing, **item)]
    ))

