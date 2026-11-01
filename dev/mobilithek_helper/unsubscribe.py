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

Deletes each given Mobilithek subscription.

Usage: python dev/mobilithek_helper/unsubscribe.py <subscription id> [<subscription id> ...]
"""

import sys

from mobilithek_client import MobilithekClient


def unsubscribe(subscription_ids: list[str]):
    client = MobilithekClient()
    for subscription_id in subscription_ids:
        client.unsubscribe(subscription_id)
        print(f'subscription {subscription_id}: deleted')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(f'Usage: {sys.argv[0]} <subscription id> [<subscription id> ...]')
    unsubscribe(sys.argv[1:])
