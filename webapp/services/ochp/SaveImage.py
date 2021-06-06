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
from wtfjson import DictInput
from typing import List, Union
from wtfjson.fields import StringField, IntegerField
from wtfjson.validators import Length, AnyOf, NumberRange, URL
from ...extensions import logger
from .Helper import get_nsmap, get_field
from ...enums import ImageCategory
from ..generic.SaveImage import ImageUpdate


image_category_mapping = {
    'networkLogo': ImageCategory.NETWORK,
    'operatorLogo': ImageCategory.OPERATOR,
    'ownerLogo': ImageCategory.OWNER,
    'stationPhoto': ImageCategory.CHARGER,
    'locationPhoto': ImageCategory.LOCATION,
    'entrancePhoto': ImageCategory.ENTRANCE,
    'otherPhoto': ImageCategory.OTHER,
    'otherLogo': ImageCategory.OTHER,
    'otherGraphic': ImageCategory.OTHER
}


def get_image_updates(data_chargepoint: etree) -> List[ImageUpdate]:
    nsmap = get_nsmap()
    image_updates = []
    for data_image in get_field(data_chargepoint, 'images', nsmap, list=True, text=False, default=[]):
        image_update = get_image_update(data_image)
        if image_update:
            image_updates.append(image_update)
    return image_updates


def get_image_update(data_connector: etree) -> Union[ImageUpdate, None]:
    image = {}
    nsmap = get_nsmap()
    image['external_url'] = get_field(data_connector, 'uri', nsmap)
    image['category'] = get_field(data_connector, 'class', nsmap)
    image['type'] = get_field(data_connector, 'type', nsmap)
    if get_field(data_connector, 'width', nsmap):
        image['width'] = get_field(data_connector, 'width', nsmap)
    if get_field(data_connector, 'height', nsmap):
        image['type'] = get_field(data_connector, 'height', nsmap)

    validator = ImageValidator(image)
    if not validator.validate():
        logger.error('ochp.chargepoint', 'invalid image found: %s' % image)
        return
    image_update = ImageUpdate()
    validator.populate_obj(image_update)
    return image_update


class ImageValidator(DictInput):
    external_url = StringField(validators=[Length(max=255), URL()])
    type = StringField(validators=[AnyOf(['gif', 'jpeg', 'png', 'svg'])])
    category = StringField(
        validators=[AnyOf(list(image_category_mapping.keys()))],
        output_filters=[lambda item: image_category_mapping.get(item)]
    )
    width = IntegerField(required=False, validators=[NumberRange(min=1)])
    height = IntegerField(required=False, validators=[NumberRange(min=1)])
