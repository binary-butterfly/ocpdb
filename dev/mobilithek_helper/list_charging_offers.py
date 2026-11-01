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

Writes all charging data offers of the Mobilithek as CSV, with the subscription status of the Mobilithek account and the
OCPDB import service covering the offer, if there is one. Afterwards, it prints the ids of all brokered charging data
offers without an active or requested subscription, which can be passed to subscribe.py.

Usage: python dev/mobilithek_helper/list_charging_offers.py [<output file>]
Without output file, the CSV is written to temp/mobilithek_charging_offers.csv.
"""

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

from mobilithek_client import MobilithekClient

DEFAULT_OUTPUT_PATH = Path(__file__).parents[2] / 'temp' / 'mobilithek_charging_offers.csv'

CHARGING_CATEGORY = 'https://w3id.org/mdp/schema/data_categories#FILLING_AND_CHARGING_STATIONS'

# Charging data offers which the publisher filed in another data category
EXTRA_DATA_OFFER_IDS: list[str] = [
    '974006122901856256',  # AFIR-recharging-dyn-Eulektro, filed as PARKING_AND_REST_AREA_INFORMATION
]

MATCH_MOBILITHEK = 'Mobilithek import service'
MATCH_OTHER_SOURCE = 'other source, same data'
MATCH_OTHER_SOURCE_LIKELY = 'other source, likely same data'
MATCH_OWN_PUBLICATION = 'own publication'

# The Mobilithek import services just know their subscription ids from config, and the other import services fetch
# their data from the original source, so this mapping has to be maintained by hand. The 'likely' matches are guessed
# from publisher and description of the offer.
CONVERTER_BY_DATA_OFFER_ID: dict[str, tuple[str, str]] = {
    '972837891969273856': ('datex2_ampeco', MATCH_MOBILITHEK),
    '972842599324557312': ('datex2_ampeco', MATCH_MOBILITHEK),
    '978597062404620288': ('datex2_chargecloud', MATCH_MOBILITHEK),
    '980862594474274816': ('datex2_chargecloud', MATCH_MOBILITHEK),
    '996825300704600064': ('datex2_e_clearing_net', MATCH_MOBILITHEK),
    '996823601386508288': ('datex2_e_clearing_net', MATCH_MOBILITHEK),
    '907574882292453376': ('datex2_enbw', MATCH_MOBILITHEK),
    '907575401287241728': ('datex2_enbw', MATCH_MOBILITHEK),
    '961625658278940672': ('datex2_eround', MATCH_MOBILITHEK),
    '961629419076456448': ('datex2_eround', MATCH_MOBILITHEK),
    '954064102947180544': ('datex2_ecomovement', MATCH_MOBILITHEK),
    '955166494396665856': ('datex2_ecomovement', MATCH_MOBILITHEK),
    '936298491949047808': ('datex2_elu_mobility', MATCH_MOBILITHEK),
    '971513500454850560': ('datex2_elu_mobility', MATCH_MOBILITHEK),
    '963766220171735040': ('datex2_enio', MATCH_MOBILITHEK),
    '968541134128902144': ('datex2_enio', MATCH_MOBILITHEK),
    # giroe fetches the same data directly from GLS Mobility
    '980559859451379712': ('datex2_giroe; giroe', MATCH_MOBILITHEK),
    '980563757096464384': ('datex2_giroe; giroe', MATCH_MOBILITHEK),
    '984104561811357696': ('datex2_gridandco', MATCH_MOBILITHEK),
    '984103903968534528': ('datex2_gridandco', MATCH_MOBILITHEK),
    '962721207430316032': ('datex2_lichtblick', MATCH_MOBILITHEK),
    '962731482363617280': ('datex2_lichtblick', MATCH_MOBILITHEK),
    '979435003058024448': ('datex2_midorion', MATCH_MOBILITHEK),
    '979433370303545344': ('datex2_midorion', MATCH_MOBILITHEK),
    '963836072152719360': ('datex2_monta', MATCH_MOBILITHEK),
    '963870983660167168': ('datex2_monta', MATCH_MOBILITHEK),
    '970305056590979072': ('datex2_msu', MATCH_MOBILITHEK),
    '970388804493828096': ('datex2_msu', MATCH_MOBILITHEK),
    '969322788846231552': ('datex2_pump', MATCH_MOBILITHEK),
    '972963216296222720': ('datex2_qwello', MATCH_MOBILITHEK),
    '972966368902897664': ('datex2_qwello', MATCH_MOBILITHEK),
    '980809280034390016': ('datex2_smatrics', MATCH_MOBILITHEK),
    '961319990963605504': ('datex2_smatrics', MATCH_MOBILITHEK),
    '1000749522967314432': ('datex2_taubert', MATCH_MOBILITHEK),
    '1000746576770711552': ('datex2_taubert', MATCH_MOBILITHEK),
    '953828817873125376': ('datex2_tesla', MATCH_MOBILITHEK),
    '953843379766972416': ('datex2_tesla', MATCH_MOBILITHEK),
    '979363267193040896': ('datex2_vaylens', MATCH_MOBILITHEK),
    '979364650281549824': ('datex2_vaylens', MATCH_MOBILITHEK),
    '983008874583728128': ('datex2_volkswagen', MATCH_MOBILITHEK),
    '983006934617260032': ('datex2_volkswagen', MATCH_MOBILITHEK),
    '869246425829892096': ('datex2_wirelane', MATCH_MOBILITHEK),
    '876587237907525632': ('datex2_wirelane', MATCH_MOBILITHEK),
    '998571342932365312': ('datex2_audi', MATCH_MOBILITHEK),
    '998567365272563712': ('datex2_audi', MATCH_MOBILITHEK),
    # eaaze_pbw fetches the PBW part of the EAAZE data via OCPI
    '980426161955500032': ('datex2_eaaze; eaaze_pbw', MATCH_MOBILITHEK),
    '980425456721260544': ('datex2_eaaze; eaaze_pbw', MATCH_MOBILITHEK),
    '1037036344672452608': ('datex2_enerando', MATCH_MOBILITHEK),
    '1037038702374617088': ('datex2_enerando', MATCH_MOBILITHEK),
    '973938793916375040': ('datex2_eulektro', MATCH_MOBILITHEK),
    '974006122901856256': ('datex2_eulektro', MATCH_MOBILITHEK),
    '993495185148837888': ('datex2_ah_beteiligung', MATCH_MOBILITHEK),
    '993494022504546304': ('datex2_ah_beteiligung', MATCH_MOBILITHEK),
    '981180413145477120': ('datex2_inselwerke', MATCH_MOBILITHEK),
    '981170994693238784': ('datex2_inselwerke', MATCH_MOBILITHEK),
    '988133177339846656': ('datex2_ladesonne', MATCH_MOBILITHEK),
    '988137788909801472': ('datex2_ladesonne', MATCH_MOBILITHEK),
    '993499364131065856': ('datex2_r_m_beteiligung', MATCH_MOBILITHEK),
    '993498817080557568': ('datex2_r_m_beteiligung', MATCH_MOBILITHEK),
    '979427073235566592': ('datex2_sonnenstrom_saarpfalz', MATCH_MOBILITHEK),
    '979428785661079552': ('datex2_sonnenstrom_saarpfalz', MATCH_MOBILITHEK),
    '989311807176560640': ('datex2_ev_price', MATCH_MOBILITHEK),
    '989311073915731968': ('datex2_ev_price', MATCH_MOBILITHEK),
    '1024264572575293440': ('datex2_ewe', MATCH_MOBILITHEK),
    '1006184570533171200': ('datex2_ewe', MATCH_MOBILITHEK),
    '1004450433724211200': ('datex2_flavia', MATCH_MOBILITHEK),
    '1004756865530970112': ('datex2_flavia', MATCH_MOBILITHEK),
    '997111469996658688': ('datex2_gp_joule', MATCH_MOBILITHEK),
    '997190851637440512': ('datex2_gp_joule', MATCH_MOBILITHEK),
    '1043944773714128896': ('datex2_inergia', MATCH_MOBILITHEK),
    '1043947032435105792': ('datex2_inergia', MATCH_MOBILITHEK),
    '983747474988376064': ('datex2_kul_rudnick', MATCH_MOBILITHEK),
    '1021366453630017536': ('datex2_road', MATCH_MOBILITHEK),
    '1021364001002217472': ('datex2_road', MATCH_MOBILITHEK),
    '1042468553977937920': ('datex2_virta', MATCH_MOBILITHEK),
    '1042472664437800960': ('datex2_virta', MATCH_MOBILITHEK),
    '854410608351543296': ('datex2_ulm', MATCH_MOBILITHEK),
    '854416606814023680': ('datex2_ulm', MATCH_MOBILITHEK),
    # eliso uses a custom JSON format instead of DATEX II
    '843477276990078976': ('eliso', MATCH_MOBILITHEK),
    '843502085052710912': ('eliso', MATCH_MOBILITHEK),
    '951517095896416256': ('bnetza_api', MATCH_OTHER_SOURCE_LIKELY),
    '842113170303512576': ('bnetza_excel', MATCH_OTHER_SOURCE_LIKELY),
    # Bundled data of MobiData BW, which is the output of OCPDB itself
    '-2035239451501556619': ('', MATCH_OWN_PUBLICATION),
    '980084361378099200': ('', MATCH_OWN_PUBLICATION),
    '981124859836461056': ('', MATCH_OWN_PUBLICATION),
}

# Offers in the charging category which are no charging data sources, so we don't subscribe to them
IGNORE_REASON_BY_DATA_OFFER_ID: dict[str, str] = {
    '935580278881759232': 'fuel station',
    '937348385824550912': 'fuel station',
    '753618942489935872': 'fuel station',
    '834870693179846656': 'fuel station',
    '968150797115953152': 'test data',
    '981218494322012160': 'test data',
    '981223821767557120': 'test data',
    '1006136734156312576': 'test data',
    '755033335157133312': 'statistical analysis',
    '1033716358314917888': 'organisation data only',
    '980084361378099200': 'own publication',
    '981124859836461056': 'own publication',
}

# Subscriptions in these states don't need a new subscription
OPEN_SUBSCRIPTION_STATUSES = ('ACTIVE', 'REQUESTED')

FIELDS = [
    'publicationId',
    'title',
    'publisher',
    'dataModel',
    'license',
    'mobilithekBrokering',
    'region',
    'subscriptionStatus',
    'subscriptionId',
    'converter',
    'converterMatch',
    'ignoreReason',
    'url',
]


def short_uri(uri: str | None) -> str:
    """
    Strips vocabulary URIs like https://w3id.org/mdp/schema/license#NO_LICENSE down to NO_LICENSE
    """
    if not uri:
        return ''
    return uri.rsplit('#', 1)[-1]


def get_row(data_offer: dict, subscriptions: list[dict]) -> dict:
    publication_id = data_offer['publicationId']
    converter, converter_match = CONVERTER_BY_DATA_OFFER_ID.get(publication_id, ('', ''))
    data_models = {
        short_uri(content_data.get('dataModel'))
        for content_data in data_offer.get('contentData') or []
        if content_data.get('dataModel')
    }
    return {
        'publicationId': publication_id,
        'title': data_offer['title'].strip(),
        'publisher': data_offer['agents']['publisher']['name'],
        'dataModel': '; '.join(sorted(data_models)),
        'license': short_uri(data_offer.get('rights')),
        # Brokered offers are delivered by the Mobilithek itself and can be pulled with the machine certificate
        'mobilithekBrokering': data_offer.get('mdpBrokering'),
        'region': '; '.join(nuts['name'] for nuts in (data_offer.get('spatialCoverage') or {}).get('nuts') or []),
        'subscriptionStatus': '; '.join(subscription['contractStatus'] for subscription in subscriptions),
        'subscriptionId': '; '.join(subscription['id'] for subscription in subscriptions),
        'converter': converter,
        'converterMatch': converter_match,
        'ignoreReason': IGNORE_REASON_BY_DATA_OFFER_ID.get(publication_id, ''),
        'url': f'https://mobilithek.info/offers/{publication_id}',
    }


def is_missing_subscription(row: dict) -> bool:
    return (
        row['mobilithekBrokering'] is True
        and not row['ignoreReason']
        and not any(status in OPEN_SUBSCRIPTION_STATUSES for status in row['subscriptionStatus'].split('; '))
    )


def list_charging_offers(output_path: Path):
    client = MobilithekClient()
    data_offers = client.search_data_offers([CHARGING_CATEGORY])
    known_data_offer_ids = {data_offer['publicationId'] for data_offer in data_offers}
    data_offers += [
        client.get_data_offer_by_id(data_offer_id)
        for data_offer_id in EXTRA_DATA_OFFER_IDS
        if data_offer_id not in known_data_offer_ids
    ]
    data_offers.sort(key=lambda data_offer: (data_offer['agents']['publisher']['name'], data_offer['title']))

    subscriptions_by_data_offer_id: dict[str, list[dict]] = defaultdict(list)
    for subscription in client.get_subscriptions():
        subscriptions_by_data_offer_id[subscription['dataOfferId']].append(subscription)

    rows = [
        get_row(data_offer, subscriptions_by_data_offer_id[data_offer['publicationId']]) for data_offer in data_offers
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', newline='', encoding='utf-8') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f'{len(rows)} charging data offers written to {output_path}')
    overview = Counter(
        (
            'converter' if row['converter'] or row['converterMatch'] else 'no converter',
            row['subscriptionStatus'] or 'no subscription',
        )
        for row in rows
    )
    for (converter, subscription_status), count in sorted(overview.items()):
        print(f'  {converter}, {subscription_status}: {count}')

    missing_rows = [row for row in rows if is_missing_subscription(row)]
    print(f'{len(missing_rows)} brokered charging data offers without active or requested subscription:')
    for row in missing_rows:
        print(f'  {row["publicationId"]}  {row["publisher"]}: {row["title"]}')
    if missing_rows:
        print(f'subscribe with: subscribe.py {" ".join(row["publicationId"] for row in missing_rows)}')


if __name__ == '__main__':
    list_charging_offers(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH)
