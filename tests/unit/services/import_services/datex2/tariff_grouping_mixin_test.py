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

from datetime import datetime, timezone
from decimal import Decimal

from webapp.models.connector import ConnectorFormat, ConnectorType
from webapp.models.enums import TariffDimensionType, TariffType
from webapp.services.import_services.datex2.tariff_grouping_mixin import TariffGroupingMixin
from webapp.services.import_services.models import (
    ChargingStationUpdate,
    ConnectorUpdate,
    EvseUpdate,
    LocationUpdate,
    PriceComponentUpdate,
    RestrictionsUpdate,
    SourceInfo,
    TariffAssociationUpdate,
    TariffElementUpdate,
    TariffUpdate,
    TaxPercentageUpdate,
)

SOURCE_UID = 'datex2_test'


class TariffGroupingService(TariffGroupingMixin):
    """Minimal host for the mixin: it only needs a source_info to name the source in its log line."""

    source_info = SourceInfo(
        uid=SOURCE_UID,
        name='DATEX2 Test',
        public_url='https://example.org',
        has_realtime_data=False,
    )


def group_identical_tariffs(location_updates: list[LocationUpdate]) -> int:
    return TariffGroupingService().group_identical_tariffs(location_updates)


def _build_tariff_update(
    *,
    uid: str,
    price: str = '0.49',
    currency: str | None = 'EUR',
    tariff_type: TariffType | None = TariffType.AD_HOC_PAYMENT,
    tax_percentage: str | None = '19',
    max_duration: int | None = None,
    last_updated: datetime | None = None,
) -> TariffUpdate:
    price_component = PriceComponentUpdate(
        type=TariffDimensionType.ENERGY,
        price=Decimal(price),
    )
    if tax_percentage is not None:
        price_component.taxes = [TaxPercentageUpdate(name='VAT', percentage=Decimal(tax_percentage))]

    tariff_element = TariffElementUpdate(price_components=[price_component])
    if max_duration is not None:
        tariff_element.restrictions = RestrictionsUpdate(max_duration=max_duration)

    return TariffUpdate(
        uid=uid,
        source=SOURCE_UID,
        currency=currency,
        type=tariff_type,
        last_updated=last_updated,
        elements=[tariff_element],
    )


def _build_location_update(*tariff_updates: TariffUpdate) -> LocationUpdate:
    """
    Wrap each tariff into its own EVSE, mirroring how the DATEX2 mappers attach one tariff
    association per EVSE.
    """
    evse_updates: list[EvseUpdate] = []
    for index, tariff_update in enumerate(tariff_updates):
        evse_updates.append(
            EvseUpdate(
                uid=f'evse-{index}',
                evse_id=f'DE*TST*E{index}',
                connectors=[
                    ConnectorUpdate(
                        uid=str(index),
                        standard=ConnectorType.IEC_62196_T2,
                        format=ConnectorFormat.SOCKET,
                    ),
                ],
                tariff_association=[
                    TariffAssociationUpdate(
                        uid=f'association-{index}',
                        source=SOURCE_UID,
                        tariff=tariff_update,
                    ),
                ],
            ),
        )

    return LocationUpdate(
        uid='location-1',
        source=SOURCE_UID,
        charging_pool=[ChargingStationUpdate(uid='station-1', evses=evse_updates)],
        lat=Decimal('48.7758459'),
        lon=Decimal('9.1829321'),
        time_zone='Europe/Berlin',
    )


def test_group_identical_tariffs_collapses_identical_fees() -> None:
    """Tariffs with identical fees share one uid, no matter which uid they started with."""
    tariff_updates = [_build_tariff_update(uid='first'), _build_tariff_update(uid='second')]
    location_update = _build_location_update(*tariff_updates)

    assert group_identical_tariffs([location_update]) == 1

    assert tariff_updates[0].uid == tariff_updates[1].uid
    # The grouped uid is a fingerprint of the fees, not one of the original uids.
    assert tariff_updates[0].uid not in ['first', 'second']
    assert len(tariff_updates[0].uid) == 32


def test_group_identical_tariffs_uses_newest_last_updated() -> None:
    """A group is stamped with the newest last_updated of its members."""
    oldest = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    newest = datetime(2026, 5, 17, 8, 30, tzinfo=timezone.utc)
    tariff_updates = [
        _build_tariff_update(uid='first', last_updated=oldest),
        _build_tariff_update(uid='second', last_updated=newest),
        _build_tariff_update(uid='third', last_updated=datetime(2026, 3, 2, 12, 0, tzinfo=timezone.utc)),
    ]

    assert group_identical_tariffs([_build_location_update(*tariff_updates)]) == 1

    assert [tariff_update.last_updated for tariff_update in tariff_updates] == [newest, newest, newest]


def test_group_identical_tariffs_keeps_last_updated_none_without_timestamps() -> None:
    tariff_updates = [_build_tariff_update(uid='first'), _build_tariff_update(uid='second')]

    assert group_identical_tariffs([_build_location_update(*tariff_updates)]) == 1

    assert [tariff_update.last_updated for tariff_update in tariff_updates] == [None, None]


def test_group_identical_tariffs_keeps_differing_fees_apart() -> None:
    """Any difference in the fees keeps the tariffs separate."""
    reference = _build_tariff_update(uid='reference')
    tariff_updates = [
        reference,
        _build_tariff_update(uid='other-price', price='0.59'),
        _build_tariff_update(uid='other-currency', currency='CHF'),
        _build_tariff_update(uid='other-type', tariff_type=TariffType.REGULAR),
        _build_tariff_update(uid='other-tax', tax_percentage='7'),
        _build_tariff_update(uid='without-tax', tax_percentage=None),
        _build_tariff_update(uid='other-restriction', max_duration=3600),
    ]

    assert group_identical_tariffs([_build_location_update(*tariff_updates)]) == len(tariff_updates)

    assert len({tariff_update.uid for tariff_update in tariff_updates}) == len(tariff_updates)


def test_group_identical_tariffs_groups_across_locations() -> None:
    """Grouping spans the whole import, not just a single location."""
    first = _build_tariff_update(uid='first')
    second = _build_tariff_update(uid='second')

    assert group_identical_tariffs([_build_location_update(first), _build_location_update(second)]) == 1

    assert first.uid == second.uid


def test_group_identical_tariffs_is_deterministic_across_imports() -> None:
    """
    The same fees always produce the same uid, so a re-import updates the existing tariff row
    instead of creating a new one.
    """
    first_import = _build_tariff_update(uid='first', last_updated=datetime(2026, 1, 1, tzinfo=timezone.utc))
    second_import = _build_tariff_update(uid='second', last_updated=datetime(2026, 6, 1, tzinfo=timezone.utc))

    group_identical_tariffs([_build_location_update(first_import)])
    group_identical_tariffs([_build_location_update(second_import)])

    assert first_import.uid == second_import.uid


def test_group_identical_tariffs_ignores_evses_without_tariffs() -> None:
    location_update = _build_location_update()
    location_update.charging_pool[0].evses = [
        EvseUpdate(uid='evse-without-tariff', evse_id='DE*TST*E0', connectors=[]),
    ]

    assert group_identical_tariffs([location_update]) == 0
