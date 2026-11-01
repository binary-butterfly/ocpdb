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

Validates DATEX II static and realtime data of a Mobilithek subscription against the validators and mappers of the
DATEX II v3.5 and v3.7 import services, without touching the database. This shows which import service base class
fits the data and why an import fails. The static data is validated as a whole, so a single invalid site lets the
whole import fail. Realtime EVSE references are matched against the EVSE ids of the static data.

Each argument is either a local file or a Mobilithek subscription id, which is fetched with the machine certificate.
This script needs the webapp, so it has to run in the flask container:

Usage: docker compose run --rm flask python dev/mobilithek_helper/validate_datex2.py <static> [<realtime>] [--json]
"""

import json
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import requests
from validataclass.exceptions import ValidationError
from validataclass.helpers import UnsetValue
from validataclass.validators import DataclassValidator

sys.path.insert(0, str(Path(__file__).parents[2]))

from webapp.services.import_services.datex2.v3_5.base_datex2_v3_5_import_service import (  # noqa: E402
    BaseDatex2V35ImportService,
)
from webapp.services.import_services.datex2.v3_5.datex2_v3_5_json_static_mapper import (  # noqa: E402
    Datex2V35JSONStaticMapper,
)
from webapp.services.import_services.datex2.v3_7.base_datex2_v3_7_import_service import (  # noqa: E402
    BaseDatex2V37ImportService,
)
from webapp.services.import_services.datex2.v3_7.datex2_v3_7_json_static_mapper import (  # noqa: E402
    Datex2V37JSONStaticMapper,
)
from webapp.shared.datex2.models import MessageContainerWrapperInput  # noqa: E402
from webapp.shared.datex2.v3_5_json_static.models.d_a_t_e_x_i_i3_d2_payload_input import (  # noqa: E402
    DATEXII3D2PayloadInput as V35StaticPayloadInput,
)
from webapp.shared.datex2.v3_5_json_static.models.energy_infrastructure_site_input import (  # noqa: E402
    EnergyInfrastructureSiteInput as V35SiteInput,
)
from webapp.shared.datex2.v3_7.static.d_a_t_e_x_i_i3_d2_payload_input import (  # noqa: E402
    DATEXII3D2PayloadInput as V37StaticPayloadInput,
)
from webapp.shared.datex2.v3_7.static.energy_infrastructure_site_input import (  # noqa: E402
    EnergyInfrastructureSiteInput as V37SiteInput,
)

SUBSCRIPTION_URL = 'https://mobilithek.info:8443/mobilithek/api/v1.0/subscription'
CERT = (
    str(Path(__file__).parents[2] / 'files' / 'mobilithek-binary-butterfly.crt.pem'),
    str(Path(__file__).parents[2] / 'files' / 'mobilithek-binary-butterfly.key.pem'),
)

VERSIONS = {
    '3.5': {
        'static_validator': DataclassValidator(V35StaticPayloadInput),
        'site_validator': DataclassValidator(V35SiteInput),
        'realtime_payloads': lambda data: get_v3_5_realtime_payloads(data),
        'mapper': Datex2V35JSONStaticMapper(),
    },
    '3.7': {
        'static_validator': DataclassValidator(V37StaticPayloadInput),
        'site_validator': DataclassValidator(V37SiteInput),
        'realtime_payloads': BaseDatex2V37ImportService.get_realtime_payloads,
        'mapper': Datex2V37JSONStaticMapper(),
    },
}


@dataclass
class StaticResult:
    valid: bool = False
    site_count: int = 0
    invalid_site_count: int = 0
    location_count: int = 0
    unmapped_site_count: int = 0
    evse_count: int = 0
    errors: list[str] = field(default_factory=list)
    evse_uids: set[str] = field(default_factory=set)


@dataclass
class RealtimeResult:
    valid: bool = False
    status_count: int = 0
    unmapped_status_count: int = 0
    matched_count: int = 0
    errors: list[str] = field(default_factory=list)


def load_data(source: str) -> dict | None:
    """
    Loads a local file or fetches a Mobilithek subscription. Returns None for empty responses.
    """
    if Path(source).is_file():
        raw = Path(source).read_bytes()
    else:
        response = requests.get(SUBSCRIPTION_URL, params={'subscriptionID': source}, cert=CERT, timeout=300)
        response.raise_for_status()
        raw = response.content
    if not raw.strip():
        return None
    return json.loads(raw)


def flatten_errors(error: dict, path: str = '') -> list[str]:
    """
    Flattens nested validataclass errors to paths, with list indices replaced by [*]
    """
    errors: list[str] = []
    for key, child in (error.get('field_errors') or {}).items():
        errors += flatten_errors(child, f'{path}.{key}')
    for child in (error.get('item_errors') or {}).values():
        errors += flatten_errors(child, f'{path}[*]')
    if not errors:
        reason = error.get('reason') or error.get('code')
        errors.append(f'{path or "."}: {reason}')
    return errors


def summarize_errors(errors: list[str], limit: int = 8) -> list[str]:
    return [f'{count}x {error}' for error, count in Counter(errors).most_common(limit)]


def get_sites(data: dict) -> list[dict]:
    publication = (data.get('payload') or {}).get('aegiEnergyInfrastructureTablePublication') or {}
    return [
        site
        for table in publication.get('energyInfrastructureTable') or []
        for site in table.get('energyInfrastructureSite') or []
    ]


def validate_static(data: dict, version: str) -> StaticResult:
    config = VERSIONS[version]
    result = StaticResult()
    # Same hack as in the import services to support an invalid MessageContainer
    if 'messageContainer' in data:
        data = {'payload': data['messageContainer']['payload'][0]}

    sites = get_sites(data)
    result.site_count = len(sites)
    site_errors: list[str] = []
    for site in sites:
        try:
            config['site_validator'].validate(site)
        except ValidationError as e:
            result.invalid_site_count += 1
            site_errors += flatten_errors(e.to_dict(), 'site')

    try:
        datex_input = config['static_validator'].validate(data)
    except ValidationError as e:
        result.errors = summarize_errors(site_errors or flatten_errors(e.to_dict()))
        return result

    publication = datex_input.payload.aegiEnergyInfrastructureTablePublication
    if publication is UnsetValue or not publication.energyInfrastructureTable:
        result.errors = ['missing aegiEnergyInfrastructureTablePublication']
        return result
    if version == '3.7' and len(publication.energyInfrastructureTable) != 1:
        result.errors = [
            f'{len(publication.energyInfrastructureTable)} energyInfrastructureTables, 3.7 needs exactly one'
        ]
        return result

    result.valid = True
    for table in publication.energyInfrastructureTable:
        for site in table.energyInfrastructureSite:
            location_update = config['mapper'].map_energy_infrastructure_site_to_location('validation', site)
            if location_update is None:
                result.unmapped_site_count += 1
                continue
            result.location_count += 1
            for charging_station in location_update.charging_pool:
                for evse in charging_station.evses:
                    result.evse_count += 1
                    result.evse_uids.add(evse.uid)
    return result


def get_v3_5_realtime_payloads(data: dict) -> list:
    """
    Same envelope handling as BaseDatex2V35ImportService.fetch_realtime_data
    """
    datex_input = DataclassValidator(MessageContainerWrapperInput).validate(
        BaseDatex2V35ImportService.wrap_realtime_payload(data),
    )
    if not datex_input.messageContainer or not datex_input.messageContainer.payload:
        raise ValidationError(reason='missing messageContainer payload')
    return [datex_input.messageContainer.payload[0]]


def validate_realtime(data: dict, version: str, evse_uids: set[str]) -> RealtimeResult:
    config = VERSIONS[version]
    result = RealtimeResult()
    try:
        payloads = config['realtime_payloads'](data)
    except ValidationError as e:
        result.errors = summarize_errors(flatten_errors(e.to_dict()))
        return result

    for payload in payloads:
        if payload is UnsetValue or payload.aegiEnergyInfrastructureStatusPublication is UnsetValue:
            result.errors = ['missing aegiEnergyInfrastructureStatusPublication']
            return result

    result.valid = True
    for payload in payloads:
        for site_status in payload.aegiEnergyInfrastructureStatusPublication.energyInfrastructureSiteStatus or []:
            if site_status.energyInfrastructureStationStatus is UnsetValue:
                continue
            for station_status in site_status.energyInfrastructureStationStatus:
                if station_status.refillPointStatus is UnsetValue:
                    continue
                for refill_point_status_g in station_status.refillPointStatus:
                    result.status_count += 1
                    evse_update = config['mapper'].map_energy_infrastructure_station_status(refill_point_status_g)
                    if evse_update is None:
                        result.unmapped_status_count += 1
                    elif evse_update.evse_id in evse_uids:
                        result.matched_count += 1
    return result


def validate(static_source: str, realtime_source: str | None) -> dict:
    report: dict = {}
    static_data = load_data(static_source)
    realtime_data = load_data(realtime_source) if realtime_source else None
    if static_data is None:
        report['static'] = 'empty response'
    if realtime_source and realtime_data is None:
        report['realtime'] = 'empty response'

    for version in VERSIONS:
        version_report: dict = {}
        evse_uids: set[str] = set()
        if static_data is not None:
            static_result = validate_static(static_data, version)
            evse_uids = static_result.evse_uids
            version_report['static'] = {
                key: value for key, value in static_result.__dict__.items() if key != 'evse_uids'
            }
        if realtime_data is not None:
            version_report['realtime'] = validate_realtime(realtime_data, version, evse_uids).__dict__
        report[version] = version_report
    return report


def print_report(report: dict):
    for key in ('static', 'realtime'):
        if isinstance(report.get(key), str):
            print(f'{key}: {report[key]}')
    for version in VERSIONS:
        static = report[version].get('static')
        if static:
            state = 'valid' if static['valid'] else 'INVALID'
            print(
                f'v{version} static {state}: {static["site_count"]} sites, {static["invalid_site_count"]} invalid, '
                f'{static["location_count"]} locations mapped, {static["unmapped_site_count"]} unmapped, '
                f'{static["evse_count"]} EVSEs',
            )
            for error in static['errors']:
                print(f'    {error}')
        realtime = report[version].get('realtime')
        if realtime:
            state = 'valid' if realtime['valid'] else 'INVALID'
            print(
                f'v{version} realtime {state}: {realtime["status_count"]} statuses, '
                f'{realtime["unmapped_status_count"]} unmapped, {realtime["matched_count"]} matching static EVSEs',
            )
            for error in realtime['errors']:
                print(f'    {error}')


if __name__ == '__main__':
    arguments = [argument for argument in sys.argv[1:] if argument != '--json']
    if not 1 <= len(arguments) <= 2:
        sys.exit(f'Usage: {sys.argv[0]} <static file or subscription id> [<realtime file or subscription id>] [--json]')
    validation_report = validate(arguments[0], arguments[1] if len(arguments) > 1 else None)
    if '--json' in sys.argv:
        print(json.dumps(validation_report))
    else:
        print_report(validation_report)
