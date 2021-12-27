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

import os
import requests
from datetime import datetime
from typing import List, Optional
from dataclasses import dataclass, asdict
from validataclass.helpers import OptionalUnsetNone, UnsetValue
from webapp.models import Image, Chargepoint
from webapp.extensions import logger, db
from webapp.enums import ImageCategory
from webapp.common.helpers import get_now_localized


@dataclass
class ImageUpdate:
    external_url: OptionalUnsetNone[str] = UnsetValue
    type: OptionalUnsetNone[str] = UnsetValue
    category: OptionalUnsetNone[ImageCategory] = UnsetValue
    width: OptionalUnsetNone[int] = UnsetValue
    height: OptionalUnsetNone[int] = UnsetValue


def upsert_images(
        image_updates: List[ImageUpdate],
        chargepoint: Chargepoint,
        download_before: Optional[datetime] = None,
        download: bool = True) -> List[Image]:
    images = []
    for image_update in image_updates:
        image = upsert_image(image_update, commit=False)
        db.session.add(image)
        images.append(image)
    chargepoint.images = images
    db.session.add(chargepoint)
    db.session.commit()
    if download:
        download_images(images, download_before)
    return images


def upsert_image(
        image_update: ImageUpdate,
        old_image: Optional[Image] = None,
        commit: Optional[bool] = True) -> Image:
    image = old_image if old_image else Image.query.filter_by(external_url=image_update.external_url).first()
    if image:
        update_required = False
        for field, value in asdict(image_update).items():
            if value is not UnsetValue and getattr(image, field) != value:
                update_required = True
                break
        if not update_required:
            return image
    else:
        image = Image()
    for field, value in asdict(image_update).items():
        if value is UnsetValue:
            continue
        setattr(image, field, value)
    if commit:
        db.session.add(image)
        db.session.commit()
        logger.info('ochp.chargepoint.update', 'updated image %s' % image.id)
    return image


def download_images(images: List[Image], download_before: Optional[datetime] = None):
    for image in images:
        download_image(image, download_before)


def download_image(image: Image, download_before: Optional[datetime] = None):
    if image.last_download is not None and download_before is not None and image.last_download > download_before:
        return

    logger.info('ochp.chargepoint.download', 'download image %s from %s' % (image.id, image.external_url))
    image_request = requests.get(image.external_url, stream=True)
    if os.path.exists(image.path):
        os.remove(image.path)
    with open(image.path, 'wb') as fd:
        for chunk in image_request.iter_content(chunk_size=1024):
            fd.write(chunk)
    image.last_download = get_now_localized()
    db.session.add(image)
    db.session.commit()


