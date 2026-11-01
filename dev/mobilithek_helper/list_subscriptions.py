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

Writes all subscriptions of the Mobilithek account as CSV, including their status (REQUESTED, ACTIVE, INACTIVE) and
metadata of the subscribed data offer like licence, category and data model. For restricted or withdrawn data offers,
only parts of the metadata are available, see column metadataComplete.

Usage: python dev/mobilithek_helper/list_subscriptions.py [<output file>]
Without output file, the CSV is written to temp/mobilithek_subscriptions.csv.
"""

import csv
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from mobilithek_client import MobilithekClient

DEFAULT_OUTPUT_PATH = Path(__file__).parents[2] / 'temp' / 'mobilithek_subscriptions.csv'

SUBSCRIPTION_FIELDS = [
    'id',
    'dataOfferId',
    'dataOfferTitle',
    'providerOrgName',
    'contractStatus',
    'providerApproved',
    'napApproved',
    'validFrom',
    'validTo',
    'deliveryMode',
    'currentAccessCount',
    'maxAccessCount',
]

DATA_OFFER_FIELDS = [
    'metadataComplete',
    'license',
    'standardLicense',
    'customLicense',
    'dataCategory',
    'dataCategoryDetail',
    'themes',
    'transportMode',
    'dataModel',
    'accrualPeriodicity',
    'spatialCoverage',
    'keywords',
    'dataOfferModified',
    'irregularSince',
]


def short_uri(uri: str | None) -> str:
    """
    Strips vocabulary URIs like https://w3id.org/mdp/schema/license#NO_LICENSE down to NO_LICENSE
    """
    if not uri:
        return ''
    return uri.rsplit('#', 1)[-1] if '#' in uri else uri.rsplit('/', 1)[-1]


def join_values(values: list | None) -> str:
    return '; '.join(str(value) for value in values or [] if value)


def get_data_offer_row(data_offer: dict, metadata_complete: bool) -> dict:
    custom_license = data_offer.get('customLicenseAsResource') or {}
    return {
        'metadataComplete': metadata_complete,
        'license': short_uri(data_offer.get('rights')),
        'standardLicense': data_offer.get('standardLicense') or '',
        'customLicense': (custom_license.get('instance') or {}).get('fileName') or '',
        'dataCategory': short_uri(data_offer.get('dataCategory')),
        'dataCategoryDetail': join_values([short_uri(uri) for uri in data_offer.get('dataCategoryDetail') or []]),
        'themes': join_values([short_uri(uri) for uri in data_offer.get('themes') or []]),
        'transportMode': join_values([short_uri(uri) for uri in data_offer.get('transportMode') or []]),
        'dataModel': join_values([short_uri(item.get('dataModel')) for item in data_offer.get('contentData') or []]),
        'accrualPeriodicity': short_uri(data_offer.get('accrualPeriodicity')),
        'spatialCoverage': join_values(
            [nuts.get('name') for nuts in (data_offer.get('spatialCoverage') or {}).get('nuts') or []],
        ),
        'keywords': join_values(data_offer.get('keyword')),
        'dataOfferModified': data_offer.get('modified') or '',
        'irregularSince': data_offer.get('irregularSince') or '',
    }


def list_subscriptions(output_path: Path):
    client = MobilithekClient()
    subscriptions = client.get_subscriptions()
    subscriptions.sort(key=lambda subscription: (subscription['providerOrgName'] or '', subscription['dataOfferTitle']))

    # One request per subscription, so we parallelize a bit
    with ThreadPoolExecutor(max_workers=8) as executor:
        data_offers = executor.map(client.get_data_offer, subscriptions)
        rows = [
            {**subscription, **get_data_offer_row(data_offer, metadata_complete)}
            for subscription, (data_offer, metadata_complete) in zip(subscriptions, data_offers, strict=True)
        ]

    with output_path.open('w', newline='', encoding='utf-8') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=SUBSCRIPTION_FIELDS + DATA_OFFER_FIELDS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

    print(f'{len(rows)} subscriptions written to {output_path}')


if __name__ == '__main__':
    list_subscriptions(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH)
