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

Sends a German plain text reminder to the contact person of a data provider, asking to approve our pending
subscriptions of the given charging data offers. All data offers have to belong to the same provider and have a
REQUESTED subscription.

The Mobilithek does not expose contact email addresses of other organisations, so the recipient has to be given
explicitly. SMTP credentials are read from .env: SMTP_HOST, SMTP_PORT (465 uses SSL, everything else STARTTLS),
SMTP_USER, SMTP_PASSWORD and SMTP_FROM.

Usage: python dev/mobilithek_helper/send_reminder.py [--dry-run] --to <email> [--to <email> ...] [--cc <email> ...]
    <data offer id> [<data offer id> ...]
"""

import argparse
import os
import smtplib
import ssl
import sys
import textwrap
from datetime import datetime
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

from mobilithek_client import MobilithekClient

SUBJECT = 'Mobilithek: Bitte um Freigabe unserer Abonnement-Anfrage'


def format_request_date(subscription: dict) -> str:
    if not subscription.get('createdAt'):
        return 'Datum unbekannt'
    return datetime.fromisoformat(subscription['createdAt'].replace('Z', '+00:00')).strftime('%d.%m.%Y')


def build_body(provider_name: str, subscriptions: list[dict]) -> str:
    plural = len(subscriptions) > 1
    offer_lines = '\n'.join(
        f'- {subscription["dataOfferTitle"].strip()} (angefragt am {format_request_date(subscription)})\n'
        f'  https://mobilithek.info/offers/{subscription["dataOfferId"]}'
        for subscription in subscriptions
    )
    sender_name = f'{subscriptions[0]["subscriberUserFirstName"]} {subscriptions[0]["subscriberUserLastName"]}'.strip()

    paragraphs = [
        'Guten Tag,',
        (
            'im Auftrag der NVBW – Nahverkehrsgesellschaft Baden-Württemberg mbH betreiben wir die '
            'Ladeinfrastruktur-Datenbank von MobiData BW, der Mobilitätsdatenplattform des Landes Baden-Württemberg. '
            'Dort führen wir die Daten öffentlich zugänglicher Ladepunkte aus vielen Quellen zusammen und stellen sie '
            'als Open Data für Apps, Routenplaner und Reiseinformation bereit:'
        ),
        'https://mobidata-bw.de',
        (
            f'Gerne würden wir prüfen, ob sich auch die Daten von {provider_name} für eine Aufnahme eignen. Dazu '
            f'haben wir über die Mobilithek {"folgende Datenangebote" if plural else "folgendes Datenangebot"} '
            'abonniert:'
        ),
        offer_lines,
        (
            f'{"Diese Anfragen sind" if plural else "Diese Anfrage ist"} bisher noch nicht freigegeben. Wir würden uns '
            f'sehr freuen, wenn Sie sie in der Mobilithek unter „Organisation“ → „Abonnements“ '
            'bestätigen könnten:'
        ),
        'https://mobilithek.info/organisation/subscriptions',
        (
            'Zum Hintergrund: Nach Art. 20 der Verordnung (EU) 2023/1804 über den Aufbau der Infrastruktur für '
            'alternative Kraftstoffe (AFIR) müssen Betreiber öffentlich zugänglicher Ladepunkte statische und dynamische '
            'Daten zu ihren Ladepunkten kostenlos und diskriminierungsfrei über den nationalen Zugangspunkt '
            'bereitstellen. In Deutschland ist das die Mobilithek. Solange ein Abonnement nicht freigegeben ist, sind die '
            'Daten für Nutzer jedoch nicht abrufbar.'
        ),
        (
            'Falls Sie Fragen haben oder die Anfrage an eine andere Stelle in Ihrem Haus gehen sollte, melden Sie sich '
            'gerne.'
        ),
        f'Vielen Dank und viele Grüße\n{sender_name}',
    ]
    # The offer list is already formatted, everything else is wrapped for plain text email clients
    return (
        '\n\n'.join(
            paragraph if paragraph == offer_lines or '\n' in paragraph else textwrap.fill(paragraph, width=72)
            for paragraph in paragraphs
        )
        + '\n'
    )


def get_pending_subscriptions(client: MobilithekClient, data_offer_ids: list[str]) -> list[dict]:
    subscriptions_by_data_offer_id = {
        subscription['dataOfferId']: subscription
        for subscription in client.get_subscriptions()
        if subscription['contractStatus'] == 'REQUESTED'
    }
    missing = [data_offer_id for data_offer_id in data_offer_ids if data_offer_id not in subscriptions_by_data_offer_id]
    if missing:
        sys.exit(f'No REQUESTED subscription for data offer(s): {", ".join(missing)}')

    subscriptions = [subscriptions_by_data_offer_id[data_offer_id] for data_offer_id in data_offer_ids]
    providers = {subscription['providerOrgName'] for subscription in subscriptions}
    if len(providers) > 1:
        sys.exit(f'Data offers belong to different providers: {", ".join(sorted(providers))}')
    return subscriptions


def send(message: EmailMessage):
    host = os.environ['SMTP_HOST']
    port = int(os.environ.get('SMTP_PORT', '587'))
    context = ssl.create_default_context()
    if port == 465:
        smtp = smtplib.SMTP_SSL(host, port, context=context, timeout=30)
    else:
        smtp = smtplib.SMTP(host, port, timeout=30)
        smtp.starttls(context=context)
    with smtp:
        smtp.login(os.environ['SMTP_USER'], os.environ['SMTP_PASSWORD'])
        smtp.send_message(message)


def send_reminder(data_offer_ids: list[str], to: list[str], cc: list[str], dry_run: bool):
    # MobilithekClient loads .env, so the SMTP variables are available afterwards
    client = MobilithekClient()
    subscriptions = get_pending_subscriptions(client, data_offer_ids)

    message = EmailMessage()
    message['Subject'] = SUBJECT
    message['From'] = os.environ.get('SMTP_FROM', '<SMTP_FROM not set>' if dry_run else os.environ['SMTP_FROM'])
    message['To'] = ', '.join(to)
    if cc:
        message['Cc'] = ', '.join(cc)
    message['Date'] = formatdate(localtime=True)
    message['Message-ID'] = make_msgid()
    message.set_content(build_body(subscriptions[0]['providerOrgName'], subscriptions), charset='utf-8')

    if dry_run:
        print(render(message))
        return

    send(message)
    print(f'Reminder for {len(subscriptions)} data offer(s) sent to {", ".join(to + cc)}')


def render(message: EmailMessage) -> str:
    headers = '\n'.join(f'{key}: {value}' for key, value in message.items() if key in ('From', 'To', 'Cc', 'Subject'))
    return f'{headers}\n\n{message.get_content()}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sends a reminder to approve pending Mobilithek subscriptions.')
    parser.add_argument('data_offer_ids', nargs='+', metavar='data offer id')
    parser.add_argument('--to', action='append', required=True, help='recipient, can be given multiple times')
    parser.add_argument('--cc', action='append', default=[], help='cc recipient, can be given multiple times')
    parser.add_argument('--dry-run', action='store_true', help='print the email instead of sending it')
    args = parser.parse_args()
    send_reminder(args.data_offer_ids, args.to, args.cc, args.dry_run)
