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

from collections import defaultdict
from typing import List, Optional, Tuple

from lxml import etree


def xml_to_dict(
    tag: etree.Element,
    ensure_array_keys: Optional[List[Tuple[str, str]]],
    remote_type_tags: Optional[List[str]] = None,
) -> dict:
    tag_name = etree.QName(tag).localname
    tag_dict = {tag_name: {} if tag.attrib else None}
    children = list(tag)
    if children:
        aggregated_child_dict = defaultdict(list)
        for child in children:
            child_dict = xml_to_dict(child, ensure_array_keys, remote_type_tags)
            for key, value in child_dict.items():
                if type(value) is dict and next(iter(value)) in remote_type_tags:
                    value = value[next(iter(value))]
                aggregated_child_dict[key].append(value)
        tag_dict = {tag_name: {}}
        for key, value in aggregated_child_dict.items():
            if key == 'class':
                key = 'class_'

            if len(value) == 1 and (tag_name, key) not in ensure_array_keys:
                value = value[0]
            tag_dict[tag_name][key] = value

    if tag.attrib:
        tag_dict[tag_name].update((k, v) for k, v in tag.attrib.items())
    if tag.text:
        text = tag.text.strip()
        if children or tag.attrib:
            if text:
                tag_dict[tag_name]['_text'] = text
        else:
            tag_dict[tag_name] = text
    return tag_dict
