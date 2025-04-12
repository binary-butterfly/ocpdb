"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

from datetime import datetime, timezone
from time import sleep

import requests
from requests.exceptions import ConnectionError, Timeout
from urllib3.exceptions import NewConnectionError

from webapp.models import Image
from webapp.repositories import ImageRepository
from webapp.services.base_service import BaseService


class ImageImportService(BaseService):
    image_repository: ImageRepository

    def __init__(self, *, image_repository: ImageRepository, **kwargs):
        super().__init__(**kwargs)
        self.image_repository = image_repository

    def fetch_images(self):
        images = self.image_repository.fetch_outdated_images()

        for image in images:
            self.fetch_single_image(image)
            sleep(self.config_helper.get('IMAGE_IMPORT_REQUEST_DELAY'))

    def fetch_single_image(self, image: Image):
        try:
            response = requests.get(image.external_url, timeout=30)
        except (ConnectionError, NewConnectionError, Timeout) as e:
            self.logger.warn(
                'import-images',
                f'Cannot import image {image.id} from {image.external_url}: error {e}.',
            )
            return

        if response.status_code != 200:
            self.logger.warn(
                'import-images',
                f'Cannot import image {image.id} from {image.external_url}: HTTP status {response.status_code}.',
            )
            return

        image.path.unlink(missing_ok=True)

        with image.path.open('wb') as image_file:
            image_file.write(response.content)

        image.last_download = datetime.now(timezone.utc)
        self.image_repository.save_image(image)
        self.logger.info(
            'import-images',
            f'Image {image.id} downloaded from {image.external_url}.',
        )
