"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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

from decimal import Decimal

from sqlalchemy import text
from sqlalchemy.orm import scoped_session

from webapp.repositories import ObjectNotFoundException


class OfficialRegionCodeRepository:
    """
    A rather special repository for official regional codes, which are not managed by our ORM.
    """

    session: scoped_session

    def __init__(self, session: scoped_session) -> None:
        self.session = session

    def available_databases_by_country(self) -> list[str]:
        # So far, we just support the German Regionalschlüssel
        query = "SELECT tablename FROM pg_tables WHERE schemaname = 'public' AND tablename = 'regionalschluessel'"
        result = list(self.session.execute(text(query)))
        return ['DEU'] if len(result) else []

    def fetch_official_region_code_by_coordinates(self, country: str, lat: Decimal, lon: Decimal) -> str:
        if country != 'DEU':
            raise ObjectNotFoundException('So far, only Germany is supported for regional keys')

        query = (
            f'SELECT regioschlüsselaufgefüllt '  # noqa: S608
            f'FROM regionalschluessel '
            # We can be sure that this is not an SQLi because we convert to float
            f'WHERE ST_Contains(geom, ST_SetSRID(ST_MakePoint({float(lon)}, {float(lat)}), 4326))'
        )
        result = list(self.session.execute(text(query)))

        if len(result) == 0:
            raise ObjectNotFoundException('no official regional code found for coordinates')

        return result[0][0]
