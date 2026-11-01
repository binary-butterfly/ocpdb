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

import os
from pathlib import Path

import requests
from dotenv import load_dotenv

TOKEN_URL = 'https://mobilithek.info/auth/realms/MDP/protocol/openid-connect/token'
CONTRACTS_URL = 'https://mobilithek.info/mdp-api/mdp-msa-contracts/v1/contracts'
OFFERS_URL = 'https://mobilithek.info/mdp-api/mdp-msa-metadata/v2/offers'


class MobilithekClient:
    """
    Client for the (undocumented) API behind the Mobilithek web GUI. Managing subscriptions needs a user login, the
    machine certificate is not sufficient. Credentials are read from MOBILITHEK_USER and MOBILITHEK_PASSWORD in .env.
    """

    def __init__(self):
        load_dotenv(Path(__file__).parents[2] / '.env')
        response = requests.post(
            TOKEN_URL,
            data={
                'grant_type': 'password',
                'client_id': 'Platform',
                'username': os.environ['MOBILITHEK_USER'],
                'password': os.environ['MOBILITHEK_PASSWORD'],
            },
            timeout=30,
        )
        response.raise_for_status()

        self.session = requests.Session()
        self.session.headers['Authorization'] = f'Bearer {response.json()["access_token"]}'

    def get_subscriptions(self) -> list[dict]:
        subscriptions: list[dict] = []
        page = 0
        while True:
            response = self.session.post(
                f'{CONTRACTS_URL}/search',
                json={},
                params={'page': page, 'size': 100},
                timeout=30,
            )
            response.raise_for_status()
            data = response.json()
            subscriptions += data['content']
            if data['last']:
                return subscriptions
            page += 1

    def search_data_offers(self, categories: list[str]) -> list[dict]:
        """
        Returns all data offers in the given data categories, e.g. data_categories#FILLING_AND_CHARGING_STATIONS.
        Logged in, this includes restricted offers which are not visible in the public search.
        """
        data_offers: list[dict] = []
        page = 0
        while True:
            # Without explicit sorting, the order is not stable between pages, so offers get duplicated or skipped
            response = self.session.post(
                f'{OFFERS_URL}/search',
                json={'categories': categories},
                params={'page': page, 'size': 1000, 'sort': 'created,desc'},
                timeout=60,
            )
            response.raise_for_status()
            data = response.json()['dataOffers']
            data_offers += data['content']
            if data['last']:
                return data_offers
            page += 1

    def get_data_offer_by_id(self, data_offer_id: str) -> dict:
        response = self.session.get(f'{OFFERS_URL}/{data_offer_id}', timeout=30)
        response.raise_for_status()
        return response.json()

    def get_data_offer(self, subscription: dict) -> tuple[dict, bool]:
        """
        Returns the data offer of a subscription and whether its metadata is complete. Restricted or withdrawn offers
        are just available via the subscription, which only contains parts of the metadata, e.g. the licence.
        """
        response = self.session.get(f'{OFFERS_URL}/{subscription["dataOfferId"]}', timeout=30)
        if response.ok:
            return response.json(), True
        if response.status_code not in (403, 404):
            response.raise_for_status()

        response = self.session.get(f'{CONTRACTS_URL}/{subscription["id"]}/with-offer', timeout=30)
        response.raise_for_status()
        return response.json()['dataOffer'], False

    def subscribe(self, data_offer_id: str) -> str:
        response = self.session.post(
            CONTRACTS_URL,
            json={'dataOfferId': data_offer_id, 'relevantToMDVPBefG': False},
            timeout=30,
        )
        response.raise_for_status()
        # The API returns the new subscription id as plain body
        return response.text

    def unsubscribe(self, subscription_id: str):
        response = self.session.delete(f'{CONTRACTS_URL}/{subscription_id}', timeout=30)
        response.raise_for_status()
