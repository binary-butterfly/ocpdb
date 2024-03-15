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
from hashlib import sha256
from io import BytesIO
from pathlib import Path
from typing import Tuple, Dict, List

from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.error_handling.exceptions import AppException
from webapp.common.remote_helper import RemoteServerType
from webapp.services.import_services.base_import_service import BaseImportService
from .bnetza_mapper import BnetzaMapper
from .bnetza_validators import BnetzaRowInput


class BnetzaImportService(BaseImportService):
    bnetza_mapper: BnetzaMapper = BnetzaMapper()
    row_validator: DataclassValidator[BnetzaRowInput] = DataclassValidator(BnetzaRowInput)
    header_line = {
        'Betreiber': 'operator',
        'Straße': 'address',
        'Hausnummer': 'housenumber',
        'Adresszusatz': 'additional_address_data',
        'Postleitzahl': 'postcode',
        'Ort': 'locality',
        'Bundesland': 'land',
        'Kreis/kreisfreie Stadt': 'district',
        'Breitengrad': 'lat',
        'Längengrad': 'lon',
        'Inbetriebnahmedatum': 'launch_date',
        'Nennleistung Ladeeinrichtung [kW]': 'connection_power',
        'Art der Ladeeinrichung': 'chargestation_type',
        'Anzahl Ladepunkte': 'connector_count',
        'Steckertypen1': 'connector_1_type',
        'P1 [kW]': 'connector_1_power',
        'Public Key1': 'connector_1_public_key',
        'Steckertypen2': 'connector_2_type',
        'P2 [kW]': 'connector_2_power',
        'Public Key2': 'connector_2_public_key',
        'Steckertypen3': 'connector_3_type',
        'P3 [kW]': 'connector_3_power',
        'Public Key3': 'connector_3_public_key',
        'Steckertypen4': 'connector_4_type',
        'P4 [kW]': 'connector_4_power',
        'Public Key4': 'connector_4_public_key',
    }

    def load_and_save_from_web(self):
        data = self.remote_helper.get(remote_server_type=RemoteServerType.BNETZA, raw=True)
        worksheet = load_workbook(filename=BytesIO(data)).active
        self.load_and_save(worksheet)

    def load_and_save_from_file(self, import_file_path: Path):
        worksheet = load_workbook(filename=import_file_path).active
        self.load_and_save(worksheet)
        self.delete_import_files()

    def load_and_save(self, worksheet: Worksheet):
        self.check_mapping(worksheet[11])

        rows_by_location_uid = self.get_rows_by_location_uid(worksheet=worksheet)

        location_updates = []
        for location_uid, rows in rows_by_location_uid.items():
            location_updates.append(self.bnetza_mapper.map_rows_to_location_update(location_uid, rows))

        self.save_location_updates(location_updates, 'bnetza')

    def check_mapping(self, row: Tuple):
        if list(self.header_line.keys()) != [cell.value for cell in row]:
            raise AppException(message='invalid xlsx header')

    def get_rows_by_location_uid(self, worksheet: Worksheet) -> Dict[str, List[BnetzaRowInput]]:
        location_dict = {}
        # there are 10 rows of explanation over the header, plus 1 line header -> we start at row 12
        for table_row in worksheet.iter_rows(min_row=12):
            row_dict = {list(self.header_line.values())[i]: table_row[i].value for i in
                        range(0, len(self.header_line.keys()))}

            # some postcodes are integer (why?! :( )
            row_dict['postcode'] = str(row_dict['postcode'])

            # normalize connectors
            for i in range(1, 5):
                connector_types = []
                if row_dict[f'connector_{i}_type']:
                    for item in row_dict[f'connector_{i}_type'].replace(';', ',').split(','):
                        connector_types.append(item.strip())
                row_dict[f'connector_{i}_type'] = connector_types

            try:
                row = self.row_validator.validate(row_dict)
                geo_hash = sha256(('%s-%s' % (row.lat, row.lon)).encode()).hexdigest()[:20]
                if geo_hash not in location_dict:
                    location_dict[geo_hash] = []
                location_dict[geo_hash].append(row)
            except ValidationError as exception:
                print('%s: %s' % (row_dict, exception.to_dict()))
        return location_dict

    def delete_import_files(self):
        path = Path(self.config_helper.get('BNETZA_IMPORT_DIR'))
        for item in path.iterdir():
            item.unlink()
