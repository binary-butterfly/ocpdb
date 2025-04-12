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

from operator import or_

from webapp.models import Image

from .base_repository import BaseRepository


class ImageRepository(BaseRepository[Image]):
    model_cls = Image

    def fetch_image_by_id(self, image_id: int) -> Image:
        return self.fetch_resource_by_id(image_id)

    def fetch_images(self) -> list[Image]:
        return self.session.query(Image).all()

    def fetch_image_by_url(self, image_url: str) -> Image:
        image = self.session.query(Image).filter(Image.external_url == image_url).first()

        return self._or_raise(image, f'image with url {image_url} not found')

    def fetch_outdated_images(self) -> list[Image]:
        query = self.session.query(Image).filter(
            or_(
                Image.last_download.is_(None),
                Image.last_download < Image.modified,
            ),
            Image.external_url.isnot(None),
        )

        return query.all()

    def save_image(self, image: Image, *, commit: bool = True) -> None:
        self._save_resources(image, commit=commit)
