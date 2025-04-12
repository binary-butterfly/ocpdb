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

from webapp.models import Source

from .base_repository import BaseRepository


class SourceRepository(BaseRepository[Source]):
    model_cls = Source

    def fetch_sources(self) -> list[Source]:
        return self.session.query(Source).all()

    def fetch_source_by_uid(self, source_uid: str) -> Source:
        result = self.session.query(Source).filter(Source.uid == source_uid).first()

        return self._or_raise(result, f'source {source_uid} not found')

    def save_source(self, source: Source, *, commit: bool = True):
        self._save_resources(source, commit=commit)

    def delete_source(self, source: Source, *, commit: bool = True):
        self._delete_resources(source, commit=commit)
