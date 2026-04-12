"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .multi_lingual_string_value_output import MultiLingualStringValueOutput


@dataclass(kw_only=True)
class MultilingualStringOutput:
    values: list[MultiLingualStringValueOutput] | None = None
