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

from webapp.models.charging_station import CAPABILITY_BIT_BY_MEMBER, CAPABILITY_BITS, Capability

# The bit value each capability is stored as in charging_station.capabilities. Written out literally so that any change
# to the persisted encoding has to be made here too, where it is obvious that existing database rows are affected.
EXPECTED_BITS: dict[str, int] = {
    'CHARGING_PROFILE_CAPABLE': 1,
    'CHARGING_PREFERENCES_CAPABLE': 2,
    'CHIP_CARD_SUPPORT': 4,
    'CONTACTLESS_CARD_SUPPORT': 8,
    'CREDIT_CARD_PAYABLE': 16,
    'DEBIT_CARD_PAYABLE': 32,
    'PED_TERMINAL': 64,
    'REMOTE_START_STOP_CAPABLE': 128,
    'RESERVABLE': 256,
    'RFID_READER': 512,
    'TOKEN_GROUP_CAPABLE': 1024,
    'UNLOCK_CAPABLE': 2048,
    'PUBLIC': 4096,
    'LOCAL_KEY': 8192,
    'CASH': 16384,
    'IEC15118': 32768,
    'DIRECT_REMOTE': 65536,
}


class CapabilityBitsTest:
    """
    Guards the bitmask encoding of ChargingStation.capabilities. The bit values are persisted, so changing one
    reinterprets every existing row without any migration or error.
    """

    @staticmethod
    def test_bit_values_are_unchanged():
        """Every capability must keep the bit value it was stored with."""
        assert {item.name: bit for bit, item in CAPABILITY_BITS} == EXPECTED_BITS

    @staticmethod
    def test_every_capability_has_a_bit():
        """A capability missing from the table would silently never be stored or returned."""
        assert {item for _bit, item in CAPABILITY_BITS} == set(Capability)

    @staticmethod
    def test_bits_are_unique_and_single():
        """Each entry must be a distinct power of two, otherwise capabilities alias each other."""
        bits = [bit for bit, _item in CAPABILITY_BITS]

        assert len(set(bits)) == len(bits)
        for bit in bits:
            assert bit > 0
            assert bit & (bit - 1) == 0

    @staticmethod
    def test_bit_by_member_matches_the_table():
        """The lookup used by the setter must agree with the table used by the getter."""
        assert CAPABILITY_BIT_BY_MEMBER == {item: bit for bit, item in CAPABILITY_BITS}

    @staticmethod
    def test_table_is_ordered_by_bit_value():
        """The getter returns capabilities in table order, which callers expect to be ascending by bit."""
        bits = [bit for bit, _item in CAPABILITY_BITS]

        assert bits == sorted(bits)
