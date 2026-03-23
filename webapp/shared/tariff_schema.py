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
    DateField,
    DateTimeField,
    EnumField,
    IntegerField,
    JsonSchema,
    NumericField,
    Reference,
    StringField,
    UriField,
)

from webapp.models.enums import TariffType

from .location_schema import (
    display_text_component,
    energy_mix_component,
    energy_source_component,
    environmental_impact_component,
)

price_component_schema = JsonSchema(
    title='PriceComponent',
    description='A price component defines the pricing of a tariff.',
    properties={
        'type': StringField(
            description='Type of tariff dimension: ENERGY, FLAT, PARKING_TIME, or TIME.',
        ),
        'price': NumericField(
            description='Price per unit (excl. VAT) for this tariff dimension.',
        ),
        'vat': NumericField(
            required=False,
            description='Applicable VAT percentage for this tariff dimension. If omitted, no VAT is applicable.',
        ),
        'step_size': IntegerField(
            required=False,
            minimum=0,
            description='Minimum amount to be billed. This unit will be billed in this step_size blocks.',
        ),
    },
)


price_component_example = {}


price_component_component = Component('PriceComponent', price_component_schema, price_component_example)


tariff_restrictions_schema = JsonSchema(
    title='TariffRestrictions',
    description='Restrictions that apply to a tariff element.',
    properties={
        'start_time': StringField(required=False, description='Start time of day in local time (HH:MM).'),
        'end_time': StringField(required=False, description='End time of day in local time (HH:MM).'),
        'start_date': DateField(required=False, description='Start date in local time (YYYY-MM-DD).'),
        'end_date': DateField(required=False, description='End date in local time (YYYY-MM-DD).'),
        'min_kwh': NumericField(required=False, description='Minimum consumed energy in kWh.'),
        'max_kwh': NumericField(required=False, description='Maximum consumed energy in kWh.'),
        'min_current': NumericField(required=False, description='Sum of the minimum current in A over all phases.'),
        'max_current': NumericField(required=False, description='Sum of the maximum current in A over all phases.'),
        'min_power': NumericField(required=False, description='Minimum power in kW.'),
        'max_power': NumericField(required=False, description='Maximum power in kW.'),
        'min_duration': IntegerField(required=False, description='Minimum duration in seconds.'),
        'max_duration': IntegerField(required=False, description='Maximum duration in seconds.'),
        'day_of_week': ArrayField(
            items=StringField(), required=False, description='Which day(s) of the week this applies to.'
        ),
    },
)


tariff_restrictions_example = {}


tariff_restrictions_component = Component('TariffRestrictions', tariff_restrictions_schema, tariff_restrictions_example)


tariff_element_schema = JsonSchema(
    title='TariffElement',
    description='A TariffElement is a group of PriceComponents that share the same restrictions.',
    properties={
        'price_components': ArrayField(
            items=Reference(obj='PriceComponent'),
            description='List of price components that make up the pricing of this tariff element.',
        ),
        'restrictions': Reference(
            obj='TariffRestrictions',
            required=False,
            description='Restrictions that describe the applicability of this tariff element.',
        ),
    },
)


tariff_element_example = {}


tariff_element_component = Component('TariffElement', tariff_element_schema, tariff_element_example)


price_schema = JsonSchema(
    title='Price',
    description='A price with and without VAT.',
    properties={
        'excl_vat': NumericField(description='Price/Cost excluding VAT.'),
        'incl_vat': NumericField(required=False, description='Price/Cost including VAT.'),
    },
)


price_example = {}


price_ocpi_component = Component('Price', price_schema, price_example)


tariff_schema = JsonSchema(
    title='Tariff',
    description='A Tariff object describes a tariff and its properties. It consists of a list of TariffElements, which in turn '
    'consist of PriceComponents.',
    properties={
        'id': StringField(maxLength=36, description='Uniquely identifies the tariff within the CPO platform.'),
        'country_code': StringField(
            minLength=2, maxLength=2, required=False, description='ISO-3166 alpha-2 country code.'
        ),
        'party_id': StringField(
            minLength=3, maxLength=3, required=False, description='ID of the CPO that owns this tariff.'
        ),
        'currency': StringField(minLength=3, maxLength=3, description='ISO-4217 code of the currency of this tariff.'),
        'type': EnumField(
            enum=TariffType,
            required=False,
            description='Defines the type of the tariff.',
        ),
        'tariff_alt_text': ArrayField(
            items=Reference(obj='DisplayText'),
            required=False,
            description='List of multi-language alternative tariff info text.',
        ),
        'tariff_alt_url': UriField(
            required=False,
            description='URL to a web page that contains an explanation of the tariff.',
        ),
        'min_price': Reference(obj='Price', required=False, description='Minimum price when using this tariff.'),
        'max_price': Reference(obj='Price', required=False, description='Maximum price when using this tariff.'),
        'elements': ArrayField(
            items=Reference(obj='TariffElement'),
            description='List of tariff elements.',
        ),
        'start_date_time': DateTimeField(required=False, description='The time when this tariff becomes active.'),
        'end_date_time': DateTimeField(
            required=False, description='The time after which this tariff is no longer valid.'
        ),
        'energy_mix': Reference(
            obj='EnergyMix', required=False, description='Details of the energy supplied with this tariff.'
        ),
        'last_updated': DateTimeField(description='Timestamp when this Tariff was last updated (or created).'),
    },
)


tariff_example = {}


tariff_component = Component('Tariff', tariff_schema, tariff_example)


all_tariff_components = [
    display_text_component,
    energy_mix_component,
    energy_source_component,
    environmental_impact_component,
    price_ocpi_component,
    price_component_component,
    tariff_component,
    tariff_element_component,
    tariff_restrictions_component,
]
