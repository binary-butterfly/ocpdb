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
from webapp.models.enums import TariffAudience, TariffDimensionType, TariffType
from webapp.services.import_services.datex2.tariff_grouping_mixin import TariffGroupingMixin, TariffGroupingResult
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


def group_identical_tariffs(location_updates: list[LocationUpdate]) -> TariffGroupingResult:
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


def _build_tariff_association_update(
    tariff_update: TariffUpdate,
    *,
    uid: str | None = None,
    audience: TariffAudience | None = None,
    start_date_time: datetime | None = None,
    last_updated: datetime | None = None,
) -> TariffAssociationUpdate:
    return TariffAssociationUpdate(
        uid=uid if uid is not None else f'association-{tariff_update.uid}',
        source=SOURCE_UID,
        audience=audience,
        start_date_time=start_date_time,
        last_updated=last_updated,
        tariff=tariff_update,
    )


def _build_location_update(*tariff_updates: TariffUpdate) -> LocationUpdate:
    """
    Wrap each tariff into its own EVSE, mirroring how the DATEX2 mappers attach one tariff
    association per EVSE.
    """
    return _build_location_update_from_associations(
        *[[_build_tariff_association_update(tariff_update)] for tariff_update in tariff_updates],
    )


def _build_location_update_from_associations(
    *tariff_association_updates_per_evse: list[TariffAssociationUpdate],
) -> LocationUpdate:
    """Wrap each list of tariff associations into its own EVSE."""
    evse_updates: list[EvseUpdate] = []
    for index, tariff_association_updates in enumerate(tariff_association_updates_per_evse):
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
                tariff_association=tariff_association_updates,
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


def _grouped_tariff_association_updates(*location_updates: LocationUpdate) -> list[TariffAssociationUpdate]:
    """The tariff associations which survived the grouping, in the order the EVSEs hold them."""
    return [
        tariff_association_update
        for location_update in location_updates
        for charging_station_update in location_update.charging_pool
        for evse_update in charging_station_update.evses
        for tariff_association_update in evse_update.tariff_association or []
    ]


def _grouped_tariff_updates(*location_updates: LocationUpdate) -> list[TariffUpdate]:
    """The tariffs which survived the grouping, in the order their associations appear."""
    return [
        tariff_association_update.tariff
        for tariff_association_update in _grouped_tariff_association_updates(*location_updates)
    ]


def test_group_identical_tariffs_collapses_identical_fees() -> None:
    """Tariffs with identical fees collapse into one tariff, no matter which uid they started with."""
    tariff_updates = [_build_tariff_update(uid='first'), _build_tariff_update(uid='second')]
    location_update = _build_location_update(*tariff_updates)

    assert group_identical_tariffs([location_update]) == TariffGroupingResult(
        tariff_count=1,
        tariff_association_count=1,
    )

    # Both EVSEs keep a tariff association, but they now share one, and so the duplicated tariff is gone.
    grouped_tariff_association_updates = _grouped_tariff_association_updates(location_update)
    assert len(grouped_tariff_association_updates) == 2
    assert grouped_tariff_association_updates[0] is grouped_tariff_association_updates[1]

    grouped_tariff_updates = _grouped_tariff_updates(location_update)
    assert grouped_tariff_updates[0] is grouped_tariff_updates[1]

    # The grouped uids are fingerprints of the content, not one of the original uids.
    assert grouped_tariff_updates[0].uid not in ['first', 'second']
    assert len(grouped_tariff_updates[0].uid) == 32
    assert grouped_tariff_association_updates[0].uid not in ['association-first', 'association-second']
    assert len(grouped_tariff_association_updates[0].uid) == 32


def test_group_identical_tariffs_keeps_differing_audiences_apart() -> None:
    """
    One price list offered to two audiences is one tariff, but it stays two associations, because the
    audience decides who pays these fees.
    """
    location_update = _build_location_update_from_associations(
        [
            _build_tariff_association_update(
                _build_tariff_update(uid='ad-hoc'),
                audience=TariffAudience.AD_HOC_PAYMENT,
            ),
        ],
        [
            _build_tariff_association_update(
                _build_tariff_update(uid='contract'),
                audience=TariffAudience.EMSP_CONTRACT,
            ),
        ],
    )

    assert group_identical_tariffs([location_update]) == TariffGroupingResult(
        tariff_count=1,
        tariff_association_count=2,
    )

    grouped_tariff_updates = _grouped_tariff_updates(location_update)
    assert grouped_tariff_updates[0] is grouped_tariff_updates[1]


def test_group_identical_tariffs_uses_newest_last_updated() -> None:
    """A group is stamped with the newest last_updated of its members."""
    oldest = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    newest = datetime(2026, 5, 17, 8, 30, tzinfo=timezone.utc)
    middle = datetime(2026, 3, 2, 12, 0, tzinfo=timezone.utc)
    location_update = _build_location_update_from_associations(
        *[
            [
                _build_tariff_association_update(
                    _build_tariff_update(uid=uid, last_updated=last_updated),
                    last_updated=last_updated,
                ),
            ]
            for uid, last_updated in [('first', oldest), ('second', newest), ('third', middle)]
        ],
    )

    assert group_identical_tariffs([location_update]) == TariffGroupingResult(
        tariff_count=1,
        tariff_association_count=1,
    )

    assert _grouped_tariff_updates(location_update)[0].last_updated == newest
    assert _grouped_tariff_association_updates(location_update)[0].last_updated == newest


def test_group_identical_tariffs_uses_oldest_start_date_time() -> None:
    """The grouped association starts when the first EVSE of its group started to charge these fees."""
    oldest = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    newest = datetime(2026, 5, 17, 8, 30, tzinfo=timezone.utc)
    location_update = _build_location_update_from_associations(
        *[
            [_build_tariff_association_update(_build_tariff_update(uid=uid), start_date_time=start_date_time)]
            for uid, start_date_time in [('first', newest), ('second', oldest)]
        ],
    )

    assert group_identical_tariffs([location_update]).tariff_association_count == 1

    assert _grouped_tariff_association_updates(location_update)[0].start_date_time == oldest


def test_group_identical_tariffs_keeps_timestamps_none_without_timestamps() -> None:
    location_update = _build_location_update(
        _build_tariff_update(uid='first'),
        _build_tariff_update(uid='second'),
    )

    assert group_identical_tariffs([location_update]) == TariffGroupingResult(
        tariff_count=1,
        tariff_association_count=1,
    )

    grouped_tariff_association_update = _grouped_tariff_association_updates(location_update)[0]
    assert grouped_tariff_association_update.tariff.last_updated is None
    assert grouped_tariff_association_update.last_updated is None
    assert grouped_tariff_association_update.start_date_time is None


def test_group_identical_tariffs_keeps_differing_fees_apart() -> None:
    """Any difference in the fees keeps the tariffs, and with them their associations, separate."""
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

    assert group_identical_tariffs([_build_location_update(*tariff_updates)]) == TariffGroupingResult(
        tariff_count=len(tariff_updates),
        tariff_association_count=len(tariff_updates),
    )

    assert len({tariff_update.uid for tariff_update in tariff_updates}) == len(tariff_updates)


def test_group_identical_tariffs_groups_across_locations() -> None:
    """Grouping spans the whole import, not just a single location."""
    first_location_update = _build_location_update(_build_tariff_update(uid='first'))
    second_location_update = _build_location_update(_build_tariff_update(uid='second'))

    assert group_identical_tariffs([first_location_update, second_location_update]) == TariffGroupingResult(
        tariff_count=1,
        tariff_association_count=1,
    )

    grouped_tariff_association_updates = _grouped_tariff_association_updates(
        first_location_update,
        second_location_update,
    )
    assert grouped_tariff_association_updates[0] is grouped_tariff_association_updates[1]


def test_group_identical_tariffs_collapses_duplicated_associations_of_one_evse() -> None:
    """
    An EVSE cannot hold the same association twice, so two of its rates which collapse into one
    association leave it with a single association.
    """
    location_update = _build_location_update_from_associations(
        [
            _build_tariff_association_update(_build_tariff_update(uid='first'), uid='first-rate'),
            _build_tariff_association_update(_build_tariff_update(uid='second'), uid='second-rate'),
        ],
    )

    assert group_identical_tariffs([location_update]) == TariffGroupingResult(
        tariff_count=1,
        tariff_association_count=1,
    )

    assert len(_grouped_tariff_association_updates(location_update)) == 1


def test_group_identical_tariffs_is_deterministic_across_imports() -> None:
    """
    The same content always produces the same uids, so a re-import updates the existing rows
    instead of creating new ones.
    """
    first_import = _build_tariff_association_update(
        _build_tariff_update(uid='first', last_updated=datetime(2026, 1, 1, tzinfo=timezone.utc)),
        uid='first-association',
        last_updated=datetime(2026, 1, 1, tzinfo=timezone.utc),
    )
    second_import = _build_tariff_association_update(
        _build_tariff_update(uid='second', last_updated=datetime(2026, 6, 1, tzinfo=timezone.utc)),
        uid='second-association',
        last_updated=datetime(2026, 6, 1, tzinfo=timezone.utc),
    )

    group_identical_tariffs([_build_location_update_from_associations([first_import])])
    group_identical_tariffs([_build_location_update_from_associations([second_import])])

    assert first_import.tariff.uid == second_import.tariff.uid
    assert first_import.uid == second_import.uid


def test_group_identical_tariffs_ignores_evses_without_tariffs() -> None:
    location_update = _build_location_update()
    location_update.charging_pool[0].evses = [
        EvseUpdate(uid='evse-without-tariff', evse_id='DE*TST*E0', connectors=[]),
    ]

    assert group_identical_tariffs([location_update]) == TariffGroupingResult(
        tariff_count=0,
        tariff_association_count=0,
    )

    # An EVSE without tariffs keeps its untouched tariff_association, instead of an empty list.
    assert location_update.charging_pool[0].evses[0].tariff_association is None
