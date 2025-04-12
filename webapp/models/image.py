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
from enum import Enum
from pathlib import Path

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

    external_url: Mapped[str | None] = db.Column(db.String(255), index=True, nullable=True)
    type: Mapped[str | None] = db.Column(db.String(4), nullable=True)
    category: Mapped[ImageCategory | None] = db.Column(db.Enum(ImageCategory), nullable=True)
    width: Mapped[int | None] = db.Column(db.Integer, nullable=True)
    height: Mapped[int | None] = db.Column(db.Integer, nullable=True)
    last_download: Mapped[datetime | None] = db.Column(UtcDateTime(timezone=True), nullable=True)

    @property
    def url(self) -> str:
        return f'{current_app.config["PROJECT_URL"]}/static/images/dynamic/{self.id}.{self.type}'

    @property
    def path(self) -> Path:
        return Path(current_app.config['DYNAMIC_IMAGE_DIR'], f'{self.id}.{self.type}')

    @property
    def url_thumbnail(self) -> str:
        return f'{current_app.config["PROJECT_URL"]}/static/images/dynamic/{self.id}.thumb.{self.type}'

    @property
    def path_thumbnail(self):
        return Path(current_app.config['DYNAMIC_IMAGE_DIR'], f'{self.id}.thumb.{self.type}')

    def to_dict(self, *args, strict: bool = False, ignore: list[str] | None = None, **kwargs) -> dict:
        ignore = ignore or []
        ignore += ['id', 'created', 'modified', 'external_url', 'last_download']

        result = super().to_dict(*args, ignore, **kwargs)

        result['url'] = self.url

        if not strict:
            result['original_url'] = self.external_url
            result['last_download'] = self.last_download

        return result


# TODO: use this for UPDATE checks
# @event.listens_for(Image, 'before_insert')
# @event.listens_for(Image, 'before_update')
# def set_geometry(mapper, connection, image):
#    state = db.inspect(image)
#    for attr in state.attrs:
#      print(state.get_history(attr.key, True))
