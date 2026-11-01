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

Requests a subscription for each given Mobilithek data offer id. New subscriptions start as REQUESTED and have to be
approved by the data provider.

Usage: python dev/mobilithek_helper/subscribe.py <data offer id> [<data offer id> ...]
"""

import sys

from mobilithek_client import MobilithekClient


def subscribe(data_offer_ids: list[str]):
    client = MobilithekClient()
    for data_offer_id in data_offer_ids:
        subscription_id = client.subscribe(data_offer_id)
        print(f'data offer {data_offer_id}: subscription {subscription_id}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(f'Usage: {sys.argv[0]} <data offer id> [<data offer id> ...]')
    subscribe(sys.argv[1:])
