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
from datetime import datetime
from enum import Enum
from typing import List, Optional

from flask import current_app
from sqlalchemy_utc import UtcDateTime

from webapp.common.sqlalchemy import Mapped
from webapp.extensions import db

from .base import BaseModel


class ImageCategory(Enum):
    CHARGER = 'CHARGER'
    ENTRANCE = 'ENTRANCE'
    LOCATION = 'LOCATION'
    NETWORK = 'NETWORK'
    OPERATOR = 'OPERATOR'
    OTHER = 'OTHER'
    OWNER = 'OWNER'


class Image(db.Model, BaseModel):
    __tablename__ = 'image'

    external_url: Mapped[str] = db.Column(db.String(255), index=True)
    type: Mapped[str] = db.Column(db.String(4))
    category: Mapped[ImageCategory] = db.Column(db.Enum(ImageCategory))
    width: Mapped[int] = db.Column(db.Integer)
    height: Mapped[int] = db.Column(db.Integer)
    last_download: Mapped[datetime] = db.Column(UtcDateTime(timezone=True))

    @property
    def url(self):
        return '%s/static/images/dynamic/%s.%s' % (current_app.config['PROJECT_URL'], self.id, self.type)

    @property
    def path(self):
        return os.path.abspath(os.path.join(current_app.config['DYNAMIC_IMAGE_DIR'], '%s.%s' % (self.id, self.type)))

    @property
    def url_thumbnail(self):
        return '%s/static/images/dynamic/%s.thumb.%s' % (current_app.config['PROJECT_URL'], self.id, self.type)

    @property
    def path_thumbnail(self):
        return os.path.abspath(
            os.path.join(current_app.config['DYNAMIC_IMAGE_DIR'], '%s.thumb.%s' % (self.id, self.type)),
        )

    def to_dict(self, fields: Optional[List[str]] = None, ignore: Optional[List[str]] = None) -> dict:
        result = super().to_dict(fields, ignore)
        result['url'] = self.url
        return result


# TODO: use this for UPDATE checks
# @event.listens_for(Image, 'before_insert')
# @event.listens_for(Image, 'before_update')
# def set_geometry(mapper, connection, image):
#    state = db.inspect(image)
#    for attr in state.attrs:
#      print(state.get_history(attr.key, True))
