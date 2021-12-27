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
from enum import Enum
from typing import Optional, List
from sqlalchemy_utc import UtcDateTime
from flask import current_app
from .base import BaseModel
from ..extensions import db


class ImageCategory(Enum):
    CHARGER = 'CHARGER'
    ENTRANCE = 'ENTRANCE'
    LOCATION = 'LOCATION'
    NETWORK = 'NETWORK'
    OPERATOR = 'OPERATOR'
    OTHER = 'OTHER'
    OWNER = 'OWNER'


class Image(db.Model, BaseModel):
    __tablename__ = "image"

    external_url = db.Column(db.String(255))
    type = db.Column(db.String(4))
    category = db.Column(db.Enum(ImageCategory, name='ImageCategory'))
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    last_download = db.Column(UtcDateTime(timezone=True))

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
        return os.path.abspath(os.path.join(
            current_app.config['DYNAMIC_IMAGE_DIR'],
            '%s.thumb.%s' % (self.id, self.type)
        ))

    def to_dict(self, fields: Optional[List[str]] = None, ignore: Optional[List[str]] = None) -> dict:
        result = super().to_dict(fields, ignore)
        result['url'] = self.url
        return result
