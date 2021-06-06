# encoding: utf-8

"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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


def generate_idtag(id, prefix=''):
    length = len(char_map)
    result = ''
    for i in range(10, 0, -1):
        result = str(char_map[id % length]) + result
        id = id // length
    return prefix + result


def reverse_idtag(uid):
    uid = uid[2:]
    length = len(char_map)
    result = 0
    for i in range(10, 0, -1):
        result += char_map.index(uid[i-1:i]) * (length ** (10 - i))
    return result


def generate_directid(id):
    length = len(char_map)
    result = ''
    for i in range(18, 0, -1):
        result = str(char_map[id % length]) + result
        id = id // length
    return result


def reverse_directid(uid):
    uid = uid[2:]
    length = len(char_map)
    result = 0
    for i in range(18, 0, -1):
        result += char_map.index(uid[i-1:i]) * (length ** (11 - i))
    return result


char_map = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]
