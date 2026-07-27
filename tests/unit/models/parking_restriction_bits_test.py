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

from webapp.models.evse import (
    PARKING_RESTRICTION_BIT_BY_MEMBER,
    PARKING_RESTRICTION_BITS,
    ParkingRestriction,
)

# The bit value each parking restriction is stored as in evse.parking_restrictions. Written out literally so that any
# change to the persisted encoding has to be made here too, where it is obvious that existing rows are affected.
EXPECTED_BITS: dict[str, int] = {
    'EV_ONLY': 1,
    'PLUGGED': 2,
    'DISABLED': 4,
    'CUSTOMERS': 8,
    'MOTORCYCLES': 16,
    'CARSHARING': 32,
    'BICYCLE_ONLY': 64,
}


class ParkingRestrictionBitsTest:
    """
    Guards the bitmask encoding of Evse.parking_restrictions. The bit values are persisted, so changing one
    reinterprets every existing row without any migration or error.
    """

    @staticmethod
    def test_bit_values_are_unchanged():
        """Every parking restriction must keep the bit value it was stored with."""
        assert {item.name: bit for bit, item in PARKING_RESTRICTION_BITS} == EXPECTED_BITS

    @staticmethod
    def test_every_parking_restriction_has_a_bit():
        """A restriction missing from the table would silently never be stored or returned."""
        assert {item for _bit, item in PARKING_RESTRICTION_BITS} == set(ParkingRestriction)

    @staticmethod
    def test_bits_are_unique_and_single():
        """Each entry must be a distinct power of two, otherwise restrictions alias each other."""
        bits = [bit for bit, _item in PARKING_RESTRICTION_BITS]

        assert len(set(bits)) == len(bits)
        for bit in bits:
            assert bit > 0
            assert bit & (bit - 1) == 0

    @staticmethod
    def test_bit_by_member_matches_the_table():
        """The lookup used by the setter must agree with the table used by the getter."""
        assert PARKING_RESTRICTION_BIT_BY_MEMBER == {item: bit for bit, item in PARKING_RESTRICTION_BITS}

    @staticmethod
    def test_table_is_ordered_by_bit_value():
        """The getter returns restrictions in table order, which callers expect to be ascending by bit."""
        bits = [bit for bit, _item in PARKING_RESTRICTION_BITS]

        assert bits == sorted(bits)

    @staticmethod
    def test_bicycle_only_bit_used_by_the_tile_summary_query():
        """
        fetch_locations_summary_by_bounds() counts bike chargepoints with a raw SQL bitmask test built from this
        constant. It used to be a hardcoded 64.
        """
        assert PARKING_RESTRICTION_BIT_BY_MEMBER[ParkingRestriction.BICYCLE_ONLY] == 64
